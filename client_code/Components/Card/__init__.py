from ._anvil_designer import CardTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.designer

class Card(CardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    if anvil.designer.in_designer:
      self.dom_nodes['empty-image'].style.display = "none"
      self.dom_nodes['empty-content'].style.display = "none"

    # Any code you write here will run before the form opens.
