﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on February 17, 2022, at 16:32
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division
from turtle import left

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, parallel
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import psychopy
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'Braille_Stim_Final'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\physicsuser\\Documents\\MATLAB\\gonzalo\\Braille_paradigm\\Braille_Stim_Final.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation
from utils.braille_functions import toBraille, sendStim
# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
new_trial_text = visual.TextStim(win=win, name='new_trial_text',
    text='New trial',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
true_pattern = parallel.ParallelPort(address='0xDFF8 ')
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
cue_right = visual.ShapeStim(
    win=win, name='cue_right', vertices=[(-0.4,0.05),(-0.4,-0.05),(-.2,-0.05),(-.2,-0.1),(0,0),(-.2,0.1),(-.2,0.05)],
    size=(0.25, 0.25),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
cue_left = visual.ShapeStim(
    win=win, name='cue_left', vertices=[(0.4,0.05),(0.4,-0.05),(.2,-0.05),(.2,-0.1),(0,0),(.2,0.1),(.2,0.05)],
    size=(0.25, 0.25),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
pattern1 = parallel.ParallelPort(address='0xDFF8 ')
button_resp1 = keyboard.Keyboard()
pattern2 = parallel.ParallelPort(address='0xDFF8 ')
button_resp2 = keyboard.Keyboard()
pattern3 = parallel.ParallelPort(address='0xDFF8 ')
button_resp3 = keyboard.Keyboard()
pattern4 = parallel.ParallelPort(address='0xDFF8 ')
button_resp4 = keyboard.Keyboard()
pattern5 = parallel.ParallelPort(address='0xDFF8 ')
button_resp5 = keyboard.Keyboard()
cross2 = visual.ShapeStim(
    win=win, name='cross2', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-15.0, interpolate=True)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedback_string = visual.TextStim(win=win, name='feedback_string',
    text='This is the feedback routine',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
Paradigm = data.TrialHandler(nReps=8.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Paradigm')
thisExp.addLoop(Paradigm)  # add the loop to the experiment
thisParadigm = Paradigm.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisParadigm.rgb)
if thisParadigm != None:
    for paramName in thisParadigm:
        exec('{} = thisParadigm[paramName]'.format(paramName))
# Set up paradigm variables
AttendHand = [] # list of cues
pp = np.array(
[   [1, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 1],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1]
]
    ) # Possible braille patterns
patterns = []
all_down = toBraille(np.zeros([1,8],dtype="int32"),0)
# Define trigger channels
START_trig = 1
SAMPLE_trig = 2
# Pattern triggers
TRUE_trig = 4
FALSEL_trig = 3
FALSER_trig = 5

CUELEFT_trig = 6
CUERIGHT_trig = 7
LEFT_PRESS = 8
RIGHT_PRESS = 16
# Create port object to send the triggers
trigport = parallel.ParallelPort(address='0xDFF8 ')
# Create variables to keep track of presses for the feedback
totalpresses = 0
true_patterns_sent = 0
correctpresses = 0
true_pattern_chosen = []
left_keys = ['b','y']
right_keys = ['r','g']

for thisParadigm in Paradigm:
    currentLoop = Paradigm
    # abbreviate parameter names if possible (e.g. rgb = thisParadigm.rgb)
    if thisParadigm != None:
        for paramName in thisParadigm:
            exec('{} = thisParadigm[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    first_set = data.TrialHandler(nReps=10.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='first_set')
    thisExp.addLoop(first_set)  # add the loop to the experiment
    thisFirst_set = first_set.trialList[0]  # so we can initialise stimuli with some values
    # Choose random cues for the 10 trials 1 is for left, 2 is for right
    Cues = np.append(np.ones([int(first_set.nReps/2),1]), 2*np.ones([int(first_set.nReps/2),1]))
    Cues = np.random.permutation(Cues)
    AttendHand.append(Cues)
    # Choose how many target patterns there will be per trial
    g = np.random.gamma(4, 0.3, first_set.nReps)
    g = np.round(g)
    g[g>5] = 5

    # abbreviate parameter names if possible (e.g. rgb = thisFirst_set.rgb)
    if thisFirst_set != None:
        for paramName in thisFirst_set:
            exec('{} = thisFirst_set[paramName]'.format(paramName))
    
    for thisFirst_set in first_set:
        # Choose the patterns to send
        r = np.random.randint(0,pp.shape[0]) # Choose the true pattern
        true_pattern_chosen.append(r)
        true_patterns = g[first_set.thisN]
        stimuli = np.array([range(0,pp.shape[0])])
        np.place(stimuli, stimuli==r, np.random.randint(0,pp.shape[0],pp.shape[0])) 
        stimuli = np.random.permutation(stimuli)
        for i in range(0,int(true_patterns)):
            index = np.random.randint(0,pp.shape[0])
            stimuli[0,index] = r
        patterns.append(stimuli)

        currentLoop = first_set
        # abbreviate parameter names if possible (e.g. rgb = thisFirst_set.rgb)
        if thisFirst_set != None:
            for paramName in thisFirst_set:
                exec('{} = thisFirst_set[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        routineTimer.add(16.000000)
        # update component parameters for each repeat
        button_resp1.keys = []
        button_resp1.rt = []
        _button_resp1_allKeys = []
        button_resp2.keys = []
        button_resp2.rt = []
        _button_resp2_allKeys = []
        button_resp3.keys = []
        button_resp3.rt = []
        _button_resp3_allKeys = []
        button_resp4.keys = []
        button_resp4.rt = []
        _button_resp4_allKeys = []
        button_resp5.keys = []
        button_resp5.rt = []
        _button_resp5_allKeys = []
        # keep track of which components have finished
        trialComponents = [new_trial_text, true_pattern, cross, cue_right, cue_left, pattern1, button_resp1, pattern2, button_resp2, pattern3, button_resp3, pattern4, button_resp4, pattern5, button_resp5, cross2]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        # Log which hand
        if Cues[first_set.thisN] == 2: # Right hand
            logging.data("Right hand cued")
        elif Cues[first_set.thisN] == 1:# Left hand
            logging.data("Left hand cued")
        # -------Run Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *new_trial_text* updates
            if new_trial_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                trigport.setData(START_trig)
                core.wait(0.1)
                trigport.setData(0)
                # keep track of start time/frame for later
                new_trial_text.frameNStart = frameN  # exact frame index
                new_trial_text.tStart = t  # local t and not account for scr refresh
                new_trial_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(new_trial_text, 'tStartRefresh')  # time at next scr refresh
                new_trial_text.setAutoDraw(True)
            if new_trial_text.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 0.7-frameTolerance:
                    # keep track of stop time/frame for later
                    new_trial_text.tStop = t  # not accounting for scr refresh
                    new_trial_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(new_trial_text, 'tStopRefresh')  # time at next scr refresh
                    new_trial_text.setAutoDraw(False)
            # *true_pattern* updates
            if true_pattern.status == NOT_STARTED and t >= 1-frameTolerance:
                # keep track of start time/frame for later
                true_pattern.frameNStart = frameN  # exact frame index
                true_pattern.tStart = t  # local t and not account for scr refresh
                true_pattern.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(true_pattern, 'tStartRefresh')  # time at next scr refresh
                true_pattern.status = STARTED
                # win.callOnFlip(true_pattern.setData, int(1))
            if true_pattern.status == STARTED:
                # Send the true pattern
                seq = toBraille(pp[r,:],0)
                sendStim(seq,pattern1)
                trigport.setData(SAMPLE_trig)
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > true_pattern.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    true_pattern.tStop = t  # not accounting for scr refresh
                    true_pattern.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(true_pattern, 'tStopRefresh')  # time at next scr refresh
                    true_pattern.status = FINISHED
                    # win.callOnFlip(true_pattern.setData, int(0))
            
            # *cross* updates
            if cross.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                cross.frameNStart = frameN  # exact frame index
                cross.tStart = t  # local t and not account for scr refresh
                cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
                cross.setAutoDraw(True)
            if cross.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 3-frameTolerance:
                    # keep track of stop time/frame for later
                    cross.tStop = t  # not accounting for scr refresh
                    cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cross, 'tStopRefresh')  # time at next scr refresh
                    cross.setAutoDraw(False)
                    trigport.setData(0)
                    sendStim(all_down,pattern1) # Put the pins down after 2 seconds
            
            if Cues[first_set.thisN] == 2: #Right hand hand
                # *cue_right* updates
                if cue_right.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                    # keep track of start time/frame for later
                    cue_right.frameNStart = frameN  # exact frame index
                    cue_right.tStart = t  # local t and not account for scr refresh
                    cue_right.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cue_right, 'tStartRefresh')  # time at next scr refresh
                    cue_right.setAutoDraw(True)
                    trigport.setData(CUERIGHT_trig)
                if cue_right.status == STARTED:
                    # is it time to stop? (based on local clock)
                    if tThisFlip > 6-frameTolerance:
                        # keep track of stop time/frame for later
                        cue_right.tStop = t  # not accounting for scr refresh
                        cue_right.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(cue_right, 'tStopRefresh')  # time at next scr refresh
                        cue_right.setAutoDraw(False)
                        trigport.setData(0)
            elif Cues[first_set.thisN] ==1: #Left hand
                # *cue_left* updates
                if cue_left.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                    # keep track of start time/frame for later
                    cue_left.frameNStart = frameN  # exact frame index
                    cue_left.tStart = t  # local t and not account for scr refresh
                    cue_left.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cue_left, 'tStartRefresh')  # time at next scr refresh
                    cue_left.setAutoDraw(True)
                    trigport.setData(CUELEFT_trig)
                if cue_left.status == STARTED:
                    # is it time to stop? (based on local clock)
                    if tThisFlip > 6-frameTolerance:
                        # keep track of stop time/frame for later
                        cue_left.tStop = t  # not accounting for scr refresh
                        cue_left.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(cue_left, 'tStopRefresh')  # time at next scr refresh
                        cue_left.setAutoDraw(False)
                        trigport.setData(0)
            # *pattern1* updates
            if pattern1.status == NOT_STARTED and t >= 7-frameTolerance:
                logging.data("Sending pattern 1")
                leftright = np.random.randint(1,3)
                logging.data("The trial number is ")
                if stimuli[0,0] == r and Cues[first_set.thisN] == leftright:
                    logging.data("True pattern sent!")
                    true_patterns_sent += 1
                    trigport.setData(TRUE_trig)
                else:
                    if leftright == 1:
                        logging.data("False left")
                        trigport.setData(FALSEL_trig)
                    elif leftright == 2:
                        logging.data("False right")
                        trigport.setData(FALSER_trig)
                core.wait(0.01)
                trigport.setData(0)
                seq = toBraille(pp[stimuli[0,0],:],leftright)
                sendStim(seq,pattern1)
                # keep track of start time/frame for later
                pattern1.frameNStart = frameN  # exact frame index
                pattern1.tStart = t  # local t and not account for scr refresh
                pattern1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pattern1, 'tStartRefresh')  # time at next scr refresh
                pattern1.status = STARTED
                # win.callOnFlip(pattern1.setData, int(1))
            if pattern1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > pattern1.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    pattern1.tStop = t  # not accounting for scr refresh
                    pattern1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(pattern1, 'tStopRefresh')  # time at next scr refresh
                    pattern1.status = FINISHED
                    sendStim(all_down,pattern1)
                    # win.callOnFlip(pattern1.setData, int(0))
            
            # *button_resp1* updates
            waitOnFlip = False
            if button_resp1.status == NOT_STARTED and tThisFlip >= 7.1-frameTolerance:
                # keep track of start time/frame for later
                button_resp1.frameNStart = frameN  # exact frame index
                button_resp1.tStart = t  # local t and not account for scr refresh
                button_resp1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_resp1, 'tStartRefresh')  # time at next scr refresh
                button_resp1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(button_resp1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(button_resp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if button_resp1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > button_resp1.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    button_resp1.tStop = t  # not accounting for scr refresh
                    button_resp1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(button_resp1, 'tStopRefresh')  # time at next scr refresh
                    button_resp1.status = FINISHED
            if button_resp1.status == STARTED and not waitOnFlip:
                theseKeys = button_resp1.getKeys(keyList=['b', 'g', 'r', 'y'], waitRelease=False)
                _button_resp1_allKeys.extend(theseKeys)
                if len(_button_resp1_allKeys):
                    button_resp1.keys = _button_resp1_allKeys[0].name  # just the first key pressed
                    totalpresses += 1
                    if button_resp1.keys in left_keys:
                        trigport.setData(LEFT_PRESS)
                        logging.data("left press")
                        if stimuli[0,0] == r and leftright == 1:
                            correctpresses += 1
                    elif button_resp1.keys in right_keys:
                        trigport.setData(RIGHT_PRESS)
                        logging.data("right press")
                        if stimuli[0,0] == r and leftright == 2:
                            correctpresses += 1
                    core.wait(0.015)
                    trigport.setData(0)
                    button_resp1.rt = _button_resp1_allKeys[0].rt
                    _button_resp1_allKeys = [] #Reset the list
            # *pattern2* updates
            if pattern2.status == NOT_STARTED and t >= 8.1-frameTolerance:
                logging.data("Sending pattern 2")
                leftright = np.random.randint(1,3)
                if stimuli[0,1] == r and Cues[first_set.thisN] == leftright:
                    logging.data("True pattern sent!")
                    true_patterns_sent += 1
                    trigport.setData(TRUE_trig)
                else:
                    if leftright == 1:
                        logging.data("False left")
                        trigport.setData(FALSEL_trig)
                    elif leftright == 2:
                        logging.data("False right")
                        trigport.setData(FALSER_trig)
                core.wait(0.02)
                trigport.setData(0)
                seq = toBraille(pp[stimuli[0,1],:],leftright)
                sendStim(seq,pattern2)
                # keep track of start time/frame for later
                pattern2.frameNStart = frameN  # exact frame index
                pattern2.tStart = t  # local t and not account for scr refresh
                pattern2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pattern2, 'tStartRefresh')  # time at next scr refresh
                pattern2.status = STARTED
                # win.callOnFlip(pattern2.setData, int(1))
            if pattern2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > pattern2.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    pattern2.tStop = t  # not accounting for scr refresh
                    pattern2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(pattern2, 'tStopRefresh')  # time at next scr refresh
                    pattern2.status = FINISHED
                    sendStim(all_down,pattern1)
                    # win.callOnFlip(pattern2.setData, int(0))
            
            # *button_resp2* updates
            waitOnFlip = False
            if button_resp2.status == NOT_STARTED and tThisFlip >= 8.2-frameTolerance:
                # keep track of start time/frame for later
                button_resp2.frameNStart = frameN  # exact frame index
                button_resp2.tStart = t  # local t and not account for scr refresh
                button_resp2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_resp2, 'tStartRefresh')  # time at next scr refresh
                button_resp2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(button_resp2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(button_resp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if button_resp2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > button_resp2.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    button_resp2.tStop = t  # not accounting for scr refresh
                    button_resp2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(button_resp2, 'tStopRefresh')  # time at next scr refresh
                    button_resp2.status = FINISHED
            if button_resp2.status == STARTED and not waitOnFlip:
                theseKeys = button_resp2.getKeys(keyList=['b', 'g', 'r', 'y'], waitRelease=False)
                _button_resp2_allKeys.extend(theseKeys)
                if len(_button_resp2_allKeys):
                    button_resp2.keys = _button_resp2_allKeys[0].name  # just the first key pressed
                    totalpresses += 1
                    if button_resp2.keys in left_keys:
                        trigport.setData(LEFT_PRESS)
                        logging.data("left press")
                        if stimuli[0,1] == r and leftright == 1:
                            correctpresses += 1
                    elif button_resp2.keys in right_keys:
                        trigport.setData(RIGHT_PRESS)
                        logging.data("right press")
                        if stimuli[0,1] == r and leftright == 2:
                            correctpresses += 1
                    core.wait(0.015)
                    trigport.setData(0)
                    button_resp2.rt = _button_resp2_allKeys[0].rt
                    _button_resp2_allKeys = [] # Reset the list
                    
            # *pattern3* updates
            if pattern3.status == NOT_STARTED and t >= 9.2-frameTolerance:
                logging.data("Sending pattern 3")
                leftright = np.random.randint(1,3)
                if stimuli[0,2] == r and Cues[first_set.thisN] == leftright:
                    logging.data("True pattern sent!")
                    true_patterns_sent += 1
                    trigport.setData(TRUE_trig)
                else:
                    if leftright == 1:
                        logging.data("False left")
                        trigport.setData(FALSEL_trig)
                    elif leftright == 2:
                        logging.data("False right")
                        trigport.setData(FALSER_trig)
                core.wait(0.02)
                trigport.setData(0)
                seq = toBraille(pp[stimuli[0,2],:],leftright)
                sendStim(seq,pattern3)
                # keep track of start time/frame for later
                pattern3.frameNStart = frameN  # exact frame index
                pattern3.tStart = t  # local t and not account for scr refresh
                pattern3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pattern3, 'tStartRefresh')  # time at next scr refresh
                pattern3.status = STARTED
                # win.callOnFlip(pattern3.setData, int(1))
            if pattern3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > pattern3.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    pattern3.tStop = t  # not accounting for scr refresh
                    pattern3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(pattern3, 'tStopRefresh')  # time at next scr refresh
                    pattern3.status = FINISHED
                    sendStim(all_down,pattern1)
                    # win.callOnFlip(pattern3.setData, int(0))
            
            # *button_resp3* updates
            waitOnFlip = False
            if button_resp3.status == NOT_STARTED and tThisFlip >= 9.3-frameTolerance:
                # keep track of start time/frame for later
                button_resp3.frameNStart = frameN  # exact frame index
                button_resp3.tStart = t  # local t and not account for scr refresh
                button_resp3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_resp3, 'tStartRefresh')  # time at next scr refresh
                button_resp3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(button_resp3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(button_resp3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if button_resp3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > button_resp3.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    button_resp3.tStop = t  # not accounting for scr refresh
                    button_resp3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(button_resp3, 'tStopRefresh')  # time at next scr refresh
                    button_resp3.status = FINISHED
            if button_resp3.status == STARTED and not waitOnFlip:
                theseKeys = button_resp3.getKeys(keyList=['b', 'g', 'r', 'y'], waitRelease=False)
                _button_resp3_allKeys.extend(theseKeys)
                if len(_button_resp3_allKeys):
                    button_resp3.keys = _button_resp3_allKeys[0].name  # just the first key pressed
                    totalpresses += 1
                    if button_resp3.keys in left_keys:
                        trigport.setData(LEFT_PRESS)
                        logging.data("left press")
                        if stimuli[0,2] == r and leftright == 1:
                            correctpresses += 1
                    elif button_resp3.keys in right_keys:
                        trigport.setData(RIGHT_PRESS)
                        logging.data("right press")
                        if stimuli[0,2] == r and leftright == 2:
                            correctpresses += 1
                    core.wait(0.015)
                    trigport.setData(0)
                    button_resp3.rt = _button_resp3_allKeys[0].rt
                    _button_resp3_allKeys = [] #Reset the list
            # *pattern4* updates
            if pattern4.status == NOT_STARTED and t >= 10.3-frameTolerance:
                logging.data("Sending pattern 4")
                leftright = np.random.randint(1,3)
                if stimuli[0,3] == r and Cues[first_set.thisN] == leftright:
                    logging.data("True pattern sent!")
                    true_patterns_sent += 1
                    trigport.setData(TRUE_trig)
                else:
                    if leftright == 1:
                        logging.data("False left")
                        trigport.setData(FALSEL_trig)
                    elif leftright == 2:
                        logging.data("False right")
                        trigport.setData(FALSER_trig)
                core.wait(0.02)
                trigport.setData(0)
                seq = toBraille(pp[stimuli[0,3],:],leftright)
                sendStim(seq,pattern4)
                # keep track of start time/frame for later
                pattern4.frameNStart = frameN  # exact frame index
                pattern4.tStart = t  # local t and not account for scr refresh
                pattern4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pattern4, 'tStartRefresh')  # time at next scr refresh
                pattern4.status = STARTED
                # win.callOnFlip(pattern4.setData, int(1))
            if pattern4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > pattern4.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    pattern4.tStop = t  # not accounting for scr refresh
                    pattern4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(pattern4, 'tStopRefresh')  # time at next scr refresh
                    pattern4.status = FINISHED
                    sendStim(all_down,pattern1)
                    # win.callOnFlip(pattern4.setData, int(0))
            
            # *button_resp4* updates
            waitOnFlip = False
            if button_resp4.status == NOT_STARTED and tThisFlip >= 10.4-frameTolerance:
                # keep track of start time/frame for later
                button_resp4.frameNStart = frameN  # exact frame index
                button_resp4.tStart = t  # local t and not account for scr refresh
                button_resp4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_resp4, 'tStartRefresh')  # time at next scr refresh
                button_resp4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(button_resp4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(button_resp4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if button_resp4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > button_resp4.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    button_resp4.tStop = t  # not accounting for scr refresh
                    button_resp4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(button_resp4, 'tStopRefresh')  # time at next scr refresh
                    button_resp4.status = FINISHED
            if button_resp4.status == STARTED and not waitOnFlip:
                theseKeys = button_resp4.getKeys(keyList=['b', 'g', 'r', 'y'], waitRelease=False)
                _button_resp4_allKeys.extend(theseKeys)
                if len(_button_resp4_allKeys):
                    button_resp4.keys = _button_resp4_allKeys[0].name  # just the first key pressed
                    totalpresses += 1
                    if button_resp4.keys in left_keys:
                        trigport.setData(LEFT_PRESS)
                        logging.data("left press")
                        if stimuli[0,3] == r and leftright == 1:
                            correctpresses += 1
                    elif button_resp4.keys in right_keys:
                        trigport.setData(RIGHT_PRESS)
                        logging.data("right press")
                        if stimuli[0,3] == r and leftright == 2:
                            correctpresses += 1
                    core.wait(0.015)
                    trigport.setData(0)
                    button_resp4.rt = _button_resp4_allKeys[0].rt
                    _button_resp4_allKeys = [] #Reset the list
                    
            # *pattern5* updates
            if pattern5.status == NOT_STARTED and t >= 11.4-frameTolerance:
                logging.data("Sending pattern 5")
                leftright = np.random.randint(1,3)
                if stimuli[0,4] == r and Cues[first_set.thisN] == leftright:
                    logging.data("True pattern sent!")
                    true_patterns_sent += 1
                    trigport.setData(TRUE_trig)
                else:
                    if leftright == 1:
                        logging.data("False left")
                        trigport.setData(FALSEL_trig)
                    elif leftright == 2:
                        logging.data("False right")
                        trigport.setData(FALSER_trig)
                core.wait(0.02)
                trigport.setData(0)
                seq = toBraille(pp[stimuli[0,4],:],leftright)
                sendStim(seq,pattern5)
                # keep track of start time/frame for later
                pattern5.frameNStart = frameN  # exact frame index
                pattern5.tStart = t  # local t and not account for scr refresh
                pattern5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pattern5, 'tStartRefresh')  # time at next scr refresh
                pattern5.status = STARTED
                # win.callOnFlip(pattern5.setData, int(1))
            if pattern5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > pattern5.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    pattern5.tStop = t  # not accounting for scr refresh
                    pattern5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(pattern5, 'tStopRefresh')  # time at next scr refresh
                    pattern5.status = FINISHED
                    sendStim(all_down,pattern1)
                    # win.callOnFlip(pattern5.setData, int(0))
            
            # *button_resp5* updates
            waitOnFlip = False
            if button_resp5.status == NOT_STARTED and tThisFlip >= 11.5-frameTolerance:
                # keep track of start time/frame for later
                button_resp5.frameNStart = frameN  # exact frame index
                button_resp5.tStart = t  # local t and not account for scr refresh
                button_resp5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_resp5, 'tStartRefresh')  # time at next scr refresh
                button_resp5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(button_resp5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(button_resp5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if button_resp5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > button_resp5.tStartRefresh + 1-frameTolerance:
                    # keep track of sexit()
                    # op time/frame for later
                    button_resp5.tStop = t  # not accounting for scr refresh
                    button_resp5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(button_resp5, 'tStopRefresh')  # time at next scr refresh
                    button_resp5.status = FINISHED
            if button_resp5.status == STARTED and not waitOnFlip:
                theseKeys = button_resp5.getKeys(keyList=['b', 'g', 'r', 'y'], waitRelease=False)
                _button_resp5_allKeys.extend(theseKeys)
                if len(_button_resp5_allKeys):
                    button_resp5.keys = _button_resp5_allKeys[0].name  # just the first key pressed
                    totalpresses += 1
                    if button_resp5.keys in left_keys:
                        trigport.setData(LEFT_PRESS)
                        logging.data("left press")
                        if stimuli[0,4] == r and leftright == 1:
                            correctpresses += 1
                    elif button_resp5.keys in right_keys:
                        trigport.setData(RIGHT_PRESS)
                        logging.data("right press")
                        if stimuli[0,4] == r and leftright == 2:
                            correctpresses += 1
                    core.wait(0.015)
                    trigport.setData(0)
                    button_resp5.rt = _button_resp5_allKeys[0].rt
                    _button_resp5_allKeys = [] # Reset list
                    
                    
            
            # *cross2* updates
            if cross2.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
                # keep track of start time/frame for later
                cross2.frameNStart = frameN  # exact frame index
                cross2.tStart = t  # local t and not account for scr refresh
                cross2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross2, 'tStartRefresh')  # time at next scr refresh
                cross2.setAutoDraw(True)
            if cross2.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 16-frameTolerance:
                    # keep track of stop time/frame for later
                    cross2.tStop = t  # not accounting for scr refresh
                    cross2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cross2, 'tStopRefresh')  # time at next scr refresh
                    cross2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        first_set.addData('new_trial_text.started', new_trial_text.tStartRefresh)
        first_set.addData('new_trial_text.stopped', new_trial_text.tStopRefresh)
        if true_pattern.status == STARTED:
            win.callOnFlip(true_pattern.setData, int(0))
        first_set.addData('true_pattern.started', true_pattern.tStart)
        first_set.addData('true_pattern.stopped', true_pattern.tStop)
        first_set.addData('cross.started', cross.tStartRefresh)
        first_set.addData('cross.stopped', cross.tStopRefresh)
        first_set.addData('cue_right.started', cue_right.tStartRefresh)
        first_set.addData('cue_right.stopped', cue_right.tStopRefresh)
        first_set.addData('cue_left.started', cue_left.tStartRefresh)
        first_set.addData('cue_left.stopped', cue_left.tStopRefresh)
        if pattern1.status == STARTED:
            win.callOnFlip(pattern1.setData, int(0))
        first_set.addData('pattern1.started', pattern1.tStart)
        first_set.addData('pattern1.stopped', pattern1.tStop)
        # check responses
        if button_resp1.keys in ['', [], None]:  # No response was made
            button_resp1.keys = None
        first_set.addData('button_resp1.keys',button_resp1.keys)
        if button_resp1.keys != None:  # we had a response
            first_set.addData('button_resp1.rt', button_resp1.rt)
        first_set.addData('button_resp1.started', button_resp1.tStartRefresh)
        first_set.addData('button_resp1.stopped', button_resp1.tStopRefresh)
        if pattern2.status == STARTED:
            win.callOnFlip(pattern2.setData, int(0))
        first_set.addData('pattern2.started', pattern2.tStart)
        first_set.addData('pattern2.stopped', pattern2.tStop)
        # check responses
        if button_resp2.keys in ['', [], None]:  # No response was made
            button_resp2.keys = None
        first_set.addData('button_resp2.keys',button_resp2.keys)
        if button_resp2.keys != None:  # we had a response
            first_set.addData('button_resp2.rt', button_resp2.rt)
        first_set.addData('button_resp2.started', button_resp2.tStartRefresh)
        first_set.addData('button_resp2.stopped', button_resp2.tStopRefresh)
        if pattern3.status == STARTED:
            win.callOnFlip(pattern3.setData, int(0))
        first_set.addData('pattern3.started', pattern3.tStart)
        first_set.addData('pattern3.stopped', pattern3.tStop)
        # check responses
        if button_resp3.keys in ['', [], None]:  # No response was made
            button_resp3.keys = None
        first_set.addData('button_resp3.keys',button_resp3.keys)
        if button_resp3.keys != None:  # we had a response
            first_set.addData('button_resp3.rt', button_resp3.rt)
        first_set.addData('button_resp3.started', button_resp3.tStartRefresh)
        first_set.addData('button_resp3.stopped', button_resp3.tStopRefresh)
        if pattern4.status == STARTED:
            win.callOnFlip(pattern4.setData, int(0))
        first_set.addData('pattern4.started', pattern4.tStart)
        first_set.addData('pattern4.stopped', pattern4.tStop)
        # check responses
        if button_resp4.keys in ['', [], None]:  # No response was made
            button_resp4.keys = None
        first_set.addData('button_resp4.keys',button_resp4.keys)
        if button_resp4.keys != None:  # we had a response
            first_set.addData('button_resp4.rt', button_resp4.rt)
        first_set.addData('button_resp4.started', button_resp4.tStartRefresh)
        first_set.addData('button_resp4.stopped', button_resp4.tStopRefresh)
        if pattern5.status == STARTED:
            win.callOnFlip(pattern5.setData, int(0))
        first_set.addData('pattern5.started', pattern5.tStart)
        first_set.addData('pattern5.stopped', pattern5.tStop)
        # check responses
        if button_resp5.keys in ['', [], None]:  # No response was made
            button_resp5.keys = None
        first_set.addData('button_resp5.keys',button_resp5.keys)
        if button_resp5.keys != None:  # we had a response
            first_set.addData('button_resp5.rt', button_resp5.rt)
        first_set.addData('button_resp5.started', button_resp5.tStartRefresh)
        first_set.addData('button_resp5.stopped', button_resp5.tStopRefresh)
        first_set.addData('cross2.started', cross2.tStartRefresh)
        first_set.addData('cross2.stopped', cross2.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 10.0 repeats of 'first_set'
    
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(16.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    feedbackComponents = [feedback_string]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_string* updates
        if feedback_string.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_string.frameNStart = frameN  # exact frame index
            feedback_string.tStart = t  # local t and not account for scr refresh
            feedback_string.tStartRefresh = tThisFlipGlobal  # on global time
            feedback_string.text = "Total button presses {} \n You got {} out {} true patterns sent".format(totalpresses, correctpresses, true_patterns_sent)
            win.timeOnFlip(feedback_string, 'tStartRefresh')  # time at next scr refresh
            feedback_string.setAutoDraw(True)
        if feedback_string.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_string.tStartRefresh + 16-frameTolerance:
                # keep track of stop time/frame for later
                feedback_string.tStop = t  # not accounting for scr refresh
                feedback_string.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_string, 'tStopRefresh')  # time at next scr refresh
                feedback_string.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Paradigm.addData('feedback_string.started', feedback_string.tStartRefresh)
    Paradigm.addData('feedback_string.stopped', feedback_string.tStopRefresh)
    thisExp.nextEntry()
    #Reset counters
    totalpresses = 0
    true_patterns_sent = 0
    correctpresses = 0
# completed 8.0 repeats of 'Paradigm'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# Write paradigm data to json file
All_Cues = np.concatenate(AttendHand, axis = 0)
np.savetxt("All_Cues.csv", All_Cues, delimiter=",")
true_pattern_chosen = np.concatenate(true_pattern_chosen)
np.savetxt("true_patterns_chose.csv", true_pattern_chosen, delimiter=",")
All_patterns_sent = np.concatenate(patterns, axis =0)
np.savetxt("All_patterns_sent.csv", All_patterns_sent, delimiter=",")
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
