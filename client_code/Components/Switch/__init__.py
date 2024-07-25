from ._anvil_designer import SwitchTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js.window import document, getComputedStyle
from anvil.js import window
from anvil import HtmlTemplate
from ...Functions import theme_color_to_css, role_property, tooltip_property, enabled_property, style_property, color_property, theme_color_to_css, property_with_callback, margin_property
import anvil.designer


class Switch(SwitchTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self._tooltip_node = None
    self._props = properties
    self.init_components(**properties)
    self.add_event_handler("x-anvil-page-added", self._on_mount)
    self.add_event_handler("x-anvil-page-removed", self._on_cleanup)
    
  def _on_mount(self, **event_args):
    self.dom_nodes['anvil-m3-switch-input'].addEventListener("change", self._handle_change)
    
  def _on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-switch-input'].removeEventListener("change", self._handle_change)

  def _handle_change(self, event):
    if self.enabled:
      #self.dom_nodes['anvil-m3-switch-input'].focus()
      self.selected = not self.selected
      self.raise_event("change")

  def _set_color_styles(self, value=None):
    if self.selected:
      self.dom_nodes['anvil-m3-switch-slider'].style.backgroundColor = theme_color_to_css(self.selected_background_color) if self.selected_background_color else None
      if self.selected_thumb_color:
        self.dom_nodes['anvil-m3-switch-slider'].style.setProperty('--anvil-m3-selected-thumb-color', theme_color_to_css(self.selected_thumb_color))
      else:
        self.dom_nodes['anvil-m3-switch-slider'].style.setProperty('--anvil-m3-selected-thumb-color', 'var(--anvil-m3-on-primary)')
    else:
      self.dom_nodes['anvil-m3-switch-slider'].style.backgroundColor = theme_color_to_css(self.unselected_background_color) if self.unselected_background_color else None
      self.dom_nodes['anvil-m3-switch-slider'].style.borderColor = theme_color_to_css(self.unselected_outline_color) if self.unselected_outline_color else None
      if self.unselected_thumb_color:
        self.dom_nodes['anvil-m3-switch-slider'].style.setProperty('--anvil-m3-unselected-thumb-color', theme_color_to_css(self.unselected_thumb_color))
      else:
        self.dom_nodes['anvil-m3-switch-slider'].style.setProperty('--anvil-m3-unselected-thumb-color', 'var(--anvil-m3-outline)')

  #!componentEvent(material_3.Switch)!1: {name: "change", description: "When the state of the Switch is changed.", parameters:[{name: "file", description: "The first selected file. Set the 'multiple' property to allow loading more than one file."},{name: "files", description: "A list of loaded files. Set the 'multiple' property to allow loading more than one file."}]}
  #!componentEvent(material_3.Switch)!1: {name: "show", description: "When the Switch is shown on the screen."}
  #!componentEvent(material_3.Switch)!1: {name: "hide", description: "When the Switch is removed from the screen."}
  #!componentProp(material_3.Switch)!1: {name:"enabled",type:"boolean",description:"If True, this component allows user interaction."}
  #!componentProp(material_3.Switch)!1: {name:"align",type:"enum", options:["left", "center", "right"],description:"The position of this component in the available space."} 
  #!componentProp(material_3.Switch)!1: {name:"visible",type:"boolean",description:"If True, the component will be displayed."} 
  #!componentProp(material_3.Switch)!1: {name:"margin",type:"margin",description:"The margin (pixels) of the component."}
  #!componentProp(material_3.Switch)!1: {name:"tooltip",type:"string",description:"The text to display when the mouse is hovered over this component."}
  #!componentProp(material_3.Switch)!1: {name:"role",type:"themeRole",description:"A style for this component defined in CSS and added to Roles."} 
  #!componentProp(material_3.Switch)!1: {name:"selected_background_color",type:"color",description:"The color of the background of this component."}
  
  #!componentProp(material_3.Switch)!1: {name:"text",type:"string",description:"The text displayed on this component"}
  #!componentProp(material_3.Switch)!1: {name:"text_color",type:"color",description:"The color of the text on the component."} 
  #!componentProp(material_3.Switch)!1: {name:"icon_color",type:"color",description:"The color of the icon displayed on this component."}
  #!componentProp(material_3.Switch)!1: {name:"underline",type:"boolean",description:"If True, this component’s text will be underlined."}
  #!componentProp(material_3.Switch)!1: {name:"italic",type:"boolean",description:"If True, this component’s text will be italic."}
  #!componentProp(material_3.Switch)!1: {name:"bold",type:"boolean",description:"If True, this component’s text will be bold."}
  #!componentProp(material_3.Switch)!1: {name:"font_family",type:"string",description:"The font family to use for this component."}
  #!componentProp(material_3.Switch)!1: {name:"icon_size",type:"number",description:"The size (pixels) of the icon displayed on this component."}
  #!componentProp(material_3.Switch)!1: {name:"font_size",type:"number",description:"The font size of text displayed on this component."}
  #!componentProp(material_3.Switch)!1: {name:"border",type:"string",description:"The border of this component. Can take any valid CSS border value."}
  #!componentProp(material_3.Switch)!1: {name:"appearance",type:"enum",options:["filled", "elevated", "tonal", "outlined", "text"],description:"A predefined style for this component."}
  #!componentProp(material_3.Switch)!1: {name:"show_state",type:"boolean",description:"If True, display a message describing selected files."}
  #!componentProp(material_3.Switch)!1: {name:"material_icon",type:"enum",description:"The icon to display on this component."} 
  #!componentProp(material_3.Switch)!1: {name:"file_types",type:"string",description:"Specify what type of file to upload. Can accept a MIME type (eg 'image/png' or 'image/*'), an extension (eg '.png'), or a comma-separated set of them (eg '.png,.jpg,.jpeg')."} 
  #!componentProp(material_3.Switch)!1: {name:"multiple",type:"boolean",description:"If True, this Switch can load multiple files at the same time."} 
  #!componentProp(material_3.Switch)!1: {name:"file",type:"object",description:"The currently selected file (or the first, if multiple files are selected). This is a Media object."} 

  enabled = enabled_property('anvil-m3-switch-input')
  align = style_property('anvil-m3-switch-container', 'justifyContent', 'align')
  visible = HtmlTemplate.visible
  margin = margin_property('anvil-m3-switch-container')
  tooltip = tooltip_property('anvil-m3-switch')
  role = role_property('anvil-m3-switch')
  selected_background_color = property_with_callback('selected_background_color', _set_color_styles)
  unselected_background_color = property_with_callback('unselected_background_color', _set_color_styles)
  selected_thumb_color = property_with_callback('selected_thumb_color', _set_color_styles)
  unselected_thumb_color = property_with_callback('unselected_thumb_color', _set_color_styles)
  unselected_outline_color = property_with_callback('unselected_outline_color', _set_color_styles)

  @property
  def selected_icon(self):
    return self._selected_icon

  @selected_icon.setter
  def selected_icon(self, value):
    link_icon = self.dom_nodes['anvil-m3-enabled-switch-icon']
    switch_slider = self.dom_nodes['anvil-m3-switch-slider']
    self._selected_icon = value
    link_icon.classList.remove("material-symbols-outlined")
    if value:
      link_icon.classList.add("material-symbols-outlined")
      link_icon.innerText = value
      switch_slider.classList.add('anvil-m3-has-enabled-icon')
  
  @property
  def unselected_icon(self):
    return self._unselected_icon

  @unselected_icon.setter
  def unselected_icon(self, value):
    link_icon = self.dom_nodes['anvil-m3-disabled-switch-icon']
    switch_slider = self.dom_nodes['anvil-m3-switch-slider']
    self._unselected_icon = value
    
    link_icon.classList.remove("material-symbols-outlined")
    if value:
      link_icon.classList.add("material-symbols-outlined")
      link_icon.innerText = value
      switch_slider.classList.add('anvil-m3-has-disabled-icon')

  @property
  def selected(self):
    return self._props.get('selected')
    # return self.dom_nodes['anvil-m3-switch-input'].checked

  @selected.setter
  def selected(self, value):
    self._props['selected'] = value
    self.dom_nodes['anvil-m3-switch-input'].checked = value
    self._set_color_styles()

#!defClass(material_3, Switch, anvil.Component)!: