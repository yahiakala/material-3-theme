from ._anvil_designer import CheckboxTemplate
from anvil import *
from ...Functions import checked_property, innerText_property, enabled_property
import anvil.designer

#TODO: 
# * add in designer text edit
# * add component name when added to page
# * add focus method
# * add change event

class Checkbox(CheckboxTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self._text = properties.get('text', '')
    self.dom_nodes['anvil-m3-checkbox-hover'].addEventListener("click", self.handle_click)

  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    print(bool(self.text))
    if anvil.designer.in_designer and not self.text:
      print('yes')
      self.text = anvil.designer.get_design_name(self)
      self.dom_nodes['anvil-m3-checkbox-label'].style.fontStyle = "italic"
      self.dom_nodes['anvil-m3-checkbox-label'].style.color = "#bbb"
      

  enabled = enabled_property('anvil-m3-checkbox')
  selected = checked_property('anvil-m3-checkbox')
  label = innerText_property('anvil-m3-checkbox-label')

  @property
  def text(self):
    return self._text

  @text.setter
  def text(self, value):
    self._text = value
    self.dom_nodes['anvil-m3-checkbox-label'].innerHTML = value or ""

  @property
  def error(self):
    return self._error

  @error.setter
  def error(self, value):
    self.dom_nodes['anvil-m3-checkbox-container'].classList.remove('anvil-m3-checkbox-error')
    self._error = value
    if value:
      self.dom_nodes['anvil-m3-checkbox-container'].classList.add('anvil-m3-checkbox-error')
      self._error = value

  def handle_click(self, event):
    if self.enabled:
      self.dom_nodes['anvil-m3-checkbox'].focus()
      self.selected = not self.selected
      self.raise_event("click")
