from ._anvil_designer import ButtonTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.js
from ...Functions import color_property, custom_bold_property, font_family_property, font_size_property, style_property, property_with_callback, underline_property, bold_property, italic_property
from anvil import HtmlTemplate
import anvil.designer

class Button(ButtonTemplate):
  def __init__(self, **properties):
    self._props = properties
    self._text = properties.get('text', '')
    self.init_components(**properties)
    self.dom_nodes['anvil-m3-button'].addEventListener("click", self.handle_click)
    self.handle_click = self.handle_click
    self.add_event_handler("x-anvil-page-added", self.on_mount)
    self.add_event_handler("x-anvil-page-removed", self.on_cleanup)

  def on_mount(self, **event_args):
    self.dom_nodes['anvil-m3-button'].addEventListener("click", self.handle_click)
  def on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-button'].removeEventListener("click", self.handle_click)

  def set_align(self, value):
    self.dom_nodes['anvil-m3-button'].classList.toggle('full-width', False)
    if value is 'full':
      self.dom_nodes['anvil-m3-button'].classList.toggle('full-width', True)
    else:
      self.dom_nodes['anvil-m3-button-component'].style.justifyContent = value
  align = property_with_callback('align', set_align)
  visible = HtmlTemplate.visible
  
  def handle_click(self, event):
    event.preventDefault()
    if self.enabled:
      self.raise_event("click")

  def _anvil_get_interactions_(self):
    return [{
      "type": "whole_component",
      "title": "Edit text",
      "icon": "edit",
      "default": True,
      "callbacks": {
        "execute": lambda: anvil.designer.start_inline_editing(self, "text", self.dom_nodes['anvil-m3-button-text'])
      }
    }]

  def set_icon(self):
    if self.material_icon:
      self.dom_nodes['anvil-m3-button-icon'].innerText = self.material_icon
      self.dom_nodes['anvil-m3-button-icon'].style.display = "flex"
      if self.text or anvil.designer.in_designer:
        self.dom_nodes['anvil-m3-button'].classList.remove('anvil-m3-icon-padding')
    else:
      self.dom_nodes['anvil-m3-button-icon'].innerText = ""
      self.dom_nodes['anvil-m3-button-icon'].style.display = "none"

  def set_text(self):
    if self.text:
      self.dom_nodes['anvil-m3-button-text'].innerText = self.text
    else:
      if not self.material_icon:
        if anvil.designer.in_designer:
          self.dom_nodes['anvil-m3-button-text'].innerText = anvil.designer.get_design_name(self)
        else: 
          self.dom_nodes['anvil-m3-button-text'].innerText = "Button"
      
  def update_button_look(self, value = None):
    buttonNode = self.dom_nodes['anvil-m3-button']
    iconNode = self.dom_nodes['anvil-m3-button-icon']
    textNode = self.dom_nodes['anvil-m3-button-text']
    #  reset all styles to nothing
    buttonNode.classList.remove('anvil-m3-icon-padding')
    
    self.set_icon()
    self.set_text()
    # set appropriate styles
    
    
    '''
    has text, has image, in designer
      set padding
    no text, has image, in designer
      no padding
    has text, no image, in designer
      no padding
    no text, no image, in designer
      no padding
    has text, has image, not in designer
      set padding
    no text, has image, not in designer
      no padding
    has text, no image, not in designer
      no padding
    no text, no image, not in designer
      no padding
    '''
    
    # pass

  # def set_icon(self, value):
    # self.update_button_look()
    # button = self.dom_nodes['anvil-m3-button']
    # button_icon = self.dom_nodes['anvil-m3-button-icon']
    # if value:
    #   button_icon.innerText = value
    #   button_icon.style.display = "block"
    #   if self.text:
    #     button.classList.add('anvil-m3-icon-padding')
        
    #   # button.classList.add('anvil-m3-icon-padding')
    #   # if not anvil.designer.in_designer:
    #   #   self.dom_nodes['anvil-m3-button-icon'].style.paddingRight: '0px'
    #   # if not self.text:
    #   #   button.classList.remove('anvil-m3-icon-padding')
    #   #   if anvil.designer.in_designer:
    #   #     self.dom_nodes['anvil-m3-button-text'].innerHTML = ""
          
    #       # self.dom_nodes['anvil-m3-button-text'].classList.toggle('anvil-m3-textlessComponentText', not bool(value))
    # else: 
    #   if not self.text:
    #     if anvil.designer.in_designer:
    #       self.dom_nodes['anvil-m3-button-text'].innerHTML = anvil.designer.get_design_name(self)
    #       self.dom_nodes['anvil-m3-button-text'].classList.toggle('anvil-m3-textlessComponentText', not bool(value))
    #   button_icon.innerText = ""
    #   button_icon.style.display = "none"
    #   button.classList.remove('anvil-m3-icon-padding')
  material_icon = property_with_callback("material_icon", update_button_look)
  
  # def set_text(self, value):
  #   self.update_button_look()
    # self.dom_nodes['anvil-m3-button-text'].classList.toggle('anvil-m3-textlessComponentText', False)
    # if value:
    #   self.dom_nodes['anvil-m3-button-text'].innerHTML = value
    #   self.dom_nodes['anvil-m3-button'].classList.toggle('noText', not bool(value))
    # else:
    #   if not self.material_icon and anvil.designer.in_designer:
    #     self.dom_nodes['anvil-m3-button-text'].innerHTML = anvil.designer.get_design_name(self)
    #     self.dom_nodes['anvil-m3-button-text'].classList.toggle('anvil-m3-textlessComponentText', not bool(value))
  text = property_with_callback("text", update_button_look)

  def set_enabled(self, value):
    if value:
      self.dom_nodes['anvil-m3-button'].removeAttribute("disabled")
    else:
      self.dom_nodes['anvil-m3-button'].setAttribute("disabled", " ")
  enabled = property_with_callback("enabled", set_enabled)

  def set_appearance(self, value):
    button = self.dom_nodes['anvil-m3-button']
    button.classList.remove('anvil-m3-elevated')
    button.classList.remove('anvil-m3-filled')
    button.classList.remove('anvil-m3-tonal')
    button.classList.remove('anvil-m3-outlined')
    if value:
      button.classList.add(f"anvil-m3-{value}")
  appearance = property_with_callback("appearance", set_appearance)

  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    # if not (self.text or self.material_icon):
    #   if anvil.designer.in_designer:
    #     # self.text = anvil.designer.get_design_name(self)
    #     self.dom_nodes['anvil-m3-button-text'].innerHTML = anvil.designer.get_design_name(self)
    #     self.dom_nodes['anvil-m3-button-text'].classList.toggle('anvil-m3-textlessComponentText', True)
    #   else:
    #     self.text = "Button"
    self.update_button_look()
    # pass
    
  text_color = color_property('anvil-m3-button-text', 'color', 'text_color')
  font_family = font_family_property('anvil-m3-button-text')
  font_size = font_size_property('anvil-m3-button-text')
  underline = underline_property('anvil-m3-button-text')
  italic = italic_property('anvil-m3-button-text')
  bold = custom_bold_property('anvil-m3-button-text')
  icon_color = color_property('anvil-m3-button-icon', 'color', 'icon_color')
  icon_size = font_size_property('anvil-m3-button-icon', 'icon_size')
  background = color_property('anvil-m3-button', 'backgroundColor', 'background')

  def set_icon_align(self, value):
    self.dom_nodes['anvil-m3-button'].classList.toggle('anvil-m3-right-icon', value is 'right')
  icon_align = property_with_callback('icon_align', set_icon_align)



  
