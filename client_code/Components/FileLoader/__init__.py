from ._anvil_designer import FileLoaderTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...Functions import underline_property, italic_property, style_property, color_property, innerText_property, bold_property, font_size_property, enabled_property
from anvil.js.window import FileReader, Uint8Array
from ...utils import gen_id


class FileLoader(FileLoaderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self._props = properties
    self.init_components(**properties)
    self.add_event_handler("x-anvil-page-added", self.on_mount)
    self.add_event_handler("x-anvil-page-removed", self.on_cleanup)
    if not anvil.designer.in_designer:
      id = gen_id()
      self.dom_nodes["anvil-m3-fileloader-input"].id = id
      self.dom_nodes["anvil-m3-fileloader-label"].setAttribute("for", id)

  def focus(self):
    self.dom_nodes['anvil-m3-fileloader-container'].focus()

  def on_mount(self, **event_args):
    self.dom_nodes['anvil-m3-fileloader-input'].addEventListener("change", self.handle_change)
    
  def on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-fileloader-input'].removeEventListener("change", self.handle_change)

  def handle_change(self, event, **event_args):
    files = self.dom_nodes['anvil-m3-fileloader-input'].files
    file_reader = FileReader()
    def onload(e):
      as_buffer = file_reader.result
      as_bytes = Uint8Array(as_buffer)
      self.raise_event('change', file=BlobMedia(content_type=files[0].type, content=as_bytes))
    file_reader.onload = onload
    file_reader.readAsArrayBuffer(files[0])
    
  text = innerText_property('anvil-m3-fileloader-label')
  visible = HtmlTemplate.visible
  enabled = enabled_property('anvil-m3-fileloader-input')
  text_color = color_property('anvil-m3-fileloader-label', 'color')
  icon_color = color_property('anvil-m3-fileloader-icon', 'color')
  background_color = color_property('anvil-m3-fileloader-form', 'backgroundColor')
  underline = underline_property('anvil-m3-fileloader-label')
  italic = italic_property('anvil-m3-fileloader-label')
  bold = bold_property('anvil-m3-fileloader-label')
  font = style_property('anvil-m3-fileloader-label', 'fontFamily')
  icon_size = font_size_property('anvil-m3-fileloader-icon', 'icon_size')
  font_size = font_size_property('anvil-m3-fileloader-label', 'font_size')
  align = style_property('anvil-m3-fileloader-form', 'justifyContent')

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

  @property
  def file_types(self):
    return self._props.get("file_types")

  @file_types.setter
  def file_types(self, value):
    self._props["file_types"] = value
    self.dom_nodes['anvil-m3-fileloader-input'].accept = value

  



