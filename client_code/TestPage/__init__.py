from ._anvil_designer import TestPageTemplate
from anvil import *
import plotly.graph_objects as go

class TestPage(TestPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #self.checkbox_1.checked = None

  def link_1_click(self, **event_args):
    """This method is called clicked"""
    print('hola')






  

  




