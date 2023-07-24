from ._anvil_designer import CheckboxTemplate
from anvil import *

class Checkbox(CheckboxTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  @property
  def disabled(self):
    return self.dom_nodes['anvil-m3-checkbox'].disabled

  @disabled.setter
  def disabled(self, value):
    self.dom_nodes['anvil-m3-checkbox'].disabled = value

  @property
  def selected(self):
    return self.dom_nodes['anvil-m3-checkbox'].checked

  @selected.setter
  def selected(self, value):
    self.dom_nodes['anvil-m3-checkbox'].checked = value

  @property
  def label(self):
    return self.dom_nodes['anvil-m3-checkbox-label'].innerText

  @label.setter
  def label(self, value):
    self.dom_nodes['anvil-m3-checkbox-label'].innerText = value

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
