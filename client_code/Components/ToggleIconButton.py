from .IconButton import IconButton
from ..Functions import property_with_callback

icon_button_properties = getattr(IconButton, "_anvil_properties_", [])

selected_property = {"name": "selected", "type": "boolean", "group": "Attributes", "important": True, "default_value": False}
selected_border = {"name": "selected_border", "type": "string", "group": "Style", "description": "Border style when component is in the selected state. Accepts any valid CSS border value."}
selected_background = {"name": "selected_background", "type": "color", "group": "Style", "description": "Background color when component is in the selected state."}
selected_icon_color = {"name": "selected_icon_color", "type": "color", "group": "Style", "description": "Icon color when component is in the selected state."}

class ToggleIconButton(IconButton):
  _anvil_properties_ = [selected_property, selected_border, selected_background, selected_icon_color, *icon_button_properties]

  def selected_setter(self, value):
    self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle("selected", value)
    self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle("selected", value)
    self.apply_styles()

  selected = property_with_callback("selected", selected_setter)
  selected_border = property_with_callback("selected_border", apply_styles)
  selected_background = property_with_callback("selected_background", apply_styles)
  selected_icon_color = property_with_callback("selected_icon_color", apply_styles)
  
  """
    @property
  def selected(self):
    return self._props.get("selected") #return selected or None if doesn't exist. Dont' have to do the thing from ln 14
  @selected.setter
  def selected(self, value):
    self._props["selected"] = value
    
  """

  """  def appearance_setter(self, value):
    self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle("filled", False)
    self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle("filled-tonal", False)
    self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle("outlined", False)
    self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle("filled", False)
    self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle("filled-tonal", False)
    self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle("outlined", False)
    
    if value is not None:
      class_name = self._appearance_css_classes[value]
      self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle(class_name, True)
      self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle(class_name, True)

  appearance = property_with_callback("appearance", appearance_setter)"""

  # This will be deprecated v soon.
  def _anvil_get_design_info_(self, as_layout=False): 
    design_info = super()._anvil_get_design_info_(as_layout)
    design_info["propertyDescriptions"] = [selected_property] + design_info["propertyDescriptions"]
    return design_info