from ._anvil_designer import IndeterminateProgressIndicatorTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...Functions import property_with_callback, style_property
from math import cos, sin, pi
from anvil.js.window import document
from anvil import HtmlTemplate

class IndeterminateProgressIndicator(IndeterminateProgressIndicatorTemplate):
  def __init__(self, **properties):
    self._props = properties
    self.arc_timer.interval = 0
    self.timer.interval = 0
  
    self.init_components(**properties)
    self._t = 0
    self._phi = 0
    self._arc = 5

  def set_shapes(self, value):
    if value is "linear":
      self.dom_nodes['anvil-m3-progressindicator-linear'].classList.toggle("anvil-m3-progressindicator-hidden", False)
      self.dom_nodes['anvil-m3-progressindicator-circular'].classList.toggle("anvil-m3-progressindicator-hidden", True)
      self.arc_timer.interval = 0
      self.timer.interval = 0
      
    else:
      self.dom_nodes['anvil-m3-progressindicator-linear'].classList.toggle("anvil-m3-progressindicator-hidden", True)
      self.dom_nodes['anvil-m3-progressindicator-circular'].classList.toggle("anvil-m3-progressindicator-hidden", False)
      self.arc_timer.interval = 0.0001
      self.timer.interval = .0015
  shape = property_with_callback("shape", set_shapes)
  align = style_property('anvil-m3-progressindicator-component', 'justifyContent')
  visible = HtmlTemplate.visible
  
  def draw_circular_path(self):
    cx, cy = 24, 24 #center of circle
    rx, ry = 18, 18 #major/minor radius
    t1 = 3 * pi / 2 #start angle in radians
    phi = self._phi
    
    radian = pi * self._arc /  50
    delta = -radian # Angle to sweep in radians (positive)
    d = self.f_svg_ellipse_arc(cx, cy, rx, ry, t1, delta, phi)
    self.dom_nodes['anvil-m3-progressindicator-arc'].setAttribute("d", d)

  def f_matrix_times(self, matrix, vector):
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    x, y = vector[0], vector[1]
    return [a * x + b * y, c * x + d * y]

  def f_rotate_matrix(self, x):
    return [[cos(x), -sin(x)],
            [sin(x), cos(x)]]

  def f_vec_add(self, vector1, vector2):
    return [vector1[0] + vector2[0], vector1[1] + vector2[1]]

  def f_svg_ellipse_arc(self, cx, cy, rx, ry, t1, delta, phi = 0):
    delta = delta % (2 * pi)
    rotMatrix = self.f_rotate_matrix(phi)
    sX, sY = self.f_vec_add(self.f_matrix_times(rotMatrix, [rx * cos(t1), ry * sin(t1)]), [cx, cy])
    eX, eY = self.f_vec_add(self.f_matrix_times(rotMatrix, [rx * cos(t1 + delta), ry * sin(t1 + delta)]), [cx, cy])
    fA = 1 if delta > pi else 0
    fS = 1 if delta > 0 else 0
    return f"M {sX} {sY} A {rx} {ry} {(phi / (2 * pi)) * 360} {fA} {fS} {eX} {eY}"

  def timer_tick(self, **event_args):
    self._phi -= pi / 160
    self.draw_circular_path()   

  def arc_timer_tick(self, **event_args):
    # timing not quite right - need to clip the valley a bit more
    self._t +=  15 * self.timer.interval
    self._t %= 2 * pi
    A = 43
    B = 50
    C = 2
    c = cos(self._t - pi/4)
    self._arc = A * (((1 + C ** 2) / (1 + (C * c) ** 2 )) ** 0.5 ) * c + B

  def _anvil_get_design_info_(self, as_layout=False):
    di = super()._anvil_get_design_info_(as_layout)
    di['interactions'] = [
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
    }]
    return di 

  def toggle_visible(self):
    self.visible = not self.visible
    anvil.designer.update_component_properties(self, {'visible': self.visible})

  def setAlignment(self, value):
    self.align = value
    anvil.designer.update_component_properties(self, {'align': self.align})
