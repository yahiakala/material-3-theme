import anvil.server
from . import TextInput
import anvil.designer
import anvil.js
from ...Functions import property_with_callback, italic_property, bold_property, underline_property, font_family_property, font_size_property, color_property

class TextArea(TextInput):
  def __init__(self, **properties):
    super().__init__(**properties)
    self.init_components(**properties)
    hiddenInput = self.dom_nodes['anvil-m3-textfield']
    self.dom_nodes['anvil-m3-input-container'].removeChild(hiddenInput)

    self.update_height = self.update_height
    self.on_key_down = self.on_key_down
    self.on_change = self.on_change

    self.add_event_handler("x-anvil-page-added", self.on_mount)
    self.add_event_handler("x-anvil-page-removed", self.on_cleanup)

  def on_mount(self, **event_args):
    self.dom_nodes['anvil-m3-textarea'].addEventListener("input", self.update_height)
    self.dom_nodes['anvil-m3-textarea'].addEventListener("input", self.on_input)
    self.dom_nodes['anvil-m3-textarea'].addEventListener("keydown", self.on_key_down)
    self.dom_nodes['anvil-m3-textarea'].addEventListener("change", self.on_change)
    
  def on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-textarea'].removeEventListener("input", self.update_height)
    self.dom_nodes['anvil-m3-textarea'].removeEventListener("input", self.on_input)
    self.dom_nodes['anvil-m3-textarea'].removeEventListener("keydown", self.on_key_down)
    self.dom_nodes['anvil-m3-textarea'].removeEventListener("change", self.on_change)
  
  italic_display = italic_property('anvil-m3-textarea', 'italic_label')
  bold_display = bold_property('anvil-m3-textarea', 'bold_display')
  underline_display = underline_property('anvil-m3-textarea', 'underline_display')
  display_font_size = font_size_property('anvil-m3-textarea', 'display_font_size')
  display_font = font_family_property('anvil-m3-textarea', 'display_font')
  display_text_color = color_property('anvil-m3-textarea', 'color', 'display_text_color')

  def set_placeholder(self, value):
    input = self.dom_nodes['anvil-m3-textarea']
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
      self.dom_nodes['anvil-m3-textarea'].classList.toggle('has_label_text', True)
    else:
      self.dom_nodes['anvil-m3-textarea'].classList.toggle('has_label_text', anvil.designer.in_designer)
      
  label_text = property_with_callback("label_text", set_label)
  
  def set_enabled(self, value):
    supporting_text = self.dom_nodes['anvil-m3-subcontent']
    if value:
      self.dom_nodes['anvil-m3-textarea'].removeAttribute("disabled")
      supporting_text.classList.remove("anvil-m3-textinput-disabled")
    else:
      self.dom_nodes['anvil-m3-textarea'].setAttribute("disabled", " ")
      supporting_text.classList.add("anvil-m3-textinput-disabled")
      
  enabled = property_with_callback("enabled", set_enabled)

  def set_id(self, value):
    super().set_id(value)
    self.dom_nodes["anvil-m3-textarea"].id = value

  def update_height(self, event):
    self.dom_nodes['anvil-m3-textarea'].style.height = '56px' #min-height based off specs
    h = event.target.scrollHeight;
    self.dom_nodes['anvil-m3-textarea'].style.height = f'{h}px'
    self.dom_nodes['anvil-m3-border-container'].style.height = f'{h}px'

  def set_character_limit(self, value):
    if value is None or value < 1:
      text_field_input = self.dom_nodes['anvil-m3-textarea'].removeAttribute("maxlength")
      self.dom_nodes['anvil-m3-character-counter'].style = "display: none"
    else:
      text_field_input = self.dom_nodes['anvil-m3-textarea'].setAttribute("maxlength", value)
      self.dom_nodes['anvil-m3-character-counter'].style = "display: inline"
      self.dom_nodes['anvil-m3-character-limit'].innerText = int(value)
      
  character_limit = property_with_callback("character_limit", set_character_limit)