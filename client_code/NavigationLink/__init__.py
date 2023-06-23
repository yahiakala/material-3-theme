from ._anvil_designer import NavigationLinkTemplate
from anvil import *
import anvil.js

class NavigationLink(NavigationLinkTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print(self.dom_nodes['navigation-link'].classList[0])
    print(self.icon)

  @property
  def url(self):
    return self.dom_nodes['navigation-link'].href

  @url.setter
  def url(self, value):
    if value:
      self.dom_nodes['navigation-link'].href = value

  @property
  def icon(self):
    print(self.dom_nodes['link-icon'].classList[1])
    return self.dom_nodes['link-icon'].classList[1]

  @icon.setter
  def icon(self, value):
    print(value)
    value = value.replace(":", "-")
    print(value)
    if value:
      self.dom_nodes['link-icon'].className = ""
      self.dom_nodes['link-icon'].classList.add("fa")
      self.dom_nodes['link-icon'].classList.add(value)
      


