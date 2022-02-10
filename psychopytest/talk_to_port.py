# from psychopy import parallel
from utils.braille_functions import toBraille
import numpy as np
import psychopy.core as core


# port = parallel.ParallelPort(address=0xDFF8)


pp = np.array(
    [   [1, 1, 0, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0, 1, 1],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1],
    ]
)

r = np.random.randint(0,pp.shape[0],5)
all_down = toBraille(np.zeros([1,8],dtype="int32"),0)
seq = toBraille(pp[4,:],0)
# sendStim(seq,port)
core.wait(10)
# sendStim(all_down,port)
