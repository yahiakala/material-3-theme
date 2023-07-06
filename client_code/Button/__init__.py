from ._anvil_designer import ButtonTemplate
from anvil import *

class Button(ButtonTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @property
  def material_icon(self):
    return self._material_icon

  @material_icon.setter
  def material_icon(self, value):
    button_icon = self.dom_nodes['button-icon']
    self._material_icon = value
    if value:
      button_icon.innerText = value
    else:
      button_icon.style.display = "none"
