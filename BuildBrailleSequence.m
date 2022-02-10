function pulse = BuildBrailleSequence(seq,hand)
% Creates data stream for selected pattern
pulse = [];
dat = 32; % data
clk = 64; % clock
stb = 128; % strobe 

for it = 1:size(seq(:),1)
    if seq(it) == 1
        pulse = cat(2,pulse,[dat dat+clk]);
    else
        pulse = cat(2,pulse,[0 clk]);
    end
end

switch hand
    case 1
    % Sends pattern to left stimualtor only
    pulse = cat(2,repmat([0 clk],1,8),pulse);
    case 2
    % Sends pattern to right stimualtor only
    pulse = cat(2,pulse,repmat([0 clk],1,8));    
    case 0
    % Sends same pattern to both stimualtors
    pulse = repmat(pulse,1,2);
end

pulse(33) = stb;

