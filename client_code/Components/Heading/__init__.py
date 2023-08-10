from ._anvil_designer import HeadingTemplate
from anvil import *
import anvil.designer
from anvil.js import window
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

  @property
  def underline(self):
    return self._underline

  @underline.setter
  def underline(self, value):
    self._underline = value
    if value:
      self.dom_nodes['anvil-m3-heading-display'].style.textDecoration = 'underline'
      self.dom_nodes['anvil-m3-heading-headline'].style.textDecoration = 'underline'
      self.dom_nodes['anvil-m3-heading-title'].style.textDecoration = 'underline'
    else:
      self.dom_nodes['anvil-m3-heading-display'].style.textDecoration = 'none'
      self.dom_nodes['anvil-m3-heading-headline'].style.textDecoration = 'none'
      self.dom_nodes['anvil-m3-heading-title'].style.textDecoration = 'none'

  @property
  def italic(self):
    return self._italic

  @italic.setter
  def italic(self, value):
    self._italic = value
    if value:
      self.dom_nodes['anvil-m3-heading-display'].style.fontStyle = 'italic'
      self.dom_nodes['anvil-m3-heading-headline'].style.fontStyle = 'italic'
      self.dom_nodes['anvil-m3-heading-title'].style.fontStyle = 'italic'
    else:
      self.dom_nodes['anvil-m3-heading-display'].style.fontStyle = 'none'
      self.dom_nodes['anvil-m3-heading-headline'].style.fontStyle = 'none'
      self.dom_nodes['anvil-m3-heading-title'].style.fontStyle = 'none'

  @property
  def bold(self):
    return self._bold

  @bold.setter
  def bold(self, value):
    self._bold = value
    if value:
      self.dom_nodes['anvil-m3-heading-display'].style.fontWeight = 'bold'
      self.dom_nodes['anvil-m3-heading-headline'].style.fontWeight = 'bold'
      self.dom_nodes['anvil-m3-heading-title'].style.fontWeight = 'bold'
    else:
      self.dom_nodes['anvil-m3-heading-display'].style.fontWeight = 'normal'
      self.dom_nodes['anvil-m3-heading-headline'].style.fontWeight = 'normal'
      self.dom_nodes['anvil-m3-heading-title'].style.fontWeight = 'normal'

  @property
  def font_size(self):
    return self._font_size

  @font_size.setter
  def font_size(self, value):
    self._font_size = value
    self.dom_nodes['anvil-m3-heading-display'].style.fontSize = f'{value}px'
    self.dom_nodes['anvil-m3-heading-headline'].style.fontSize = f'{value}px'
    self.dom_nodes['anvil-m3-heading-title'].style.fontSize = f'{value}px'

  @property
  def font_size(self):
    return self._font_size

  @font_size.setter
  def font_size(self, value):
    self._font_size = value
    self.dom_nodes['anvil-m3-heading-display'].style.fontSize = f'{value}px'
    self.dom_nodes['anvil-m3-heading-headline'].style.fontSize = f'{value}px'
    self.dom_nodes['anvil-m3-heading-title'].style.fontSize = f'{value}px'
  
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
    display = self.dom_nodes['anvil-m3-heading-display']
    headline = self.dom_nodes['anvil-m3-heading-headline']
    title = self.dom_nodes['anvil-m3-heading-title']
    if value == 'display':
      display.style.display = 'block'
      headline.style.display = 'none'
      title.style.display = 'none'
    elif value == 'headline':
      display.style.display = 'none'
      headline.style.display = 'block'
      title.style.display = 'none'
    elif value == 'title':
      display.style.display = 'none'
      headline.style.display = 'none'
      title.style.display = 'block'


  @property
  def scale(self):
    return self._style

  @scale.setter
  def scale(self, value):
    self._style = value
    self.dom_nodes['anvil-m3-heading'].classList.remove('anvil-m3-heading-large', 'anvil-m3-heading-medium', 'anvil-m3-heading-small')
    self.dom_nodes['anvil-m3-heading'].classList.add(f'anvil-m3-heading-{value}')

