import anvil.server
from . import TextInput
import anvil.designer
from ...Functions import property_with_callback, theme_color_to_css

# max_height_property = {"name": "max_height", "type": "string"}

class TextField(TextInput):
  _anvil_properties_ = [*TextInput._anvil_properties_]
  def __init__(self, **properties):
    super().__init__(**properties)
    self.init_components(**properties)