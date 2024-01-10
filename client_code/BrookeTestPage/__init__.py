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
    # self.layout.layout.show_sidesheet = False
    print('in the init:', self.switch_1.selected)
        
  def button_1_click(self, **event_args):
    """This method is called when the component is clicked"""
    self.layout.layout.show_sidesheet = not self.layout.layout.show_sidesheet

  def file_loader_2_focus(self, **event_args):
    """This method is called when the FileLoader gets focus"""
    print('im so focused rn')

  def file_loader_2_lost_focus(self, **event_args):
    """This method is called when the FileLoader loses focus"""
    print('im so unfocused')

  def file_loader_5_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    download(file)

  def interactive_card_1_click(self, **event_args):
    """This method is called when the component is clicked"""

  def file_loader_1_change(self, file, files, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    print(files)

  def file_loader_2_change(self, file, files, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    print(files)

  def button_3_click(self, **event_args):
    """This method is called when the component is clicked"""
    self.switch_1.selected = not self.switch_1.selected








