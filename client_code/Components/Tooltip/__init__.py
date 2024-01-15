from ._anvil_designer import TooltipTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...Functions import innerText_property

class Tooltip(TooltipTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self._props = properties
    self.init_components(**properties)

  def show_tooltip(self, e):
    self.dom_nodes['anvil-m3-tooltip'].style.opacity = 1
  
  def hide_tooltip(self, e):
    self.dom_nodes['anvil-m3-tooltip'].style.opacity = 0

  text = innerText_property('anvil-m3-tooltip')


