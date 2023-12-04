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
    
  def file_loader_2_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    time.sleep(5)
    print(file)
    
  def button_1_click(self, **event_args):
    """This method is called when the component is clicked"""
    self.layout.show_sidesheet = True
    print(self.layout.show_sidesheet)
    print(self.layout.layout)
    #self.layout.navigation_link_1_click()
    self.layout.layout.test_function()


  def file_loader_2_focus(self, **event_args):
    """This method is called when the FileLoader gets focus"""
    print('im so focused rn')

  def file_loader_2_lost_focus(self, **event_args):
    """This method is called when the FileLoader loses focus"""
    print('im so unfocused')

  def file_loader_5_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    download(file)






