from ._anvil_designer import IconButtonToggleTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...Functions import innerText_property, enabled_property, color_property, style_property
from anvil import HtmlTemplate

class IconButtonToggle(IconButtonToggleTemplate):
  def __init__(self, **properties):
    self.background = None
    self.border = None
    self.icon_color = None
    self.selected = False
    
    self._appearance_css_classes = {
      "Filled": "filled",
      "Filled tonal": "filled-tonal",
      "Outlined": "outlined"}
    self._appearance = ""
    self.init_components(**properties)

    self.handle_click = self.handle_click

    self.add_event_handler("x-anvil-page-added", self.on_mount)
    self.add_event_handler("x-anvil-page-removed", self.on_cleanup)

  def on_mount(self, **event_args):
    self.dom_nodes['anvil-m3-iconbutton-container'].addEventListener('click', self.handle_click)
  def on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-iconbutton-container'].removeEventListener('click', self.handle_click)

  def handle_click(self, event):
    event.preventDefault()
    self.selected = not self.selected
    self.raise_event("click")
    
  @property
  def selected(self):
    return self._selected
  @selected.setter
  def selected(self, value):
    self._selected = value
    self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle("selected", value)
    self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle("selected", value)
    self.apply_styles()
    

  @property
  def background(self):
    return self._background
  @background.setter
  def background(self, value):
    self._background = value
    self.apply_styles()

  @property
  def border(self):
    return self._border
  @border.setter
  def border(self, value):
    self._border = value
    self.apply_styles()

  @property
  def icon_color(self):
    return self._icon_color
  @icon_color.setter
  def icon_color(self, value):
    self._icon_color = value
    self.apply_styles()

  @property
  def selected_background(self):
    return self._selected_background
  @selected_background.setter
  def selected_background(self, value):
    self._selected_background = value
    self.apply_styles()

  @property
  def selected_border(self):
    return self._selected_border
  @selected_border.setter
  def selected_border(self, value):
    self._selected_border = value
    self.apply_styles()

  @property
  def selected_icon_color(self):
    return self._selected_icon_color
  @selected_icon_color.setter
  def selected_icon_color(self, value):
    self._selected_icon_color = value
    self.apply_styles()

  @property
  def appearance(self):
    return self._appearance
  @appearance.setter
  def appearance(self, value):
    self._appearance = value
    self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle("filled", False)
    self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle("filled-tonal", False)
    self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle("outlined", False)
    self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle("filled", False)
    self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle("filled-tonal", False)
    self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle("outlined", False)

    if value is not None:
      class_name = self._appearance_css_classes[value]
      self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle(class_name, True)
      self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle(class_name, True)

  visible = HtmlTemplate.visible
  icon = innerText_property('anvil-m3-iconbutton-icon')
  enabled = enabled_property('anvil-m3-iconbutton-container')
  
  # border = style_property('anvil-m3-iconbutton-container', 'border')
  # icon_color = color_property('anvil-m3-iconbutton-icon', 'color')
  # background = color_property('anvil-m3-iconbutton-container', 'backgroundColor')

  # def update_selected_border(self):
  #   pass

  # def update_selected_background(self):
  #   pass

  # def update_selected_icon_color(self):
  #   pass

  def apply_styles(self):
    if self.selected:
      pass
    else:
      # self.dom_nodes[dom_node_name].style[style_prop] = value
      self.dom_nodes['anvil-m3-iconbutton-container'].style.backgroundColor = self.background