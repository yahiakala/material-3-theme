from ._anvil_designer import TestPageTemplate
from anvil import *
import plotly.graph_objects as go

class TestPage(TestPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print(self.checkbox_1.selected)

    # Any code you write here will run before the form opens.

  def button_3_click(self, **event_args):
    """This method is called when the component is clicked"""
    alert("clicked button in elevated card")

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.text_field_2.error = True




