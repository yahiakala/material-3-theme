from ._anvil_designer import NavigationLinkTemplate
from anvil import *
import anvil.js
from ...Functions import theme_color_to_css

#Currently, material_icon works and not icon (because they can't both work at the same time)
class NavigationLink(NavigationLinkTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.dom_nodes['navigation-link'].addEventListener("click", self.handle_click)


  def handle_click(self, event):
    event.preventDefault()
    self.raise_event("click")
    if self.navigate_to:
      open_form(self.navigate_to)
      self.selected = True
      
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
    return self._icon

  @icon.setter
  def icon(self, value):
    link_icon = self.dom_nodes['navigation-link-icon']
    self._icon = value
    # value = value.replace(":", "-")
    # if value:
    #   link_icon.className = ""
    #   link_icon.classList.add("fa")
    #   link_icon.classList.add(value)
    

  @property
  def material_icon(self):
    return self._material_icon

  @material_icon.setter
  def material_icon(self, value):
    link_icon = self.dom_nodes['navigation-link-icon']
    self._material_icon = value
    if value:
      link_icon.className = ""
      link_icon.classList.add("material-symbols-outlined")
      link_icon.innerText = value

  @property
  def selected(self):
    return self._selected

  @selected.setter
  def selected(self, value):
    if value:
      self.dom_nodes['navigation-link'].classList.add('selected')
    else:
      self.dom_nodes['navigation-link'].classList.remove('selected')
    self._selected = value

  @property
  def badge(self):
    return self._badge

  @badge.setter
  def badge(self, value):
    if value:
      self.dom_nodes['icon-badge'].style.display = "block"
    else:
      self.dom_nodes['icon-badge'].style.display = "none"
    self._badge = value

  @property
  def badge_count(self):
    return self._badge_count

  @badge_count.setter
  def badge_count(self, value):
    if value and self.badge:
      self.dom_nodes['icon-badge'].innerHTML = value
      self.dom_nodes['icon-badge'].classList.add("large-badge")
    else:
      self.dom_nodes['icon-badge'].innerHTML = ""
      self.dom_nodes['icon-badge'].classList.remove("large-badge")
    self._badge_count = value

  @property
  def navigate_to(self):
    return self._navigate_to

  @navigate_to.setter
  def navigate_to(self, value):
    self._navigate_to = value
  
  @property
  def icon_size(self):
    return self.dom_nodes['navigation-link-icon'].style.fontSize

  @icon_size.setter
  def icon_size(self, value):
    self.dom_nodes['navigation-link-icon'].style.fontSize = value

  @property
  def font_size(self):
    return self.dom_nodes['navigation-link-text'].style.fontSize

  @font_size.setter
  def font_size(self, value):
    self.dom_nodes['navigation-link-text'].style.fontSize = value

  @property
  def font_family(self):
    return self.dom_nodes['navigation-link-text'].style.fontFamily

  @font_family.setter
  def font_family(self, value):
    self.dom_nodes['navigation-link-text'].style.fontFamily = value
  
  @property
  def text_color(self):
    return self.dom_nodes['navigation-link-text'].style.color

  @text_color.setter
  def text_color(self, value):
    if value:
      self.dom_nodes['navigation-link-text'].style.color = theme_color_to_css(value)
  
  @property
  def icon_color(self):
    return self.dom_nodes['navigation-link-icon'].style.color

  @icon_color.setter
  def icon_color(self, value):
    if value:
      self.dom_nodes['navigation-link-icon'].style.color = theme_color_to_css(value)


