from .IconButton import IconButton
from ..Functions import property_with_callback

icon_button_properties = getattr(IconButton, "_anvil_properties_", [])

selected_property = {"name": "selected", "type": "boolean", "group": "Attributes", "important": True, "default_value": False}
selected_border_property = {"name": "selected_border", "type": "string", "group": "Toggled Style" , "description": "Border style when component is in the selected state. Accepts any valid CSS border value."}
selected_background_property = {"name": "selected_background", "type": "color", "group": "Toggled Style" , "description": "Background color when component is in the selected state."}
selected_icon_color_property = {"name": "selected_icon_color", "type": "color", "group": "Toggled Style" , "description": "Icon color when component is in the selected state."}

class ToggleIconButton(IconButton):
  _anvil_properties_ = [selected_property, selected_border_property, selected_background_property, selected_icon_color_property, *icon_button_properties]
  def __init__(self, **properties):
    super().__init__(**properties)
    self.init_components(**properties)
  
    self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle("toggle", True)
    self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle("toggle", True)   

    # I think there is a smarter way to do this. I don't know the setter isn't getting called in the beginning.
    self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle("selected", self.selected)
    self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle("selected", self.selected)
    
  # Properties 
  def apply_styles(self, value):
    if value:
      self.dom_nodes['anvil-m3-iconbutton-container'].style.backgroundColor = self.selected_background
      self.dom_nodes['anvil-m3-iconbutton-container'].style.border = self.selected_border
      self.dom_nodes['anvil-m3-iconbutton-icon'].style.color = self.selected_icon_color
    else:
      self.dom_nodes['anvil-m3-iconbutton-container'].style.backgroundColor = self.background
      self.dom_nodes['anvil-m3-iconbutton-container'].style.border = self.border
      self.dom_nodes['anvil-m3-iconbutton-icon'].style.color = self.icon_color

  def selected_setter(self, value):
    self.dom_nodes['anvil-m3-iconbutton-container'].classList.toggle("selected", value)
    self.dom_nodes['anvil-m3-iconbutton-icon'].classList.toggle("selected", value)
    self.apply_styles(value)
    
  border = property_with_callback("border", apply_styles)
  icon_color = property_with_callback("icon_color", apply_styles)
  background = property_with_callback("background", apply_styles)
  selected_border = property_with_callback("selected_border", apply_styles)
  selected_background = property_with_callback("selected_background", apply_styles)
  selected_icon_color = property_with_callback("selected_icon_color", apply_styles)
  selected = property_with_callback("selected", selected_setter)
  
  def handle_click(self, event):
    event.preventDefault()
    self.selected = not self.selected
    self.raise_event("click")
  
  # This will be deprecated v soon.
  def _anvil_get_design_info_(self, as_layout=False): 
    design_info = super()._anvil_get_design_info_(as_layout)
    design_info["propertyDescriptions"] = [selected_property, selected_border_property, selected_background_property, selected_icon_color_property] + design_info["propertyDescriptions"]
    design_info["interactions"] = [
      {
      "type": "whole_component_multi",
      "title": "Align",
      "options": [{
        "name": "Left Align",
        "id": "left",
        "icon" : "align-left",
      },{
        "name": "Left Center",
        "id": "center",
        "icon" : "align-center",
      },{
        "name": "Left Right",
        "id": "right",
        "icon" : "align-right",
      }],
      "callbacks": {
        "execute": self.setAlignment
      }
    },
      {
      "type": "whole_component",
      "title": "Visible",
      "icon": "add", #TODO: eye icon
      "callbacks": {
        "execute": self.toggle_visible
      }
    }, {
      "type": "whole_component",
      "title": "Enable",
      "icon": "add", #TODO: power icon
      "callbacks": {
        "execute": self.toggle_enabled
      } 
    },{
      "type": "region",
      "bounds": self.dom_nodes['anvil-m3-iconbutton-component'],
      "callbacks": {
        "doubleClick": self.toggle_selected
      }
    } ]
    return design_info

  def setAlignment(self, value):
    self.align = value
    anvil.designer.update_component_properties(self, {'align': self.align})
  def toggle_visible(self):
    self.visible = not self.visible
    anvil.designer.update_component_properties(self, {'visible': self.visible})
  def toggle_enabled(self):
    self.enabled = not self.enabled
    anvil.designer.update_component_properties(self, {'enabled': self.enabled})
  def toggle_selected(self):
    self.selected = not self.selected
    anvil.designer.update_component_properties(self, {'selected': self.selected})


"""
 def toggle_selected(self):
    self.selected = not self.selected
    anvil.designer.update_component_properties(self, {'selected': self.selected})

  def toggle_enabled(self):
    self.enabled = not self.enabled
    anvil.designer.update_component_properties(self, {'enabled': self.enabled})

  def toggle_visible(self):
    self.visible = not self.visible
    anvil.designer.update_component_properties(self, {'visible': self.visible})

  def setAlignment(self, value):
    self.align = value
    anvil.designer.update_component_properties(self, {'align': self.align})

"""