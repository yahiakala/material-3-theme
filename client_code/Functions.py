from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

def m3_alert(title=None, content=None, buttons="OK", icon=None, dividers=False, centered=False):
  pass

def theme_color_to_css(color:str):
  if color.startswith('theme:'):
    color = color.lstrip('theme:')
    return app.theme_colors[color]
  else:
    return color

#REUSABLE PROPERTIES
def property_with_callback(prop, cb):
  def getter(self):
    return self._props.get(prop)

  def setter(self, value):
    self._props[prop] = value
    cb(self, value)
  
  return property(getter, setter)
  
def property_without_callback(prop):
  def getter(self):
    return self._props.get(prop)

  def setter(self, value):
    self._props[prop] = value
  
  return property(getter, setter)

def color_property(dom_node_name, style_prop):
  def getter(self):
    return self.dom_nodes[dom_node_name].style[style_prop]

  def setter(self, value):
    if value: value = theme_color_to_css(value)
    self.dom_nodes[dom_node_name].style[style_prop] = value

  return property(getter, setter)

def style_property(dom_node_name, style_prop):
  def getter(self):
    return self.dom_nodes[dom_node_name].style[style_prop]

  def setter(self, value):
    self.dom_nodes[dom_node_name].style[style_prop] = value

  return property(getter, setter)

def innerHTML_property(dom_node_name):
  def getter(self):
    return self.dom_nodes[dom_node_name].innerHTML

  def setter(self, value):
    self.dom_nodes[dom_node_name].innerHTML = value

  return property(getter, setter)

def innerText_property(dom_node_name):
  def getter(self):
    return self.dom_nodes[dom_node_name].innerText

  def setter(self, value):
    self.dom_nodes[dom_node_name].innerText = value

  return property(getter, setter)

def href_property(dom_node_name):
  def getter(self):
    return self.dom_nodes[dom_node_name].href

  def setter(self, value):
    self.dom_nodes[dom_node_name].href = value

  return property(getter, setter)

def checked_property(dom_node_name):
  def getter(self):
    return self.dom_nodes[dom_node_name].checked

  def setter(self, value):
    self.dom_nodes[dom_node_name].checked = value

  return property(getter, setter)

def enabled_property(dom_node_name):
  def getter(self):
    return self._enabled

  def setter(self, value):
    self._enabled = value
    if value:
      self.dom_nodes[dom_node_name].removeAttribute("disabled")
    else:
      self.dom_nodes[dom_node_name].setAttribute("disabled", " ")
      
  return property(getter, setter)

def name_property(dom_node_name):
  def getter(self):
    return self.dom_nodes[dom_node_name].name

  def setter(self, value):
    self.dom_nodes[dom_node_name].name = value

  return property(getter, setter)

def value_property(dom_node_name):
  def getter(self):
    return self.dom_nodes[dom_node_name].value

  def setter(self, value):
    self.dom_nodes[dom_node_name].value = value

  return property(getter, setter)

def underline_property(dom_node_name):
  def getter(self):
    return self._props['underline']

  def setter(self, value):
    self._props.get('underline')
    if value:
      self.dom_nodes[dom_node_name].style.textDecoration = 'underline'
    else:
      self.dom_nodes[dom_node_name].style.textDecoration = 'none'

  return property(getter, setter)

def italic_property(dom_node_name):
  def getter(self):
    return self._props.get('italic')

  def setter(self, value):
    self._props['italic'] = value
    if value:
      self.dom_nodes[dom_node_name].style.fontStyle = 'italic'
    else:
      self.dom_nodes[dom_node_name].style.fontStyle = 'normal'

  return property(getter, setter)

def bold_property(dom_node_name):
  def getter(self):
    return self._props.get('bold')

  def setter(self, value):
    self._props['bold'] = value
    if value:
      self.dom_nodes[dom_node_name].style.fontWeight = 'bold'
    else:
      self.dom_nodes[dom_node_name].style.fontWeight = 'normal'

  return property(getter, setter)

def font_size_property(dom_node_name):
  def getter(self):
    return self._font_size

  def setter(self, value):
    self._font_size = value
    if value: value = f'{value}px'
    self.dom_nodes[dom_node_name].style.fontSize = value

  return property(getter, setter)

def margin_property(dom_node_name, prop_name="margin"):
  def getter(self):
    return self._props.get('margin')

  def setter(self, value):
    self._props['margin'] = value
    #value = value
    self.dom_nodes[dom_node_name].style.margin = f"{value}px"
    
  return property(getter, setter)
  
  


