from ._anvil_designer import StandardPageLayoutTemplate
from anvil import *

class StandardPageLayout(StandardPageLayoutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  
  @property
  def navigation_rail_collapse_to(self):
    return self._navigation_rail_collapse_to

  @navigation_rail_collapse_to.setter
  def navigation_rail_collapse_to(self, value):
    self._navigation_rail_collapse_to = value
    value = value.lower().replace(' ', '-')
    self.dom_nodes['navigation-rail'].className = "navigation-rail"
    self.dom_nodes['navigation-rail'].classList.add(value)
    self._navigation_rail_collapse_to = value


