from ._anvil_designer import FileLoaderTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...Functions import underline_property, italic_property, style_property, color_property, innerText_property, bold_property, font_size_property


class FileLoader(FileLoaderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  text = innerText_property('anvil-m3-fileloader-label')



