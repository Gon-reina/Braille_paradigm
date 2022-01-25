%% Script for basic button press in OPM lab
% Uses fORP box by Current Designs
clear;

% coloured buttons - blue, yellow, green, red
left_hand = KbName({'b','y'});
right_hand = KbName({'g','r'});
response_key = KbName({'b','y','g','r'});
LeftPress = 8;
RightPress = 4;

% button to start each block (corresponding to index finger button)
blue_key = KbName(response_key(1)); %i.e. '6^'
% initialise key press queue
keylist=zeros(1,256);%%create a list of 256 zeros
keylist(response_key)=1;%%set keys you interested in to 1

%% Set up triggers
%Clear ports
address = 57336;
io_obj = io64;
% initialize the interface to the inpoutx64 system driver
status = io64(io_obj);
io64(io_obj,address,0);
disp('Ports Cleared')
io64(io_obj,address,16);
pause(0.1)
io64(io_obj,address,0);
% Trigger channels for each colour button
trig_chans = [1 2 4 8];

%% Click button to start
disp('Press the blue button to start');
begin = 0;
while (~begin)
    [key_pressed, seconds, key_code] = KbCheck();
    disp(find(key_code))
    if (key_pressed)
        key_number = find(key_code);
        if ismember(key_number,left_hand)
            io64(io_obj, address, LeftPress);
            pause(0.05)
            io64(io_obj, address, 0);
            disp("left_press")
        elseif ismember(key_number,right_hand)
            io64(io_obj, address, RightPress);
            pause(0.05)
            io64(io_obj, address, 0);
            disp("right_press")
        end
%         send_trig = trig_chans(logical(key_code(response_key)));
%         disp(send_trig)
        % send trigbbbyybbyyyybbbb
%         io64(io_obj, address, send_trig);
%         pause(0.05)
%         io64(io_obj, address, 0);
        
        % exit loop if blue key pressed
        
        begin = find(key_code) == KbName(blue_key);
%     break
    end
end
disp('Success!')

%% Some code for during trials that may be useful to someone

% KbQueueFlush(); % removes all keyboard presses
% KbQueueStart();
% 
% while (current_time <= stimulus_duration)
%     [key_pressed, t_first_press, key_code] = KbQueueCheck();
%     if key_pressed
%         response = 1;
%         %                     RT = t_first_press - trial_start_time;
%     end
%     current_time = GetSecs - stim_ontime;
% end
