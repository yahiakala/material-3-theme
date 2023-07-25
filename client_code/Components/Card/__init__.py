from ._anvil_designer import CardTemplate
from anvil import *

class Card(CardTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    
  @property
  def appearance(self):
    return self._appearance
    
  @appearance.setter
  def appearance(self, value):
    self._appearance = value
    classes = self.dom_nodes['anvil-m3-card'].classList
    # classes = self.dom_nodes['anvil-m3-card'].classList
    if (value):
      for c in classes:
        if (c in ["anvil-m3-outlined", "anvil-m3-filled", "anvil-m3-elevated"]):
          classes.remove(c)
      classes.add(f"anvil-m3-{value}")
    
  @property
  def interactive(self):
    return self._interactive
    
  @interactive.setter
  def interactive(self, value):
    self._interactive = value
    classes = self.dom_nodes['anvil-m3-card'].classList
    classes.toggle('anvil-m3-interactive', value)
      
  @property
  def disabled(self):
    return self.disabled
    
  @disabled.setter
  def disabled(self, value):
    self._disabled = value
    classes = self.dom_nodes['anvil-m3-card'].classList
    classes.toggle('anvil-m3-disabled', value)
      
  # def hasClass(self, className):
  #   classes = self.dom_nodes['anvil-m3-card'].classList
  #   return classes.contains(className)

  # def printAllClasses(self):
  #   classes = self.dom_nodes['anvil-m3-card'].classList
  #   for c in classes:
  #     print(c)
