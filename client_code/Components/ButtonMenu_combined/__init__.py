from ._anvil_designer import ButtonMenu_combinedTemplate
from anvil import *
from anvil.js import window
from anvil.js.window import document
import random, string, math
import anvil.designer

class ButtonMenu_combined(ButtonMenu_combinedTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    
    self.window_size = {}
    self.menu_size = {}
    self.button_positioning = {}
    
    # self.id = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    # self.dom_nodes['anvil-m3-buttonMenu-container'].id = self.id
    self.shield = document.createElement("div")
    # self.shield.id = f'shield-{self.id}'
    self.shield.classList.toggle("anvil-m3-menu-clickShield", True)

  @property
  def text(self):
    return self._text
  @text.setter
  def text(self, value):
    self._text = value
    self.menu_button.text = value

  @property
  def appearance(self):
    return self._appearance
  @appearance.setter
  def appearance(self, value):
    self.menu_button.appearance = value

  @property
  def enabled(self):
    return self._enabled
  @enabled.setter
  def enabled(self, value):
    self._enabled = value
    self.menu_button.enabled = value

  def toggle_menu_visibility(self, **event_args):
    self.set_visibility()

  def update_menu_placement(self):
    menuNode = self.dom_nodes['anvil-m3-buttonMenu-items-container']
    self.window_size = {"width": window.innerWidth, "height": window.innerHeight}
    self.menu_size = {"width": menuNode.offsetWidth, "height": menuNode.offsetHeight}
    # horizontal placement
    menuLeft = self.button_positioning['left']
    menuRight = menuLeft + self.menu_size['width']
    if self.window_size['width'] < menuRight:
      menuNode.style.right = '5px'
    else:
      menuNode.style.left = f"{math.floor(menuLeft) + 5}px"
      
    # vertical placement
    menuTop = self.button_positioning['bottom']
    menuBottom = menuTop + self.menu_size['height']

    ## menu too tall!
    if (self.window_size['height'] - self.button_positioning['height']) < self.menu_size['height']: 
      spaceAtTop = self.button_positioning['top']
      spaceAtBottom = self.window_size['height'] - (spaceAtTop + self.button_positioning['height'])

      # put at the top and set container height
      if spaceAtTop > spaceAtBottom:
        menuNode.style.bottom = f"{math.floor(self.window_size['height'] - (self.button_positioning['top'] - 5))}px"
        menuNode.style.height = f"{math.floor(spaceAtTop - 7)}px"
        
      # put at the bottom and set container height
      else:
        menuNode.style.top = f"{math.floor(menuTop + 5)}px"
        menuNode.style.height = f"{math.floor(spaceAtBottom - 7)}px"

    ## menu fits
    else: 
      # default placement is out of bounds
      if self.window_size['height'] < menuBottom:
        menuNode.style.bottom = f"{math.floor(self.window_size['height'] - (self.button_positioning['top'] - 5))}px"
      # fits in default position
      else:
        menuNode.style.top = f"{math.floor(menuTop + 5)}px"
    
  def set_visibility(self, value = None):
    menuNode = self.dom_nodes['anvil-m3-buttonMenu-items-container']
    classes = menuNode.classList
    if value is not None:
      classes.toggle('anvil-m3-buttonMenu-items-hidden', not value)
    else:
      classes.toggle('anvil-m3-buttonMenu-items-hidden')
      
    visible = not classes.contains('anvil-m3-buttonMenu-items-hidden')
    if visible:
      menuNode.addEventListener('click', self.child_clicked) #need to remove event handler
      
      if not anvil.designer.in_designer:
        self.place_shield()
      self.get_button_measurements()
      self.update_menu_placement()
    else:
      menuNode.removeAttribute("style")
    return visible
    
  def _anvil_get_design_info_(self, as_layout=False):
    design_info = super()._anvil_get_design_info_(as_layout)
    design_info["interactions"] = [
      {
        "type": "on_selection",
        "callbacks": {
          "onSelectDescendent": self._on_select_descendent,
          "onSelectOther": self._on_select_other
        }
      },
    ]
    return design_info

  def _on_select_descendent(self):
    self.set_visibility(True)

  def _on_select_other(self):
    self.set_visibility(False)

  def get_button_measurements(self):
    rect = self.menu_button.dom_nodes['anvil-m3-button'].getBoundingClientRect()
    self.button_positioning = {
      "top": rect.top,
      "right": rect.right,
      "bottom": rect.bottom,
      "left": rect.left,
      "height": rect.bottom - rect.top,
      "width": rect.right - rect.left,
    }

  def place_shield(self):
    document.body.appendChild(self.shield)
    self.shield.addEventListener('click', self.remove_shield_handler) #need to remove event handler magix x- remove! for shield 
    document.body.style.overflow = "hidden"
    
  def remove_shield_handler(self, event):
    self.remove_shield()
    
  def remove_shield(self):
    if document.contains(self.shield):
      document.body.removeChild(self.shield)
      self.toggle_menu_visibility()
      document.body.style.removeProperty("overflow")
    
  def child_clicked(self, event):
    self.remove_shield()