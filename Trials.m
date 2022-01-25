classdef Trials

   properties (Constant)
       N = 80 % Number of trials
       NStims = 5 %Number of Stimuli per trial
       patterns = [ 1 1 0 0 1 1 0 0  %Allowed patterns
                    0 0 1 1 0 0 1 1
                    0 1 1 0 0 1 1 0
                    1 1 1 1 0 0 0 0
                    0 0 0 0 1 1 1 1];
       Npatterns = size(Trials.patterns,1) % Number of allowed patterns
   end
   
    methods
        function obj = Trials
            disp("Constructor called")
        end
    end
end