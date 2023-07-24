from ._anvil_designer import CardTemplate
from anvil import *

class Card(CardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.printList()
    print()
    self.hasClass("anvil-m3-card")

  def printList(self):
    classes = self.dom_nodes['anvil-m3-card'].classList
    for c in classes:
      print(c)

  @property
  def appearance(self):
    return self._appearance

  @appearance.setter
  def appearance(self, value):
    card = self.dom_nodes['anvil-m3-card']
    if value:
      card.classList.add(value)
    # needs to replace instead of adding.

  @property
  def interactive(self):
    return self._interactive

  @interactive.setter
  def interactive(self, value):
    card = self.dom_nodes['anvil-m3-card']
    # if value is false
    #   check if card includes interactive. remove if it does.
    # if value is true
    #   check if card includes interactive. add it if it doesn't.


  def hasClass(self, className):
    classes = self.dom_nodes['anvil-m3-card'].classList
    if className in classes:
      print("YESSS")
      
  