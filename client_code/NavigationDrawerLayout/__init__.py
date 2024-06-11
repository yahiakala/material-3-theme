from ._anvil_designer import NavigationDrawerLayoutTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class NavigationDrawerLayout(NavigationDrawerLayoutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.nav_drawer_open_btn.addEventListener('click', self.open_nav_drawer)
    self.nav_drawer_close_btn.addEventListener('click', self.hide_nav_drawer)
    self.nav_drawer_scrim.addEventListener('click', self.hide_nav_drawer)

    # Any code you write here will run before the form opens.
  def open_nav_drawer(self, e):
    self.nav_rail.style.width = '360px'
    self.nav_rail.style.left = "0px"
    self.nav_rail.classList.add('anvil-m3-shown')
    self.nav_drawer_scrim.animate([{'opacity': '0'},{'opacity': '1'}], {'duration': 250, 'iterations': 1})

  def hide_nav_drawer(self, e):
    self.nav_rail.style.left = "-101%"
    self.nav_drawer_scrim.animate([{'opacity': '1'},{'opacity': '0'}], {'duration': 250, 'iterations': 1})
    window.setTimeout(lambda: self.nav_rail.style.setProperty('width', '0px'), 250)
    window.setTimeout(lambda: self.nav_rail.classList.remove('anvil-m3-shown'), 245)
