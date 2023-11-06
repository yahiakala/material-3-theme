from ._anvil_designer import SwitchTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js.window import document
from anvil.js import window
from ...Functions import theme_color_to_css, enabled_property, style_property, color_property, theme_color_to_css, property_with_callback


class Switch(SwitchTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self._props = properties
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

  def set_color_styles(self, selected):
    switch_slider = self.dom_nodes['anvil-m3-switch-slider']
    if selected and self.selected_background_color:
      switch_slider.style.backgroundColor = self.selected_background_color
    elif self.unselected_background_color and not selected:
      switch_slider.style.backgroundColor = self.unselected_background_color
    
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
    self.set_color_styles(value)

  # @property
  # def selected_background_color(self):
  #   return self._selected_background_color

  # @selected_background_color.setter
  # def selected_background_color(self, value):
  #   self._selected_background_color = value
  #   self.set_color_styles(self.selected)

  # @property
  # def unselected_background_color(self):
  #   return self._unselected_background_color

  # @unselected_background_color.setter
  # def unselected_background_color(self, value):
  #   self._unselected_background_color = value
  #   self.set_color_styles(self.selected)
      
  enabled = enabled_property('anvil-m3-switch-input')
  align = style_property('anvil-m3-switch-container', 'justifyContent')
  selected_background_color('selected_background_color', set_color_styles)
  unelected_background_color('selected_background_color', set_color_styles)
  
  

  
  
