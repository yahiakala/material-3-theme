from ._anvil_designer import ButtonMenu_combinedTemplate
from anvil import *
from anvil.js import window
from anvil.js.window import document
import random, string, math
import anvil.designer

class ButtonMenu_combined(ButtonMenu_combinedTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
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

  @property #todo: make this internal
  def position(self):
    return self._position;
  @position.setter
  def position(self, value = {"top": 0, "left": 0, "bottom": 0, "right": 0, "height": 0, "width": 0}):
    self._position = value
    self.windowSize = {"width": window.innerWidth, "height": window.innerHeight}
    menuNode = self.dom_nodes['anvil-m3-buttonMenu-items-container']
    self.menuSize = {"width": menuNode.offsetWidth, "height": menuNode.offsetHeight}

  def windowSize(self): #todo: make this internal
    return self._windowSize
  def windowSize(self, value):
    self._windowSize = value
    
  @property #todo: make this internal
  def menuSize(self):
    return self._menuSize
  @menuSize.setter
  def menuSize(self, value):
    self._menuSize = value

  def toggle_menu_visibility(self, **event_args):
    # menuNode = self.dom_nodes['anvil-m3-buttonMenu-items-container']
    self.set_visibility()
    

  def update_menu_placement(self):
      menuNode = self.dom_nodes['anvil-m3-buttonMenu-items-container']
    
      # horizontal placement
      menuLeft = self.position['left']
      menuRight = menuLeft + self.menuSize['width']
      if self.windowSize['width'] < menuRight:
        menuNode.style.right = '5px'
      else:
        menuNode.style.left = f"{math.floor(menuLeft) + 5}px"
        
      # vertical placement
      menuTop = self.position['bottom']
      menuBottom = menuTop + self.menuSize['height']

      ## menu too tall!
      if (self.windowSize['height'] - self.position['height']) < self.menuSize['height']: 
        spaceAtTop = self.position['top']
        spaceAtBottom = self.windowSize['height'] - (spaceAtTop + self.position['height'])

        # put at the top and set container height
        if spaceAtTop > spaceAtBottom:
          menuNode.style.bottom = f"{math.floor(self.windowSize['height'] - (self.position['top'] - 5))}px"
          menuNode.style.height = f"{math.floor(spaceAtTop - 7)}px"
          
        # put at the bottom and set container height
        else:
          menuNode.style.top = f"{math.floor(menuTop + 5)}px"
          menuNode.style.height = f"{math.floor(spaceAtBottom - 7)}px"

      ## menu fits
      else: 
        # default placement is out of bounds
        if self.windowSize['height'] < menuBottom:
          menuNode.style.bottom = f"{math.floor(self.windowSize['height'] - (self.position['top'] - 5))}px"
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
      self.get_button_position()
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

  def get_button_position(self):
    rect = self.menu_button.dom_nodes['anvil-m3-button'].getBoundingClientRect()
    self.position = {
      "top": rect.top,
      "right": rect.right,
      "bottom": rect.bottom,
      "left": rect.left,
      "height": rect.bottom - rect.top,
      "width": rect.right - rect.left,
    }

  def printPosition(self):
    print(self.position["top"])
    print(self.position["right"])
    print(self.position["bottom"])
    print(self.position["left"])
    print(self.position["height"])
    print(self.position["width"])
    print()
    print(self.windowSize["width"])
    print(self.windowSize["height"])
    print()
    print(self.menuSize["width"])
    print(self.menuSize["height"])
    print("*****")

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
    # print("child clicked")
    # print(event)
    # print(event.target)
    self.remove_shield()