from ._anvil_designer import LinkTemplate
from anvil import *
import anvil.designer
from ...Functions import tooltip_property, role_property, underline_property, italic_property, style_property, color_property, innerText_property, bold_property, font_size_property, href_property, font_family_property, margin_property

from anvil import HtmlTemplate

class Link(LinkTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self._props = properties
    self._tooltip_node = None
    self.init_components(**properties)
    self.add_event_handler("x-anvil-page-added", self._on_mount)
    self.add_event_handler("x-anvil-page-removed", self._on_cleanup)

  def _on_mount(self, **event_args):
    self.dom_nodes['anvil-m3-link'].addEventListener("click", self._handle_click)
    
  def _on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-link'].removeEventListener("click", self._handle_click)
    
  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    if anvil.designer.in_designer and not self.text and not self.get_components():
      self.dom_nodes['anvil-m3-link-text'].innerText = anvil.designer.get_design_name(self)
    
  def _handle_click(self, event):
    self.raise_event("click")

  def _anvil_get_interactions_(self):
    return [{
      "type": "whole_component",
      "title": "Edit text",
      "icon": "edit",
      "default": True,
      "callbacks": {
        "execute": lambda: anvil.designer.start_inline_editing(self, "text", self.dom_nodes['anvil-m3-link-text'])
      }
    }]

  text = innerText_property('anvil-m3-link-text')
  # url = href_property('anvil-m3-link')
  align = style_property('anvil-m3-link', 'justifyContent', 'align')
  italic = italic_property('anvil-m3-link-text')
  bold = bold_property('anvil-m3-link')
  font = font_family_property('anvil-m3-link', 'font')
  font_size = font_size_property('anvil-m3-link')
  material_icon = innerText_property('anvil-m3-link-icon')
  underline = underline_property('anvil-m3-link-text')
  visible = HtmlTemplate.visible
  text_color = color_property('anvil-m3-link', 'color', 'text_color')
  icon_color = color_property('anvil-m3-link-icon', 'color', 'icon_color')
  border = style_property('anvil-m3-link', 'border', 'border')
  margin = margin_property('anvil-m3-link')
  tooltip = tooltip_property('anvil-m3-link')
  role = role_property('anvil-m3-link')

  @property
  def url(self):
    return self._props.get('url')

  @url.setter
  def url(self, value):
    if value:
      self._props['url'] = value
      self.dom_nodes['anvil-m3-link'].href = value
    else:
      self.dom_nodes['anvil-m3-link'].href = 'javascript:void(0)'

  @property
  def icon_size(self):
    return self._icon_size

  @icon_size.setter
  def icon_size(self, value):
    self._icon_size = value
    if value: value = f'{value}px'
    self.dom_nodes['anvil-m3-link-icon'].style.fontSize = value

  @property
  def material_icon(self):
    return self.dom_nodes['anvil-m3-link-icon'].innerText

  @material_icon.setter
  def material_icon(self, value):
    if value:
      self.dom_nodes['anvil-m3-link-icon'].style.marginRight = "8px"
    else:
      self.dom_nodes['anvil-m3-link-icon'].style.marginRight = ""
    self.dom_nodes['anvil-m3-link-icon'].innerText = value
  