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
    link_icon = self.dom_nodes['enabled-switch-icon']
    switch_slider = self.dom_nodes['switch-slider']
    self._enabled_icon = value
    link_icon.classList.remove("material-symbols-outlined")
    if value:
      link_icon.classList.add("material-symbols-outlined")
      link_icon.innerText = value
      switch_slider.classList.add('has-enabled-icon')
  
  @property
  def disabled_icon(self):
    return self._disabled_icon

  @disabled_icon.setter
  def disabled_icon(self, value):
    link_icon = self.dom_nodes['disabled-switch-icon']
    switch_slider = self.dom_nodes['switch-slider']
    self._disabled_icon = value
    
    link_icon.classList.remove("material-symbols-outlined")
    if value:
      link_icon.classList.add("material-symbols-outlined")
      link_icon.innerText = value
      switch_slider.classList.add('has-disabled-icon')