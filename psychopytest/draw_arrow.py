# -*- coding: utf-8 -*-

"""
Demo of psychopy.visual.ShapeStim: lines and arbitrary fillable shapes
See shapeContains.py for dynamic interaction of ShapeStim and Mouse.
"""

from __future__ import division

from psychopy import visual, event, core
from psychopy.visual import ShapeStim

win = visual.Window(size=(500, 400), units='height')

# some shapes:
arrowVert = [(-0.4,0.05),(-0.4,-0.05),(-.2,-0.05),(-.2,-0.1),(0,0),(-.2,0.1),(-.2,0.05)]
arrow = ShapeStim(win, vertices=arrowVert, fillColor='gray', size=.5, lineColor='white')

while not event.getKeys():
    arrow.draw()

    win.flip()

win.close()
core.quit()

# The contents of this file are in the public domain.