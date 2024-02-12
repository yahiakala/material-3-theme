from ._anvil_designer import DividerTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...Functions import color_property

class Divider(DividerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self._props = properties
    self.init_components(**properties)

  visible = HtmlTemplate.visible
  color = color_property('anvil-m3-divider', 'border-color', 'color')
  
  @property
  def type(self):
    return self._type

  @type.setter
  def type(self, value):
    divider = self.dom_nodes['anvil-m3-divider']
    self._type = value
    value = value.lower().replace(' ', '-')
    divider.className = "anvil-m3-divider"
    self.dom_nodes['anvil-m3-divider'].classList.add(value)


