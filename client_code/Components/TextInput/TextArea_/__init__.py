from ._anvil_designer import TextArea_Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import TextInput
from anvil.property_utils import anvil_property

class TextArea(TextInput):
  _anvil_properties_ = [*TextInput._anvil_properties_]
  
  def __init__(self, **properties):
    super().__init__(**properties)
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
