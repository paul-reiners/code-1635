"""
Author: Paul Reiners
Based on Wolfram Cellular Automata by Daniel Shiffman.

Simple demonstration of a Wolfram 1-dimensional three-color cellular automata
When the system reaches bottom of the window, it restarts with a new ruleset
Mouse click restarts as well. 
"""

from ThreeColorCA import ThreeColorCA   # Object to describe the Wolfram basic three-color Cellular Automata

def setup():
    global ca
    size(1280, 720)
    ruleset = 1635  # An initial rule system
    ca = ThreeColorCA(ruleset)                    # Initialize CA
    background(0)

def draw():
    ca.render()      # Draw the CA
    ca.generate()    # Generate the next level

def mousePressed():
    background(0)
    ca.randomize()
    ca.restart()
