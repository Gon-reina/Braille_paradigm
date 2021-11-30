function [] = SendTrig(PortNum,TrigVal)

outp(PortNum,TrigVal)
pause(0.025)
outp(PortNum,0)
