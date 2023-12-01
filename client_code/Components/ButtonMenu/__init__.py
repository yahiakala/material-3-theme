from ._anvil_designer import ButtonMenuTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import HtmlTemplate
from anvil.js import window, get_dom_node
from anvil.js.window import document
import random, string, math
import anvil.designer
from ..Menu.MenuItem import MenuItem
from ...Functions import property_with_callback
from ...utils import fui, noop

class ButtonMenu(ButtonMenuTemplate):
  def __init__(self, **properties):
    self._props = properties
    self._design_name = ""
    self.init_components(**properties)
    self.open = False
    self._cleanup = noop

    self.hoverIndex = None
    self.itemIndices = set()
    self.children = None

    self.menuNode = self.dom_nodes['anvil-m3-buttonMenu-items-container']
    self.btnNode = get_dom_node(self.menu_button).firstElementChild

    self.add_event_handler("x-anvil-page-added", self.on_mount)
    self.add_event_handler("x-anvil-page-removed", self.on_cleanup)

  def on_mount(self, **event_args):
    document.addEventListener('keydown', self.handle_keyboard_events)
    self.menuNode.addEventListener('click', self.child_clicked)
    document.addEventListener('click', self.body_click)
    # this is a bit of a hack, we still have a reference to the dom node but we've moved it to the body
    # this gets around the whole, anvil containers love to set their overflow to hidden
    document.body.append(self.menuNode)

    self._cleanup = fui.auto_update(self.btnNode, self.menuNode)
  
  def on_cleanup(self, **event_args):
    document.removeEventListener('keydown', self.handle_keyboard_events)
    self.menuNode.removeEventListener('click', self.child_clicked)
    document.removeEventListener('click', self.body_click)
    self._cleanup()
    # remove the menu node we put on the body
    self.menuNode.remove()
  
  visible = HtmlTemplate.visible
  
  def set_text(self, value):
    v = value
    self.menu_button.dom_nodes['anvil-m3-button-text'].classList.toggle('anvil-m3-textlessComponentText', False)
    if anvil.designer.in_designer and not value:
      v = self._design_name
      self.menu_button.dom_nodes['anvil-m3-button-text'].classList.toggle('anvil-m3-textlessComponentText', True)
    self.menu_button.text = v
  text = property_with_callback("text", set_text)

  def set_appearance(self, value):
    self.menu_button.appearance = value
  appearance = property_with_callback("appearance", set_appearance)

  def set_enabled(self, value):
    self.menu_button.enabled = value
  enabled = property_with_callback("enabled", set_enabled)

  def toggle_menu_visibility(self, **event_args):
    self.set_visibility()

  def set_visibility(self, value = None):
    classes = self.menuNode.classList
    if value is not None:
      classes.toggle('anvil-m3-buttonMenu-items-hidden', not value)
    else:
      classes.toggle('anvil-m3-buttonMenu-items-hidden')
      
    self.open = not classes.contains('anvil-m3-buttonMenu-items-hidden')
    if self.open:
      self.get_hover_index_information()
    else:
      self.hoverIndex = None
      self.clear_hover_styles()

    
  def child_clicked(self, event):
    # do the click action. The child should handle this
    self.set_visibility(False)

  def body_click(self, event):
    if self.btnNode.contains(event.target) or self.menuNode.contains(event.target):
      return
    self.set_visibility(False)
  
  def get_hover_index_information(self):
    self.children = self.get_components()[1:]
    for i in range(0, len(self.children)):
      if isinstance(self.children[i], MenuItem):
        self.itemIndices.add(i)
   
  def handle_keyboard_events(self, event):
    if not self.open:
      return

    action_keys = set(["ArrowUp", "ArrowDown", "Tab", "Escape", " ", "Enter"])
    if event.key not in action_keys:
      #TODO: eventually want to use this to jump somewhere in the list
      return
    
    if event.key in ["ArrowUp", "ArrowDown"]:
      self.iterate_hover(event.key is "ArrowDown")
      return
      
    # if event.key is "Tab":
    #   pass
    hover = self.hoverIndex #holding value for situation like alerts where it awaits 
    self.set_visibility(False)
    
    def attemptSelect():
      event.preventDefault();
      if not hover is None:
        self.children[hover].raise_event("click")
    
    if (event.key is " "): #space key as " " is stupid
      attemptSelect()
    if (event.key is "Enter"):
      attemptSelect()
      
  def iterate_hover(self, inc = True):
    if inc:
      if self.hoverIndex is None or self.hoverIndex is (len(self.children) - 1):
        self.hoverIndex = -1
      while True:
        self.hoverIndex += 1
        if self.hoverIndex in self.itemIndices:
          break;
    else:
      if self.hoverIndex is None or self.hoverIndex is 0:
        self.hoverIndex = len(self.children)
      while True:
        self.hoverIndex -= 1
        if self.hoverIndex in self.itemIndices:
          break; 
    self.update_hover_styles();

  def clear_hover_styles(self):
    if self.children is not None:
      for child in self.children:
        if isinstance(child, MenuItem):
          child.dom_nodes['anvil-m3-menuItem-container'].classList.toggle('anvil-m3-menuItem-container-keyboardHover', False)

  def update_hover_styles(self):
    self.clear_hover_styles()
    self.children[self.hoverIndex].dom_nodes['anvil-m3-menuItem-container'].classList.toggle('anvil-m3-menuItem-container-keyboardHover', True)
    
  def _anvil_get_interactions_(self):
    return [
      {
        "type": "designer_events",
        "callbacks": {"onSelectDescendent": self._on_select_descendent, "onSelectOther": self._on_select_other},
      },
      {
        "type": "whole_component",
        "title": "Edit text",
        "icon": "edit",
        "default": True,
        "callbacks": {
          "execute": lambda: anvil.designer.start_inline_editing(
            self, "text", self.menu_button.dom_nodes["anvil-m3-button-text"]
          )
        },
      },
    ]

  def _on_select_descendent(self):
    self.set_visibility(True)

  def _on_select_other(self):
    self.set_visibility(False)

  def form_show(self, **event_args):
    if anvil.designer.in_designer:
      self._design_name = anvil.designer.get_design_name(self)
      if not self.text:
        self.menu_button.text = self._design_name
