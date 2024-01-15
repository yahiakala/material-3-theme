from ._anvil_designer import TooltipTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Tooltip(TooltipTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self._props = properties
    self.init_components(**properties)
    self.tooltip_node = self.dom_nodes['anvil-m3-tooltip']

  def show_tooltip(self, e):
    self.dom_nodes['anvil-m3-tooltip'].style.opacity = 1
  
  def hide_tooltip(self, e):
    self.dom_nodes['anvil-m3-tooltip'].style.opacity = 0

  @property
  def text(self):
    return self._props.get(text)

  @text.setter
  def text(self, value):
    self._props['text'] = value
    self.dom_nodes['anvil-m3-tooltip'].innerText = value

