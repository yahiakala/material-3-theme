from ._anvil_designer import AnotherPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class AnotherPage(AnotherPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print(self.button_menu_1.get_components())
    alert(title="I'm an alert title")
  

  def link_1_click(self, sender, **event_args):
    """This method is called clicked"""
    self.button_menu_1.text = sender.text

  def link_2_click(self, sender, **event_args):
    """This method is called clicked"""
    self.button_menu_1.text = sender.text

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    print('file loader change:', file)

  def button_1_click(self, **event_args):
    """This method is called when the component is clicked."""
    self.file_loader_1.clear()
    print('cleared', self.file_loader_1.file)
