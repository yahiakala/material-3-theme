from ..IconButton import IconButton

icon_button_properties = getattr(IconButton, "_anvil_properties_", [])

selected_property = {"name": "selected", "type": "boolean"}

class ToggleIconButton(IconButton):
  _anvil_properties_ = [selected_property, *icon_button_properties]

  @property
  def selected(self):
    return self._selected
  @selected.setter
  def selected(self, value):
    self._selected = value

  