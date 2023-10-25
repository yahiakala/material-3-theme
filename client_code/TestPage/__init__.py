from ._anvil_designer import TestPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go
from anvil.tables import app_tables
from ..Components.Menu.MenuItem import MenuItem
import time

class TestPage(TestPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.item = anvil.server.call('get_jobs')
    
    self.init_components(**properties)

  def button_1_click(self, **event_args):
    """This method is called when the component is clicked"""
    self.determinate_progress_indicator_3.progress = 0
    self.determinate_progress_indicator_1.progress = 0
    self.start_count()
    
  def start_count(self):
    self.determinate_progress_indicator_1.progress = 0
    start_time = time.time()
    end_time = start_time + 20  # 20 seconds timer

    while time.time() < end_time and self.determinate_progress_indicator_1.progress <= 100:
        self.determinate_progress_indicator_3.progress += 10
        self.determinate_progress_indicator_1.progress += 10
        time.sleep(0.1)  # Adjust the sleep time to change the speed of counting

    
    