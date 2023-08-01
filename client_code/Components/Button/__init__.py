from ._anvil_designer import ButtonTemplate
from anvil import *
import anvil.js

class Button(ButtonTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.dom_nodes['button'].addEventListener("click", self.handle_click)

  def handle_click(self, event):
    event.preventDefault()
    self.raise_event("click")

  @property
  def material_icon(self):
    return self._material_icon

  @material_icon.setter
  def material_icon(self, value):
    button = self.dom_nodes['button']
    button_icon = self.dom_nodes['button-icon']
    self._material_icon = value
    if value:
      button_icon.innerText = value
      button_icon.style.display = "block"
      button.classList.add('anvil-m3-icon-padding')

  @property
  def text(self):
    return self.dom_nodes['button-text'].innerHTML

  @text.setter
  def text(self, value):
    if value:
      self.dom_nodes['button-text'].innerHTML = value

  @property
  def enabled(self):
    return self._enabled

  @enabled.setter
  def enabled(self, value):
    self._enabled = value
    if value:
      self.dom_nodes['button'].removeAttribute("disabled")
    else:
      self.dom_nodes['button'].setAttribute("disabled", " ")

  @property
  def appearance(self):
    return self._appearance

  @appearance.setter
  def appearance(self, value):
    self._appearance = value
    button = self.dom_nodes['button']
    if value:
      button.classList.add(f"anvil-m3-{value}")


  
