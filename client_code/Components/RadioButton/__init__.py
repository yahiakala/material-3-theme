from ._anvil_designer import RadioButtonTemplate
from anvil import *
from anvil.js.window import document
import anvil.designer
from ...Functions import checked_property, name_property, innerText_property

class RadioButton(RadioButtonTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.dom_nodes['anvil-m3-radiobutton-hover'].addEventListener("click", self.handle_click)

  # Properties 
  group_name = name_property('anvil-m3-radiobutton-input')

  @property
  def value(self):
    return self._value;
  @value.setter
  def value(self, value):
    self._value = value
    self.dom_nodes['anvil-m3-radiobutton-input'].value = value or ""
    
  @property
  def text(self):
    return self._text
  @text.setter
  def text(self, value):
    self._text = value
    if value:
      self.updateText(value, False)
 
  @property
  def selected(self):
    return self._selected
  @selected.setter
  def selected(self, value):
    self._selected = value
    self.dom_nodes['anvil-m3-radiobutton-input'].checked = value
   
  @property
  def enabled(self):
    return self._enabled
  @enabled.setter
  def enabled(self, value):
    self._enabled = value
    self.dom_nodes['anvil-m3-radiobutton-input'].disabled = not value

  # Class Functions
  def _anvil_get_design_info_(self, as_layout=False):
    di = super()._anvil_get_design_info_(as_layout)
    di['interactions'] = [{
      "type": "whole_component",
      "title": "Edit text",
      "icon": "edit",
      "default": True,
      "callbacks": {
        "execute": lambda: anvil.designer.start_inline_editing(self, "text", self.dom_nodes['anvil-m3-radiobutton-label'])
      }
    }]
    return di 
    
  def handle_click(self, event):
    if self.enabled:
      self.dom_nodes['anvil-m3-radiobutton-input'].focus()
      self.selected = True
      self.raise_event("click")
      
  def updateText(self, value, in_designer_placeholder):
    self.dom_nodes['anvil-m3-radiobutton-label'].innerText = value or ""
    if not in_designer_placeholder:
      self.dom_nodes['anvil-m3-radiobutton-label'].removeAttribute("style")
   
  def form_show(self, **event_args):
    if anvil.designer.in_designer:
      if not self.text:
        self.updateText(anvil.designer.get_design_name(self), True)

  def get_group_value(self):
    selectedItem = document.querySelector(f".anvil-m3-radiobutton-input[name={self.group_name}]:checked")
    return selectedItem.value
