function sendStim(seq,ioObjStim ,PortAddressStim)
% Sends sequence to stimulators through parallel port 
    for ii = 1:33
        outp(PortAddressStim,seq(ii));
        outp(PortAddressStim,0);
%         io64(ioObjStim,PortAddressStim,seq(ii));   
%         io64(ioObjStim,PortAddressStim,0);  
    end
end