from ._anvil_designer import TextInputTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...Functions import property_without_callback, property_with_callback, italic_property, bold_property, underline_property, font_size_property, font_family_property, color_property, spacing_property
from anvil import HtmlTemplate
from ...utils import gen_id

class TextInput(TextInputTemplate):
  def __init__(self, **properties):
    self._props = properties
    self.init_components(**properties)
    
    self.on_input = self.on_input
    
  visible = HtmlTemplate.visible
  italic_label = italic_property('label-text', 'italic_label')
  bold_label = bold_property('label-text', 'bold_label')
  underline_label = underline_property('label-text', 'underline_label')
  label_font_size = font_size_property('label-text', 'label_font_size')
  label_font = font_family_property('label-text', 'label_font')
  label_text_color = color_property('label-text', 'color', 'label_text_color')
  spacing = spacing_property('textinput-component')
  
  def set_appearance(self, value):
    if value == 'outlined':
      self.dom_nodes['textinput-component'].classList.toggle('outlined', True) 
    else:
      self.dom_nodes['textinput-component'].classList.toggle('outlined', False)
  appearance = property_with_callback("appearance", set_appearance)
  
  def set_supporting_text(self, value):
    self.dom_nodes['supporting-text'].innerHTML = value
  supporting_text = property_with_callback("supporting_text", set_supporting_text)

  def set_error(self, value):
    classes = self.dom_nodes['textinput-component'].classList
    if value:
      classes.add("anvil-m3-textinput-error")
    else:
      classes.remove("anvil-m3-textinput-error")
  error = property_with_callback("error", set_error)
  
  def set_id(self, value):
    self.dom_nodes["label-text"].setAttribute("for", value)
    self.dom_nodes["supporting-text"].setAttribute("for", value)
    self.dom_nodes["character-amount"].setAttribute("for", value)
  
  def form_show(self, **event_args):
    id = gen_id();
    self.set_id(id)
    
    if anvil.designer.in_designer:
      if not self.label_text:
        self.dom_nodes['label-text'].innerText = anvil.designer.get_design_name(self)

  def on_input(self, e):
    self.dom_nodes['character-amount'].innerText = len(e.target.value);

  def on_change(self, e):
    self.raise_event("change")

  def on_focus(self, e):
    self.raise_event("focus")

  def on_lost_focus(self, e):
    self.raise_event("lost_focus")

  def _anvil_get_interactions_(self):
    return [{
      "type": "whole_component",
      "title": "Edit text",
      "icon": "edit",
      "default": True,
      "callbacks": {
        "execute": lambda: anvil.designer.start_inline_editing(self, "label_text", self.dom_nodes['label-text'])
      }
    }]