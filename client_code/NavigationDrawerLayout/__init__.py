from ._anvil_designer import NavigationDrawerLayoutTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js import window


class NavigationDrawerLayout(NavigationDrawerLayoutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.nav_drawer = self.dom_nodes['anvil-m3-navigation-drawer']
    self.nav_drawer_open_btn = self.dom_nodes['anvil-m3-drawer-open-btn']
    # self.nav_drawer_close_btn = self.dom_nodes['anvil-m3-drawer-close-btn']
    self.nav_drawer_scrim = self.dom_nodes['anvil-m3-navigation-drawer-scrim']
    self.app_bar = self.dom_nodes['anvil-m3-top-app-bar']

    window.document.addEventListener('scroll', self.add_scroll_class)
    self.nav_drawer_open_btn.addEventListener('click', self.open_nav_drawer)
    # self.nav_drawer_close_btn.addEventListener('click', self.hide_nav_drawer)
    self.nav_drawer_scrim.addEventListener('click', self.hide_nav_drawer)

  def open_nav_drawer(self, e):
    self.nav_drawer.style.width = '360px'
    self.nav_drawer.style.left = "0px"
    self.nav_drawer.classList.add('anvil-m3-shown')
    self.nav_drawer_scrim.animate([{'opacity': '0'},{'opacity': '1'}], {'duration': 250, 'iterations': 1})

  def hide_nav_drawer(self, e):
    self.nav_drawer.style.left = "-101%"
    self.nav_drawer_scrim.animate([{'opacity': '1'},{'opacity': '0'}], {'duration': 250, 'iterations': 1})
    window.setTimeout(lambda: self.nav_drawer.style.setProperty('width', '0px'), 250)
    window.setTimeout(lambda: self.nav_drawer.classList.remove('anvil-m3-shown'), 245)

  def add_scroll_class(self, e):
    if self.app_bar.classList.contains('anvil-m3-scrolled'):
      if window.scrollY == 0:
        self.app_bar.classList.remove('anvil-m3-scrolled')
    else:
      self.app_bar.classList.add('anvil-m3-scrolled')   
