from ._anvil_designer import AnotherPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .._Components.Link import Link as M3_Link
from .._Components.Slider import Slider
from .._Components.NavigationLink import NavigationLink

class AnotherPage(AnotherPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    nav_link = NavigationLink(text="Test")
    self.layout.layout.add_to_nav_rail(nav_link)
    self.image_1.tag.test = 'hello'
    print('image:', self.image_1.tag, self.image_1.tag.test)


  def text_field_3_pressed_enter(self, **event_args):
    """This method is called when the user presses enter in this component."""
    pass

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    print('button:', self.button_1.tag)
    self.button_1.tag.color = 'green'
    print(self.button_1.tag, self.button_1.tag.color)

 
    





