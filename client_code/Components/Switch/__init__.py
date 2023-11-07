from ._anvil_designer import SwitchTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js.window import document
from anvil.js import window
from ...Functions import theme_color_to_css, enabled_property, style_property, color_property, theme_color_to_css, property_with_callback
import anvil.designer


class Switch(SwitchTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self._props = properties
    self.init_components(**properties)
    self.add_event_handler("x-anvil-page-added", self.on_mount)
    self.add_event_handler("x-anvil-page-removed", self.on_cleanup)

  def on_mount(self, **event_args):
    self.dom_nodes['anvil-m3-switch-input'].addEventListener("change", self.handle_change)
    
  def on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-switch-input'].removeEventListener("change", self.handle_change)

  def handle_change(self, event):
    if self.enabled:
      #self.dom_nodes['anvil-m3-switch-input'].focus()
      self.selected = not self.selected
      self.raise_event("change")


  def set_color_styles(self, value=None):
    if self.selected:
      self.dom_nodes['anvil-m3-switch-slider'].style.backgroundColor = theme_color_to_css(self.selected_background_color) if self.selected_background_color else None
    else:
      self.dom_nodes['anvil-m3-switch-slider'].style.backgroundColor = theme_color_to_css(self.unselected_background_color) if self.unselected_background_color else None
    
  @property
  def selected_icon(self):
    return self._selected_icon

  @selected_icon.setter
  def selected_icon(self, value):
    link_icon = self.dom_nodes['anvil-m3-enabled-switch-icon']
    switch_slider = self.dom_nodes['anvil-m3-switch-slider']
    self._selected_icon = value
    link_icon.classList.remove("material-symbols-outlined")
    if value:
      link_icon.classList.add("material-symbols-outlined")
      link_icon.innerText = value
      switch_slider.classList.add('anvil-m3-has-enabled-icon')
  
  @property
  def unselected_icon(self):
    return self._unselected_icon

  @unselected_icon.setter
  def unselected_icon(self, value):
    link_icon = self.dom_nodes['anvil-m3-disabled-switch-icon']
    switch_slider = self.dom_nodes['anvil-m3-switch-slider']
    self._unselected_icon = value
    
    link_icon.classList.remove("material-symbols-outlined")
    if value:
      link_icon.classList.add("material-symbols-outlined")
      link_icon.innerText = value
      switch_slider.classList.add('anvil-m3-has-disabled-icon')

  @property
  def selected(self):
    return self.dom_nodes['anvil-m3-switch-input'].checked

  @selected.setter
  def selected(self, value):
    self.dom_nodes['anvil-m3-switch-input'].checked = value
    self.set_color_styles()
      
  enabled = enabled_property('anvil-m3-switch-input')
  align = style_property('anvil-m3-switch-container', 'justifyContent')
  selected_background_color = property_with_callback('selected_background_color', set_color_styles)
  unelected_background_color = property_with_callback('unselected_background_color', set_color_styles)
  
  

  
  
