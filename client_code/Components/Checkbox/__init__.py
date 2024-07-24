from ._anvil_designer import CheckboxTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import HtmlTemplate
from ...Functions import enabled_property, role_property, tooltip_property, style_property, underline_property, italic_property, bold_property, font_size_property, color_property, theme_color_to_css, innerText_property, margin_property, font_family_property, border_property
from ...utils import gen_id
import anvil.designer

class Checkbox(CheckboxTemplate):
  def __init__(self, **properties):
    self._props = properties
    self._tooltip_node = None
    self._allow_indeterminate = properties['allow_indeterminate']
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.add_event_handler("x-anvil-page-added", self._on_mount)
    self.add_event_handler("x-anvil-page-removed", self._on_cleanup)
    if not anvil.designer.in_designer:
      id = gen_id()
      self.dom_nodes["anvil-m3-checkbox"].id = id
      self.dom_nodes["anvil-m3-checkbox-label"].setAttribute("for", id)

  def _on_mount(self, **event_args):
    self.dom_nodes['anvil-m3-checkbox-hover'].addEventListener("click", self._handle_change)

  def _on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-checkbox-hover'].removeEventListener('click', self._handle_change)

  def focus(self):
    self.dom_nodes['anvil-m3-checkbox'].focus()

  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    if anvil.designer.in_designer and not self.text:
      self.text = anvil.designer.get_design_name(self)

  def _anvil_get_interactions_(self):
    return [
      {
        "type": "whole_component",
        "title": "Edit",
        "icon": "edit",
        "default": True,
        "callbacks": {
          "execute":  lambda: anvil.designer.start_inline_editing(self, "text", self.dom_nodes['anvil-m3-checkbox-label'])
        }
      },
      {
        "type": "region",
        "bounds": self.dom_nodes['anvil-m3-checkbox-hover'],
        "sensitivity": 0,
        "callbacks": {
          "execute": self._toggle_checked
        }
      }
    ]

  def _toggle_checked(self):
    self.checked = not self.checked
    anvil.designer.update_component_properties(self, {'checked': self.checked})

  def _handle_change(self, event):
    if self.enabled:
      self.dom_nodes['anvil-m3-checkbox'].focus()
      self.checked = not self.checked
      self.raise_event("change")

  #!defAttr()!1: {name:"enabled",type:"boolean",description:"If True, this component allows user interaction."}
  #!defAttr()!1: {name:"visible",type:"boolean",description:"If True, the component will be displayed."} 
  #!defAttr()!1: {name:"underline",type:"boolean",description:"If True, this component’s text will be underlined."}
  #!defAttr()!1: {name:"italic",type:"boolean",description:"If True, this component’s text will be italic."}
  #!defAttr()!1: {name:"bold",type:"boolean",description:"If True, this component’s text will be bold."}
  #!defAttr()!1: {name:"role",type:"themeRole",description:"A style for this component defined in CSS and added to Roles"} 
  #!defAttr()!1: {name:"text_color",type:"color",description:"The color of the text on the component."} 
  #!defAttr()!1: {name:"font_family",type:"string",description:"The font family to use for this component."}
  #!defAttr()!1: {name:"text",type:"string",description:"The text displayed on this component"}
  #!defAttr()!1: {name:"font_size",type:"number",description:"The font size of text displayed on this component."}
  #!defAttr()!1: {name:"background",type:"color",description:"The color of the background of this component."}
  #!defAttr()!1: {name:"align",type:"enum",description:"The position of this component in the available space."} 
  #!defAttr()!1: {name:"margin",type:"margin",description:"The margin (pixels) of the component."}
  #!defAttr()!1: {name:"border",type:"string",description:"The border of this component. Can take any valid CSS border value."}
  #!defAttr()!1: {name:"tooltip",type:"string",description:"The text to display when the mouse is hovered over this component."}
  
  enabled = enabled_property('anvil-m3-checkbox')
  visible = HtmlTemplate.visible
  underline = underline_property('anvil-m3-checkbox-label')
  italic = italic_property('anvil-m3-checkbox-label')
  bold = bold_property('anvil-m3-checkbox-label')
  font_size = font_size_property('anvil-m3-checkbox-label')
  border = border_property('anvil-m3-checkbox-container')
  font = font_family_property('anvil-m3-checkbox-label', 'font')
  text_color = color_property('anvil-m3-checkbox-label', 'color', 'text_color')
  background = color_property('anvil-m3-checkbox-component', 'backgroundColor', 'background')
  align = style_property('anvil-m3-checkbox-component', 'justifyContent', 'align')
  margin = margin_property('anvil-m3-checkbox-component')
  tooltip = tooltip_property('anvil-m3-checkbox-container')
  role = role_property('anvil-m3-checkbox-container')

  @property
  def text(self):
    return self._props.get('text')

  @text.setter
  def text(self, value):
    self._props['text'] = value
    if value:
      self.dom_nodes['anvil-m3-checkbox-label'].innerText = value
      self.dom_nodes['anvil-m3-checkbox-label'].style.display = 'block'
    else:
      self.dom_nodes['anvil-m3-checkbox-label'].style.display = 'none'

  @property
  def checkbox_color(self):
    return self._props.get('checkbox_color')

  @checkbox_color.setter
  def checkbox_color(self, value):
    self._props['checkbox_color'] = value
    if value:
      value = theme_color_to_css(value)
      self.dom_nodes['anvil-m3-checkbox-unchecked'].style.color = value
      self.dom_nodes['anvil-m3-checkbox-checked'].style.color = value
      self.dom_nodes['anvil-m3-checkbox-indeterminate'].style.color = value

  @property
  def checked(self):
    return self._props.get('checked')

  @checked.setter
  def checked(self, value):
    self._props['checked'] = value
    if value == None and self.allow_indeterminate:
      self.dom_nodes['anvil-m3-checkbox'].indeterminate = True
      self.dom_nodes['anvil-m3-checkbox-unchecked'].style.display = 'none'
      self.dom_nodes['anvil-m3-checkbox-checked'].style.display = 'none'
      self.dom_nodes['anvil-m3-checkbox-indeterminate'].style.display = 'inline'
    else:
      self.dom_nodes['anvil-m3-checkbox'].checked = value

  @property
  def allow_indeterminate(self):
    return self._props.get('allow_indeterminate')

  @allow_indeterminate.setter
  def allow_indeterminate(self, value):
    self._props['allow_indeterminate'] = value

  @property
  def error(self):
    return self._props.get('error')

  @error.setter
  def error(self, value):
    self.dom_nodes['anvil-m3-checkbox-container'].classList.remove('anvil-m3-checkbox-error')
    self._props['error'] = value
    if value:
      self.dom_nodes['anvil-m3-checkbox-container'].classList.add('anvil-m3-checkbox-error')

#!defClass(material_3,Button)!:
