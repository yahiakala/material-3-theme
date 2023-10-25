from .IconButton import IconButton

icon_button_properties = getattr(IconButton, "_anvil_properties_", [])

selected_property = {"name": "selected", "type": "boolean", "group": "Attributes", "important": True}

class ToggleIconButton(IconButton):
  _anvil_properties_ = [selected_property, *icon_button_properties]

  @property
  def selected(self):
    return self._props.get("selected")
  @selected.setter
  def selected(self, value):
    self._props["selected"] = value

  # This will be deprecated v soon.
  def _anvil_get_design_info_(self, as_layout=False): 
    design_info = super()._anvil_get_design_info_(as_layout)
    design_info["propertyDescriptions"] = [selected_property] + design_info["propertyDescriptions"]
    return design_info

  