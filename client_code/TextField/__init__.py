from ._anvil_designer import TextFieldTemplate
from anvil import *

class TextField(TextFieldTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @property
  def max_characters(self):
    return self._max_characters

  @max_characters.setter
  def max_characters(self, value):
    character_count = self.dom_nodes['text-field-character-count']
    if value:
      character_count.style.display = "block"
      character_count.innerHTML = value



  

  
