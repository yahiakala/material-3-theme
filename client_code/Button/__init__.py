from ._anvil_designer import ButtonTemplate
from anvil import *

class Button(ButtonTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
