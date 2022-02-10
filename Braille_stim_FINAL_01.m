% Liuzzi Lucrezia, George Roberts
% Metec braille cells both hands attention modulation paradigm.
% Using Markus's control circuit board.

% Modified 07/04/17: Added 4s pause after last stimulus in each trial and
% eliminated jitter between trials. New Trial lenght is 12.5s . 
% Now accepts any button (or keyboard!) presses,ygyggrygyryrgrgrgybrgr not just the blue buttons. 
% Using only 5 easy patterns from Bauer 2006 paper. 

clear all
close all
clc
warning off
%%
% 06/04/17 Changed patterns to make task easier
pp = [  1 1 0 0 1 1 0 0     % easy
    0 0 1 1 0 0 1 1     % easy
    0 1 1 0 0 1 1 0     % easy
    1 1 1 1 0 0 0 0     % easy
    0 0 0 0 1 1 1 1];   % easy 

Npat = size(pp,1);

all_down = BuildBrailleSequence(zeros(1,8),0);

%%
% Gives feedback every 10 trials.
nfeedback = 2;
Ntrials = 10;
PortAddress = 57336;

% coloured buttons - blue, yellow, green, red
%Only list to keys r g b y
keyFlags = zeros(1,256);
keyFlags([66,89,71,82])=1;
% Set arrays for each hand
left_press = [66,89];
right_press = [71,82];
%%%%% set up triggers
TriggerStart = 1;
TriggerSample = 2;
TriggerTrue = 4;
TriggerFalseL = 3;
TriggerFalseR = 5;
TriggerLeft = 6;
TriggerRight = 7;
LeftPress = 8;
RightPress = 16;
% Set up attend left/right condition in a pseudorandomised way: 50 left, 50 right
Attendlr = [ones(1,Ntrials/2), ones(1,Ntrials/2)*2];
Attendlr = Attendlr(randperm(Ntrials));

% Defines how many targets there are in each trial
Ntrials = 80;
g = gamrnd(4,.3,1,Ntrials);
g = round(g);
g(g>5) = 5;
% Defines how many targets there are in each trial
% correcthand = gamrnd(2,.25,Nstims,Ntrials);
% correcthand = ~round(correcthand);

%% Initialise Parallel Port IO
ioObjTrig = io64;
% initialize the interface to the inpoutx64 system driver
status = io64(ioObjTrig);
io64(ioObjTrig,PortAddress,0);

global cogent;
config_io
io64(cogent.io.ioObj,PortAddress,0);
disp('Ports Cleared')
% ioObjTrig = io64;
% statusStim = io64(ioObjTrig);
% io64(ioObjTrig,PortAddress,0);
% r = 5;
% seq = BuildBrailleSequence(pp(r,:),0);
% sendStim(seq,ioObjTrig ,PortAddress);
% io64(ioObjTrig,PortAddress,TriggerSample);
% io64(ioObjTrig,PortAddress,0);
% sendStim(all_down,ioObjTrig ,PortAddress);
%% Initialise PTB
PsychDefaultSetup(2);
screens = Screen('Screens');
screenNumber = max(screens);
white = WhiteIndex(screenNumber);
black = BlackIndex(screenNumber);
%  PsychDebugWindowConfiguration;
[window, windowRect] = PsychImaging('OpenWindow', screenNumber, white/2);
[screenXpixels, screenYpixels] = Screen('WindowSize', window);
ifi = Screen('GetFlipInterval', window);
Screen('BlendFunction', window, 'GL_SRC_ALPHA', 'GL_ONE_MINUS_SRC_ALPHA');
Screen('TextFont', window, 'Arial');
Screen('TextSize', window, 72);
[xCenter, yCenter] = RectCenter(windowRect);
fixCrossDimPix = 20;
xCoords = [-fixCrossDimPix fixCrossDimPix 0 0];
yCoords = [0 0 -fixCrossDimPix fixCrossDimPix];
allCoords = [xCoords; yCoords];
lineWidthPix = 6;

%% Stimulus Bit

DrawFormattedText(window, 'Ready' , 'center', 'center', white);
Screen('Flip',window);
begin = 0;
while (~begin)
    [key_pressed, seconds, key_code] = KbCheck;
    if (key_pressed)
        begin = find (key_code) == KbName ('space');
    end;
end;

Screen('DrawLines', window, allCoords,...
    lineWidthPix, white, [xCenter yCenter], 2);
Screen('Flip', window);


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

% PTB uses time relative to a generated timecode to start trials, to
% generated the deltas (and accommodate the 2 second jitter in trial
% lengths)

Trial_length = StimOn + StimGap*Nstims+PauseEndtrial;
del = 0:Trial_length:(Ntrials-1)*Trial_length;
if jitteryn == 1
    % Example on how to add jitter
    jitter = 2*rand(1,length(del)-1);
    del = [0 del(2:end)+cumsum(jitter)]; % del_jittered
end

% add extra pause every 10 trials to display feedback
feedbackpause=repmat(0:Ntrials/nfeedback-1,nfeedback,1);
feedbackpause = reshape(feedbackpause,[nfeedback*(Ntrials/nfeedback ),1]);
del = del + feedbackpause'*Restblock ; 

trialpattern = zeros(Ntrials,Nstims);
handstim = zeros(Ntrials,Nstims);
pause(3)
sendStim(all_down,ioObjTrig ,PortAddress);
t = GetSecs();
Screen('TextSize', window, 36);

correctpress = 0;
wrongpress = 0;
misspress = 0;
% 
rarray = zeros(1,Ntrials);
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
    sendStim(seq,ioObjTrig ,PortAddress);
    io64(ioObjTrig,PortAddress,TriggerSample);

    Screen('DrawLines', window, allCoords,...
        lineWidthPix, [1 1 1], [xCenter yCenter], 2);
    Screen('Flip', window, t+del(ii)+SampleOff);

    % Reset stimulators
    sendStim(all_down,ioObjTrig ,PortAddress);
    io64(ioObjTrig,PortAddress,0)
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Display text 'left' (1) or 'right' (2)
    Screen('DrawLines', window, ...
        fixCrossDimPix*[-1 1 (Attendlr(ii)-1.5)*2*[.25 .9 .25 .9]; 0 0 .75 0 -.75 0],...
        lineWidthPix, [1 1 1], [xCenter yCenter], 2);
    % Send trigger 'left' (4) or 'right' (8)
    
%     io64(ioObjTrig,PortAddress,Attendlr(ii)+5)

    Screen('Flip', window, t+del(ii)+CueOn);
    io64(ioObjTrig,PortAddress,Attendlr(ii)+5)
    

    Screen('DrawLines', window, allCoords,...
        lineWidthPix, [1 1 1], [xCenter yCenter], 2);
    Screen('Flip', window, t+del(ii)+CueOff);
    io64(ioObjTrig,PortAddress,0)
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
        Screen('DrawLines', window, allCoords,...
            lineWidthPix, [1 1 1], [xCenter yCenter], 2);
        Screen('Flip', window, t+del(ii)+ StimOn + StimGap*(kk-1));
        seq = BuildBrailleSequence(pp(stimuli(kk),:),leftright);
        sendStim(seq,ioObjTrig ,PortAddress);
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
        Screen('DrawLines', window, allCoords,...
            lineWidthPix, [1 1 1], [xCenter yCenter], 2);
        Screen('Flip', window, t+del(ii)+ StimOff + StimGap*(kk-1));
        sendStim(all_down,ioObjTrig ,PortAddress);
        io64(ioObjTrig,PortAddress,0)
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        % Check button press
        disp("All good in the hood")
        press_start = GetSecs()+StimGap;
        now = GetSecs() ;
        fprintf("The time difference is %d",press_start-now)
        KbQueueRelease(0);
        KbQueueCreate(0,keyFlags); % initialize the Queue
        KbQueueStart;% start keyboard monitoring
        key_pressed = [];
        while now <= press_start
            [pressed, firstPress]=KbQueueCheck;
            if pressed
                key_pressed = find(firstPress);
                disp("Key pressed!!")
                if ismember(key_pressed,left_press)
                    io64(ioObjTrig, PortAddress, LeftPress);
                    pause(0.05)
                    io64(ioObjTrig, PortAddress, 0);
                elseif ismember(key_pressed,right_press)
                    io64(ioObjTrig, PortAddress, RightPress);
                    pause(0.05)
                    io64(ioObjTrig, PortAddress, 0);
                end
                break
            end
        end
        KbQueueStop;
        disp("I died")
        key = KbName(find(key_pressed));
        fprintf('Keycode for pressed: %d.\n',key)
%         % Considers any buttons pressed
%         
        if size(key,1) > 0            
            if  stimuli(kk) == r && Attendlr(ii) == leftright
                correctpress = correctpress +1
            else
                wrongpress  = wrongpress +1
            end        
        else % if buttons are not pressed but stimulus is correct
            if stimuli(kk) == r && Attendlr(ii) == leftright
                misspress = misspress +1
            end
        end               
                     
        disp("i keep going")
    end
    trialpattern(ii,:) = stimuli;
    rarray(ii) =r;
    
    if mod(ii,nfeedback) ==0        

        feddbacktext = sprintf('Score: %d/%d   \n\ntriggerfinger: %d   \n\nPlease take a short break',...
            correctpress,(correctpress+misspress), wrongpress);
        DrawFormattedText(window, feddbacktext , 'center', 'center');
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
    DrawFormattedText(window, '' , 'center', 'center', white);   
    Screen('Flip', window, t+del(ii)+ StimOff + StimGap*(kk-1)+PauseEndtrial);    
    
    % need to save 'attendlr', 'r' and 'stimuli' and 'leftright'
end
dd=datestr(datetime('today'));
save(['logfiles/Braille_stim5_',dd,'.mat'],'trialpattern','Attendlr','rarray','handstim')
DrawFormattedText(window, 'Fin' , 'center', 'center', white);
Screen('Flip',window,t+del(ii)+1);

Screen('Flip',window,t+del(ii)+17);
KbWait();

