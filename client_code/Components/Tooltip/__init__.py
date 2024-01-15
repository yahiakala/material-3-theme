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

  text = innerText_property('anvil-m3-tooltip')

  @property
  def opacity(self):
    return self._props['opacity']

  @opacity.setter
  def opacity(self, value):
    self._props.get('opacity')
    self.dom_nodes['anvil-m3-tooltip'].style.opacity = value


