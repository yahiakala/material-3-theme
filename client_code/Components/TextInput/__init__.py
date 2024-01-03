from ._anvil_designer import TextInputTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...Functions import property_without_callback, property_with_callback
from anvil import HtmlTemplate

class TextInput(TextInputTemplate):
  def __init__(self, **properties):
    
    self._props = properties
    self.init_components(**properties)
    
  visible = HtmlTemplate.visible
  supporting_text = property_without_callback("supporting_text")
  placeholder = property_without_callback("label_text")

  def set_appearance(self, value):
    self.dom_nodes['textinput-component'].classList.toggle('outlined', bool(value))  
  appearance = property_with_callback("appearance", set_appearance)
  
  def set_placeholder(self, value):
    pass
  placeholder = property_with_callback('placeholder', set_placeholder)

  def set_label(self, value):
    pass
  label_text = property_with_callback("label_text", set_label)