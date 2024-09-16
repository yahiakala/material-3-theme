from ._anvil_designer import AnotherPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .._Components.Link import Link as M3_Link
from .._Components.Slider import Slider

class AnotherPage(AnotherPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.m3_slider = Slider()
    file_contents = "Hello, world".encode()
    my_media = anvil.BlobMedia(content_type="text/plain", content=file_contents, name="hello.txt")
    self.link_1.url = my_media
    self.link_2.url = my_media

  def slider_1_change(self, **event_args):
    """This method is called when the value of the component is changed"""
    self.text_1.text = self.slider_1.value

  def text_field_3_pressed_enter(self, **event_args):
    """This method is called when the user presses enter in this component."""
    self.m3_slider.value = 3

  def icon_button_1_click(self, **event_args):
    self.layout.layout.show_sidesheet = False




