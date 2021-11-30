clear 
close all
clc

pp = [  1 1 0 0 1 1 0 0
        0 0 1 1 0 0 1 1
        0 1 1 0 0 1 1 0
        1 1 1 1 0 0 0 0
        0 0 0 0 1 1 1 1];

Npat = size(pp,1);
all_down = BuildBrailleSequence(zeros(1,8),0);
% Gives feedback every 10 trials.
nfeedback = 10;
Ntrials = 80;
PortAddress = 57336;
% set up triggers
TriggerStart = 1;
TriggerSample = 2;
TriggerLeft = 4;
TriggerRight = 8;
TriggerFalseL = 16;
TriggerFalseR = 32;
TriggerTrue = 64;
% Set up attend left/right condition in a pseudorandomised way: 50 left, 50 right
Attendlr = [ones(1,Ntrials/2), ones(1,Ntrials/2)*2];
Attendlr = Attendlr(randperm(Ntrials));
% Defines how many targets there are in each trial
g = gamrnd(4,.3,1,Ntrials);
g = round(g);
g(g>5) = 5;


jitteryn = 0;

Sampletime = 1;
Sampleduration = 2;
SampleOff = Sampletime + Sampleduration;%3
CueTime = SampleOff + 2; % 5s
CueDuration = 2;%%was0.5 MJB
CueOn = CueTime - CueDuration/2; % 4s
CueOff = CueTime + CueDuration/2; % 6s
StimOn = CueTime + 2; % 7s
StimGap = 1.1; % Pause between stimuli, including stim duration
StimDuration = 0.1;
StimOff = StimOn + StimDuration;
% Number of stimuli in each trial
Nstims = 5;
PauseEndtrial = 4;
Restblock = 21;

for ii = 1:Ntrials
    DrawFormattedText(window, 'New trial' , 'center', 'center', white);
    Screen('Flip', window, t+del(ii));
    io64(ioObjTrig,PortAddress,TriggerStart);
    DrawFormattedText(window, 'New trial' , 'center', 'center', white);
    Screen('Flip', window, t+del(ii)+0.1);
    io64(ioObjTrig,PortAddress,0);
    Screen('DrawLines', window, allCoords,...
        lineWidthPix, [1 1 1], [xCenter yCenter], 2);
    Screen('Flip', window, t+del(ii)+Sampletime);    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Send the sample pattern
    r = randi(Npat,1);
    seq = BuildBrailleSequence(pp(r,:),0);
    sendStim(seq,ioObjStim ,PortAddressStim);
    io64(ioObjTrig,PortAddress,TriggerSample);
    Screen('DrawLines', window, allCoords,...
        lineWidthPix, [1 1 1], [xCenter yCenter], 2);
    Screen('Flip', window, t+del(ii)+SampleOff);
    % Reset stimulators
    sendStim(all_down,ioObjStim ,PortAddressStim);
    io64(ioObjTrig,PortAddress,0)
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Display text 'left' (1) or 'right' (2)
    Screen('DrawLines', window, ...
        fixCrossDimPix*[-1 1 (Attendlr(ii)-1.5)*2*[.25 .9 .25 .9]; 0 0 .75 0 -.75 0],...
        lineWidthPix, [1 1 1], [xCenter yCenter], 2);
    % Send trigger 'left' (4) or 'right' (8)
    io64(ioObjTrig,PortAddress,Attendlr(ii)*4)
    Screen('Flip', window, t+del(ii)+CueOn);
    io64(ioObjTrig,PortAddress,0)
    Screen('DrawLines', window, allCoords,...
        lineWidthPix, [1 1 1], [xCenter yCenter], 2);
    Screen('Flip', window, t+del(ii)+CueOff);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Randomly choose patterns excluding sample pattern
    rrange = [1:r-1, r+1:Npat];
    stimindex = randi(Npat-1,1,Nstims);
    stimuli = rrange(stimindex);
    % Add correct patterns
    for jj = 1:g(ii)
        stimuli(jj) = r;
    end
    stimuli = stimuli(randperm(Nstims));
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % STIMULUS 1
    % Choose which hand randomly 50% probability
    for kk = 1:Nstims
        leftright = round(rand(1))+1;
        handstim(ii,kk) = leftright;

        seq = BuildBrailleSequence(pp(stimuli(kk),:),leftright);
        sendStim(seq,ioObjStim ,PortAddressStim);
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        % Send triggers to the MEG
        % Correct pattern on correct hand.
        if stimuli(kk) == r && Attendlr(ii) == leftright
            io64(ioObjTrig,PortAddress,TriggerTrue)
        % Correct pattern on wrong hand.
        else
            % Wrong pattern.
            if leftright == 1;
                io64(ioObjTrig,PortAddress,TriggerFalseL);
            elseif leftright == 2;
                io64(ioObjTrig,PortAddress,TriggerFalseR);
            end
        end
        % Rest pins
        sendStim(all_down,ioObjStim ,PortAddressStim);
        io64(ioObjTrig,PortAddress,0)
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        % Check button press
        if  stimuli(kk) == r && Attendlr(ii) == leftright
            if leftright == 1
                disp('TARGET LEFT!!!!!!!!!!!!!');
            elseif leftright == 2
                disp('TARGET RIGHT!!!!!!!!!!!!!');
            end
        end
        [~, keyCode] = KbWait(0,2,t+del(ii)+ StimOn + StimGap*(kk-1)+1);
        key = KbName(find(keyCode))
        % Considers any buttons pressed
        
        if size(key,1) > 0            
            if  stimuli(kk) == r && Attendlr(ii) == leftright
                correctpress = correctpress +1;
            else
                wrongpress  = wrongpress +1;
            end        
        else % if buttons are not pressed but stimulus is correct
            if stimuli(kk) == r && Attendlr(ii) == leftright
                misspress = misspress +1;
            end
        end               
                     
        
    end
    trialpattern(ii,:) = stimuli;
    rarray(ii) =r;
    
    if mod(ii,nfeedback) ==0        

        feddbacktext = sprintf('Score: %d/%d   \n\ntriggerfinger: %d   \n\nPlease take a short break',...
            correctpress,(correctpress+misspress), wrongpress);

        correctpress = 0;
        misspress = 0;
        wrongpress = 0;
        pause(PauseEndtrial)
        io64(ioObjTrig,PortAddress,TriggerStart);
        pause(1)
        io64(ioObjTrig,PortAddress,0);

    else    
        DrawFormattedText(window, '' , 'center', 'center', white);   
    
    end
    
    Screen('Flip', window, t+del(ii)+ StimOff + StimGap*(kk-1)+PauseEndtrial);    
    
    % need to save 'attendlr', 'r' and 'stimuli' and 'leftright'
end
