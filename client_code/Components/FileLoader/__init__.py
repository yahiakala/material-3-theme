from ._anvil_designer import FileLoaderTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...Functions import underline_property, italic_property, style_property, color_property, innerText_property, bold_property, font_size_property, enabled_property


class FileLoader(FileLoaderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  text = innerText_property('anvil-m3-fileloader-label')
  visible = HtmlTemplate.visible
  enabled = enabled_property('anvil-m3-fileloader-form')
  
  @property
  def material_icon(self):
    return self._material_icon

  @material_icon.setter
  def material_icon(self, value):
    self._material_icon = value
    if value:
      self.dom_nodes['anvil-m3-fileloader-icon'].style.marginRight = "8px"
    else:
      self.dom_nodes['anvil-m3-fileloader-icon'].style.marginRight = ""
    self.dom_nodes['anvil-m3-fileloader-icon'].innerText = value



