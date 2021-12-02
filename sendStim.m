function sendStim(seq,ioObjStim ,PortAddress)
% Sends sequence to stimulators through parallel port 
    for i = 1:33
        outp(PortAddress,seq(i));
        outp(PortAddress,0);
        pause(0.001)
    end
end