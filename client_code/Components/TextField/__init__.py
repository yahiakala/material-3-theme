from ._anvil_designer import TextFieldTemplate
from anvil import *

class TextField(TextFieldTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @property
  def label_text(self):
    return self.dom_nodes['label-text'].innerHTML

  @label_text.setter
  def label_text(self, value):
    if value:
      self.dom_nodes['label-text'].innerHTML = value

  @property
  def supporting_text(self):
    return self.dom_nodes['text-field-supporting'].innerHTML

  @supporting_text.setter
  def supporting_text(self, value):
    if value:
      self.dom_nodes['text-field-supporting'].innerHTML = value

  @property
  def max_characters(self):
    return self._max_characters

  @max_characters.setter
  def max_characters(self, value):
    character_count = self.dom_nodes['text-field-character-count']
    if value:
      character_count.style.display = "block"
      character_count.innerHTML = value

  @property
  def leading_icon(self):
    return self._leading_icon

  @leading_icon.setter
  def leading_icon(self, value):
    text_field_label = self.dom_nodes['text-field-label']
    leading_icon = self.dom_nodes['leading-icon']
    text_field_input = self.dom_nodes['text-field-input']
    self._material_icon = value
    if value:
      leading_icon.style.display = "block"
      leading_icon.innerText = value
      text_field_label.style.paddingLeft = "12px"
      text_field_input.style.paddingLeft = "48px"

  @property
  def trailing_icon(self):
    return self._trailing_icon

  @trailing_icon.setter
  def trailing_icon(self, value):
    text_field_label = self.dom_nodes['text-field-label']
    trailing_icon = self.dom_nodes['trailing-icon']
    text_field_input = self.dom_nodes['text-field-input']
    self._material_icon = value
    if value:
      trailing_icon.style.display = "block"
      trailing_icon.innerText = value
      text_field_input.style.paddingRight = "48px"
    else:
      trailing_icon.style.display = "block"
      trailing_icon.innerText = value
      text_field_input.style.paddingRight = "48px"

  @property
  def enabled(self):
    return self._enabled

  @enabled.setter
  def enabled(self, value):
    self._enabled = value
    input = self.dom_nodes['text-field-input']
    supporting_text = self.dom_nodes['text-field-supporting']
    if value:
      input.removeAttribute("disabled")
      supporting_text.classList.remove("anvil-m3-text-field-supporting-disabled")
    else:
      input.setAttribute("disabled", " ")
      supporting_text.classList.add("anvil-m3-text-field-supporting-disabled")

  @property
  def appearance(self):
    return self._appearance

  @appearance.setter
  def appearance(self, value):
    self._appearance = value
    classes = self.dom_nodes['text-field'].classList
    classes.remove("anvil-m3-outlined")
    if value:
      classes.add(f"anvil-m3-{value}")


  

  
