from ._anvil_designer import AnotherPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Components.Link import Link as M3_Link
from ..Components.Slider import Slider

class AnotherPage(AnotherPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def slider_1_change(self, **event_args):
    """This method is called when the value of the component is changed"""
    self.text_1.text = self.slider_1.value




