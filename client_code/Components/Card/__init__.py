from ._anvil_designer import CardTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.designer
from anvil import HtmlTemplate
from ...Functions import property_with_callback, style_property

class Card(CardTemplate):
  def __init__(self, **properties):
    self._props = properties
    self.init_components(**properties)
    if not anvil.designer.in_designer:
      self.dom_nodes['empty-image'].style.display = "none"
      self.dom_nodes['empty-content'].style.display = "none"

  # align = style_property('anvil-m3-card-component', 'justifyContent', 'align')
  visible = HtmlTemplate.visible

  def set_nodes_class_by_image(self, image_position, val):
    self.dom_nodes['anvil-m3-card'].classList.toggle(f'{image_position}-image', val)
    self.dom_nodes['content'].classList.toggle(f'{image_position}-image', val)
    self.dom_nodes['image'].classList.toggle(f'{image_position}-image', val)
    
  def set_image_position(self, value):
    for position in ['none', 'top', 'bottom', 'left', 'right', 'full']:
      self.set_nodes_class_by_image(position, False)
    self.set_nodes_class_by_image(value, True)
  image_position = property_with_callback("image_position", set_image_position)

  def set_class_of_nodes(self, appearance, val):
    self.dom_nodes['anvil-m3-card'].classList.toggle(f'anvil-m3-{appearance}', val)
    self.dom_nodes['image'].classList.toggle(f'anvil-m3-{appearance}', val)
    self.dom_nodes['content'].classList.toggle(f'anvil-m3-{appearance}', val)
    
  def set_appearance(self, value):
    for appearance in ['outlined', 'filled', 'elevated']:
      self.set_class_of_nodes(appearance, False)

    self.set_class_of_nodes(value, True)
  appearance = property_with_callback("appearance", set_appearance)

  image_width = align = style_property('image', 'width', 'image_width')
  image_height = align = style_property('image', 'height', 'image_height')

  # Todo: this will change from string to the URI property
  def set_image(self, value):
    if value:
      self.dom_nodes['image'].style.backgroundImage = f"url('{value}')";
    else:
      self.dom_nodes['image'].style.removeProperty = "background-image"
  card_image = property_with_callback("card_image", set_image)

  def set_rounded_img(self, value):
     self.dom_nodes['image'].classList.toggle('anvil-m3-card-rounded', value)
  rounded_image = property_with_callback("rounded_image", set_rounded_img)