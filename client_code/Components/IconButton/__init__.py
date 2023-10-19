from ._anvil_designer import IconButtonTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...Functions import innerText_property

class IconButton(IconButtonTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  @property
  def selected(self):
    return self._selected
  @selected.setter
  def selected(self, value):
    self._selected = value
    # todo update the css of the dom

  @property
  def appearance(self):
    return self._appearance
  @appearance.setter
  def appearance(self, value):
    self._appearance = value
    # todo update the css of the dom

  icon = innerText_property('anvil-m3-iconbutton-icon')
    