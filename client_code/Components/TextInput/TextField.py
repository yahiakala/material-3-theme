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
                         "default_value": "",
                         # "include_none_option": True, 
                         # "none_option_label": "None", 
                         "description": "right side icon"}
trailing_icon_property = {"name": "trailing_icon", 
                         "type": "enum", 
                         "options": _m3_icons, 
                         "group": "Attributes", 
                         "important": True, 
                         "default_value": "",
                         # "include_none_option": True, 
                         "description": "left side icon"}

class TextField(TextInput):
  _anvil_properties_ = [leading_icon_property, trailing_icon_property, *TextInput._anvil_properties_]

  def __init__(self, **properties):
    super().__init__(**properties)
    self.init_components(**properties)
    hiddenInput = self.dom_nodes['textarea']
    self.dom_nodes['input-container'].removeChild(hiddenInput)
    
    self.on_input = self.on_input

    self.add_event_handler("x-anvil-page-added", self.on_mount)
    self.add_event_handler("x-anvil-page-removed", self.on_cleanup)

  def on_mount(self, **event_args):
    self.dom_nodes['textfield'].addEventListener("input", self.on_input)
    
  def on_cleanup(self, **event_args):
    self.dom_nodes['textfield'].removeEventListener("keydown", self.on_input)
  

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

  def set_enabled(self, value):
    supporting_text = self.dom_nodes['subcontent']
    if value:
      self.dom_nodes['textfield'].removeAttribute("disabled")
      supporting_text.classList.remove("anvil-m3-textinput-disabled")
    else:
      self.dom_nodes['textfield'].setAttribute("disabled", " ")
      supporting_text.classList.add("anvil-m3-textinput-disabled")
  enabled = property_with_callback("enabled", set_enabled)
  
  def set_id(self, value):
    super().set_id(value)
    self.dom_nodes["textfield"].id = value

  def set_error(self, value):
    super().set_error(value)
    icon = "error" if value else self.trailing_icon
    self.set_trailing_icon(icon)
  error = property_with_callback("error", set_error)

  @anvil_property('enum')
  def leading_icon(self):
    return self._props.get('leading_icon')

  @leading_icon.setter
  def leading_icon(self, value):
    self._props['leading_icon'] = value
    self.set_leading_icon(value)

  @anvil_property('enum')
  def trailing_icon(self):
    return self._props.get('trailing_icon')

  @trailing_icon.setter
  def trailing_icon(self, value):
    self._props['trailing_icon'] = value
    self.set_trailing_icon(value)
    
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
  # leading_icon = property_with_callback("leading_icon", set_leading_icon)  
  
  def set_trailing_icon(self, value):
    icon_container = self.dom_nodes['icon-container']
    trailing_icon = self.dom_nodes['trailing-icon']
    text_field_input = self.dom_nodes['textfield']

    if value:
      trailing_icon.style.display = "block"
      trailing_icon.innerText = value
      text_field_input.style.paddingRight = "48px"
    else:
      trailing_icon.style.display = "none"
      trailing_icon.innerText = ""
      text_field_input.style.paddingRight = "16px"
  # trailing_icon = property_with_callback("trailing_icon", set_trailing_icon)

  def set_character_limit(self, value):
    if value is None or value < 1:
      text_field_input = self.dom_nodes['textfield'].removeAttribute("maxlength")
      self.dom_nodes['character-counter'].style = "display: none";
    else:
      text_field_input = self.dom_nodes['textfield'].setAttribute("maxlength", value)
      self.dom_nodes['character-counter'].style = "display: inline";
      self.dom_nodes['character-limit'].innerText = int(value);
  character_limit = property_with_callback("character_limit", set_character_limit)

  def on_input(self, e):
    self.dom_nodes['character-amount'].innerText = len(e.target.value);
