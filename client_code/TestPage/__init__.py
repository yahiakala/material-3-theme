from ._anvil_designer import TestPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go
from anvil.tables import app_tables
from ..Components.Menu.MenuItem import MenuItem

class TestPage(TestPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.item = anvil.server.call('get_jobs')
    
    self.init_components(**properties)
    # self.selecty_items = [(cat['Items'], cat) for cat in app_tables.test.search()]
    # self.drop_down_1.items = self.selecty_items

  def icon_button_1_click(self, **event_args):
    alert("clicked!!!!")
    
  def icon_button_toggle_1_click(self, **event_args):
    alert("toggled")



