from ._anvil_designer import testTemplate
from anvil import *
import anvil.server
from ..components import Button



class test(testTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.column_panel_1.add_component(Button(text="Click me"))
    

    # Any code you write here will run before the form opens.
