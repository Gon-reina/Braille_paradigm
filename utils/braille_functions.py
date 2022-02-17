import numpy as np
import psychopy.core as core

def toBraille(seq,hand):
    pulse = []
    data = 32
    clk = 64
    stb = 128
    for pin in np.nditer(seq):
        pulse.append(np.array([[pin*data, clk+ (pin*data)]]))
    pulse = np.concatenate(pulse, axis=1)
    if hand == 1: # Left hand blue sticker
        pulse = np.append(np.tile(np.array([[0, clk]]), (1,8)), pulse, axis=1)
    elif hand == 2: # Right hand 
        pulse = np.append(pulse, np.tile(np.array([[0, clk]]), (1,8)), axis=1)
    elif hand == 0: #Both hands
        pulse = np.append(pulse,pulse, axis=1)
    pulse = np.append(pulse,np.array([[stb]]),axis=1)
    return pulse

def sendStim(seq, port):
    # Send the data to the port
    for pin in np.nditer(seq):
        port.setData(int(pin))
        core.wait(0.005)
        port.setData(0)
