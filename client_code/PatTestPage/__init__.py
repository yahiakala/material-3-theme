from ._anvil_designer import PatTestPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class PatTestPage(PatTestPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print(self.radio_group_panel_1.selected_button)
    print(self.radio_group_panel_1.buttons)

    # Any code you write here will run before the form opens.

  def radio_button_2_select(self, **event_args):
    """This method is called when the radio button is selected."""
    print(self.radio_group_panel_1.selected_button)
