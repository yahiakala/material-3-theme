from ._anvil_designer import LinkTemplate
from anvil import *
import anvil.designer
from ...Functions import visible_property, underline_property, italic_property, style_property, color_property, innerText_property, bold_property, font_size_property, href_property


class Link(LinkTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.dom_nodes['anvil-m3-link'].addEventListener("click", self.handle_click) 
    
  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    print(self.url)
    if anvil.designer.in_designer and not self.text and not self.get_components():
      self.dom_nodes['anvil-m3-link-text'].innerText = anvil.designer.get_design_name(self)
    
  def handle_click(self, event):
    self.raise_event("click")

  def _anvil_get_design_info_(self, as_layout=False):
    di = super()._anvil_get_design_info_(as_layout)
    di['interactions'] = [{
      "type": "whole_component",
      "title": "Edit text",
      "icon": "edit",
      "default": True,
      "callbacks": {
        "execute": lambda: anvil.designer.start_inline_editing(self, "text", self.dom_nodes['anvil-m3-link-text'])
      }
    }]
    return di

  text = innerText_property('anvil-m3-link-text')
  url = href_property('anvil-m3-link')
  align = style_property('anvil-m3-link-container', 'justifyContent')
  italic = italic_property('anvil-m3-link-text')
  bold = bold_property('anvil-m3-link')
  font = style_property('anvil-m3-link', 'fontFamily')
  font_size = font_size_property('anvil-m3-link')
  material_icon = innerText_property('anvil-m3-link-icon')
  underline = underline_property('anvil-m3-link-text')
  visible = visible_property('anvil-m3-link-container', 'flex')
  text_color = color_property('anvil-m3-link', 'color')
  icon_color = color_property('anvil-m3-link-icon', 'color')

  @property
  def icon_size(self):
    return self._icon_size

  @icon_size.setter
  def icon_size(self, value):
    self._icon_size = value
    if value: value = f'{value}px'
    self.dom_nodes['anvil-m3-link-icon'].style.fontSize = value
  