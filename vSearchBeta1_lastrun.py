#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on June 17, 2020, at 19:16
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'vSearchBeta1'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Andrew\\Documents\\Work\\Projects\\v-search-beta1\\vSearchBeta1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1088, 614], fullscr=True, screen=0, 
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

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruction1"
instruction1Clock = core.Clock()
instr1 = visual.TextStim(win=win, name='instr1',
    text='In this task you will see sets of shapes made of four different shapes as outlined below. Only press the ‘s’ key if you see the upright “T” shape, which is the last shape. Otherwise, press the ‘k’ key. There will be 6, 12, or 18 shapes to observe in each trial. Press ‘space’ to continue.',
    font='Arial',
    pos=[0,0.1], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyResp1 = keyboard.Keyboard()
l1ex1 = visual.ImageStim(
    win=win,
    name='l1ex1', 
    image='L1.png', mask=None,
    ori=0, pos=(-0.3, -0.3), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
l2ex1 = visual.ImageStim(
    win=win,
    name='l2ex1', 
    image='L2.png', mask=None,
    ori=0, pos=(-0.1, -0.3), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
t1ex1 = visual.ImageStim(
    win=win,
    name='t1ex1', 
    image='T1.png', mask=None,
    ori=0, pos=(0.1, -0.3), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
tTex1 = visual.ImageStim(
    win=win,
    name='tTex1', 
    image='TT.png', mask=None,
    ori=0, pos=(0.3, -0.3), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
trialFix = visual.TextStim(win=win, name='trialFix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trialL11 = visual.ImageStim(
    win=win,
    name='trialL11', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
trialL12 = visual.ImageStim(
    win=win,
    name='trialL12', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
trialL21 = visual.ImageStim(
    win=win,
    name='trialL21', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
trialL22 = visual.ImageStim(
    win=win,
    name='trialL22', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
trialT11 = visual.ImageStim(
    win=win,
    name='trialT11', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
trialT12 = visual.ImageStim(
    win=win,
    name='trialT12', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
trialL13 = visual.ImageStim(
    win=win,
    name='trialL13', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
trialL14 = visual.ImageStim(
    win=win,
    name='trialL14', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
trialL23 = visual.ImageStim(
    win=win,
    name='trialL23', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
trialL24 = visual.ImageStim(
    win=win,
    name='trialL24', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
trialT13 = visual.ImageStim(
    win=win,
    name='trialT13', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
trialT14 = visual.ImageStim(
    win=win,
    name='trialT14', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
trialL15 = visual.ImageStim(
    win=win,
    name='trialL15', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-13.0)
trialL16 = visual.ImageStim(
    win=win,
    name='trialL16', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
trialL25 = visual.ImageStim(
    win=win,
    name='trialL25', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
trialL26 = visual.ImageStim(
    win=win,
    name='trialL26', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
trialT15 = visual.ImageStim(
    win=win,
    name='trialT15', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
trialT16 = visual.ImageStim(
    win=win,
    name='trialT16', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
trialTT = visual.ImageStim(
    win=win,
    name='trialTT', 
    image='TT.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
trialResp = keyboard.Keyboard()

# Initialize components for Routine "instruction2"
instruction2Clock = core.Clock()
instr2 = visual.TextStim(win=win, name='instr2',
    text='A quick break before the next set of trials. Remember, only press the ‘s’ key if you see the upright “T” shape, which is the last shape below. Otherwise, press the ‘k’ key. There will be 6, 12, or 18 shapes to observe in each trial. Press ‘space’ to continue.',
    font='Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyResp2 = keyboard.Keyboard()
l1ex2 = visual.ImageStim(
    win=win,
    name='l1ex2', 
    image='L1.png', mask=None,
    ori=0, pos=(-0.3, -0.3), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
l2ex2 = visual.ImageStim(
    win=win,
    name='l2ex2', 
    image='L2.png', mask=None,
    ori=0, pos=(-0.1, -0.3), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
t1ex2 = visual.ImageStim(
    win=win,
    name='t1ex2', 
    image='T1.png', mask=None,
    ori=0, pos=(0.1, -0.3), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
tTex2 = visual.ImageStim(
    win=win,
    name='tTex2', 
    image='TT.png', mask=None,
    ori=0, pos=(0.3, -0.3), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
trialFix = visual.TextStim(win=win, name='trialFix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trialL11 = visual.ImageStim(
    win=win,
    name='trialL11', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
trialL12 = visual.ImageStim(
    win=win,
    name='trialL12', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
trialL21 = visual.ImageStim(
    win=win,
    name='trialL21', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
trialL22 = visual.ImageStim(
    win=win,
    name='trialL22', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
trialT11 = visual.ImageStim(
    win=win,
    name='trialT11', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
trialT12 = visual.ImageStim(
    win=win,
    name='trialT12', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
trialL13 = visual.ImageStim(
    win=win,
    name='trialL13', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
trialL14 = visual.ImageStim(
    win=win,
    name='trialL14', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
trialL23 = visual.ImageStim(
    win=win,
    name='trialL23', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
trialL24 = visual.ImageStim(
    win=win,
    name='trialL24', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
trialT13 = visual.ImageStim(
    win=win,
    name='trialT13', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
trialT14 = visual.ImageStim(
    win=win,
    name='trialT14', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
trialL15 = visual.ImageStim(
    win=win,
    name='trialL15', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-13.0)
trialL16 = visual.ImageStim(
    win=win,
    name='trialL16', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
trialL25 = visual.ImageStim(
    win=win,
    name='trialL25', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
trialL26 = visual.ImageStim(
    win=win,
    name='trialL26', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
trialT15 = visual.ImageStim(
    win=win,
    name='trialT15', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
trialT16 = visual.ImageStim(
    win=win,
    name='trialT16', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
trialTT = visual.ImageStim(
    win=win,
    name='trialTT', 
    image='TT.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
trialResp = keyboard.Keyboard()

# Initialize components for Routine "instruction3"
instruction3Clock = core.Clock()
instr3 = visual.TextStim(win=win, name='instr3',
    text='A quick break before the next set of trials. Remember, only press the ‘s’ key if you see the upright “T” shape, which is the last shape below. Otherwise, press the ‘k’ key. There will be 6, 12, or 18 shapes to observe in each trial. Press ‘space’ to continue.',
    font='Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyResp3 = keyboard.Keyboard()
l1ex3 = visual.ImageStim(
    win=win,
    name='l1ex3', 
    image='L1.png', mask=None,
    ori=0, pos=(-0.3, -0.3), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
l2ex3 = visual.ImageStim(
    win=win,
    name='l2ex3', 
    image='L2.png', mask=None,
    ori=0, pos=(-0.1, -0.3), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
t1ex3 = visual.ImageStim(
    win=win,
    name='t1ex3', 
    image='T1.png', mask=None,
    ori=0, pos=(0.1, -0.3), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
tTex3 = visual.ImageStim(
    win=win,
    name='tTex3', 
    image='TT.png', mask=None,
    ori=0, pos=(0.3, -0.3), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
trialFix = visual.TextStim(win=win, name='trialFix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trialL11 = visual.ImageStim(
    win=win,
    name='trialL11', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
trialL12 = visual.ImageStim(
    win=win,
    name='trialL12', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
trialL21 = visual.ImageStim(
    win=win,
    name='trialL21', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
trialL22 = visual.ImageStim(
    win=win,
    name='trialL22', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
trialT11 = visual.ImageStim(
    win=win,
    name='trialT11', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
trialT12 = visual.ImageStim(
    win=win,
    name='trialT12', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
trialL13 = visual.ImageStim(
    win=win,
    name='trialL13', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
trialL14 = visual.ImageStim(
    win=win,
    name='trialL14', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
trialL23 = visual.ImageStim(
    win=win,
    name='trialL23', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
trialL24 = visual.ImageStim(
    win=win,
    name='trialL24', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
trialT13 = visual.ImageStim(
    win=win,
    name='trialT13', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
trialT14 = visual.ImageStim(
    win=win,
    name='trialT14', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
trialL15 = visual.ImageStim(
    win=win,
    name='trialL15', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-13.0)
trialL16 = visual.ImageStim(
    win=win,
    name='trialL16', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
trialL25 = visual.ImageStim(
    win=win,
    name='trialL25', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
trialL26 = visual.ImageStim(
    win=win,
    name='trialL26', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
trialT15 = visual.ImageStim(
    win=win,
    name='trialT15', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
trialT16 = visual.ImageStim(
    win=win,
    name='trialT16', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
trialTT = visual.ImageStim(
    win=win,
    name='trialTT', 
    image='TT.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
trialResp = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
thanks = visual.TextStim(win=win, name='thanks',
    text='This is the end of the experiment. Thank you for your time. Please remember to return to the questionnaire to carry on with the study. Press ‘space’ to exit.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction1"-------
continueRoutine = True
# update component parameters for each repeat
keyResp1.keys = []
keyResp1.rt = []
_keyResp1_allKeys = []
# keep track of which components have finished
instruction1Components = [instr1, keyResp1, l1ex1, l2ex1, t1ex1, tTex1]
for thisComponent in instruction1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction1"-------
while continueRoutine:
    # get current time
    t = instruction1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr1* updates
    if instr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr1.frameNStart = frameN  # exact frame index
        instr1.tStart = t  # local t and not account for scr refresh
        instr1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr1, 'tStartRefresh')  # time at next scr refresh
        instr1.setAutoDraw(True)
    
    # *keyResp1* updates
    waitOnFlip = False
    if keyResp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyResp1.frameNStart = frameN  # exact frame index
        keyResp1.tStart = t  # local t and not account for scr refresh
        keyResp1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyResp1, 'tStartRefresh')  # time at next scr refresh
        keyResp1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyResp1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyResp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyResp1.status == STARTED and not waitOnFlip:
        theseKeys = keyResp1.getKeys(keyList=['space'], waitRelease=False)
        _keyResp1_allKeys.extend(theseKeys)
        if len(_keyResp1_allKeys):
            keyResp1.keys = _keyResp1_allKeys[-1].name  # just the last key pressed
            keyResp1.rt = _keyResp1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *l1ex1* updates
    if l1ex1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        l1ex1.frameNStart = frameN  # exact frame index
        l1ex1.tStart = t  # local t and not account for scr refresh
        l1ex1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(l1ex1, 'tStartRefresh')  # time at next scr refresh
        l1ex1.setAutoDraw(True)
    
    # *l2ex1* updates
    if l2ex1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        l2ex1.frameNStart = frameN  # exact frame index
        l2ex1.tStart = t  # local t and not account for scr refresh
        l2ex1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(l2ex1, 'tStartRefresh')  # time at next scr refresh
        l2ex1.setAutoDraw(True)
    
    # *t1ex1* updates
    if t1ex1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        t1ex1.frameNStart = frameN  # exact frame index
        t1ex1.tStart = t  # local t and not account for scr refresh
        t1ex1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(t1ex1, 'tStartRefresh')  # time at next scr refresh
        t1ex1.setAutoDraw(True)
    
    # *tTex1* updates
    if tTex1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tTex1.frameNStart = frameN  # exact frame index
        tTex1.tStart = t  # local t and not account for scr refresh
        tTex1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tTex1, 'tStartRefresh')  # time at next scr refresh
        tTex1.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction1"-------
for thisComponent in instruction1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr1.started', instr1.tStartRefresh)
thisExp.addData('instr1.stopped', instr1.tStopRefresh)
thisExp.addData('l1ex1.started', l1ex1.tStartRefresh)
thisExp.addData('l1ex1.stopped', l1ex1.tStopRefresh)
thisExp.addData('l2ex1.started', l2ex1.tStartRefresh)
thisExp.addData('l2ex1.stopped', l2ex1.tStopRefresh)
thisExp.addData('t1ex1.started', t1ex1.tStartRefresh)
thisExp.addData('t1ex1.stopped', t1ex1.tStopRefresh)
thisExp.addData('tTex1.started', tTex1.tStartRefresh)
thisExp.addData('tTex1.stopped', tTex1.tStopRefresh)
# the Routine "instruction1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('vSearchCond1.xlsx'),
    seed=None, name='trials1')
thisExp.addLoop(trials1)  # add the loop to the experiment
thisTrials1 = trials1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials1.rgb)
if thisTrials1 != None:
    for paramName in thisTrials1:
        exec('{} = thisTrials1[paramName]'.format(paramName))

for thisTrials1 in trials1:
    currentLoop = trials1
    # abbreviate parameter names if possible (e.g. rgb = thisTrials1.rgb)
    if thisTrials1 != None:
        for paramName in thisTrials1:
            exec('{} = thisTrials1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    trialL11.setPos([loc1,loc2])
    trialL12.setPos([loc3,loc4])
    trialL21.setPos([loc5,loc6])
    trialL22.setPos([loc7,loc8])
    trialT11.setPos([loc9,loc10])
    trialT12.setPos([loc11,loc12])
    trialL13.setPos((loc13, loc14))
    trialL14.setPos((loc15, loc16))
    trialL23.setPos((loc17, loc18))
    trialL24.setPos((loc19, loc20))
    trialT13.setPos((loc21, loc22))
    trialT14.setPos((loc23, loc24))
    trialL15.setPos((loc25, loc26))
    trialL16.setPos((loc27, loc28))
    trialL25.setPos((loc29, loc30))
    trialL26.setPos((loc31, loc32))
    trialT15.setPos((loc33, loc34))
    trialT16.setPos((loc35, loc36))
    trialTT.setPos([loc37,loc38])
    trialResp.keys = []
    trialResp.rt = []
    _trialResp_allKeys = []
    # keep track of which components have finished
    trialComponents = [trialFix, trialL11, trialL12, trialL21, trialL22, trialT11, trialT12, trialL13, trialL14, trialL23, trialL24, trialT13, trialT14, trialL15, trialL16, trialL25, trialL26, trialT15, trialT16, trialTT, trialResp]
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
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trialFix* updates
        if trialFix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trialFix.frameNStart = frameN  # exact frame index
            trialFix.tStart = t  # local t and not account for scr refresh
            trialFix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialFix, 'tStartRefresh')  # time at next scr refresh
            trialFix.setAutoDraw(True)
        if trialFix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trialFix.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                trialFix.tStop = t  # not accounting for scr refresh
                trialFix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trialFix, 'tStopRefresh')  # time at next scr refresh
                trialFix.setAutoDraw(False)
        
        # *trialL11* updates
        if trialL11.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL11.frameNStart = frameN  # exact frame index
            trialL11.tStart = t  # local t and not account for scr refresh
            trialL11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL11, 'tStartRefresh')  # time at next scr refresh
            trialL11.setAutoDraw(True)
        
        # *trialL12* updates
        if trialL12.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL12.frameNStart = frameN  # exact frame index
            trialL12.tStart = t  # local t and not account for scr refresh
            trialL12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL12, 'tStartRefresh')  # time at next scr refresh
            trialL12.setAutoDraw(True)
        
        # *trialL21* updates
        if trialL21.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL21.frameNStart = frameN  # exact frame index
            trialL21.tStart = t  # local t and not account for scr refresh
            trialL21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL21, 'tStartRefresh')  # time at next scr refresh
            trialL21.setAutoDraw(True)
        
        # *trialL22* updates
        if trialL22.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL22.frameNStart = frameN  # exact frame index
            trialL22.tStart = t  # local t and not account for scr refresh
            trialL22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL22, 'tStartRefresh')  # time at next scr refresh
            trialL22.setAutoDraw(True)
        
        # *trialT11* updates
        if trialT11.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialT11.frameNStart = frameN  # exact frame index
            trialT11.tStart = t  # local t and not account for scr refresh
            trialT11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialT11, 'tStartRefresh')  # time at next scr refresh
            trialT11.setAutoDraw(True)
        
        # *trialT12* updates
        if trialT12.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialT12.frameNStart = frameN  # exact frame index
            trialT12.tStart = t  # local t and not account for scr refresh
            trialT12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialT12, 'tStartRefresh')  # time at next scr refresh
            trialT12.setAutoDraw(True)
        
        # *trialL13* updates
        if trialL13.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL13.frameNStart = frameN  # exact frame index
            trialL13.tStart = t  # local t and not account for scr refresh
            trialL13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL13, 'tStartRefresh')  # time at next scr refresh
            trialL13.setAutoDraw(True)
        
        # *trialL14* updates
        if trialL14.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL14.frameNStart = frameN  # exact frame index
            trialL14.tStart = t  # local t and not account for scr refresh
            trialL14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL14, 'tStartRefresh')  # time at next scr refresh
            trialL14.setAutoDraw(True)
        
        # *trialL23* updates
        if trialL23.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL23.frameNStart = frameN  # exact frame index
            trialL23.tStart = t  # local t and not account for scr refresh
            trialL23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL23, 'tStartRefresh')  # time at next scr refresh
            trialL23.setAutoDraw(True)
        
        # *trialL24* updates
        if trialL24.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL24.frameNStart = frameN  # exact frame index
            trialL24.tStart = t  # local t and not account for scr refresh
            trialL24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL24, 'tStartRefresh')  # time at next scr refresh
            trialL24.setAutoDraw(True)
        
        # *trialT13* updates
        if trialT13.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialT13.frameNStart = frameN  # exact frame index
            trialT13.tStart = t  # local t and not account for scr refresh
            trialT13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialT13, 'tStartRefresh')  # time at next scr refresh
            trialT13.setAutoDraw(True)
        
        # *trialT14* updates
        if trialT14.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialT14.frameNStart = frameN  # exact frame index
            trialT14.tStart = t  # local t and not account for scr refresh
            trialT14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialT14, 'tStartRefresh')  # time at next scr refresh
            trialT14.setAutoDraw(True)
        
        # *trialL15* updates
        if trialL15.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL15.frameNStart = frameN  # exact frame index
            trialL15.tStart = t  # local t and not account for scr refresh
            trialL15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL15, 'tStartRefresh')  # time at next scr refresh
            trialL15.setAutoDraw(True)
        
        # *trialL16* updates
        if trialL16.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL16.frameNStart = frameN  # exact frame index
            trialL16.tStart = t  # local t and not account for scr refresh
            trialL16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL16, 'tStartRefresh')  # time at next scr refresh
            trialL16.setAutoDraw(True)
        
        # *trialL25* updates
        if trialL25.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL25.frameNStart = frameN  # exact frame index
            trialL25.tStart = t  # local t and not account for scr refresh
            trialL25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL25, 'tStartRefresh')  # time at next scr refresh
            trialL25.setAutoDraw(True)
        
        # *trialL26* updates
        if trialL26.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL26.frameNStart = frameN  # exact frame index
            trialL26.tStart = t  # local t and not account for scr refresh
            trialL26.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL26, 'tStartRefresh')  # time at next scr refresh
            trialL26.setAutoDraw(True)
        
        # *trialT15* updates
        if trialT15.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialT15.frameNStart = frameN  # exact frame index
            trialT15.tStart = t  # local t and not account for scr refresh
            trialT15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialT15, 'tStartRefresh')  # time at next scr refresh
            trialT15.setAutoDraw(True)
        
        # *trialT16* updates
        if trialT16.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialT16.frameNStart = frameN  # exact frame index
            trialT16.tStart = t  # local t and not account for scr refresh
            trialT16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialT16, 'tStartRefresh')  # time at next scr refresh
            trialT16.setAutoDraw(True)
        
        # *trialTT* updates
        if trialTT.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialTT.frameNStart = frameN  # exact frame index
            trialTT.tStart = t  # local t and not account for scr refresh
            trialTT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialTT, 'tStartRefresh')  # time at next scr refresh
            trialTT.setAutoDraw(True)
        
        # *trialResp* updates
        waitOnFlip = False
        if trialResp.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialResp.frameNStart = frameN  # exact frame index
            trialResp.tStart = t  # local t and not account for scr refresh
            trialResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialResp, 'tStartRefresh')  # time at next scr refresh
            trialResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trialResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trialResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trialResp.status == STARTED and not waitOnFlip:
            theseKeys = trialResp.getKeys(keyList=['s', 'k', 'w', 'e', 'a', 'd', 'z', 'x', 'i', 'o', 'j', 'm', ',', 'l'], waitRelease=False)
            _trialResp_allKeys.extend(theseKeys)
            if len(_trialResp_allKeys):
                trialResp.keys = _trialResp_allKeys[-1].name  # just the last key pressed
                trialResp.rt = _trialResp_allKeys[-1].rt
                # was this correct?
                if (trialResp.keys == str(corrAns)) or (trialResp.keys == corrAns):
                    trialResp.corr = 1
                else:
                    trialResp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
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
    trials1.addData('trialFix.started', trialFix.tStartRefresh)
    trials1.addData('trialFix.stopped', trialFix.tStopRefresh)
    trials1.addData('trialL11.started', trialL11.tStartRefresh)
    trials1.addData('trialL11.stopped', trialL11.tStopRefresh)
    trials1.addData('trialL12.started', trialL12.tStartRefresh)
    trials1.addData('trialL12.stopped', trialL12.tStopRefresh)
    trials1.addData('trialL21.started', trialL21.tStartRefresh)
    trials1.addData('trialL21.stopped', trialL21.tStopRefresh)
    trials1.addData('trialL22.started', trialL22.tStartRefresh)
    trials1.addData('trialL22.stopped', trialL22.tStopRefresh)
    trials1.addData('trialT11.started', trialT11.tStartRefresh)
    trials1.addData('trialT11.stopped', trialT11.tStopRefresh)
    trials1.addData('trialT12.started', trialT12.tStartRefresh)
    trials1.addData('trialT12.stopped', trialT12.tStopRefresh)
    trials1.addData('trialL13.started', trialL13.tStartRefresh)
    trials1.addData('trialL13.stopped', trialL13.tStopRefresh)
    trials1.addData('trialL14.started', trialL14.tStartRefresh)
    trials1.addData('trialL14.stopped', trialL14.tStopRefresh)
    trials1.addData('trialL23.started', trialL23.tStartRefresh)
    trials1.addData('trialL23.stopped', trialL23.tStopRefresh)
    trials1.addData('trialL24.started', trialL24.tStartRefresh)
    trials1.addData('trialL24.stopped', trialL24.tStopRefresh)
    trials1.addData('trialT13.started', trialT13.tStartRefresh)
    trials1.addData('trialT13.stopped', trialT13.tStopRefresh)
    trials1.addData('trialT14.started', trialT14.tStartRefresh)
    trials1.addData('trialT14.stopped', trialT14.tStopRefresh)
    trials1.addData('trialL15.started', trialL15.tStartRefresh)
    trials1.addData('trialL15.stopped', trialL15.tStopRefresh)
    trials1.addData('trialL16.started', trialL16.tStartRefresh)
    trials1.addData('trialL16.stopped', trialL16.tStopRefresh)
    trials1.addData('trialL25.started', trialL25.tStartRefresh)
    trials1.addData('trialL25.stopped', trialL25.tStopRefresh)
    trials1.addData('trialL26.started', trialL26.tStartRefresh)
    trials1.addData('trialL26.stopped', trialL26.tStopRefresh)
    trials1.addData('trialT15.started', trialT15.tStartRefresh)
    trials1.addData('trialT15.stopped', trialT15.tStopRefresh)
    trials1.addData('trialT16.started', trialT16.tStartRefresh)
    trials1.addData('trialT16.stopped', trialT16.tStopRefresh)
    trials1.addData('trialTT.started', trialTT.tStartRefresh)
    trials1.addData('trialTT.stopped', trialTT.tStopRefresh)
    # check responses
    if trialResp.keys in ['', [], None]:  # No response was made
        trialResp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           trialResp.corr = 1;  # correct non-response
        else:
           trialResp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials1 (TrialHandler)
    trials1.addData('trialResp.keys',trialResp.keys)
    trials1.addData('trialResp.corr', trialResp.corr)
    if trialResp.keys != None:  # we had a response
        trials1.addData('trialResp.rt', trialResp.rt)
    trials1.addData('trialResp.started', trialResp.tStartRefresh)
    trials1.addData('trialResp.stopped', trialResp.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials1'


# ------Prepare to start Routine "instruction2"-------
continueRoutine = True
# update component parameters for each repeat
keyResp2.keys = []
keyResp2.rt = []
_keyResp2_allKeys = []
# keep track of which components have finished
instruction2Components = [instr2, keyResp2, l1ex2, l2ex2, t1ex2, tTex2]
for thisComponent in instruction2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction2"-------
while continueRoutine:
    # get current time
    t = instruction2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr2* updates
    if instr2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr2.frameNStart = frameN  # exact frame index
        instr2.tStart = t  # local t and not account for scr refresh
        instr2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr2, 'tStartRefresh')  # time at next scr refresh
        instr2.setAutoDraw(True)
    
    # *keyResp2* updates
    waitOnFlip = False
    if keyResp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyResp2.frameNStart = frameN  # exact frame index
        keyResp2.tStart = t  # local t and not account for scr refresh
        keyResp2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyResp2, 'tStartRefresh')  # time at next scr refresh
        keyResp2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyResp2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyResp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyResp2.status == STARTED and not waitOnFlip:
        theseKeys = keyResp2.getKeys(keyList=['space'], waitRelease=False)
        _keyResp2_allKeys.extend(theseKeys)
        if len(_keyResp2_allKeys):
            keyResp2.keys = _keyResp2_allKeys[-1].name  # just the last key pressed
            keyResp2.rt = _keyResp2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *l1ex2* updates
    if l1ex2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        l1ex2.frameNStart = frameN  # exact frame index
        l1ex2.tStart = t  # local t and not account for scr refresh
        l1ex2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(l1ex2, 'tStartRefresh')  # time at next scr refresh
        l1ex2.setAutoDraw(True)
    
    # *l2ex2* updates
    if l2ex2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        l2ex2.frameNStart = frameN  # exact frame index
        l2ex2.tStart = t  # local t and not account for scr refresh
        l2ex2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(l2ex2, 'tStartRefresh')  # time at next scr refresh
        l2ex2.setAutoDraw(True)
    
    # *t1ex2* updates
    if t1ex2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        t1ex2.frameNStart = frameN  # exact frame index
        t1ex2.tStart = t  # local t and not account for scr refresh
        t1ex2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(t1ex2, 'tStartRefresh')  # time at next scr refresh
        t1ex2.setAutoDraw(True)
    
    # *tTex2* updates
    if tTex2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tTex2.frameNStart = frameN  # exact frame index
        tTex2.tStart = t  # local t and not account for scr refresh
        tTex2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tTex2, 'tStartRefresh')  # time at next scr refresh
        tTex2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction2"-------
for thisComponent in instruction2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr2.started', instr2.tStartRefresh)
thisExp.addData('instr2.stopped', instr2.tStopRefresh)
thisExp.addData('l1ex2.started', l1ex2.tStartRefresh)
thisExp.addData('l1ex2.stopped', l1ex2.tStopRefresh)
thisExp.addData('l2ex2.started', l2ex2.tStartRefresh)
thisExp.addData('l2ex2.stopped', l2ex2.tStopRefresh)
thisExp.addData('t1ex2.started', t1ex2.tStartRefresh)
thisExp.addData('t1ex2.stopped', t1ex2.tStopRefresh)
thisExp.addData('tTex2.started', tTex2.tStartRefresh)
thisExp.addData('tTex2.stopped', tTex2.tStopRefresh)
# the Routine "instruction2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('vSearchCond2.xlsx'),
    seed=None, name='trials2')
thisExp.addLoop(trials2)  # add the loop to the experiment
thisTrials2 = trials2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
if thisTrials2 != None:
    for paramName in thisTrials2:
        exec('{} = thisTrials2[paramName]'.format(paramName))

for thisTrials2 in trials2:
    currentLoop = trials2
    # abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
    if thisTrials2 != None:
        for paramName in thisTrials2:
            exec('{} = thisTrials2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    trialL11.setPos([loc1,loc2])
    trialL12.setPos([loc3,loc4])
    trialL21.setPos([loc5,loc6])
    trialL22.setPos([loc7,loc8])
    trialT11.setPos([loc9,loc10])
    trialT12.setPos([loc11,loc12])
    trialL13.setPos((loc13, loc14))
    trialL14.setPos((loc15, loc16))
    trialL23.setPos((loc17, loc18))
    trialL24.setPos((loc19, loc20))
    trialT13.setPos((loc21, loc22))
    trialT14.setPos((loc23, loc24))
    trialL15.setPos((loc25, loc26))
    trialL16.setPos((loc27, loc28))
    trialL25.setPos((loc29, loc30))
    trialL26.setPos((loc31, loc32))
    trialT15.setPos((loc33, loc34))
    trialT16.setPos((loc35, loc36))
    trialTT.setPos([loc37,loc38])
    trialResp.keys = []
    trialResp.rt = []
    _trialResp_allKeys = []
    # keep track of which components have finished
    trialComponents = [trialFix, trialL11, trialL12, trialL21, trialL22, trialT11, trialT12, trialL13, trialL14, trialL23, trialL24, trialT13, trialT14, trialL15, trialL16, trialL25, trialL26, trialT15, trialT16, trialTT, trialResp]
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
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trialFix* updates
        if trialFix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trialFix.frameNStart = frameN  # exact frame index
            trialFix.tStart = t  # local t and not account for scr refresh
            trialFix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialFix, 'tStartRefresh')  # time at next scr refresh
            trialFix.setAutoDraw(True)
        if trialFix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trialFix.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                trialFix.tStop = t  # not accounting for scr refresh
                trialFix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trialFix, 'tStopRefresh')  # time at next scr refresh
                trialFix.setAutoDraw(False)
        
        # *trialL11* updates
        if trialL11.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL11.frameNStart = frameN  # exact frame index
            trialL11.tStart = t  # local t and not account for scr refresh
            trialL11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL11, 'tStartRefresh')  # time at next scr refresh
            trialL11.setAutoDraw(True)
        
        # *trialL12* updates
        if trialL12.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL12.frameNStart = frameN  # exact frame index
            trialL12.tStart = t  # local t and not account for scr refresh
            trialL12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL12, 'tStartRefresh')  # time at next scr refresh
            trialL12.setAutoDraw(True)
        
        # *trialL21* updates
        if trialL21.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL21.frameNStart = frameN  # exact frame index
            trialL21.tStart = t  # local t and not account for scr refresh
            trialL21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL21, 'tStartRefresh')  # time at next scr refresh
            trialL21.setAutoDraw(True)
        
        # *trialL22* updates
        if trialL22.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL22.frameNStart = frameN  # exact frame index
            trialL22.tStart = t  # local t and not account for scr refresh
            trialL22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL22, 'tStartRefresh')  # time at next scr refresh
            trialL22.setAutoDraw(True)
        
        # *trialT11* updates
        if trialT11.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialT11.frameNStart = frameN  # exact frame index
            trialT11.tStart = t  # local t and not account for scr refresh
            trialT11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialT11, 'tStartRefresh')  # time at next scr refresh
            trialT11.setAutoDraw(True)
        
        # *trialT12* updates
        if trialT12.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialT12.frameNStart = frameN  # exact frame index
            trialT12.tStart = t  # local t and not account for scr refresh
            trialT12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialT12, 'tStartRefresh')  # time at next scr refresh
            trialT12.setAutoDraw(True)
        
        # *trialL13* updates
        if trialL13.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL13.frameNStart = frameN  # exact frame index
            trialL13.tStart = t  # local t and not account for scr refresh
            trialL13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL13, 'tStartRefresh')  # time at next scr refresh
            trialL13.setAutoDraw(True)
        
        # *trialL14* updates
        if trialL14.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL14.frameNStart = frameN  # exact frame index
            trialL14.tStart = t  # local t and not account for scr refresh
            trialL14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL14, 'tStartRefresh')  # time at next scr refresh
            trialL14.setAutoDraw(True)
        
        # *trialL23* updates
        if trialL23.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL23.frameNStart = frameN  # exact frame index
            trialL23.tStart = t  # local t and not account for scr refresh
            trialL23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL23, 'tStartRefresh')  # time at next scr refresh
            trialL23.setAutoDraw(True)
        
        # *trialL24* updates
        if trialL24.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL24.frameNStart = frameN  # exact frame index
            trialL24.tStart = t  # local t and not account for scr refresh
            trialL24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL24, 'tStartRefresh')  # time at next scr refresh
            trialL24.setAutoDraw(True)
        
        # *trialT13* updates
        if trialT13.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialT13.frameNStart = frameN  # exact frame index
            trialT13.tStart = t  # local t and not account for scr refresh
            trialT13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialT13, 'tStartRefresh')  # time at next scr refresh
            trialT13.setAutoDraw(True)
        
        # *trialT14* updates
        if trialT14.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialT14.frameNStart = frameN  # exact frame index
            trialT14.tStart = t  # local t and not account for scr refresh
            trialT14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialT14, 'tStartRefresh')  # time at next scr refresh
            trialT14.setAutoDraw(True)
        
        # *trialL15* updates
        if trialL15.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL15.frameNStart = frameN  # exact frame index
            trialL15.tStart = t  # local t and not account for scr refresh
            trialL15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL15, 'tStartRefresh')  # time at next scr refresh
            trialL15.setAutoDraw(True)
        
        # *trialL16* updates
        if trialL16.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL16.frameNStart = frameN  # exact frame index
            trialL16.tStart = t  # local t and not account for scr refresh
            trialL16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL16, 'tStartRefresh')  # time at next scr refresh
            trialL16.setAutoDraw(True)
        
        # *trialL25* updates
        if trialL25.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL25.frameNStart = frameN  # exact frame index
            trialL25.tStart = t  # local t and not account for scr refresh
            trialL25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL25, 'tStartRefresh')  # time at next scr refresh
            trialL25.setAutoDraw(True)
        
        # *trialL26* updates
        if trialL26.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL26.frameNStart = frameN  # exact frame index
            trialL26.tStart = t  # local t and not account for scr refresh
            trialL26.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL26, 'tStartRefresh')  # time at next scr refresh
            trialL26.setAutoDraw(True)
        
        # *trialT15* updates
        if trialT15.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialT15.frameNStart = frameN  # exact frame index
            trialT15.tStart = t  # local t and not account for scr refresh
            trialT15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialT15, 'tStartRefresh')  # time at next scr refresh
            trialT15.setAutoDraw(True)
        
        # *trialT16* updates
        if trialT16.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialT16.frameNStart = frameN  # exact frame index
            trialT16.tStart = t  # local t and not account for scr refresh
            trialT16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialT16, 'tStartRefresh')  # time at next scr refresh
            trialT16.setAutoDraw(True)
        
        # *trialTT* updates
        if trialTT.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialTT.frameNStart = frameN  # exact frame index
            trialTT.tStart = t  # local t and not account for scr refresh
            trialTT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialTT, 'tStartRefresh')  # time at next scr refresh
            trialTT.setAutoDraw(True)
        
        # *trialResp* updates
        waitOnFlip = False
        if trialResp.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialResp.frameNStart = frameN  # exact frame index
            trialResp.tStart = t  # local t and not account for scr refresh
            trialResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialResp, 'tStartRefresh')  # time at next scr refresh
            trialResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trialResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trialResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trialResp.status == STARTED and not waitOnFlip:
            theseKeys = trialResp.getKeys(keyList=['s', 'k', 'w', 'e', 'a', 'd', 'z', 'x', 'i', 'o', 'j', 'm', ',', 'l'], waitRelease=False)
            _trialResp_allKeys.extend(theseKeys)
            if len(_trialResp_allKeys):
                trialResp.keys = _trialResp_allKeys[-1].name  # just the last key pressed
                trialResp.rt = _trialResp_allKeys[-1].rt
                # was this correct?
                if (trialResp.keys == str(corrAns)) or (trialResp.keys == corrAns):
                    trialResp.corr = 1
                else:
                    trialResp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
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
    trials2.addData('trialFix.started', trialFix.tStartRefresh)
    trials2.addData('trialFix.stopped', trialFix.tStopRefresh)
    trials2.addData('trialL11.started', trialL11.tStartRefresh)
    trials2.addData('trialL11.stopped', trialL11.tStopRefresh)
    trials2.addData('trialL12.started', trialL12.tStartRefresh)
    trials2.addData('trialL12.stopped', trialL12.tStopRefresh)
    trials2.addData('trialL21.started', trialL21.tStartRefresh)
    trials2.addData('trialL21.stopped', trialL21.tStopRefresh)
    trials2.addData('trialL22.started', trialL22.tStartRefresh)
    trials2.addData('trialL22.stopped', trialL22.tStopRefresh)
    trials2.addData('trialT11.started', trialT11.tStartRefresh)
    trials2.addData('trialT11.stopped', trialT11.tStopRefresh)
    trials2.addData('trialT12.started', trialT12.tStartRefresh)
    trials2.addData('trialT12.stopped', trialT12.tStopRefresh)
    trials2.addData('trialL13.started', trialL13.tStartRefresh)
    trials2.addData('trialL13.stopped', trialL13.tStopRefresh)
    trials2.addData('trialL14.started', trialL14.tStartRefresh)
    trials2.addData('trialL14.stopped', trialL14.tStopRefresh)
    trials2.addData('trialL23.started', trialL23.tStartRefresh)
    trials2.addData('trialL23.stopped', trialL23.tStopRefresh)
    trials2.addData('trialL24.started', trialL24.tStartRefresh)
    trials2.addData('trialL24.stopped', trialL24.tStopRefresh)
    trials2.addData('trialT13.started', trialT13.tStartRefresh)
    trials2.addData('trialT13.stopped', trialT13.tStopRefresh)
    trials2.addData('trialT14.started', trialT14.tStartRefresh)
    trials2.addData('trialT14.stopped', trialT14.tStopRefresh)
    trials2.addData('trialL15.started', trialL15.tStartRefresh)
    trials2.addData('trialL15.stopped', trialL15.tStopRefresh)
    trials2.addData('trialL16.started', trialL16.tStartRefresh)
    trials2.addData('trialL16.stopped', trialL16.tStopRefresh)
    trials2.addData('trialL25.started', trialL25.tStartRefresh)
    trials2.addData('trialL25.stopped', trialL25.tStopRefresh)
    trials2.addData('trialL26.started', trialL26.tStartRefresh)
    trials2.addData('trialL26.stopped', trialL26.tStopRefresh)
    trials2.addData('trialT15.started', trialT15.tStartRefresh)
    trials2.addData('trialT15.stopped', trialT15.tStopRefresh)
    trials2.addData('trialT16.started', trialT16.tStartRefresh)
    trials2.addData('trialT16.stopped', trialT16.tStopRefresh)
    trials2.addData('trialTT.started', trialTT.tStartRefresh)
    trials2.addData('trialTT.stopped', trialTT.tStopRefresh)
    # check responses
    if trialResp.keys in ['', [], None]:  # No response was made
        trialResp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           trialResp.corr = 1;  # correct non-response
        else:
           trialResp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials2 (TrialHandler)
    trials2.addData('trialResp.keys',trialResp.keys)
    trials2.addData('trialResp.corr', trialResp.corr)
    if trialResp.keys != None:  # we had a response
        trials2.addData('trialResp.rt', trialResp.rt)
    trials2.addData('trialResp.started', trialResp.tStartRefresh)
    trials2.addData('trialResp.stopped', trialResp.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials2'


# ------Prepare to start Routine "instruction3"-------
continueRoutine = True
# update component parameters for each repeat
keyResp3.keys = []
keyResp3.rt = []
_keyResp3_allKeys = []
# keep track of which components have finished
instruction3Components = [instr3, keyResp3, l1ex3, l2ex3, t1ex3, tTex3]
for thisComponent in instruction3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction3"-------
while continueRoutine:
    # get current time
    t = instruction3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr3* updates
    if instr3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr3.frameNStart = frameN  # exact frame index
        instr3.tStart = t  # local t and not account for scr refresh
        instr3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr3, 'tStartRefresh')  # time at next scr refresh
        instr3.setAutoDraw(True)
    
    # *keyResp3* updates
    waitOnFlip = False
    if keyResp3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyResp3.frameNStart = frameN  # exact frame index
        keyResp3.tStart = t  # local t and not account for scr refresh
        keyResp3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyResp3, 'tStartRefresh')  # time at next scr refresh
        keyResp3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyResp3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyResp3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyResp3.status == STARTED and not waitOnFlip:
        theseKeys = keyResp3.getKeys(keyList=['space'], waitRelease=False)
        _keyResp3_allKeys.extend(theseKeys)
        if len(_keyResp3_allKeys):
            keyResp3.keys = _keyResp3_allKeys[-1].name  # just the last key pressed
            keyResp3.rt = _keyResp3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *l1ex3* updates
    if l1ex3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        l1ex3.frameNStart = frameN  # exact frame index
        l1ex3.tStart = t  # local t and not account for scr refresh
        l1ex3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(l1ex3, 'tStartRefresh')  # time at next scr refresh
        l1ex3.setAutoDraw(True)
    
    # *l2ex3* updates
    if l2ex3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        l2ex3.frameNStart = frameN  # exact frame index
        l2ex3.tStart = t  # local t and not account for scr refresh
        l2ex3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(l2ex3, 'tStartRefresh')  # time at next scr refresh
        l2ex3.setAutoDraw(True)
    
    # *t1ex3* updates
    if t1ex3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        t1ex3.frameNStart = frameN  # exact frame index
        t1ex3.tStart = t  # local t and not account for scr refresh
        t1ex3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(t1ex3, 'tStartRefresh')  # time at next scr refresh
        t1ex3.setAutoDraw(True)
    
    # *tTex3* updates
    if tTex3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tTex3.frameNStart = frameN  # exact frame index
        tTex3.tStart = t  # local t and not account for scr refresh
        tTex3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tTex3, 'tStartRefresh')  # time at next scr refresh
        tTex3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction3"-------
for thisComponent in instruction3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr3.started', instr3.tStartRefresh)
thisExp.addData('instr3.stopped', instr3.tStopRefresh)
thisExp.addData('l1ex3.started', l1ex3.tStartRefresh)
thisExp.addData('l1ex3.stopped', l1ex3.tStopRefresh)
thisExp.addData('l2ex3.started', l2ex3.tStartRefresh)
thisExp.addData('l2ex3.stopped', l2ex3.tStopRefresh)
thisExp.addData('t1ex3.started', t1ex3.tStartRefresh)
thisExp.addData('t1ex3.stopped', t1ex3.tStopRefresh)
thisExp.addData('tTex3.started', tTex3.tStartRefresh)
thisExp.addData('tTex3.stopped', tTex3.tStopRefresh)
# the Routine "instruction3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('vSearchCond3.xlsx'),
    seed=None, name='trials3')
thisExp.addLoop(trials3)  # add the loop to the experiment
thisTrials3 = trials3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials3.rgb)
if thisTrials3 != None:
    for paramName in thisTrials3:
        exec('{} = thisTrials3[paramName]'.format(paramName))

for thisTrials3 in trials3:
    currentLoop = trials3
    # abbreviate parameter names if possible (e.g. rgb = thisTrials3.rgb)
    if thisTrials3 != None:
        for paramName in thisTrials3:
            exec('{} = thisTrials3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    trialL11.setPos([loc1,loc2])
    trialL12.setPos([loc3,loc4])
    trialL21.setPos([loc5,loc6])
    trialL22.setPos([loc7,loc8])
    trialT11.setPos([loc9,loc10])
    trialT12.setPos([loc11,loc12])
    trialL13.setPos((loc13, loc14))
    trialL14.setPos((loc15, loc16))
    trialL23.setPos((loc17, loc18))
    trialL24.setPos((loc19, loc20))
    trialT13.setPos((loc21, loc22))
    trialT14.setPos((loc23, loc24))
    trialL15.setPos((loc25, loc26))
    trialL16.setPos((loc27, loc28))
    trialL25.setPos((loc29, loc30))
    trialL26.setPos((loc31, loc32))
    trialT15.setPos((loc33, loc34))
    trialT16.setPos((loc35, loc36))
    trialTT.setPos([loc37,loc38])
    trialResp.keys = []
    trialResp.rt = []
    _trialResp_allKeys = []
    # keep track of which components have finished
    trialComponents = [trialFix, trialL11, trialL12, trialL21, trialL22, trialT11, trialT12, trialL13, trialL14, trialL23, trialL24, trialT13, trialT14, trialL15, trialL16, trialL25, trialL26, trialT15, trialT16, trialTT, trialResp]
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
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trialFix* updates
        if trialFix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trialFix.frameNStart = frameN  # exact frame index
            trialFix.tStart = t  # local t and not account for scr refresh
            trialFix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialFix, 'tStartRefresh')  # time at next scr refresh
            trialFix.setAutoDraw(True)
        if trialFix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trialFix.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                trialFix.tStop = t  # not accounting for scr refresh
                trialFix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trialFix, 'tStopRefresh')  # time at next scr refresh
                trialFix.setAutoDraw(False)
        
        # *trialL11* updates
        if trialL11.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL11.frameNStart = frameN  # exact frame index
            trialL11.tStart = t  # local t and not account for scr refresh
            trialL11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL11, 'tStartRefresh')  # time at next scr refresh
            trialL11.setAutoDraw(True)
        
        # *trialL12* updates
        if trialL12.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL12.frameNStart = frameN  # exact frame index
            trialL12.tStart = t  # local t and not account for scr refresh
            trialL12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL12, 'tStartRefresh')  # time at next scr refresh
            trialL12.setAutoDraw(True)
        
        # *trialL21* updates
        if trialL21.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL21.frameNStart = frameN  # exact frame index
            trialL21.tStart = t  # local t and not account for scr refresh
            trialL21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL21, 'tStartRefresh')  # time at next scr refresh
            trialL21.setAutoDraw(True)
        
        # *trialL22* updates
        if trialL22.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL22.frameNStart = frameN  # exact frame index
            trialL22.tStart = t  # local t and not account for scr refresh
            trialL22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL22, 'tStartRefresh')  # time at next scr refresh
            trialL22.setAutoDraw(True)
        
        # *trialT11* updates
        if trialT11.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialT11.frameNStart = frameN  # exact frame index
            trialT11.tStart = t  # local t and not account for scr refresh
            trialT11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialT11, 'tStartRefresh')  # time at next scr refresh
            trialT11.setAutoDraw(True)
        
        # *trialT12* updates
        if trialT12.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialT12.frameNStart = frameN  # exact frame index
            trialT12.tStart = t  # local t and not account for scr refresh
            trialT12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialT12, 'tStartRefresh')  # time at next scr refresh
            trialT12.setAutoDraw(True)
        
        # *trialL13* updates
        if trialL13.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL13.frameNStart = frameN  # exact frame index
            trialL13.tStart = t  # local t and not account for scr refresh
            trialL13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL13, 'tStartRefresh')  # time at next scr refresh
            trialL13.setAutoDraw(True)
        
        # *trialL14* updates
        if trialL14.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL14.frameNStart = frameN  # exact frame index
            trialL14.tStart = t  # local t and not account for scr refresh
            trialL14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL14, 'tStartRefresh')  # time at next scr refresh
            trialL14.setAutoDraw(True)
        
        # *trialL23* updates
        if trialL23.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL23.frameNStart = frameN  # exact frame index
            trialL23.tStart = t  # local t and not account for scr refresh
            trialL23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL23, 'tStartRefresh')  # time at next scr refresh
            trialL23.setAutoDraw(True)
        
        # *trialL24* updates
        if trialL24.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL24.frameNStart = frameN  # exact frame index
            trialL24.tStart = t  # local t and not account for scr refresh
            trialL24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL24, 'tStartRefresh')  # time at next scr refresh
            trialL24.setAutoDraw(True)
        
        # *trialT13* updates
        if trialT13.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialT13.frameNStart = frameN  # exact frame index
            trialT13.tStart = t  # local t and not account for scr refresh
            trialT13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialT13, 'tStartRefresh')  # time at next scr refresh
            trialT13.setAutoDraw(True)
        
        # *trialT14* updates
        if trialT14.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialT14.frameNStart = frameN  # exact frame index
            trialT14.tStart = t  # local t and not account for scr refresh
            trialT14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialT14, 'tStartRefresh')  # time at next scr refresh
            trialT14.setAutoDraw(True)
        
        # *trialL15* updates
        if trialL15.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL15.frameNStart = frameN  # exact frame index
            trialL15.tStart = t  # local t and not account for scr refresh
            trialL15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL15, 'tStartRefresh')  # time at next scr refresh
            trialL15.setAutoDraw(True)
        
        # *trialL16* updates
        if trialL16.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL16.frameNStart = frameN  # exact frame index
            trialL16.tStart = t  # local t and not account for scr refresh
            trialL16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL16, 'tStartRefresh')  # time at next scr refresh
            trialL16.setAutoDraw(True)
        
        # *trialL25* updates
        if trialL25.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL25.frameNStart = frameN  # exact frame index
            trialL25.tStart = t  # local t and not account for scr refresh
            trialL25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL25, 'tStartRefresh')  # time at next scr refresh
            trialL25.setAutoDraw(True)
        
        # *trialL26* updates
        if trialL26.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialL26.frameNStart = frameN  # exact frame index
            trialL26.tStart = t  # local t and not account for scr refresh
            trialL26.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialL26, 'tStartRefresh')  # time at next scr refresh
            trialL26.setAutoDraw(True)
        
        # *trialT15* updates
        if trialT15.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialT15.frameNStart = frameN  # exact frame index
            trialT15.tStart = t  # local t and not account for scr refresh
            trialT15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialT15, 'tStartRefresh')  # time at next scr refresh
            trialT15.setAutoDraw(True)
        
        # *trialT16* updates
        if trialT16.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialT16.frameNStart = frameN  # exact frame index
            trialT16.tStart = t  # local t and not account for scr refresh
            trialT16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialT16, 'tStartRefresh')  # time at next scr refresh
            trialT16.setAutoDraw(True)
        
        # *trialTT* updates
        if trialTT.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialTT.frameNStart = frameN  # exact frame index
            trialTT.tStart = t  # local t and not account for scr refresh
            trialTT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialTT, 'tStartRefresh')  # time at next scr refresh
            trialTT.setAutoDraw(True)
        
        # *trialResp* updates
        waitOnFlip = False
        if trialResp.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialResp.frameNStart = frameN  # exact frame index
            trialResp.tStart = t  # local t and not account for scr refresh
            trialResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialResp, 'tStartRefresh')  # time at next scr refresh
            trialResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trialResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trialResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trialResp.status == STARTED and not waitOnFlip:
            theseKeys = trialResp.getKeys(keyList=['s', 'k', 'w', 'e', 'a', 'd', 'z', 'x', 'i', 'o', 'j', 'm', ',', 'l'], waitRelease=False)
            _trialResp_allKeys.extend(theseKeys)
            if len(_trialResp_allKeys):
                trialResp.keys = _trialResp_allKeys[-1].name  # just the last key pressed
                trialResp.rt = _trialResp_allKeys[-1].rt
                # was this correct?
                if (trialResp.keys == str(corrAns)) or (trialResp.keys == corrAns):
                    trialResp.corr = 1
                else:
                    trialResp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
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
    trials3.addData('trialFix.started', trialFix.tStartRefresh)
    trials3.addData('trialFix.stopped', trialFix.tStopRefresh)
    trials3.addData('trialL11.started', trialL11.tStartRefresh)
    trials3.addData('trialL11.stopped', trialL11.tStopRefresh)
    trials3.addData('trialL12.started', trialL12.tStartRefresh)
    trials3.addData('trialL12.stopped', trialL12.tStopRefresh)
    trials3.addData('trialL21.started', trialL21.tStartRefresh)
    trials3.addData('trialL21.stopped', trialL21.tStopRefresh)
    trials3.addData('trialL22.started', trialL22.tStartRefresh)
    trials3.addData('trialL22.stopped', trialL22.tStopRefresh)
    trials3.addData('trialT11.started', trialT11.tStartRefresh)
    trials3.addData('trialT11.stopped', trialT11.tStopRefresh)
    trials3.addData('trialT12.started', trialT12.tStartRefresh)
    trials3.addData('trialT12.stopped', trialT12.tStopRefresh)
    trials3.addData('trialL13.started', trialL13.tStartRefresh)
    trials3.addData('trialL13.stopped', trialL13.tStopRefresh)
    trials3.addData('trialL14.started', trialL14.tStartRefresh)
    trials3.addData('trialL14.stopped', trialL14.tStopRefresh)
    trials3.addData('trialL23.started', trialL23.tStartRefresh)
    trials3.addData('trialL23.stopped', trialL23.tStopRefresh)
    trials3.addData('trialL24.started', trialL24.tStartRefresh)
    trials3.addData('trialL24.stopped', trialL24.tStopRefresh)
    trials3.addData('trialT13.started', trialT13.tStartRefresh)
    trials3.addData('trialT13.stopped', trialT13.tStopRefresh)
    trials3.addData('trialT14.started', trialT14.tStartRefresh)
    trials3.addData('trialT14.stopped', trialT14.tStopRefresh)
    trials3.addData('trialL15.started', trialL15.tStartRefresh)
    trials3.addData('trialL15.stopped', trialL15.tStopRefresh)
    trials3.addData('trialL16.started', trialL16.tStartRefresh)
    trials3.addData('trialL16.stopped', trialL16.tStopRefresh)
    trials3.addData('trialL25.started', trialL25.tStartRefresh)
    trials3.addData('trialL25.stopped', trialL25.tStopRefresh)
    trials3.addData('trialL26.started', trialL26.tStartRefresh)
    trials3.addData('trialL26.stopped', trialL26.tStopRefresh)
    trials3.addData('trialT15.started', trialT15.tStartRefresh)
    trials3.addData('trialT15.stopped', trialT15.tStopRefresh)
    trials3.addData('trialT16.started', trialT16.tStartRefresh)
    trials3.addData('trialT16.stopped', trialT16.tStopRefresh)
    trials3.addData('trialTT.started', trialTT.tStartRefresh)
    trials3.addData('trialTT.stopped', trialTT.tStopRefresh)
    # check responses
    if trialResp.keys in ['', [], None]:  # No response was made
        trialResp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           trialResp.corr = 1;  # correct non-response
        else:
           trialResp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials3 (TrialHandler)
    trials3.addData('trialResp.keys',trialResp.keys)
    trials3.addData('trialResp.corr', trialResp.corr)
    if trialResp.keys != None:  # we had a response
        trials3.addData('trialResp.rt', trialResp.rt)
    trials3.addData('trialResp.started', trialResp.tStartRefresh)
    trials3.addData('trialResp.stopped', trialResp.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials3'


# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
endComponents = [thanks, key_resp]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks* updates
    if thanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks.frameNStart = frameN  # exact frame index
        thanks.tStart = t  # local t and not account for scr refresh
        thanks.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks, 'tStartRefresh')  # time at next scr refresh
        thanks.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thanks.started', thanks.tStartRefresh)
thisExp.addData('thanks.stopped', thanks.tStopRefresh)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
