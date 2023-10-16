from ._anvil_designer import DropdownMenuTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import HtmlTemplate
from ...Functions import style_property # underline_property, italic_property, , color_property, innerText_property, bold_property, font_size_property
from anvil.js import window
from anvil.js.window import document
import random, string, math
import anvil.designer
from ..Menu.MenuItem import MenuItem

class DropdownMenu(DropdownMenuTemplate):
  def __init__(self, **properties):
    self.placeholder = ""
    self.init_components(**properties)

    self._window_size = {}
    self._menu_size = {}
    self._box_positioning = {}

    self._hoverIndex = None
    self._children = None
    self._selected_menuItem = None
    
    self.selected_value = None
    
    self._has_focus = False
    self.handle_keyboard_events = self.handle_keyboard_events
    self.handle_selection_field_focus = self.handle_selection_field_focus
    self.child_clicked = self.child_clicked
    self.handle_component_click = self.handle_component_click
    
    self.add_event_handler("x-anvil-page-added", self.on_mount)
    self.add_event_handler("x-anvil-page-removed", self.on_cleanup)
    
    self.selection_field.dom_nodes['text-field-input'].style.caretColor = 'transparent'
    self.selection_field.dom_nodes['text-field-input'].setAttribute("readonly", True)
          
    self.shield = document.createElement("div")
    self.shield.classList.toggle("anvil-m3-menu-clickShield", True)
 
    self.menuNode = self.dom_nodes['anvil-m3-dropdownMenu-items-container']
    if anvil.designer.in_designer: #hides so doesn't do the ghosty visible thing when in designer cuz i want it to just straight up not show cuz its nto like you can add stuffin anyways. 
      self.menuNode.classList.toggle("anvil-m3-menu-hidden", True)

  #properties
  visible = HtmlTemplate.visible
  align = style_property('anvil-m3-dropdownMenu-component', 'justifyContent')
  
  @property
  def enabled(self):
    return self._enabled
  @enabled.setter
  def enabled(self, value):
    self._enabled = value
    self.selection_field.enabled = value
    
  @property
  def appearance(self):
    return self._appearance
  @appearance.setter
  def appearance(self, value):
    self._appearance = value
    self.selection_field.appearance = value
    
  @property
  def items(self):
    return self._items
  @items.setter
  def items(self, value):
    self._items = value

  @property
  def label_text(self):
    return self._label_text
  @label_text.setter
  def label_text(self, value):
    self._label_text = value
    self.selection_field.label_text = value or ""
    
  @property
  def placeholder(self):
    return self._placeholder
  @placeholder.setter
  def placeholder(self, value):
    self._placeholder = value

  @property
  def selected_value(self):
     return self._selected_value
  @selected_value.setter
  def selected_value(self, value):
    self._selected_value = value
    if type(value) is list:
      self.selection_field.dom_nodes['text-field-input'].value = value[0]
    else:
      self.selection_field.dom_nodes['text-field-input'].value = value
    self.raise_event("change")
  
  @property
  def include_placeholder(self):
    return self._include_placeholder
  @include_placeholder.setter
  def include_placeholder(self, value):
    self._include_placeholder = value or ""
    
  def on_mount(self, **event_args):
    document.addEventListener('keydown', self.handle_keyboard_events)
    self.dom_nodes['anvil-m3-dropdownMenu-container'].addEventListener('click', self.handle_component_click)
    self.selection_field.dom_nodes['text-field-input'].addEventListener('focus', self.handle_selection_field_focus)
    self.selection_field.dom_nodes['text-field-input'].addEventListener('blur', self.handle_selection_field_blur)
    self.shield.addEventListener('click', self.remove_shield_handler)
    self.menuNode.addEventListener('click', self.child_clicked)
    
  def on_cleanup(self, **event_args):
    document.removeEventListener('keydown', self.handle_keyboard_events)
    self.dom_nodes['anvil-m3-dropdownMenu-container'].removeEventListener('click', self.handle_component_click)
    self.selection_field.dom_nodes['text-field-input'].removeEventListener('focus', self.handle_selection_field_focus)
    self.selection_field.dom_nodes['text-field-input'].removeEventListener('blur', self.handle_selection_field_blur)
    self.shield.removeEventListener('click', self.remove_shield_handler)
    self.menuNode.removeEventListener('click', self.child_clicked)

  def handle_selection_field_focus(self, event):
    self._has_focus = True
    
  def handle_selection_field_blur(self, event):
    self._has_focus = False
    
  def handle_keyboard_events(self, event):
    if not self._has_focus:
      return
    else:
      action_keys = set(["ArrowUp", "ArrowDown", "Tab", "Escape", " ", "Enter"])
      open_keys = set(["ArrowUp", "ArrowDown", " ", "Enter"])
      if not self.menu.visible:
        if event.key in open_keys:
          self.set_menu_visibility(True)          
        return
        
      if event.key not in action_keys: #   #TODO: eventually want to use this to jump somewhere in the list
        return
      
      if event.key is "ArrowUp" or event.key is "ArrowDown":
        self.iterate_hover(event.key is "ArrowDown")
        return
        
      if event.key is "Tab" or "Escape":
        self.closeMenu()
        
      hover = self._hoverIndex #holding value for situation like alerts where it awaits 
      
      def attemptSelect():
        # event.preventDefault();
        if not self._hoverIndex is None:
          self._children[self._hoverIndex].raise_event("click")
        self.closeMenu()
      
      if (event.key is " "): #space key as " " is stupid
        attemptSelect()
      if (event.key is "Enter"):
        attemptSelect()

  def closeMenu(self):
    self.remove_shield()
    self.set_menu_visibility(False)
    
  def iterate_hover(self, inc = True):
    if inc:
      if self._hoverIndex is None or self._hoverIndex is (len(self._children) - 1):
        self._hoverIndex = -1
      self._hoverIndex += 1
    else:
      if self._hoverIndex is None or self._hoverIndex is 0:
        self._hoverIndex = len(self._children)
      self._hoverIndex -= 1
    self.update_hover_styles();
    
  def clear_hover_styles(self):
    if self._children is not None:
      for child in self._children:
        if isinstance(child, MenuItem):
          child.dom_nodes['anvil-m3-menuItem-container'].classList.toggle('anvil-m3-menuItem-container-keyboardHover', False)

  def update_hover_styles(self):
    self.clear_hover_styles()
    if self._hoverIndex is None:
      return
    self._children[self._hoverIndex].dom_nodes['anvil-m3-menuItem-container'].classList.toggle('anvil-m3-menuItem-container-keyboardHover', True)
    
  def handle_component_click(self, event):
    self.set_menu_visibility()

  def set_menu_visibility(self, value = None):
    if (value is None):
      value = not self.menu.visible
    self.menu.visible = value
    if value:
      if not anvil.designer.in_designer:
        self.place_shield()
        self.selection_field.trailing_icon = "arrow_drop_up"
      self.get_textfield_measurements()
      self.update_menu_placement()
    else:
      self.selection_field.trailing_icon = "arrow_drop_down"
      self.menuNode.removeAttribute("style")
      if self.selected_value is None:
        self._hoverIndex = None

  def update_menu_placement(self):
    # menuNode = self.dom_nodes['anvil-m3-dropdownMenu-items-container']
    menuNode = self.menu.dom_nodes['anvil-m3-menu-items-container']
    self._window_size = {"width": window.innerWidth, "height": window.innerHeight}
    self._menu_size = {"width": menuNode.offsetWidth, "height": menuNode.offsetHeight}
    # horizontal placement
    menuLeft = self._box_positioning['left']
    menuRight = menuLeft + self._menu_size['width']
    if self._window_size['width'] < menuRight:
      menuNode.style.right = '5px'
    else:
      menuNode.style.left = f"{math.floor(menuLeft) + 5}px"
      
    # vertical placement
    menuTop = self._box_positioning['bottom']
    menuBottom = menuTop + self._menu_size['height']

    ## menu too tall!
    if (self._window_size['height'] - self._box_positioning['height']) < self._menu_size['height']: 
      spaceAtTop = self._box_positioning['top']
      spaceAtBottom = self._window_size['height'] - (spaceAtTop + self._box_positioning['height'])

      # put at the top and set container height
      if spaceAtTop > spaceAtBottom:
        menuNode.style.bottom = f"{math.floor(self._window_size['height'] - (self._box_positioning['top'] - 5))}px"
        menuNode.style.height = f"{math.floor(spaceAtTop - 7)}px"
        
      # put at the bottom and set container height
      else:
        menuNode.style.top = f"{math.floor(menuTop + 5)}px"
        menuNode.style.height = f"{math.floor(spaceAtBottom - 7)}px"

    ## menu fits
    else: 
      # default placement is out of bounds
      if self._window_size['height'] < menuBottom:
        menuNode.style.bottom = f"{math.floor(self._window_size['height'] - (self._box_positioning['top'] - 5))}px"
      # fits in default position
      else:
        menuNode.style.top = f"{math.floor(menuTop + 5)}px"
    
  def get_textfield_measurements(self):
    rect = self.selection_field.dom_nodes['text-field-input'].getBoundingClientRect()
    self._box_positioning = {
      "top": rect.top,
      "right": rect.right,
      "bottom": rect.bottom,
      "left": rect.left,
      "height": rect.bottom - rect.top,
      "width": rect.right - rect.left,
    }
  
  def place_shield(self):
    if not document.contains(self.shield):
      document.body.appendChild(self.shield)
      document.body.style.overflow = "hidden"
    
  def remove_shield_handler(self, event):
    self.closeMenu()
    
  def remove_shield(self):
    if document.contains(self.shield):
      document.body.removeChild(self.shield)
      document.body.style.removeProperty("overflow")

  def child_clicked(self, event):
    event.stopPropagation()
    self.closeMenu()
    if self.selected_value is None:
      self._hoverIndex = None
    else:
      self._hoverIndex = self._children.index(self._selected_menuItem)
    self.update_hover_styles()
      
  def form_show(self, **event_args):
    self.create_menu_items()
    self._children = self.menu.get_components()
    if anvil.designer.in_designer:
      if not self.label_text:
        self.label_text = anvil.designer.get_design_name(self)

  def create_menu_items(self):
    if self.include_placeholder:
      p = MenuItem()
      p.text = self.placeholder
      p.hide_leading_icon = True
      def handle_select_placeholder(**e):
        self.selected_value = None
        
      p.add_event_handler('click', handle_select_placeholder)
      self.menu.add_component(p, slot="anvil-m3-menu-slot")
      
    for item in self.items:
      selection = MenuItem()
      selection.hide_leading_icon = True
      if type(item) is list:
        selection.text = item[0]
      else:
        selection.text = item
        
      def handle_selection_click(value = item, menuItem = selection, **e): 
        self.selected_value = value
        self._selected_menuItem = menuItem
          
      selection.add_event_handler('click', handle_selection_click)
      self.menu.add_component(selection, slot="anvil-m3-menu-slot")

 
# DESIGNER INTERACTIONS
  def _anvil_get_design_info_(self, as_layout=False):
    design_info = super()._anvil_get_design_info_(as_layout)
    design_info["interactions"] = [
      # {
      #   "type": "designer_events",
      #   "callbacks": {
      #     "onSelectDescendent": self._on_select_descendent,
      #     "onSelectOther": self._on_select_other
      #   }
      # },
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
      "type": "whole_component",
      "title": "Edit Label",
      "icon": "edit",
      "default": True,
      "callbacks": {
        "execute": lambda: anvil.designer.start_inline_editing(self.selection_field, "label_text", self.selection_field.dom_nodes['label-text'])
      }
    }]
    return design_info

  # def _on_select_descendent(self):
  #   self.set_visibility(True)

  # def _on_select_other(self):
  #   self.set_visibility(False)

  def toggle_visible(self):
    self.visible = not self.visible
    anvil.designer.update_component_properties(self, {'visible': self.visible})

  def toggle_enabled(self):
    self.enabled = not self.enabled
    anvil.designer.update_component_properties(self, {'enabled': self.enabled})















