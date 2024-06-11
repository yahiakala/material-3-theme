from ._anvil_designer import TestNavigationDrawerLayoutTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class TestNavigationDrawerLayout(TestNavigationDrawerLayoutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def icon_button_1_click(self, **event_args):
    open_form('BrookeTestPage')
