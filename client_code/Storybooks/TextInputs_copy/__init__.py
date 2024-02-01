from ._anvil_designer import TextInputs_copyTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class TextInputs_copy(TextInputs_copyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.update_tf1_icon()
    

    # Any code you write here will run before the form opens.

  def text_field_1_copy_2_click(self, **event_args):
    alert("clicked outlined style")

  def text_field_1_click(self, **event_args):
    self.text_field_1.hide_text = not self.text_field_1.hide_text 
    self.update_tf1_icon()

  def button_1_click(self, **event_args):
    """This method is called when the component is clicked."""
    self.text_field_3_copy.hide_text =  not self.text_field_3_copy.hide_text
    

  def text_field_3_copy_pressed_enter(self, **event_args):
    """This method is called when the user presses enter in this component."""
    alert("Done")

  def update_tf1_icon(self):
    if self.text_field_1.hide_text == True:
      self.text_field_1.trailing_icon = 'visibility'
    else:
      self.text_field_1.trailing_icon = 'visibility_off'

  def text_field_1_copy_copy_click(self, **event_args):
    """This method is called when the trailing icon is clicked."""
    pass
