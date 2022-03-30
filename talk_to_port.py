from psychopy import parallel
from utils.braille_functions import sendStim, toBraille
import numpy as np
import psychopy.core as core
import psychopy.visual
import psychopy.event
from psychopy import core
from psychopy import parallel 

# trigport = parallel.ParallelPort(address='0xDFF8')
# FALSEL_trig = 3
# trigport.setData(FALSEL_trig)
# core.wait(0.02)
# trigport.setData(0)

# win = psychopy.visual.Window(
#     size=[400, 400],
#     units="pix",
#     fullscr=False
# )

# core.wait(5)
# print("Nowwww")
# left_keys = ['b','y']
# right_keys = ['r','g']
# keys = psychopy.event.waitKeys(2, keyList=['b','g','r','y'])

# if keys[0] in left_keys:
#     print("left press")
# elif keys[0] in right_keys:
#     print("right press")


# win.close()

port = parallel.ParallelPort(address=0xDFF8)


pp = np.array(
    [   [1, 1, 0, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0, 1, 1],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1],
    ]
)

# g = np.random.gamma(4, 0.3, 10)
# g = np.round(g)
# g[g>5] = 5
    
# r = np.random.randint(0,pp.shape[0])
# true_patterns = 2
all_down = toBraille(np.zeros([1,8],dtype="int32"),0)
# stimuli = np.array([range(0,pp.shape[0])])
# np.place(stimuli, stimuli==r, np.random.randint(0,5,5)) 
# stimuli = np.random.permutation(stimuli)
# for i in range(0,int(true_patterns)):
#     stimuli[0,np.random.randint(0,pp.shape[0])] = r
    


seq = toBraille(pp[4,:],1)
sendStim(seq,port)
core.wait(10)
sendStim(all_down,port)


# import numpy as np
# import codecs, json 

# a = np.arange(5).reshape(1,5) # a 2 by 5 array
# b = a.tolist() # nested lists with same data, indices
# q = np.arange(10).reshape(2,5)
# q = q.tolist()
# data = {'fieldname':b,'another':q}
# file_path = "test.json" ## your path variable
# json.dump(data, codecs.open(file_path, 'w', encoding='utf-8'), 
#           separators=(',', ':'), 
#           sort_keys=True, 
#           indent=4) ### this saves the array in .json format
