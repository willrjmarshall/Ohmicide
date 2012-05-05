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
from _Livid_Framework.LividTransportComponent import LividTransportComponent
from _Livid_Framework.LividSessionZoomingComponent import LividSessionZoomingComponent
from _Livid_Framework.LividControlSurface import LividControlSurface

class Ohmicide(LividControlSurface):
  __module__ = __name__
  __doc__ = " Ohmicide controller script "

  def __init__(self, c_instance):
    LividControlSurface.__init__(self, c_instance)

  def setup_mixer(self):
    self.mixer = LividMixerComponent(faders = FADERS, sends = SENDS, 
        crossfader = CROSSFADER, 
        master = MASTER, 
        cue = CUE_VOLUME,
        solos = SOLOS,
        selects = TRACK_SELECTS, 
        master_select = MASTER_SELECT, 
        arms = ARMS)
        #mutes = MUTES)
  
  def setup_session(self):
    self.session = LividSessionComponent(matrix = MATRIX, 
        navigation = NAVIGATION_BUTTONS, 
        scene_launches = SCENE_LAUNCH, 
        stops = STOPS, 
        mixer = self.mixer)
    self.session_zoom = LividSessionZoomingComponent(self.session, SHIFT)
    
    # Session zoom

  def setup_transport(self):
    self.transport = LividTransportComponent(play = PLAY, stop = STOP, bpm_up = BPM_UP, bpm_down = BPM_DOWN)
    
