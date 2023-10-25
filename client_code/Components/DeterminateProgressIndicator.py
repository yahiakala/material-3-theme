import anvil.server
from .IndeterminateProgressIndicator import IndeterminateProgressIndicator
import anvil.designer
from ..Functions import property_with_callback
from math import pi
indeterminate_indicator_properties = getattr(IndeterminateProgressIndicator, "_anvil_properties_", [])

progress_property = {"name": "progress", "type": "number", "default_binding_prop": True, "important": True, "description": "Progress percentage as a number. eg 20% is 20", "group": "Attributes"}

class DeterminateProgressIndicator(IndeterminateProgressIndicator):
  _anvil_properties_ = [progress_property, *indeterminate_indicator_properties]
  def __init__(self, **properties):
    super().__init__(**properties)
    self.init_components(**properties)
    self.dom_nodes['anvil-m3-progressindicator-linear'].removeChild(self.dom_nodes['anvil-m3-progressindicator-extra'])
    self.dom_nodes['anvil-m3-progressindicator-indicator'].removeChild(self.dom_nodes['indicator-animate1'])
    self.dom_nodes['anvil-m3-progressindicator-indicator'].removeChild(self.dom_nodes['indicator-animate2'])
    self.dom_nodes['anvil-m3-progressindicator-circular'].style.transform = "scaleX(1)"

  def draw_path(self, percent):
    cx, cy = 24, 24 #center of circle
    rx, ry = 18, 18 #major/minor radius
    t1 = 3 * pi / 2 #start angle in radians
    phi = 0 # Rotation on the whole in radians
    
    radian = pi * percent /  50
    delta = radian # Angle to sweep in radians (positive)
    
    if percent <= 99:
      radian = pi * percent /  50
      delta = radian # Angle to sweep in radians (positive)
      d = self.f_svg_ellipse_arc(cx, cy, rx, ry, t1, delta)
      self.dom_nodes['anvil-m3-progressindicator-arc'].setAttribute("d", d)
    else:
      radian = pi * 99 /  50
      delta = radian # Angle to sweep in radians (positive)
      d = self.f_svg_ellipse_arc(cx, cy, rx, ry, t1, delta)
      self.dom_nodes['anvil-m3-progressindicator-arc'].setAttribute("d", d + " Z")
      
  # Properties 
  def update_progress(self, value):
    v = 0
    if value is None:
      v = 0
    elif value in range(0, 100):
      v = value
    elif value >= 100:
      v = 100
      
    if self.shape is "linear":
      self.dom_nodes['anvil-m3-progressindicator-indicator'].setAttribute("x2", f"{v}%")
    else:
      self.draw_path(v)

  """
  def change_progress(self, value):
    v = 0
    if value is None:
      v = 0
    elif value in range(0, 100):
      v = value
    elif value >= 100:
      v = 100
      
    if self.shape is "linear":
      self.dom_nodes['anvil-m3-progressindicator-indicator'].style.width = f"{v}%"
    else:
      self.draw_path(v)
  """
    
  progress = property_with_callback("progress", update_progress)


  
  def timer_tick(self, **event_args):
    pass  

  def arc_timer_tick(self, **event_args):
    pass
  
  # This will be deprecated v soon.
  def _anvil_get_design_info_(self, as_layout=False): 
    design_info = super()._anvil_get_design_info_(as_layout)
    design_info["propertyDescriptions"] = [progress_property] + design_info["propertyDescriptions"]
    return design_info
