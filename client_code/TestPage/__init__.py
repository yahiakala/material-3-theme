from ._anvil_designer import TestPageTemplate
from anvil import *

class TestPage(TestPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print(self.checkbox_1.selected)

    # Any code you write here will run before the form opens.
