import Live

from Constants import *
from _Framework.ControlSurface import ControlSurface
from _Framework.InputControlElement import *
from _Framework.SliderElement import SliderElement
from _Framework.ButtonElement import ButtonElement
from _Framework.EncoderElement import EncoderElement
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.MixerComponent import MixerComponent
from _Framework.ClipSlotComponent import ClipSlotComponent
from _Framework.ChannelStripComponent import ChannelStripComponent
from _Framework.SceneComponent import SceneComponent
from _Framework.SessionZoomingComponent import SessionZoomingComponent
from _Framework.ChannelTranslationSelector import ChannelTranslationSelector

from _Livid_Framework.LividMixerComponent import LividMixerComponent
from _Livid_Framework.LividSessionComponent import LividSessionComponent

class Ohmicide(ControlSurface):
  __module__ = __name__
  __doc__ = " Ohmicide controller script "

  def __init__(self, c_instance):
    ControlSurface.__init__(self, c_instance)
    self.set_suppress_rebuild_requests(True) # Turn off rebuild MIDI map until after we're done setting up

    # Configure each of the primarily elements
    self.setup_mixer()
    self.setup_session()

    self.set_suppress_rebuild_requests(False) #Turn rebuild back on, now that we're done setting up

  def setup_mixer(self):
    self.mixer = LividMixerComponent(faders = FADERS, sends = SENDS, crossfader = CROSSFADER, master = MASTER, cue = CUE_VOLUME)
  
  def setup_session(self):
    # Handily, channel defaults to 0
    self.session = LividSessionComponent(matrix = MATRIX, navigation = NAVIGATION_BUTTONS)
    
