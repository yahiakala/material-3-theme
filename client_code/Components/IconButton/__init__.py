from ._anvil_designer import IconButtonTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.designer
from ...Functions import innerText_property, enabled_property, color_property, style_property, property_with_callback
from anvil import HtmlTemplate

class IconButton(IconButtonTemplate):
  def __init__(self, **properties):
    self._props = properties
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
    self.raise_event("click")

  def appearance_setter(self, value):
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

  appearance = property_with_callback("appearance", appearance_setter)
  visible = HtmlTemplate.visible
  icon = innerText_property('anvil-m3-iconbutton-icon')
  enabled = enabled_property('anvil-m3-iconbutton-container')
  align = style_property('anvil-m3-iconbutton-component', 'justifyContent')
  
  border = style_property('anvil-m3-iconbutton-container', 'border')
  icon_color = color_property('anvil-m3-iconbutton-icon', 'color')
  background = color_property('anvil-m3-iconbutton-container', 'backgroundColor')

  def _anvil_get_interactions_(self): 
    return  [
      {
      "type": "whole_component_multi",
      "title": "Align",
      "options": [{
        "name": "Left Align",
        "id": "left",
        "icon" : "align-left",
      },{
        "name": "Left Center",
        "id": "center",
        "icon" : "align-center",
      },{
        "name": "Left Right",
        "id": "right",
        "icon" : "align-right",
      }],
      "callbacks": {
        "execute": self.setAlignment
      }
    },
      {
      "type": "whole_component",
      "title": "Visible",
      "icon": "add", #TODO: eye icon
      "callbacks": {
        "execute": self.toggle_visible
      }
    }, {
      "type": "whole_component",
      "title": "Enable",
      "icon": "add", #TODO: power icon
      "callbacks": {
        "execute": self.toggle_enabled
      }
    } ]

  def setAlignment(self, value):
    self.align = value
    anvil.designer.update_component_properties(self, {'align': self.align})
  def toggle_visible(self):
    self.visible = not self.visible
    anvil.designer.update_component_properties(self, {'visible': self.visible})
  def toggle_enabled(self):
    self.enabled = not self.enabled
    anvil.designer.update_component_properties(self, {'enabled': self.enabled})