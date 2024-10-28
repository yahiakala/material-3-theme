from ._anvil_designer import TestNavigationDrawerLayoutTemplate
from anvil import *
import anvil.server


class TestNavigationDrawerLayout(TestNavigationDrawerLayoutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def icon_button_1_click(self, **event_args):
    self.layout.layout.close_sidesheet()

  def button_1_click(self, **event_args):
    """This method is called when the component is clicked."""
    open_form('BrookeTestPage')
