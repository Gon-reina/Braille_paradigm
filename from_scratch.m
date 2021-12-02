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
N = 80;
PortAddress = 57336;
% Trigger channels
TriggerStart = 1;
TriggerSample = 2;
TriggerTrue = 4;
TriggerFalseL = 3;
TriggerFalseR = 5;
CueLeft = 6;
CueRight = 7;
% Set up attend left/right condition in a pseudorandomised way: 50 left, 50 right
Attendlr = [ones(1,N/2), ones(1,N/2)*2];
Attendlr = Attendlr(randperm(N));
% Defines how many targets there are in each trial
g = gamrnd(4,.3,1,N);
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
Trial_length = StimOn + StimGap*Nstims+PauseEndtrial;
%Time splits of all trials
del = 0:Trial_length:(N-1)*Trial_length;

% add extra pause every 10 trials to display feedback
feedbackpause=repmat(0:N/nfeedback-1,nfeedback,1);
feedbackpause = reshape(feedbackpause,[nfeedback*(N/nfeedback ),1]);
del = del + feedbackpause'*Restblock ; 


handstim = zeros(N,Nstims);

correctpress = 0;
wrongpress = 0;
misspress = 0;
% 
rarray = zeros(1,N);

%% Initialise Parallel Port IO
ioObjTrig = io64;
% initialize the interface to the inpoutx64 system driver
status = io64(ioObjTrig);
io64(ioObjTrig,PortAddress,0);
disp('Port Cleared')
%%
correctpress = 0;
wrongpress = 0;
misspress = 0;

for i = 1:N
    tic
    % First start the trial by updating screen and sending trigger
    io64(ioObjTrig,PortAddress,TriggerStart);
    pause(0.1)
    io64(ioObjTrig,PortAddress,0);

    pause(Sampletime)% Send the sample pattern to both hands at the 1 second mark
    r = randi(Npat,1); % Choose a random pattern from pp
    seq = BuildBrailleSequence(pp(r,:),0);
    sendStim(seq,ioObjTrig,PortAddress);
    io64(ioObjTrig,PortAddress,TriggerSample);
    pause(SampleOff) %Leave pattern on for 2 seconds
    sendStim(all_down,ioObjTrig ,PortAddress);
    io64(ioObjTrig,PortAddress,0)

    % Show the cue 'left' (1) or 'right' (2)
    io64(ioObjTrig,PortAddress,Attendlr(ii)+5)
    fprintf("Hand is %d \n",Attendlr(i))
    pause(CueOn)
    io64(ioObjTrig,PortAddress,0)
    pause(CueOff)
    disp("stop cue \n")

    % Randomly choose patterns excluding sample pattern
    rrange = [1:r-1, r+1:Npat];
    stimindex = randi(Npat-1,1,Nstims);
    stimuli = rrange(stimindex);
    for j = 1:g(i)
        stimuli(j) = r;
    end
    stimuli = stimuli(randperm(Nstims));
    for k = 1:Nstims
        % Randomly choose which hand to send th pattern to
        leftright = round(rand(1))+1;
        handstim(i,k) = leftright;
        pause(1.1)
        seq = BuildBrailleSequence(pp(stimuli(k),:),leftright);
        sendStim(seq,ioObjTrig ,PortAddress);          
        % Send triggers to the MEG
        if stimuli(k) == r && Attendlr(i) == leftright
            %Correct pattern on correct hand
            io64(ioObjTrig,PortAddress,TriggerTrue) 
        else
            % Wrong pattern.
            if leftright == 1
                io64(ioObjTrig,PortAddress,TriggerFalseL);
            elseif leftright == 2
                io64(ioObjTrig,PortAddress,TriggerFalseR);
            end
        end             
        pause(0.2)
        sendStim(all_down,ioObjTrig ,PortAddress);
        io64(ioObjTrig,PortAddress,0)
        % Check button press
        if  stimuli(kk) == r && Attendlr(ii) == leftright
            if leftright == 1
                disp('TARGET LEFT!!!!!!!!!!!!!');
            elseif leftright == 2
                disp('TARGET RIGHT!!!!!!!!!!!!!');
            end
        end
        % Find a way to record the button press



    end

    toc
end
