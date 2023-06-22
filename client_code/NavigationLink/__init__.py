from ._anvil_designer import NavigationLinkTemplate
from anvil import *
import anvil.js

class NavigationLink(NavigationLinkTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)



  @property
  def url(self):
    return self._url

  @url.setter
  def url(self, value):
    self._url = value
    if value:
      el = anvil.js.get_dom_node(self).querySelector(".navigation-link")
      el.setAttribute("href", value)


