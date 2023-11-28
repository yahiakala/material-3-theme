from ._anvil_designer import FileLoaderTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...Functions import underline_property, italic_property, style_property, color_property, innerText_property, bold_property, font_size_property, enabled_property, font_family_property
from anvil.js.window import FileReader, Uint8Array
from ...utils import gen_id

#Currently can only accept one file at a time 

class FileLoader(FileLoaderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self._props = properties
    self.init_components(**properties)

    self._handle_change = self._handle_change
    self._handle_focus = self._handle_focus
    self._handle_lost_focus = self._handle_lost_focus

    self.add_event_handler("x-anvil-page-added", self._on_mount)
    self.add_event_handler("x-anvil-page-removed", self._on_cleanup)
    
    if not anvil.designer.in_designer:
      id = gen_id()
      self.dom_nodes["anvil-m3-fileloader-input"].id = id
      self.dom_nodes["anvil-m3-fileloader-label"].setAttribute("for", id)

  def clear(self):
    self.dom_nodes['anvil-m3-fileloader-input'].value = ""
    print('cleared')
    print(self.text)
    self.dom_nodes['anvil-m3-fileloader-label'].innerText = self.text
    #update show_state text if present

  def focus(self):
    self.dom_nodes['anvil-m3-fileloader-container'].focus()

  def _on_mount(self, **event_args):
    self.dom_nodes['anvil-m3-fileloader-input'].addEventListener("change", self._handle_change)
    self.dom_nodes['anvil-m3-fileloader-container'].addEventListener("focus", self._handle_focus)
    self.dom_nodes['anvil-m3-fileloader-container'].addEventListener("blur", self._handle_lost_focus)
    
  def _on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-fileloader-input'].removeEventListener("change", self._handle_change)
    self.dom_nodes['anvil-m3-fileloader-container'].removeEventListener("focus", self._handle_focus)
    self.dom_nodes['anvil-m3-fileloader-container'].removeEventListener("blur", self._handle_lost_focus)

  def _handle_change(self, event, **event_args):
    files = self.dom_nodes['anvil-m3-fileloader-input'].files
    as_anvil_media
    # file_reader = FileReader()
    # def onload(e):
    #   as_buffer = file_reader.result
    #   as_bytes = Uint8Array(as_buffer)
    #   self.raise_event('change', file=BlobMedia(content_type=files[0].type, content=as_bytes))
    # file_reader.onload = onload
    # file_reader.readAsArrayBuffer(files[0])
    if self.show_state:
      num_files = len(files)
      self.dom_nodes['anvil-m3-fileloader-label'].innerText = "1 file selected" if num_files == 1 else f"{num_files} files selected"

  def _handle_focus(self, event, **event_args):
    self.raise_event("focus")

  def _handle_lost_focus(self, event, **event_args):
    self.raise_event("lost_focus")
    
  text = innerText_property('anvil-m3-fileloader-label')
  visible = HtmlTemplate.visible
  enabled = enabled_property('anvil-m3-fileloader-input')
  text_color = color_property('anvil-m3-fileloader-label', 'color', 'text_color')
  icon_color = color_property('anvil-m3-fileloader-icon', 'color', 'icon_color')
  background_color = color_property('anvil-m3-fileloader-form', 'backgroundColor', 'background_color')
  underline = underline_property('anvil-m3-fileloader-label')
  italic = italic_property('anvil-m3-fileloader-label')
  bold = bold_property('anvil-m3-fileloader-label')
  font = font_family_property('anvil-m3-fileloader-label', 'font')
  icon_size = font_size_property('anvil-m3-fileloader-icon', 'icon_size')
  font_size = font_size_property('anvil-m3-fileloader-label', 'font_size')
  align = style_property('anvil-m3-fileloader-form', 'justifyContent', 'align')
  border = style_property('anvil-m3-fileloader-container', 'border', 'border')

  @property
  def show_state(self):
    return self._props.get('show_state')

  @show_state.setter
  def show_state(self, value):
    self._props['show_state'] = value

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

  



