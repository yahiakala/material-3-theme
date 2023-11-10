from ._anvil_designer import BrookeTestPageTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import time

class BrookeTestPage(BrookeTestPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

    # Any code you write here will run before the form opens.

  def file_loader_2_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    time.sleep(5)
    print(file)
    

  def button_1_click(self, **event_args):
    """This method is called when the component is clicked"""
    self.file_loader_2.clear()

  def file_loader_2_focus(self, **event_args):
    """This method is called when the FileLoader gets focus"""
    print('im so focused rn')

  def file_loader_2_lost_focus(self, **event_args):
    """This method is called when the FileLoader loses focus"""
    print('im so unfocused')




