from ._anvil_designer import ButtonTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.js
from ...Functions import color_property, role_property, tooltip_property, custom_bold_property, font_family_property, font_size_property, style_property, property_with_callback, underline_property, bold_property, italic_property, margin_property 
from anvil import HtmlTemplate
import anvil.designer

class Button(ButtonTemplate):
  def __init__(self, **properties):
    self._props = properties
    self._text = properties.get('text', '')
    self._tooltip_node = None
    self.init_components(**properties)
    
    self._handle_click = self._handle_click
    self.add_event_handler("x-anvil-page-added", self._on_mount)
    self.add_event_handler("x-anvil-page-removed", self._on_cleanup)

  def _on_mount(self, **event_args):
    self.dom_nodes['anvil-m3-button'].addEventListener("click", self._handle_click)
  def _on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-button'].removeEventListener("click", self._handle_click)

  def _set_align(self, value):
    self.dom_nodes['anvil-m3-button'].classList.toggle('full-width', False)
    if value == 'full':
      self.dom_nodes['anvil-m3-button'].classList.toggle('full-width', True)
    else:
      self.dom_nodes['anvil-m3-button-component'].style.justifyContent = value

  #!defAttr()!1: {name:"align",type:"enum",description:"The position of this component in the available space."} 
  align = property_with_callback('align', _set_align)
  #!defAttr()!1: {name:"visible",type:"boolean",description:"If False, the component will not be displayed."} 
  visible = HtmlTemplate.visible
  #!defAttr()!1: {name:"visible",type:"themeRole",description:"If False, the component will not be displayed."} 
  role = role_property('anvil-m3-button')

  def _handle_click(self, event):
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

    
  
  def _set_icon(self):
    if self.icon:
      self.dom_nodes['anvil-m3-button-icon'].innerText = self.icon
      self.dom_nodes['anvil-m3-button-icon'].style.display = "flex"
      if self.text:
        self.dom_nodes['anvil-m3-button'].classList.add('anvil-m3-icon-padding')
      else:
        self.dom_nodes['anvil-m3-button'].classList.add('noText')
    else:
      self.dom_nodes['anvil-m3-button-icon'].innerText = ""
      self.dom_nodes['anvil-m3-button-icon'].style.display = "none"

  def _set_text(self):
    if self.text:
      self.dom_nodes['anvil-m3-button-text'].innerText = self.text
    else:
      if not self.icon:
        if anvil.designer.in_designer:
          self.dom_nodes['anvil-m3-button-text'].innerText = anvil.designer.get_design_name(self)
          self.dom_nodes['anvil-m3-button-text'].classList.add('anvil-m3-textlessComponentText')
        else: 
          self.dom_nodes['anvil-m3-button-text'].innerText = "Button"
      else:
        self.dom_nodes['anvil-m3-button-text'].innerText = ""
      
  def _update_button_look(self, value = None):
    buttonNode = self.dom_nodes['anvil-m3-button']
    iconNode = self.dom_nodes['anvil-m3-button-icon']
    textNode = self.dom_nodes['anvil-m3-button-text']

    buttonNode.classList.remove('anvil-m3-icon-padding')
    textNode.classList.remove('anvil-m3-textlessComponentText')
    buttonNode.classList.remove('noText')
    
    self._set_icon()
    self._set_text()

  #!defAttr()!1: {name:"icon",type:"enum",description:"The icon to display on this component."} 
  icon = property_with_callback("icon", _update_button_look)
  #!defAttr()!1: {name:"text",type:"string",description:"Text displayed on this component"}
  text = property_with_callback("text", _update_button_look)

  def _set_enabled(self, value):
    if value:
      self.dom_nodes['anvil-m3-button'].removeAttribute("disabled")
    else:
      self.dom_nodes['anvil-m3-button'].setAttribute("disabled", " ")
      
  #!defAttr()!1: {name:"enabled",type:"boolean",description:"If True, this component allows user interaction."}
  enabled = property_with_callback("enabled", _set_enabled)

  def _set_appearance(self, value):
    button = self.dom_nodes['anvil-m3-button']
    button.classList.remove('anvil-m3-elevated')
    button.classList.remove('anvil-m3-filled')
    button.classList.remove('anvil-m3-tonal')
    button.classList.remove('anvil-m3-outlined')
    if value:
      button.classList.add(f"anvil-m3-{value}")
      
  #!defAttr()!1: {name:"appearance",type:"enum",description:"A predefined style for this component."}    
  appearance = property_with_callback("appearance", _set_appearance)

  def form_show(self, **event_args):
    self._update_button_look()

  #!defAttr()!1: {name:"text_color",type:"color",description:"The color of the text on the component."} 
  text_color = color_property('anvil-m3-button-text', 'color', 'text_color')
  #!defAttr()!1: {name:"font_family",type:"string",description:"The font family to use for this component."}
  font_family = font_family_property('anvil-m3-button-text')
  #!defAttr()!1: {name:"font_size",type:"number",description:"The font size of text displayed on this component."}
  font_size = font_size_property('anvil-m3-button-text')
  #!defAttr()!1: {name:"underline",type:"boolean",description:"If True, this component’s text will be underlined."}
  underline = underline_property('anvil-m3-button-text')
  #!defAttr()!1: {name:"italic",type:"boolean",description:"If True, this component’s text will be italic."}
  italic = italic_property('anvil-m3-button-text')
  #!defAttr()!1: {name:"bold",type:"boolean",description:"If True, this component’s text will be bold."}
  bold = custom_bold_property('anvil-m3-button-text')
  #!defAttr()!1: {name:"icon_color",type:"color",description:"The color of the icon displayed on this component."}
  icon_color = color_property('anvil-m3-button-icon', 'color', 'icon_color')
  #!defAttr()!1: {name:"icon_size",type:"number",description:"Size (pixels) of the icon displayed on this component."}
  icon_size = font_size_property('anvil-m3-button-icon', 'icon_size')
  #!defAttr()!1: {name:"background",type:"color",description:"The color of the background of this component."}
  background = color_property('anvil-m3-button', 'backgroundColor', 'background')
  #!defAttr()!1: {name:"margin",type:"margin",description:"The margin (pixels) of the component."}
  margin = margin_property('anvil-m3-button-component')
  #!defAttr()!1: {name:"border",type:"string",description:"The border of this component. Can take any valid CSS border value."}
  border = style_property('anvil-m3-button', 'border', 'border')
  #!defAttr()!1: {name:"tooltip",type:"string",description:"Text to display when the mouse is hovered over this component."}
  tooltip = tooltip_property('anvil-m3-button')

  def _set_icon_align(self, value):
    self.dom_nodes['anvil-m3-button'].classList.toggle('anvil-m3-right-icon', value == 'right')
  
  #!defAttr()!1: {name:"icon_align",type:"enum",description:"The alignment of the icon on this component."}
  icon_align = property_with_callback('icon_align', _set_icon_align)

#!defClass(material_3,Button)!:



  
