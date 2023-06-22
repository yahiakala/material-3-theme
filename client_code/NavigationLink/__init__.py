from ._anvil_designer import NavigationLinkTemplate
from anvil import *

class NavigationLink(NavigationLinkTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  @property
  def icon(self):
      return self._icon

  @my_prop.setter
  def icon(self, value):
      self._icon = value
