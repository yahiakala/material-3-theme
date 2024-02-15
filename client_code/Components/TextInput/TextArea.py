import anvil.server
from . import TextInput
import anvil.designer
import anvil.js
from anvil.js.window import ResizeObserver
from ...Functions import property_with_callback, italic_property, bold_property, underline_property, font_family_property, font_size_property, color_property

class TextArea(TextInput):
  def __init__(self, **properties):
    super().__init__(**properties)
    self.init_components(**properties)
    hiddenInput = self.dom_nodes['textfield']
    self.dom_nodes['input-container'].removeChild(hiddenInput)

    # self.update_height = self.update_height
    self._on_change = self._on_change
    self._on_focus = self._on_focus
    self._on_lost_focus = self._on_lost_focus

    self.add_event_handler("x-anvil-page-added", self._on_mount)
    self.add_event_handler("x-anvil-page-removed", self._on_cleanup)

  def _on_mount(self, **event_args):
    self.dom_nodes['textarea'].addEventListener("input", self._update_height)
    self.dom_nodes['textarea'].addEventListener("input", self._on_input)
    self.dom_nodes['textarea'].addEventListener("change", self._on_change)
    self.dom_nodes['textarea'].addEventListener("focus", self._on_focus)
    self.dom_nodes['textarea'].addEventListener("blur", self._on_lost_focus)
    self.resize_observer = ResizeObserver(self._on_resize)
    self.resize_observer.observe(self.dom_nodes['textarea'])
    
  def _on_cleanup(self, **event_args):
    self.dom_nodes['textarea'].removeEventListener("input", self._update_height)
    self.dom_nodes['textarea'].removeEventListener("input", self._on_input)
    self.dom_nodes['textarea'].removeEventListener("change", self._on_change)
    self.dom_nodes['textarea'].removeEventListener("focus", self._on_focus)
    self.dom_nodes['textarea'].removeEventListener("blur", self._on_lost_focus)
    self.resize_observer.unobserve(self.dom_nodes['textarea'])
  
  italic_display = italic_property('textarea', 'italic_label')
  bold_display = bold_property('textarea', 'bold_display')
  underline_display = underline_property('textarea', 'underline_display')
  display_font_size = font_size_property('textarea', 'display_font_size')
  display_font = font_family_property('textarea', 'display_font')
  display_text_color = color_property('textarea', 'color', 'display_text_color')
  background = color_property('textarea', 'backgroundColor', 'background')

  def _set_placeholder(self, value):
    input = self.dom_nodes['textarea']
    if value:
      input.placeholder = value
      input.classList.add('anvil-m3-has-placeholder')
    else:
      input.placeholder = " "
      input.classList.remove('anvil-m3-has-placeholder')
  placeholder = property_with_callback('placeholder', _set_placeholder)

  @property
  def text(self):
    return self.dom_nodes['textarea'].value

  @text.setter
  def text(self, value):
    self.dom_nodes['textarea'].value = value

  def _set_label(self, value):
    self.dom_nodes['label-text'].innerText = value or ""
    if value:
      self.dom_nodes['textarea'].classList.toggle('has_label_text', True)
    else:
      self.dom_nodes['textarea'].classList.toggle('has_label_text', anvil.designer.in_designer);
  label_text = property_with_callback("label_text", _set_label)
  
  def _set_enabled(self, value):
    supporting_text = self.dom_nodes['subcontent']
    if value:
      self.dom_nodes['textarea'].removeAttribute("disabled")
      supporting_text.classList.remove("anvil-m3-textinput-disabled")
    else:
      self.dom_nodes['textarea'].setAttribute("disabled", " ")
      supporting_text.classList.add("anvil-m3-textinput-disabled")
  enabled = property_with_callback("enabled", _set_enabled)

  def _set_id(self, value):
    super()._set_id(value)
    self.dom_nodes["textarea"].id = value

  def _update_height(self, event):
    self.dom_nodes['textarea'].style.height = '56px' #min-height based off specs
    h = event.target.scrollHeight;
    self._set_height(h)

  def _on_resize(self, entries, observer):
    for entry in entries:
      h = entry.target.scrollHeight
    self._set_height(h)

  def _set_height(self, h):
    self.dom_nodes['textarea'].style.height = f'{h}px'
    self.dom_nodes['border-container'].style.height = f'{h}px'

  def _set_character_limit(self, value):
    if value is None or value < 1:
      text_field_input = self.dom_nodes['textarea'].removeAttribute("maxlength")
      self.dom_nodes['character-counter'].style = "display: none";
    else:
      text_field_input = self.dom_nodes['textarea'].setAttribute("maxlength", value)
      self.dom_nodes['character-counter'].style = "display: inline";
      self.dom_nodes['character-limit'].innerText = int(value);
  character_limit = property_with_callback("character_limit", _set_character_limit)