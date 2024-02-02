from ._anvil_designer import TextTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import HtmlTemplate
import anvil.designer
from anvil.js.window import document
from ...Functions import tooltip_property, underline_property, italic_property, style_property, color_property, innerText_property, bold_property, font_size_property, font_family_property, border_property, margin_property
from ...utils import fui, noop
import time
#TODO: figure out what to do with line height
#TODO: figure out default icon sizes 

class Text(TextTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self._props = properties
    self.tooltip_node = None
    self.init_components(**properties)
    
  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    if anvil.designer.in_designer and not self.text:
      self.text = anvil.designer.get_design_name(self)

  def _anvil_get_interactions_(self):
    return [{
      "type": "whole_component",
      "title": "Edit text",
      "icon": "edit",
      "default": True,
      "callbacks": {
        "execute": lambda: anvil.designer.start_inline_editing(self, "text", self.dom_nodes['anvil-m3-text'])
      }
    }]

  visible = HtmlTemplate.visible
  underline = underline_property('anvil-m3-text')
  italic = italic_property('anvil-m3-text')
  bold = bold_property('anvil-m3-text')
  border = border_property('anvil-m3-text-container')
  font = font_family_property('anvil-m3-text', 'font')
  text_color = color_property('anvil-m3-text-container', 'color', 'text_color')
  icon_color = color_property('anvil-m3-text-icon', 'color', 'icon_color')
  background_color = color_property('anvil-m3-text-container', 'backgroundColor', 'background_color')
  text = innerText_property('anvil-m3-text')
  align = style_property('anvil-m3-text-container', 'justifyContent', 'align')
  icon_size = font_size_property('anvil-m3-text-icon', 'icon_size')
  margin = margin_property('anvil-m3-text-container')
  tooltip = tooltip_property('anvil-m3-text-container')

  @property
  def font_size(self):
    return self._props.get('font_size')

  @font_size.setter
  def font_size(self, value):
    self._props['font_size'] = value
    if value: value = f'{value}px'
    self.dom_nodes['anvil-m3-text'].style.fontSize = value
    self.dom_nodes['anvil-m3-text-container'].style.fontSize = value
      
  # @property
  # def icon_size(self):
  #   return self._icon_size

  # @icon_size.setter
  # def icon_size(self, value):
  #   self._icon_size = value
  #   if value: value = f'{value}px'
  #   self.dom_nodes['anvil-m3-text-icon'].style.fontSize = value

  @property
  def material_icon(self):
    return self._material_icon

  @material_icon.setter
  def material_icon(self, value):
    self._material_icon = value
    if value:
      self.dom_nodes['anvil-m3-text-icon'].style.marginRight = "8px"
    else:
      self.dom_nodes['anvil-m3-text-icon'].style.marginRight = ""
    self.dom_nodes['anvil-m3-text-icon'].innerText = value

  @property
  def style(self):
    return self._style

  @style.setter
  def style(self, value):
    self._style = value
    self.dom_nodes['anvil-m3-text'].classList.remove('anvil-m3-text-label', 'anvil-m3-text-body')
    self.dom_nodes['anvil-m3-text'].classList.add(f'anvil-m3-text-{value}')
    self.dom_nodes['anvil-m3-text-container'].classList.remove('anvil-m3-text-label', 'anvil-m3-text-body')
    self.dom_nodes['anvil-m3-text-container'].classList.add(f'anvil-m3-text-{value}')

  @property
  def scale(self):
    return self._style

  @scale.setter
  def scale(self, value):
    self._style = value
    self.dom_nodes['anvil-m3-text'].classList.remove('anvil-m3-text-large', 'anvil-m3-text-medium', 'anvil-m3-text-small')
    self.dom_nodes['anvil-m3-text-container'].classList.remove('anvil-m3-text-large', 'anvil-m3-text-medium', 'anvil-m3-text-small')
    self.dom_nodes['anvil-m3-text'].classList.add(f'anvil-m3-text-{value}')
    self.dom_nodes['anvil-m3-text-container'].classList.add(f'anvil-m3-text-{value}')

      


    
      

  
