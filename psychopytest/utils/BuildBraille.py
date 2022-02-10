import numpy as np

seq = np.array([[1, 1, 0, 0, 1, 1, 0, 0]])

def toBraille(seq,hand):
    pulse = []
    data = 32
    clk = 64
    stb = 128
    for pin in np.nditer(seq):
        pulse.append(np.array([[pin*data, clk+ (pin*data)]]))
    pulse = np.concatenate(pulse, axis=1)
    if hand == 1: # Left hand blue sticker
        pulse = np.concatenate(np.tile(np.array([[0, clk]]), (1,8)), pulse, axis=1)
    elif hand == 2: # Right hand 
        pulse = np.concatenate(pulse, np.tile(np.array([[0, clk]]), (1,8)), axis=1)
    elif hand == 0: #Both hands
        pulse = np.append(pulse,pulse, axis=1)
    pulse = np.append(pulse,np.array([[stb]]),axis=1)
    return pulse


pulse = toBraille(seq, 0)
        

pp = np.array(
    [   [1, 1, 0, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0, 1, 1],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1],
    ]
)