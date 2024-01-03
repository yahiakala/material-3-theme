import anvil.server
from . import TextInput
import anvil.designer
from ...Functions import property_with_callback, theme_color_to_css
from anvil.property_utils import anvil_property
from ...utils import _m3_icons

leading_icon_property = {"name": "leading_icon", 
                         "type": "enum", 
                         "options": _m3_icons, 
                         "group": "Attributes", 
                         "important": True, 
                         "default_value": "null",
                         "include_none_option": True, 
                         "description": "right side icon"}
trailing_icon_property = {"name": "trailing_icon", 
                         "type": "enum", 
                         "options": _m3_icons, 
                         "group": "Attributes", 
                         "important": True, 
                         "default_value": "null",
                         "include_none_option": True, 
                         "description": "left side icon"}

class TextField(TextInput):
  _anvil_properties_ = [leading_icon_property, trailing_icon_property, *TextInput._anvil_properties_]

  def __init__(self, **properties):
    super().__init__(**properties)
    self.init_components(**properties)
    self.dom_nodes['textfield'].classList.remove('anvil-m3-hide-tag')

  def set_placeholder(self, value):
    input = self.dom_nodes['textfield']
    if value:
      input.placeholder = value
      input.classList.add('anvil-m3-has-placeholder')
    else:
      input.placeholder = " "
      input.classList.remove('anvil-m3-has-placeholder')
  placeholder = property_with_callback('placeholder', set_placeholder)
      

  def set_label(self, value):
    self.dom_nodes['label-text'].innerText = value or ""
    if value:
      self.dom_nodes['textfield'].classList.toggle('has_label_text', True)
    else:
      self.dom_nodes['textfield'].classList.toggle('has_label_text', anvil.designer.in_designer);
  label_text = property_with_callback("label_text", set_label)

  def set_leading_icon(self, value):
    icon_container = self.dom_nodes['icon-container']
    leading_icon = self.dom_nodes['leading-icon']
    text_field_input = self.dom_nodes['textfield']
    border_container = self.dom_nodes['border-container']

    if value:
      leading_icon.style.display = "block"
      leading_icon.innerText = value
      icon_container.style.paddingLeft = "12px"
      text_field_input.style.paddingLeft = "48px"
      border_container.classList.add("with-icon")
    else:
      leading_icon.style.display = "none"
      leading_icon.innerText = ""
      icon_container.style.paddingLeft = "16px"
      text_field_input.style.paddingLeft = "16px"
      border_container.classList.remove("with-icon")
  leading_icon = property_with_callback("leading_icon", set_leading_icon)  
  
  def set_trailing_icon(self, value):
    icon_container = self.dom_nodes['icon-container']
    leading_icon = self.dom_nodes['trailing-icon']
    text_field_input = self.dom_nodes['textfield']

    if value:
      trailing_icon.style.display = "block"
      trailing_icon.innerText = value
      text_field_input.style.paddingRight = "48px"
    else:
      trailing_icon.style.display = "none"
      trailing_icon.innerText = ""
      text_field_input.style.paddingRight = "16px"
  trailing_icon = property_with_callback("trailing_icon", set_trailing_icon)
