from .IconButton import IconButton
from ..Functions import property_with_callback

icon_button_properties = getattr(IconButton, "_anvil_properties_", [])

selected_property = {"name": "selected", "type": "boolean", "group": "Attributes", "important": True, "default_value": False}
selected_border_property = {"name": "selected_border", "type": "string", "group": "Style", "description": "Border style when component is in the selected state. Accepts any valid CSS border value."}
selected_background_property = {"name": "selected_background", "type": "color", "group": "Style", "description": "Background color when component is in the selected state."}
selected_icon_color_property = {"name": "selected_icon_color", "type": "color", "group": "Style", "description": "Icon color when component is in the selected state."}

class ToggleIconButton(IconButton):
  _anvil_properties_ = [selected_property, selected_border_property, selected_background_property, selected_icon_color_property, *icon_button_properties]
  
  # def __init__(self, **properties):
  #   super().__init__(_anvil_properties_)
    
    
  # class A(object):
  #   def __init__(self):
  #       print("world")
  
  # class B(A):
  #   def __init__(self):
  #       print("hello")
  #       super().__init__()

  
  # def __init__(self, **properties):
  #   self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle("toggle", True)
  #   self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle("toggle", True)
  # super().__init__(**properties)
  
  def selected_setter(self, value):
    self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle("selected", value)
    self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle("selected", value)
    self.apply_styles()
  def apply_styles(self):
    if self.selected:
      self.dom_nodes['anvil-m3-iconbutton-container'].style.backgroundColor = self.selected_background
      self.dom_nodes['anvil-m3-iconbutton-container'].style.border = self.selected_border
      self.dom_nodes['anvil-m3-iconbutton-icon'].style.color = self.selected_icon_color
    else:
      self.dom_nodes['anvil-m3-iconbutton-container'].style.backgroundColor = self.background
      self.dom_nodes['anvil-m3-iconbutton-container'].style.border = self.border
      self.dom_nodes['anvil-m3-iconbutton-icon'].style.color = self.icon_color

  selected = property_with_callback("selected", selected_setter)
  selected_border = property_with_callback("selected_border", apply_styles)
  selected_background = property_with_callback("selected_background", apply_styles)
  selected_icon_color = property_with_callback("selected_icon_color", apply_styles)
  

  # This will be deprecated v soon.
  def _anvil_get_design_info_(self, as_layout=False): 
    design_info = super()._anvil_get_design_info_(as_layout)
    design_info["propertyDescriptions"] = [selected_property] + design_info["propertyDescriptions"]
    return design_info