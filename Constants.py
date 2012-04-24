MIDI_CC_TYPE = 1
MIDI_NOTE_TYPE = 0

RETURNS = 0
CHANNEL = 0 # All things must be on one channel

# It is assumed that these will use the global channel
# And will be CCs
FADERS = [23, 22, 15, 14, 5, 7, 6, 4] 

# Each channel is a tuple of send encoders from bottom to top
SENDS = [
  [21, 19, 17], # Channel 1
  [20, 18, 16], # Channel 2 etc
  [13, 11, 9],
  [12, 10, 8],
  [3],
  [1],
  [0],
  [2]]

MUTE_BUTTONS = [23, 22, 15, 14, 5, 7, 6, 4] 

# Grid of button notes
MATRIX = [
    [0, 8,  16, 24, 32, 40, 48, 56],
    [1, 9,  17, 25, 33, 41, 49, 57],
    [2, 10, 18, 26, 34, 42, 50, 58],
    [3, 11, 19, 27, 35, 43, 51, 59],
    [4, 12, 20, 28, 36, 44, 52, 60]]


