from ._anvil_designer import TestPageTemplate
from anvil import *
import plotly.graph_objects as go

class TestPage(TestPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #self.checkbox_1.checked = None

  def checkbox_1_change(self, **event_args):
    """This method is called when the component is checked or unchecked"""
    print('hello')



  

  




