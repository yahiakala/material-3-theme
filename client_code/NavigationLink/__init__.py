from ._anvil_designer import NavigationLinkTemplate
from anvil import *
import anvil.js

class NavigationLink(NavigationLinkTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  @property
  def url(self):
    return self.dom_nodes['navigation-link'].href

  @url.setter
  def url(self, value):
    if value:
      self.dom_nodes['navigation-link'].href = value

  @property
  def text(self):
    return self.dom_nodes['navigation-link-text'].innerHTML

  @text.setter
  def text(self, value):
    if value:
      self.dom_nodes['navigation-link-text'].innerHTML = value

  @property
  def icon(self):
    return self.dom_nodes['navigation-link-text']

  @icon.setter
  def icon(self, value):
    link_icon = self.dom_nodes['navigation-link-icon']
    value = value.replace(":", "-")
    if value:
      link_icon.className = ""
      link_icon.classList.add("fa")
      link_icon.classList.add(value)

  @property
  def selected(self):
    return self._selected

  @selected.setter
  def selected(self, value):
    if value:
      self.dom_nodes['navigation-link'].classList.add('selected')
    else:
      self.dom_nodes['navigation-link'].classList.remove('selected')
      


