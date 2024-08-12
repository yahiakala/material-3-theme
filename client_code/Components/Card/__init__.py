from ._anvil_designer import CardTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.designer
from anvil import HtmlTemplate
from ...Functions import tooltip_property, role_property, property_with_callback, style_property, spacing_property, margin_property, padding_property, color_property, border_property

class Card(CardTemplate):
  def __init__(self, **properties):
    self.tooltip_node = None
    self._props = properties
    self._card_image_temp_url = None
    self._on_page = False
    self._tooltip_node = None
    self.init_components(**properties)
    if not anvil.designer.in_designer:
      self.dom_nodes['empty-image'].style.display = "none"
      self.dom_nodes['empty-content'].style.display = "none"

  align = style_property('anvil-m3-card', 'justifyContent', 'align')
  visible = HtmlTemplate.visible

  def _set_nodes_class_by_image(self, image_position, val):
    self.dom_nodes['anvil-m3-card'].classList.toggle(f'anvil-m3-{image_position}-image', val)
    self.dom_nodes['content'].classList.toggle(f'anvil-m3-{image_position}-image', val)
    self.dom_nodes['image'].classList.toggle(f'anvil-m3-{image_position}-image', val)
    
  def _set_image_position(self, value):
    for position in [None, 'top', 'bottom', 'left', 'right', 'full']:
      self._set_nodes_class_by_image(position or 'none', False)
    
    self._set_nodes_class_by_image(value or 'none', True)
  image_position = property_with_callback("image_position", _set_image_position)

  def _set_class_of_nodes(self, appearance, val):
    self.dom_nodes['anvil-m3-card'].classList.toggle(f'anvil-m3-{appearance}', val)
    self.dom_nodes['image'].classList.toggle(f'anvil-m3-{appearance}', val)
    self.dom_nodes['content'].classList.toggle(f'anvil-m3-{appearance}', val)
    
  def _set_appearance(self, value):
    for appearance in ['outlined', 'filled', 'elevated']:
      self._set_class_of_nodes(appearance, False)

    self._set_class_of_nodes(value, True)
  appearance = property_with_callback("appearance", _set_appearance)

  def _set_image_width(self, value):
    valid_values = ['px', 'rem', 'em', '%']
    for i in valid_values:
      if value.endswith(i):
        self.dom_nodes['image'].style.width = value
        return
    self.dom_nodes['image'].style.width = f'{value}px'
  image_width = property_with_callback('image_width', _set_image_width)

  def _set_image_height(self, value):
    valid_values = ['px', 'rem', 'em', '%']
    for i in valid_values:
      if value.endswith(i):
        self.dom_nodes['image'].style.height = value
        return
    self.dom_nodes['image'].style.height = f'{value}px'
  image_height = property_with_callback('image_height', _set_image_height)
  
  background = color_property('anvil-m3-card', 'backgroundColor', 'background')

  def _set_card_img(self, *_args):
    if self.image:
      #set a card position so the image appears
      if not self.image_position:
        self.image_position = 'top'
      if isinstance(self.image, str):
        self.dom_nodes['image'].style.backgroundImage = f"url('{self.image}')"
      elif type(self.image) is anvil.LazyMedia:
        self.dom_nodes['image'].style.backgroundImage = f"url('{self.image.get_url()}')"
      else:
        if self._on_page:
          self._card_image_temp_url = anvil.media.TempUrl(self.image)
          self.dom_nodes['image'].style.backgroundImage = f"url('{self._card_image_temp_url.url}')"
    else:
      self.dom_nodes['image'].style.removeProperty = "background-image"

  image = property_with_callback("image", _set_card_img)

  def _set_rounded_img(self, value):
     self.dom_nodes['image'].classList.toggle('anvil-m3-card-rounded', value)
  rounded_image = property_with_callback("rounded_image", _set_rounded_img)

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    self._on_page = True
    self._set_card_img()

  def form_hide(self, **event_args):
    """This method is called when the form is removed from the page"""
    self._on_page = False
    if self._card_image_temp_url:
      self._card_image_temp_url.revoke()
      self._card_image_temp_url = None

  margin = margin_property('anvil-m3-card')
  card_content_padding = padding_property('content', 'card_content_padding')
  card_image_content_padding = padding_property('image', 'card_image_content_padding')
  tooltip = tooltip_property('anvil-m3-card')
  border = style_property('anvil-m3-card', 'border', 'border')
  role = role_property('anvil-m3-card')


  #!componentProp(material_3.Card)!1: {name:"visible",type:"boolean",description:"If True, the component will be displayed."} 
  #!componentProp(material_3.Card)!1: {name:"border",type:"string",description:"The border of this component. Can take any valid CSS border value."}
  #!componentProp(material_3.Card)!1: {name:"background_color",type:"color",description:"The color of the background of this component."}
  #!componentProp(material_3.Card)!1: {name:"align",type:"enum",description:"The position of this component in the available space."} 
  #!componentProp(material_3.Card)!1: {name:"margin",type:"margin",description:"The margin (pixels) of the component."}
  #!componentProp(material_3.Card)!1: {name:"tooltip",type:"string",description:"The text to display when the mouse is hovered over this component."}
  #!componentProp(material_3.Card)!1: {name:"role",type:"themeRole",description:"A style for this component defined in CSS and added to Roles"} 
  #!componentProp(material_3.Card)!1: {name:"tag",type:"object",description:"Use this property to store any extra data for the component."}
  #!componentProp(material_3.Card)!1: {name:"appearance",type:"enum",options:["elevated", "filled", outlined"],description:"A predefined style for this component."}  
  #!componentProp(material_3.Card)!1: {name:"image",type:"uri",description:"The image to be displayed on the card. Can be a URL or an asset (eg. _/theme/....)."}  
  #!componentProp(material_3.Card)!1: {name:"image_position",type:"enum",options:["top","left","right","bottom","full"],description:"The image to be displayed on the card. Can be a URL or an asset (eg. _/theme/....)."}  
  #!componentProp(material_3.Card)!1: {name:"rounded_image",type:"boolean",description:"The image to be displayed on the card. Can be a URL or an asset (eg. _/theme/....)."}  

  
#!defClass(material_3,Card, anvil.Component)!: