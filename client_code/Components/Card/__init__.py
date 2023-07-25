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
    card = self.dom_nodes['anvil-m3-card']
    classes = 

  @property
  def interactive(self):
    return self._interactive
  @interactive.setter
  def interactive(self, value):
    card = self.dom_nodes['anvil-m3-card']
    classes = card.classList
    print(classes)
    
    alreadyInteractive = self.hasClass('interactive')
    if (alreadyInteractive and not value):
      print("remove value")
    elif (not alreadyInteractive and value):
      card.classList.add(value)  
  def hasClass(self, className):
    classes = self.dom_nodes['anvil-m3-card'].classList
    return classes.contains(className)
      
  