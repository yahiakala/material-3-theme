from ._anvil_designer import PatTestPageTemplate
from anvil import *
import anvil.server

class PatTestPage(PatTestPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print(self.radio_group_panel_1.selected_button)
    print(self.radio_group_panel_1.buttons)

    # Any code you write here will run before the form opens.
