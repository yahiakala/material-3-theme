from ._anvil_designer import SwitchTemplate
from anvil import *

class Switch(SwitchTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  @property
  def enabled_icon(self):
    return self._enabled_icon

  @enabled_icon.setter
  def enabled_icon(self, value):
    link_icon = self.dom_nodes['switch-icon']
    self._enabled_icon = value
    if value:
      link_icon.className = ""
      link_icon.classList.add("material-symbols-outlined")
      link_icon.innerText = value