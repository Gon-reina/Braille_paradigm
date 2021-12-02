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
del = 0:Trial_length:(N-1)*Trial_length;
r = randi(Npat,1);
seq = BuildBrailleSequence(pp(r,:),0);
seq = BuildBrailleSequence(seq,0);

%% Initialise Parallel Port IO
ioObjTrig = io64;
% initialize the interface to the inpoutx64 system driver
status = io64(ioObjTrig);
io64(ioObjTrig,PortAddress,0);
disp('Port Cleared')
%%

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
    pause(CueOn)
    fprintf("Hand is %d \n",Attendlr(i))
    io64(ioObjTrig,PortAddress,0)

    Screen('DrawLines', window, allCoords,...
        lineWidthPix, [1 1 1], [xCenter yCenter], 2);
    Screen('Flip', window, t+del(ii)+CueOff);
    
    toc
end
