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

  def button_2_click(self, **event_args):
    print(self.radio_button_2.get_group_value())

  def set_group_1_label(self, value):
    self.label_5.text = value
    
  def set_group_2_label(self, value):
    self.label_6.text = value
    
  def set_group_qwer_label(self, value):
    self.label_7.text = value

  def radio_button_1_click(self, **event_args):
    v = self.radio_button_1.get_group_value()
    self.set_group_1_label(f"{v}")

  def radio_button_8_click(self, **event_args):
    v = self.radio_button_8.get_group_value()
    self.set_group_qwer_label(v)


    




