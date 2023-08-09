from ._anvil_designer import HeadingTemplate
from anvil import *
import anvil.designer
from ...Functions import visible_property, underline_property, italic_property, style_property, color_property, innerText_property, bold_property, font_size_property

class Heading(HeadingTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    if anvil.designer.in_designer and not self.text:
      self.text = anvil.designer.get_design_name(self)

  def _anvil_get_design_info_(self, as_layout=False):
    di = super()._anvil_get_design_info_(as_layout)
    di['interactions'] = [{
      "type": "whole_component",
      "title": "Edit text",
      "icon": "edit",
      "default": True,
      "callbacks": {
        "execute": lambda: anvil.designer.start_inline_editing(self, "text", self.dom_nodes['anvil-m3-heading'])
      }
    }]
    return di

  visible = visible_property('anvil-m3-heading-container', 'flex')
  underline = underline_property('anvil-m3-heading')
  italic = italic_property('anvil-m3-heading')
  bold = bold_property('anvil-m3-heading')
  font_size = font_size_property('anvil-m3-heading')
  border = style_property('anvil-m3-heading-container', 'border')
  font = style_property('anvil-m3-heading', 'fontFamily')
  text_color = color_property('anvil-m3-heading', 'color')
  background_color = color_property('anvil-m3-heading-container', 'backgroundColor')
  text = innerText_property('anvil-m3-heading')
  align = style_property('anvil-m3-heading-container', 'justifyContent')

  @property
  def material_icon(self):
    return self._material_icon

  @material_icon.setter
  def material_icon(self, value):
    self._material_icon = value
    if value:
      self.dom_nodes['anvil-m3-heading-icon'].innerText = value

  @property
  def style(self):
    return self._style

  @style.setter
  def style(self, value):
    self._style = value
    self.dom_nodes['anvil-m3-heading'].classList.remove('anvil-m3-display', 'anvil-m3-headline', 'anvil-m3-title')
    self.dom_nodes['anvil-m3-heading'].classList.add(f'anvil-m3-{value}')

  @property
  def scale(self):
    return self._style

  @scale.setter
  def scale(self, value):
    self._style = value
    self.dom_nodes['anvil-m3-heading'].classList.remove('anvil-m3-heading-large', 'anvil-m3-heading-medium', 'anvil-m3-heading-small')
    self.dom_nodes['anvil-m3-heading'].classList.add(f'anvil-m3-heading-{value}')

