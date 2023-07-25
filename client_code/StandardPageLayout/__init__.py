from ._anvil_designer import StandardPageLayoutTemplate
from anvil import *
from ..Functions import innerText_property


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
    self.dom_nodes['anvil-m3-navigation-rail'].className = "anvil-m3-navigation-rail"
    self.dom_nodes['anvil-m3-navigation-rail'].classList.add(f"anvil-m3-{value}")
    self.dom_nodes['anvil-m3-content'].className = "anvil-m3-content"
    self.dom_nodes['anvil-m3-content'].classList.add(f"anvil-m3-{value}")

  app_title = innerText_property('anvil-m3-app-title')

