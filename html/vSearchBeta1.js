﻿/********************* 
 * Vsearchbeta1 Test *
 *********************/

import { PsychoJS } from './lib/core-2020.1.js';
import * as core from './lib/core-2020.1.js';
import { TrialHandler } from './lib/data-2020.1.js';
import { Scheduler } from './lib/util-2020.1.js';
import * as util from './lib/util-2020.1.js';
import * as visual from './lib/visual-2020.1.js';
import * as sound from './lib/sound-2020.1.js';

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'vSearchBeta1';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instruction1RoutineBegin());
flowScheduler.add(instruction1RoutineEachFrame());
flowScheduler.add(instruction1RoutineEnd());
const trials1LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials1LoopBegin, trials1LoopScheduler);
flowScheduler.add(trials1LoopScheduler);
flowScheduler.add(trials1LoopEnd);
flowScheduler.add(instruction2RoutineBegin());
flowScheduler.add(instruction2RoutineEachFrame());
flowScheduler.add(instruction2RoutineEnd());
const trials2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials2LoopBegin, trials2LoopScheduler);
flowScheduler.add(trials2LoopScheduler);
flowScheduler.add(trials2LoopEnd);
flowScheduler.add(instruction3RoutineBegin());
flowScheduler.add(instruction3RoutineEachFrame());
flowScheduler.add(instruction3RoutineEnd());
const trials3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials3LoopBegin, trials3LoopScheduler);
flowScheduler.add(trials3LoopScheduler);
flowScheduler.add(trials3LoopEnd);
flowScheduler.add(endRoutineBegin());
flowScheduler.add(endRoutineEachFrame());
flowScheduler.add(endRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.1.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var instruction1Clock;
var instr1;
var keyResp1;
var l1ex1;
var l2ex1;
var t1ex1;
var tTex1;
var trialClock;
var trialFix;
var trialL11;
var trialL12;
var trialL21;
var trialL22;
var trialT11;
var trialT12;
var trialL13;
var trialL14;
var trialL23;
var trialL24;
var trialT13;
var trialT14;
var trialL15;
var trialL16;
var trialL25;
var trialL26;
var trialT15;
var trialT16;
var trialTT;
var trialResp;
var instruction2Clock;
var instr2;
var keyResp2;
var l1ex2;
var l2ex2;
var t1ex2;
var tTex2;
var instruction3Clock;
var instr3;
var keyResp3;
var l1ex3;
var l2ex3;
var t1ex3;
var tTex3;
var endClock;
var thanks;
var key_resp;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "instruction1"
  instruction1Clock = new util.Clock();
  instr1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr1',
    text: 'In this task you will see sets of shapes made of four different shapes as outlined below. Only press the ‘s’ key if you see the upright “T” shape, which is the last shape. Otherwise, press the ‘k’ key. There will be 6, 12, or 18 shapes to observe in each trial. Press ‘space’ to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  keyResp1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  l1ex1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'l1ex1', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [(- 0.3), (- 0.3)], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  l2ex1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'l2ex1', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [(- 0.1), (- 0.3)], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  t1ex1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 't1ex1', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0.1, (- 0.3)], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  tTex1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'tTex1', units : undefined, 
    image : 'TT.png', mask : undefined,
    ori : 0, pos : [0.3, (- 0.3)], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  document.documentElement.style.cursor = 'none';
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  trialFix = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialFix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  trialL11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL11', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  trialL12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL12', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  trialL21 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL21', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  trialL22 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL22', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  trialT11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialT11', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  trialT12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialT12', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -6.0 
  });
  trialL13 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL13', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  trialL14 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL14', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  trialL23 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL23', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -9.0 
  });
  trialL24 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL24', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -10.0 
  });
  trialT13 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialT13', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -11.0 
  });
  trialT14 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialT14', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -12.0 
  });
  trialL15 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL15', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -13.0 
  });
  trialL16 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL16', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -14.0 
  });
  trialL25 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL25', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -15.0 
  });
  trialL26 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL26', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -16.0 
  });
  trialT15 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialT15', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -17.0 
  });
  trialT16 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialT16', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -18.0 
  });
  trialTT = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialTT', units : undefined, 
    image : 'TT.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -19.0 
  });
  trialResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instruction2"
  instruction2Clock = new util.Clock();
  instr2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr2',
    text: 'A quick break before the next set of trials. Remember, only press the ‘s’ key if you see the upright “T” shape, which is the last shape below. Otherwise, press the ‘k’ key. There will be 6, 12, or 18 shapes to observe in each trial. Press ‘space’ to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  keyResp2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  l1ex2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'l1ex2', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [(- 0.3), (- 0.3)], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  l2ex2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'l2ex2', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [(- 0.1), (- 0.3)], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  t1ex2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 't1ex2', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0.1, (- 0.3)], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  tTex2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'tTex2', units : undefined, 
    image : 'TT.png', mask : undefined,
    ori : 0, pos : [0.3, (- 0.3)], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  trialFix = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialFix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  trialL11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL11', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  trialL12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL12', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  trialL21 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL21', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  trialL22 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL22', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  trialT11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialT11', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  trialT12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialT12', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -6.0 
  });
  trialL13 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL13', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  trialL14 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL14', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  trialL23 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL23', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -9.0 
  });
  trialL24 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL24', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -10.0 
  });
  trialT13 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialT13', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -11.0 
  });
  trialT14 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialT14', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -12.0 
  });
  trialL15 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL15', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -13.0 
  });
  trialL16 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL16', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -14.0 
  });
  trialL25 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL25', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -15.0 
  });
  trialL26 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL26', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -16.0 
  });
  trialT15 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialT15', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -17.0 
  });
  trialT16 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialT16', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -18.0 
  });
  trialTT = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialTT', units : undefined, 
    image : 'TT.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -19.0 
  });
  trialResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instruction3"
  instruction3Clock = new util.Clock();
  instr3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr3',
    text: 'A quick break before the next set of trials. Remember, only press the ‘s’ key if you see the upright “T” shape, which is the last shape below. Otherwise, press the ‘k’ key. There will be 6, 12, or 18 shapes to observe in each trial. Press ‘space’ to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  keyResp3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  l1ex3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'l1ex3', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [(- 0.3), (- 0.3)], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  l2ex3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'l2ex3', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [(- 0.1), (- 0.3)], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  t1ex3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 't1ex3', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0.1, (- 0.3)], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  tTex3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'tTex3', units : undefined, 
    image : 'TT.png', mask : undefined,
    ori : 0, pos : [0.3, (- 0.3)], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  trialFix = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialFix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  trialL11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL11', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  trialL12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL12', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  trialL21 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL21', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  trialL22 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL22', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  trialT11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialT11', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  trialT12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialT12', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -6.0 
  });
  trialL13 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL13', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  trialL14 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL14', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  trialL23 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL23', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -9.0 
  });
  trialL24 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL24', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -10.0 
  });
  trialT13 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialT13', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -11.0 
  });
  trialT14 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialT14', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -12.0 
  });
  trialL15 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL15', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -13.0 
  });
  trialL16 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL16', units : undefined, 
    image : 'L1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -14.0 
  });
  trialL25 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL25', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -15.0 
  });
  trialL26 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialL26', units : undefined, 
    image : 'L2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -16.0 
  });
  trialT15 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialT15', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -17.0 
  });
  trialT16 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialT16', units : undefined, 
    image : 'T1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -18.0 
  });
  trialTT = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trialTT', units : undefined, 
    image : 'TT.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -19.0 
  });
  trialResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  thanks = new visual.TextStim({
    win: psychoJS.window,
    name: 'thanks',
    text: 'This is the end of the experiment. Thank you for your time. Please remember to return to the questionnaire to carry on with the study. Press ‘space’ to exit.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _keyResp1_allKeys;
var instruction1Components;
function instruction1RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instruction1'-------
    t = 0;
    instruction1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    keyResp1.keys = undefined;
    keyResp1.rt = undefined;
    _keyResp1_allKeys = [];
    // keep track of which components have finished
    instruction1Components = [];
    instruction1Components.push(instr1);
    instruction1Components.push(keyResp1);
    instruction1Components.push(l1ex1);
    instruction1Components.push(l2ex1);
    instruction1Components.push(t1ex1);
    instruction1Components.push(tTex1);
    
    for (const thisComponent of instruction1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
function instruction1RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instruction1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instruction1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr1* updates
    if (t >= 0.0 && instr1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr1.tStart = t;  // (not accounting for frame time here)
      instr1.frameNStart = frameN;  // exact frame index
      
      instr1.setAutoDraw(true);
    }

    
    // *keyResp1* updates
    if (t >= 0.0 && keyResp1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyResp1.tStart = t;  // (not accounting for frame time here)
      keyResp1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyResp1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyResp1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyResp1.clearEvents(); });
    }

    if (keyResp1.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyResp1.getKeys({keyList: ['space'], waitRelease: false});
      _keyResp1_allKeys = _keyResp1_allKeys.concat(theseKeys);
      if (_keyResp1_allKeys.length > 0) {
        keyResp1.keys = _keyResp1_allKeys[_keyResp1_allKeys.length - 1].name;  // just the last key pressed
        keyResp1.rt = _keyResp1_allKeys[_keyResp1_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *l1ex1* updates
    if (t >= 0.0 && l1ex1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      l1ex1.tStart = t;  // (not accounting for frame time here)
      l1ex1.frameNStart = frameN;  // exact frame index
      
      l1ex1.setAutoDraw(true);
    }

    
    // *l2ex1* updates
    if (t >= 0.0 && l2ex1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      l2ex1.tStart = t;  // (not accounting for frame time here)
      l2ex1.frameNStart = frameN;  // exact frame index
      
      l2ex1.setAutoDraw(true);
    }

    
    // *t1ex1* updates
    if (t >= 0.0 && t1ex1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      t1ex1.tStart = t;  // (not accounting for frame time here)
      t1ex1.frameNStart = frameN;  // exact frame index
      
      t1ex1.setAutoDraw(true);
    }

    
    // *tTex1* updates
    if (t >= 0.0 && tTex1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tTex1.tStart = t;  // (not accounting for frame time here)
      tTex1.frameNStart = frameN;  // exact frame index
      
      tTex1.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instruction1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instruction1RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instruction1'-------
    for (const thisComponent of instruction1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "instruction1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var trials1;
var currentLoop;
function trials1LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials1 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'vSearchCond1.xlsx',
    seed: undefined, name: 'trials1'
  });
  psychoJS.experiment.addLoop(trials1); // add the loop to the experiment
  currentLoop = trials1;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrials1 of trials1) {
    const snapshot = trials1.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(trialRoutineBegin(snapshot));
    thisScheduler.add(trialRoutineEachFrame(snapshot));
    thisScheduler.add(trialRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trials1LoopEnd() {
  psychoJS.experiment.removeLoop(trials1);

  return Scheduler.Event.NEXT;
}


var trials2;
function trials2LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'vSearchCond2.xlsx',
    seed: undefined, name: 'trials2'
  });
  psychoJS.experiment.addLoop(trials2); // add the loop to the experiment
  currentLoop = trials2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrials2 of trials2) {
    const snapshot = trials2.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(trialRoutineBegin(snapshot));
    thisScheduler.add(trialRoutineEachFrame(snapshot));
    thisScheduler.add(trialRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trials2LoopEnd() {
  psychoJS.experiment.removeLoop(trials2);

  return Scheduler.Event.NEXT;
}


var trials3;
function trials3LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials3 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'vSearchCond3.xlsx',
    seed: undefined, name: 'trials3'
  });
  psychoJS.experiment.addLoop(trials3); // add the loop to the experiment
  currentLoop = trials3;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrials3 of trials3) {
    const snapshot = trials3.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(trialRoutineBegin(snapshot));
    thisScheduler.add(trialRoutineEachFrame(snapshot));
    thisScheduler.add(trialRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trials3LoopEnd() {
  psychoJS.experiment.removeLoop(trials3);

  return Scheduler.Event.NEXT;
}


var _trialResp_allKeys;
var trialComponents;
function trialRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    trialL11.setPos([loc1, loc2]);
    trialL12.setPos([loc3, loc4]);
    trialL21.setPos([loc5, loc6]);
    trialL22.setPos([loc7, loc8]);
    trialT11.setPos([loc9, loc10]);
    trialT12.setPos([loc11, loc12]);
    trialL13.setPos([loc13, loc14]);
    trialL14.setPos([loc15, loc16]);
    trialL23.setPos([loc17, loc18]);
    trialL24.setPos([loc19, loc20]);
    trialT13.setPos([loc21, loc22]);
    trialT14.setPos([loc23, loc24]);
    trialL15.setPos([loc25, loc26]);
    trialL16.setPos([loc27, loc28]);
    trialL25.setPos([loc29, loc30]);
    trialL26.setPos([loc31, loc32]);
    trialT15.setPos([loc33, loc34]);
    trialT16.setPos([loc35, loc36]);
    trialTT.setPos([loc37, loc38]);
    trialResp.keys = undefined;
    trialResp.rt = undefined;
    _trialResp_allKeys = [];
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(trialFix);
    trialComponents.push(trialL11);
    trialComponents.push(trialL12);
    trialComponents.push(trialL21);
    trialComponents.push(trialL22);
    trialComponents.push(trialT11);
    trialComponents.push(trialT12);
    trialComponents.push(trialL13);
    trialComponents.push(trialL14);
    trialComponents.push(trialL23);
    trialComponents.push(trialL24);
    trialComponents.push(trialT13);
    trialComponents.push(trialT14);
    trialComponents.push(trialL15);
    trialComponents.push(trialL16);
    trialComponents.push(trialL25);
    trialComponents.push(trialL26);
    trialComponents.push(trialT15);
    trialComponents.push(trialT16);
    trialComponents.push(trialTT);
    trialComponents.push(trialResp);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function trialRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'trial'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *trialFix* updates
    if (t >= 0.0 && trialFix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialFix.tStart = t;  // (not accounting for frame time here)
      trialFix.frameNStart = frameN;  // exact frame index
      
      trialFix.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (trialFix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      trialFix.setAutoDraw(false);
    }
    
    // *trialL11* updates
    if (t >= 1.0 && trialL11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialL11.tStart = t;  // (not accounting for frame time here)
      trialL11.frameNStart = frameN;  // exact frame index
      
      trialL11.setAutoDraw(true);
    }

    
    // *trialL12* updates
    if (t >= 1.0 && trialL12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialL12.tStart = t;  // (not accounting for frame time here)
      trialL12.frameNStart = frameN;  // exact frame index
      
      trialL12.setAutoDraw(true);
    }

    
    // *trialL21* updates
    if (t >= 1.0 && trialL21.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialL21.tStart = t;  // (not accounting for frame time here)
      trialL21.frameNStart = frameN;  // exact frame index
      
      trialL21.setAutoDraw(true);
    }

    
    // *trialL22* updates
    if (t >= 1.0 && trialL22.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialL22.tStart = t;  // (not accounting for frame time here)
      trialL22.frameNStart = frameN;  // exact frame index
      
      trialL22.setAutoDraw(true);
    }

    
    // *trialT11* updates
    if (t >= 1.0 && trialT11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialT11.tStart = t;  // (not accounting for frame time here)
      trialT11.frameNStart = frameN;  // exact frame index
      
      trialT11.setAutoDraw(true);
    }

    
    // *trialT12* updates
    if (t >= 1.0 && trialT12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialT12.tStart = t;  // (not accounting for frame time here)
      trialT12.frameNStart = frameN;  // exact frame index
      
      trialT12.setAutoDraw(true);
    }

    
    // *trialL13* updates
    if (t >= 1.0 && trialL13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialL13.tStart = t;  // (not accounting for frame time here)
      trialL13.frameNStart = frameN;  // exact frame index
      
      trialL13.setAutoDraw(true);
    }

    
    // *trialL14* updates
    if (t >= 1.0 && trialL14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialL14.tStart = t;  // (not accounting for frame time here)
      trialL14.frameNStart = frameN;  // exact frame index
      
      trialL14.setAutoDraw(true);
    }

    
    // *trialL23* updates
    if (t >= 1.0 && trialL23.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialL23.tStart = t;  // (not accounting for frame time here)
      trialL23.frameNStart = frameN;  // exact frame index
      
      trialL23.setAutoDraw(true);
    }

    
    // *trialL24* updates
    if (t >= 1.0 && trialL24.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialL24.tStart = t;  // (not accounting for frame time here)
      trialL24.frameNStart = frameN;  // exact frame index
      
      trialL24.setAutoDraw(true);
    }

    
    // *trialT13* updates
    if (t >= 1.0 && trialT13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialT13.tStart = t;  // (not accounting for frame time here)
      trialT13.frameNStart = frameN;  // exact frame index
      
      trialT13.setAutoDraw(true);
    }

    
    // *trialT14* updates
    if (t >= 1.0 && trialT14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialT14.tStart = t;  // (not accounting for frame time here)
      trialT14.frameNStart = frameN;  // exact frame index
      
      trialT14.setAutoDraw(true);
    }

    
    // *trialL15* updates
    if (t >= 1.0 && trialL15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialL15.tStart = t;  // (not accounting for frame time here)
      trialL15.frameNStart = frameN;  // exact frame index
      
      trialL15.setAutoDraw(true);
    }

    
    // *trialL16* updates
    if (t >= 1.0 && trialL16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialL16.tStart = t;  // (not accounting for frame time here)
      trialL16.frameNStart = frameN;  // exact frame index
      
      trialL16.setAutoDraw(true);
    }

    
    // *trialL25* updates
    if (t >= 1.0 && trialL25.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialL25.tStart = t;  // (not accounting for frame time here)
      trialL25.frameNStart = frameN;  // exact frame index
      
      trialL25.setAutoDraw(true);
    }

    
    // *trialL26* updates
    if (t >= 1.0 && trialL26.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialL26.tStart = t;  // (not accounting for frame time here)
      trialL26.frameNStart = frameN;  // exact frame index
      
      trialL26.setAutoDraw(true);
    }

    
    // *trialT15* updates
    if (t >= 1.0 && trialT15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialT15.tStart = t;  // (not accounting for frame time here)
      trialT15.frameNStart = frameN;  // exact frame index
      
      trialT15.setAutoDraw(true);
    }

    
    // *trialT16* updates
    if (t >= 1.0 && trialT16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialT16.tStart = t;  // (not accounting for frame time here)
      trialT16.frameNStart = frameN;  // exact frame index
      
      trialT16.setAutoDraw(true);
    }

    
    // *trialTT* updates
    if (t >= 1.0 && trialTT.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialTT.tStart = t;  // (not accounting for frame time here)
      trialTT.frameNStart = frameN;  // exact frame index
      
      trialTT.setAutoDraw(true);
    }

    
    // *trialResp* updates
    if (t >= 1.0 && trialResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialResp.tStart = t;  // (not accounting for frame time here)
      trialResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { trialResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { trialResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { trialResp.clearEvents(); });
    }

    if (trialResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = trialResp.getKeys({keyList: ['s', 'k', 'w', 'e', 'a', 'd', 'z', 'x', 'i', 'o', 'j', 'm', ',', 'l'], waitRelease: false});
      _trialResp_allKeys = _trialResp_allKeys.concat(theseKeys);
      if (_trialResp_allKeys.length > 0) {
        trialResp.keys = _trialResp_allKeys[_trialResp_allKeys.length - 1].name;  // just the last key pressed
        trialResp.rt = _trialResp_allKeys[_trialResp_allKeys.length - 1].rt;
        // was this correct?
        if (trialResp.keys == corrAns) {
            trialResp.corr = 1;
        } else {
            trialResp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'trial'-------
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (trialResp.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         trialResp.corr = 1;  // correct non-response
      } else {
         trialResp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('trialResp.keys', trialResp.keys);
    psychoJS.experiment.addData('trialResp.corr', trialResp.corr);
    if (typeof trialResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('trialResp.rt', trialResp.rt);
        routineTimer.reset();
        }
    
    trialResp.stop();
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _keyResp2_allKeys;
var instruction2Components;
function instruction2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instruction2'-------
    t = 0;
    instruction2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    keyResp2.keys = undefined;
    keyResp2.rt = undefined;
    _keyResp2_allKeys = [];
    // keep track of which components have finished
    instruction2Components = [];
    instruction2Components.push(instr2);
    instruction2Components.push(keyResp2);
    instruction2Components.push(l1ex2);
    instruction2Components.push(l2ex2);
    instruction2Components.push(t1ex2);
    instruction2Components.push(tTex2);
    
    for (const thisComponent of instruction2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function instruction2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instruction2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instruction2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr2* updates
    if (t >= 0.0 && instr2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr2.tStart = t;  // (not accounting for frame time here)
      instr2.frameNStart = frameN;  // exact frame index
      
      instr2.setAutoDraw(true);
    }

    
    // *keyResp2* updates
    if (t >= 0.0 && keyResp2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyResp2.tStart = t;  // (not accounting for frame time here)
      keyResp2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyResp2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyResp2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyResp2.clearEvents(); });
    }

    if (keyResp2.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyResp2.getKeys({keyList: ['space'], waitRelease: false});
      _keyResp2_allKeys = _keyResp2_allKeys.concat(theseKeys);
      if (_keyResp2_allKeys.length > 0) {
        keyResp2.keys = _keyResp2_allKeys[_keyResp2_allKeys.length - 1].name;  // just the last key pressed
        keyResp2.rt = _keyResp2_allKeys[_keyResp2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *l1ex2* updates
    if (t >= 0.0 && l1ex2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      l1ex2.tStart = t;  // (not accounting for frame time here)
      l1ex2.frameNStart = frameN;  // exact frame index
      
      l1ex2.setAutoDraw(true);
    }

    
    // *l2ex2* updates
    if (t >= 0.0 && l2ex2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      l2ex2.tStart = t;  // (not accounting for frame time here)
      l2ex2.frameNStart = frameN;  // exact frame index
      
      l2ex2.setAutoDraw(true);
    }

    
    // *t1ex2* updates
    if (t >= 0.0 && t1ex2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      t1ex2.tStart = t;  // (not accounting for frame time here)
      t1ex2.frameNStart = frameN;  // exact frame index
      
      t1ex2.setAutoDraw(true);
    }

    
    // *tTex2* updates
    if (t >= 0.0 && tTex2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tTex2.tStart = t;  // (not accounting for frame time here)
      tTex2.frameNStart = frameN;  // exact frame index
      
      tTex2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instruction2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instruction2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instruction2'-------
    for (const thisComponent of instruction2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "instruction2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _keyResp3_allKeys;
var instruction3Components;
function instruction3RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instruction3'-------
    t = 0;
    instruction3Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    keyResp3.keys = undefined;
    keyResp3.rt = undefined;
    _keyResp3_allKeys = [];
    // keep track of which components have finished
    instruction3Components = [];
    instruction3Components.push(instr3);
    instruction3Components.push(keyResp3);
    instruction3Components.push(l1ex3);
    instruction3Components.push(l2ex3);
    instruction3Components.push(t1ex3);
    instruction3Components.push(tTex3);
    
    for (const thisComponent of instruction3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function instruction3RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instruction3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instruction3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr3* updates
    if (t >= 0.0 && instr3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr3.tStart = t;  // (not accounting for frame time here)
      instr3.frameNStart = frameN;  // exact frame index
      
      instr3.setAutoDraw(true);
    }

    
    // *keyResp3* updates
    if (t >= 0.0 && keyResp3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyResp3.tStart = t;  // (not accounting for frame time here)
      keyResp3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyResp3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyResp3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyResp3.clearEvents(); });
    }

    if (keyResp3.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyResp3.getKeys({keyList: ['space'], waitRelease: false});
      _keyResp3_allKeys = _keyResp3_allKeys.concat(theseKeys);
      if (_keyResp3_allKeys.length > 0) {
        keyResp3.keys = _keyResp3_allKeys[_keyResp3_allKeys.length - 1].name;  // just the last key pressed
        keyResp3.rt = _keyResp3_allKeys[_keyResp3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *l1ex3* updates
    if (t >= 0.0 && l1ex3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      l1ex3.tStart = t;  // (not accounting for frame time here)
      l1ex3.frameNStart = frameN;  // exact frame index
      
      l1ex3.setAutoDraw(true);
    }

    
    // *l2ex3* updates
    if (t >= 0.0 && l2ex3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      l2ex3.tStart = t;  // (not accounting for frame time here)
      l2ex3.frameNStart = frameN;  // exact frame index
      
      l2ex3.setAutoDraw(true);
    }

    
    // *t1ex3* updates
    if (t >= 0.0 && t1ex3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      t1ex3.tStart = t;  // (not accounting for frame time here)
      t1ex3.frameNStart = frameN;  // exact frame index
      
      t1ex3.setAutoDraw(true);
    }

    
    // *tTex3* updates
    if (t >= 0.0 && tTex3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tTex3.tStart = t;  // (not accounting for frame time here)
      tTex3.frameNStart = frameN;  // exact frame index
      
      tTex3.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instruction3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instruction3RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instruction3'-------
    for (const thisComponent of instruction3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "instruction3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_allKeys;
var endComponents;
function endRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'end'-------
    t = 0;
    endClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    endComponents = [];
    endComponents.push(thanks);
    endComponents.push(key_resp);
    
    for (const thisComponent of endComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function endRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'end'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *thanks* updates
    if (t >= 0.0 && thanks.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      thanks.tStart = t;  // (not accounting for frame time here)
      thanks.frameNStart = frameN;  // exact frame index
      
      thanks.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of endComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'end'-------
    for (const thisComponent of endComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(thisScheduler, loop) {
  // ------Prepare for next entry------
  return function () {
    if (typeof loop !== 'undefined') {
      // ------Check if user ended loop early------
      if (loop.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(loop);
        }
      thisScheduler.stop();
      } else {
        const thisTrial = loop.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(loop);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(trials) {
  return function () {
    psychoJS.importAttributes(trials.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  document.documentElement.style.cursor = 'auto';
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
