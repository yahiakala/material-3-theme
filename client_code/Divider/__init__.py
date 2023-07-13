from ._anvil_designer import DividerTemplate
from anvil import *
import anvil.server

class Divider(DividerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  @property
  def type(self):
    return self._type

  @type.setter
  def type(self, value):
    divider = self.dom_nodes['divider']
    self._type = value
    value = value.lower().replace(' ', '-')
    divider.className = "divider"
    self.dom_nodes['divider'].classList.add(value)


