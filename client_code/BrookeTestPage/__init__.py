from ._anvil_designer import BrookeTestPageTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import time
from ..AnotherPage import AnotherPage

class BrookeTestPage(BrookeTestPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.layout.layout.show_sidesheet = False
    # self.checkbox_1.checked = None
        
  def button_1_click(self, **event_args):
    """This method is called when the component is clicked"""
    self.layout.layout.show_sidesheet = not self.layout.layout.show_sidesheet

  def button_3_click(self, **event_args):
    """This method is called when the component is clicked"""
    self.switch_1.selected = not self.switch_1.selected










