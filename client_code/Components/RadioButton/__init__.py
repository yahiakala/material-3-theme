from ._anvil_designer import RadioButtonTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import HtmlTemplate
from anvil.js.window import document
import anvil.designer
from ...Functions import checked_property, name_property, innerText_property, enabled_property, style_property, underline_property, italic_property, border_property, bold_property, font_size_property, color_property, theme_color_to_css, value_property, property_with_callback, font_family_property
from ...utils import gen_id

class RadioButton(RadioButtonTemplate):
  def __init__(self, **properties):
    self._props = properties
    self._design_name = "" 
    self.init_components(**properties)
    
    self.handle_click = self.handle_click
    self.add_event_handler("x-anvil-page-added", self.on_mount)
    self.add_event_handler("x-anvil-page-removed", self.on_cleanup)
    if not anvil.designer.in_designer:
        id = gen_id()
        self.dom_nodes["anvil-m3-radiobutton-input"].id = id
        self.dom_nodes["anvil-m3-radiobutton-label"].setAttribute("for", id)

  def on_mount(self, **event_args):
    self.dom_nodes['anvil-m3-radiobutton-hover'].addEventListener("click", self.handle_click)
  def on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-radiobutton-hover'].removeEventListener("click", self.handle_click)
    
  # Properties 
  visible = HtmlTemplate.visible
  group_name = name_property('anvil-m3-radiobutton-input', "group_name")
  value = value_property('anvil-m3-radiobutton-input')
  enabled = enabled_property('anvil-m3-radiobutton-input')
  italic = italic_property('anvil-m3-radiobutton-label')
  bold = bold_property('anvil-m3-radiobutton-label')
  underline = underline_property('anvil-m3-radiobutton-label')
  font_size = font_size_property('anvil-m3-radiobutton-label')
  border = border_property('anvil-m3-radiobutton-container')
  font = font_family_property('anvil-m3-radiobutton-label', 'font')
  text_color = color_property('anvil-m3-radiobutton-label', 'color')
  background = color_property('anvil-m3-radiobutton-container', 'backgroundColor')
  align = style_property('anvil-m3-radiobutton-component', 'justifyContent', 'align')
  selected = checked_property('anvil-m3-radiobutton-input')

  def set_text(self, value):
    v = value
    self.dom_nodes['anvil-m3-radiobutton-label'].classList.toggle('anvil-m3-textlessComponentText', False)
    if anvil.designer.in_designer and not value:
      v = self._design_name
      self.dom_nodes['anvil-m3-radiobutton-label'].classList.toggle('anvil-m3-textlessComponentText', True)
    self.dom_nodes['anvil-m3-radiobutton-label'].innerText = v
  text = property_with_callback("text", set_text)
  
  # Class Functions
  def _anvil_get_interactions_(self):
    return [
      {
        "type": "whole_component",
        "title": "Edit text",
        "icon": "edit",
        "default": True,
        "callbacks": {
          "execute": lambda: anvil.designer.start_inline_editing(self, "text", self.dom_nodes['anvil-m3-radiobutton-label'])
        },   
      },
      {
        "type": "region",
        "bounds": self.dom_nodes['anvil-m3-radiobutton-hover'],
        "sensitivity": 0,
        "callbacks": {
          "execute": self.toggle_selected
        }
      }
    ]

  def toggle_selected(self):
    self.selected = not self.selected
    anvil.designer.update_component_properties(self, {'selected': self.selected})
   
  def handle_click(self, event):
    if self.enabled:
      self.dom_nodes['anvil-m3-radiobutton-input'].focus()
      self.selected = True
      self.raise_event("clicked")
    
  def form_show(self, **event_args):
    if anvil.designer.in_designer:
      self._design_name = anvil.designer.get_design_name(self)
      if not self.text:
        self.dom_nodes['anvil-m3-radiobutton-label'].innerText = self._design_name

  def get_group_value(self):
    selectedItem = document.querySelector(f".anvil-m3-radiobutton-input[name={self.group_name}]:checked")
    return selectedItem.value
