import os

from enthought.traits.api import HasTraits
from enthought.traits.ui.api import View, Item
from enthought.savage.traits.ui.svg_button import SVGButton

from os.path import dirname, join, abspath


pause_icon = os.path.join(os.path.dirname(__file__), 'player_pause.svg')
resume_icon = os.path.join(os.path.dirname(__file__), 'player_play.svg')

class SVGDemo(HasTraits):

    pause = SVGButton('Pause', filename=pause_icon,
                      toggle_filename=resume_icon,
                      toggle_state=True,
                      toggle_label='Resume',
                      toggle_tooltip='Resume',
                      tooltip='Pause', toggle=True)

    trait_view = View(Item('pause'))

SVGDemo().configure_traits()