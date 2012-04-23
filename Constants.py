MIDI_CC_TYPE = 1
MIDI_NOTE_TYPE = 0

TRACKS = 8
RETURNS = 0
CHANNEL = 0 # All things must be on one channel

# It is assumed that these will use the global channel
# And will be CCs
FADERS = [23, 22, 15, 14, 5, 7, 6, 4] 
MUTE_BUTTONS = [23, 22, 15, 14, 5, 7, 6, 4] 

GRID_HEIGHT = 8
GRID_WIDTH = 8
GRID = [range(i, GRID_HEIGHT * GRID_WIDTH, GRID_HEIGHT) for i in xrange(GRID_WIDTH)] 
