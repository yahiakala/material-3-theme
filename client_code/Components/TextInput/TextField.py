import anvil.server
from . import TextInput
import anvil.designer
from ...Functions import property_with_callback, italic_property, bold_property, underline_property, font_family_property, font_size_property, color_property
from anvil.property_utils import anvil_property
from ...utils import _m3_icons

"""
Remaining tasks on hold for DEV: 
- property "NONE" enum selection for icons
"""

leading_icon_property = {"name": "leading_icon", 
                         "type": "enum", 
                         "options": _m3_icons, 
                         "group": "Icon", 
                         "important": True, 
                         "default_value": "",
                         # "include_none_option": True, 
                         # "none_option_label": "None", 
                         "description": "The icon to display on the right side of this component."}
trailing_icon_property = {"name": "trailing_icon", 
                         "type": "enum", 
                         "options": _m3_icons, 
                         "group": "Icon", 
                         "important": True, 
                         "default_value": "",
                         # "include_none_option": True, 
                         "description": "The icon to display on the left side of this component."}

click_event = {"name": "click", "defaultEvent": True, "description": "When the trailing icon is clicked"}

class TextField(TextInput):
  _anvil_properties_ = [leading_icon_property, trailing_icon_property, *TextInput._anvil_properties_]
  _anvil_events_ = [click_event, *TextInput._anvil_events_]
  
  def __init__(self, **properties):
    super().__init__(**properties)
    self.init_components(**properties)
    hiddenInput = self.dom_nodes['anvil-m3-textarea']
    self.dom_nodes['anvil-m3-input-container'].removeChild(hiddenInput)
    
    self.on_key_down = self.on_key_down
    self.on_change = self.on_change
    self.handle_click = self.handle_click

    self.add_event_handler("x-anvil-page-added", self.on_mount)
    self.add_event_handler("x-anvil-page-removed", self.on_cleanup)

  def on_mount(self, **event_args):
    self.dom_nodes['anvil-m3-textfield'].addEventListener("input", self.on_input)
    self.dom_nodes['anvil-m3-textfield'].addEventListener("keydown", self.on_key_down)
    self.dom_nodes['anvil-m3-textfield'].addEventListener("change", self.on_change)
    self.dom_nodes['anvil-m3-trailing-icon'].addEventListener("click", self.handle_click)
    
  def on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-textfield'].removeEventListener("input", self.on_input)
    self.dom_nodes['anvil-m3-textfield'].removeEventListener("keydown", self.on_key_down)
    self.dom_nodes['anvil-m3-textfield'].removeEventListener("change", self.on_change)
    self.dom_nodes['anvil-m3-trailing-icon'].removeEventListener("click", self.handle_click)
  

  def set_placeholder(self, value):
    input = self.dom_nodes['anvil-m3-textfield']
    if value:
      input.placeholder = value
      input.classList.add('anvil-m3-has-placeholder')
    else:
      input.placeholder = " "
      input.classList.remove('anvil-m3-has-placeholder')
  placeholder = property_with_callback('placeholder', set_placeholder)
      
  def set_label(self, value):
    self.dom_nodes['anvil-m3-label-text'].innerText = value or ""
    if value:
      self.dom_nodes['anvil-m3-textfield'].classList.toggle('has_label_text', True)
    else:
      self.dom_nodes['anvil-m3-textfield'].classList.toggle('has_label_text', anvil.designer.in_designer);
  label_text = property_with_callback("label_text", set_label)

  def set_enabled(self, value):
    supporting_text = self.dom_nodes['anvil-m3-subcontent']
    if value:
      self.dom_nodes['anvil-m3-textfield'].removeAttribute("disabled")
      supporting_text.classList.remove("anvil-m3-textinput-disabled")
    else:
      self.dom_nodes['anvil-m3-textfield'].setAttribute("disabled", " ")
      supporting_text.classList.add("anvil-m3-textinput-disabled")
  enabled = property_with_callback("enabled", set_enabled)
  
  def set_id(self, value):
    super().set_id(value)
    self.dom_nodes["anvil-m3-textfield"].id = value

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
    icon_container = self.dom_nodes['anvil-m3-icon-container']
    leading_icon = self.dom_nodes['anvil-m3-leading-icon']
    text_field_input = self.dom_nodes['anvil-m3-textfield']
    border_container = self.dom_nodes['anvil-m3-border-container']

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
    icon_container = self.dom_nodes['anvil-m3-icon-container']
    trailing_icon = self.dom_nodes['anvil-m3-trailing-icon']
    text_field_input = self.dom_nodes['anvil-m3-textfield']

    if value:
      trailing_icon.style.display = "block"
      trailing_icon.innerText = value
      text_field_input.style.paddingRight = "48px"
    else:
      trailing_icon.style.display = "none"
      trailing_icon.innerText = ""
      text_field_input.style.paddingRight = "16px"
  # trailing_icon = property_with_callback("trailing_icon", set_trailing_icon)

  italic_display = italic_property('anvil-m3-textfield', 'italic_label')
  bold_display = bold_property('anvil-m3-textfield', 'bold_display')
  underline_display = underline_property('anvil-m3-textfield', 'underline_display')
  display_font_size = font_size_property('anvil-m3-textfield', 'display_font_size')
  display_font = font_family_property('anvil-m3-textfield', 'display_font')
  display_text_color = color_property('anvil-m3-textfield', 'color', 'display_text_color')

  def set_character_limit(self, value):
    if value is None or value < 1:
      text_field_input = self.dom_nodes['anvil-m3-textfield'].removeAttribute("maxlength")
      self.dom_nodes['anvil-m3-character-counter'].style = "display: none";
    else:
      text_field_input = self.dom_nodes['anvil-m3-textfield'].setAttribute("maxlength", value)
      self.dom_nodes['anvil-m3-character-counter'].style = "display: inline";
      self.dom_nodes['anvil-m3-character-limit'].innerText = int(value);
  character_limit = property_with_callback("character_limit", set_character_limit)

  def handle_click(self, event):
    event.preventDefault()
    self.raise_event("click")

