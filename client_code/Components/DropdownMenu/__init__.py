from ._anvil_designer import DropdownMenuTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import HtmlTemplate
from ...Functions import property_with_callback, property_without_callback, margin_property
from anvil.js import window, get_dom_node
from anvil.js.window import document
import random, string, math
import anvil.designer
from ..Menu.MenuItem import MenuItem
from ...utils import fui, noop

class DropdownMenu(DropdownMenuTemplate):
  def __init__(self, **properties):
    self._props = properties
    self._design_name = ""
    self.init_components(**properties)
    self._cleanup = noop

    self._menuNode = self.dom_nodes['anvil-m3-dropdownMenu-items-container']
    self._field = get_dom_node(self.selection_field).querySelector("input")

    self._hoverIndex = None
    self._children = None
    self._selected_menuItem = None

    self.selected_value = None

    self._has_focus = False
    self._handle_keyboard_events = self._handle_keyboard_events
    self._handle_selection_field_focus = self._handle_selection_field_focus
    self._child_clicked = self._child_clicked
    self._handle_component_click = self._handle_component_click

    self.add_event_handler("x-anvil-page-added", self._on_mount)
    self.add_event_handler("x-anvil-page-removed", self._on_cleanup)

    self.selection_field.dom_nodes['anvil-m3-textfield'].style.caretColor = 'transparent'
    self.selection_field.dom_nodes['anvil-m3-textfield'].style.cursor = "pointer"
    self.selection_field.dom_nodes['anvil-m3-textfield'].setAttribute("readonly", True)

    if not self.label_text and self.placeholder:
      self.selection_field.dom_nodes['anvil-m3-label-text'].innerText = self.placeholder

    if anvil.designer.in_designer: #hides so doesn't do the ghosty visible thing when in designer cuz i want it to just straight up not show cuz its nto like you can add stuffin anyways.
      self._menuNode.classList.toggle("anvil-m3-menu-hidden", True)

  #properties
  visible = HtmlTemplate.visible
  margin = margin_property('anvil-m3-dropdownMenu-textfield')

  def _set_background_color(self, value):
    self.selection_field.background_color = value
  background_color = property_with_callback("background_color", _set_background_color)

  def _set_bold_label(self, value):
    self.selection_field.bold_label = value
  bold_label = property_with_callback("bold_label", _set_bold_label)

  def _set_label_font(self, value):
    self.selection_field.label_font = value
  label_font = property_with_callback("label_font", _set_label_font)

  def _set_label_font_size(self, value):
    self.selection_field.label_font_size = value
  label_font_size = property_with_callback("label_font_size", _set_label_font_size)

  def _set_label_text_color(self, value):
    self.selection_field.label_text_color = value
  label_text_color = property_with_callback("label_text_color", _set_label_text_color)

  def _set_italic_label(self, value):
    self.selection_field.italic_label = value
  italic_label = property_with_callback("italic_label", _set_italic_label)

  def _set_underline_label(self, value):
    self.selection_field.underline_label = value
  underline_label = property_with_callback("underline_label", _set_underline_label)

  def _set_enabled(self, value):
    self.selection_field.enabled = value
  enabled = property_with_callback("enabled", _set_enabled)

  def _set_appearance(self, value):
    self.selection_field.appearance = value
  appearance = property_with_callback("appearance", _set_appearance)

  def _set_role(self, value):
    self.selection_field.role = value
  role = property_with_callback("role", _set_role)

  def _set_selected_italic_display(self, value):
    self.selection_field.selected_italic_display = value
  selected_italic_display = property_with_callback("selected_italic_display", _set_selected_italic_display)

  def _set_selected_bold_display(self, value):
    self.selection_field.selected_bold_display = value
  selected_bold_display = property_with_callback("selected_bold_display", _set_selected_bold_display)

  def _set_selected_underline_display(self, value):
    self.selection_field.selected_underline_display = value
  selected_underline_display = property_with_callback("selected_underline_display", _set_selected_underline_display)

  def _set_selected_font(self, value):
    self.selection_field.selected_font = value
  selected_font = property_with_callback("selected_font", _set_selected_font)

  def _set_selected_font_size(self, value):
    self.selection_field.selected_font_size = value
  selected_font_size = property_with_callback("selected_font_size", _set_selected_font_size)

  def _set_selected_text_color(self, value):
    self.selection_field.selected_text_color = value
  selected_text_color = property_with_callback("selected_text_color", _set_selected_text_color)

  def _set_label_text(self, value):
    v = value or ""
    self.selection_field.dom_nodes['anvil-m3-label-text'].classList.toggle('anvil-m3-textlessComponentText', False)
    if anvil.designer.in_designer and not value:
      v = self._design_name
      self.selection_field.dom_nodes['anvil-m3-label-text'].classList.toggle('anvil-m3-textlessComponentText', True)
    self.selection_field.label_text = v
  label_text = property_with_callback("label_text", _set_label_text)

  def _set_selected_value(self, value):
    if type(value) is list:
      self.selection_field.dom_nodes['anvil-m3-textfield'].value = value[0]
    else:
      self.selection_field.dom_nodes['anvil-m3-textfield'].value = value
    self.raise_event("change")
  selected_value = property_with_callback("selected_value", _set_selected_value)

  placeholder = property_without_callback("placeholder")
  items = property_without_callback("items")
  allow_none = property_without_callback("allow_none")
  bold_items = property_without_callback("bold_items")
  italic_items = property_without_callback("italic_items")
  underline_items = property_without_callback("underline_items")
  items_text_color = property_without_callback("items_text_color")
  items_background = property_without_callback("items_background")
  items_font = property_without_callback("items_font")
  items_font_size = property_without_callback("items_font_size")

  def _on_mount(self, **event_args):
    document.addEventListener('keydown', self._handle_keyboard_events)
    document.addEventListener('click', self._body_click)

    document.body.append(self._menuNode)

    self._cleanup = fui.auto_update(self._field, self._menuNode, placement="bottom-start")

    self.dom_nodes['anvil-m3-dropdownMenu-container'].addEventListener('click', self._handle_component_click)
    self.selection_field.dom_nodes['anvil-m3-textfield'].addEventListener('focus', self._handle_selection_field_focus)
    self.selection_field.dom_nodes['anvil-m3-textfield'].addEventListener('blur', self._handle_selection_field_blur)
    self._menuNode.addEventListener('click', self._child_clicked)

  def _on_cleanup(self, **event_args):
    document.removeEventListener('keydown', self._handle_keyboard_events)
    self.dom_nodes['anvil-m3-dropdownMenu-container'].removeEventListener('click', self._handle_component_click)
    self.selection_field.dom_nodes['anvil-m3-textfield'].removeEventListener('focus', self._handle_selection_field_focus)
    self.selection_field.dom_nodes['anvil-m3-textfield'].removeEventListener('blur', self._handle_selection_field_blur)
    self._menuNode.removeEventListener('click', self._child_clicked)
    self._cleanup()
    self._menuNode.remove()

  def _handle_selection_field_focus(self, event):
    self._has_focus = True

  def _handle_selection_field_blur(self, event):
    self._has_focus = False

  def _handle_keyboard_events(self, event):
    if not self._has_focus:
      return
    else:
      action_keys = set(["ArrowUp", "ArrowDown", "Tab", "Escape", " ", "Enter"])
      open_keys = set(["ArrowUp", "ArrowDown", " ", "Enter"])
      if not self.menu.visible:
        if event.key in open_keys:
          self._set_menu_visibility(True)
          event.preventDefault()
        return

      if event.key not in action_keys: #   #TODO: eventually want to use this to jump somewhere in the list
        return

      if event.key is "ArrowUp" or event.key is "ArrowDown":
        event.preventDefault()
        self._iterate_hover(event.key is "ArrowDown")
        return

      if event.key in ["Tab", "Escape"]:
        self._set_menu_visibility(False)

      if (event.key is " "): #space key as " " is stupid
        event.preventDefault()
        self._attempt_select()
      if (event.key is "Enter"):
        self._attempt_select()

  def _iterate_hover(self, inc = True):
    if inc:
      if self._hoverIndex is None or self._hoverIndex is (len(self._children) - 1):
        self._hoverIndex = -1
      self._hoverIndex += 1
    else:
      if self._hoverIndex is None or self._hoverIndex is 0:
        self._hoverIndex = len(self._children)
      self._hoverIndex -= 1
    self._update_hover_styles()

  def _attempt_select(self):
    if not self._hoverIndex is None:
      self._children[self._hoverIndex].raise_event("click")
    self._set_menu_visibility(False)

  def _clear_hover_styles(self):
    if self._children is not None:
      for child in self._children:
        if isinstance(child, MenuItem):
          child.dom_nodes['anvil-m3-menuItem-container'].classList.toggle('anvil-m3-menuItem-container-keyboardHover', False)

  def _update_hover_styles(self):
    self._clear_hover_styles()
    if self._hoverIndex is None:
      return
    self._children[self._hoverIndex].dom_nodes['anvil-m3-menuItem-container'].classList.toggle('anvil-m3-menuItem-container-keyboardHover', True)

  def _handle_component_click(self, event):
    self._set_menu_visibility()

  def _set_menu_visibility(self, value = None):
    if (value is None):
      value = not self.menu.visible
    self.menu.visible = value
    if value:
      if not self.label_text and self.placeholder:
        self.selection_field.dom_nodes['anvil-m3-label-text'].innerText = ""
      if not anvil.designer.in_designer:
        self.selection_field.trailing_icon = "arrow_drop_up"
    else:
      if not self.label_text and self.placeholder and self.selected_value is None:
        self.selection_field.dom_nodes['anvil-m3-label-text'].innerText = self.placeholder
      self.selection_field.trailing_icon = "arrow_drop_down"
      if self.selected_value is None:
        self._hoverIndex = None

  def _body_click(self, event):
    if self._field.contains(event.target) or self._menuNode.contains(event.target):
      return
    self._set_menu_visibility(False)

  def _child_clicked(self, event):
    event.stopPropagation()
    self._set_menu_visibility(False)
    if self.selected_value is None:
      self._hoverIndex = None
    else:
      self._hoverIndex = self._children.index(self._selected_menuItem)
    self._update_hover_styles()

  def form_show(self, **event_args):
    self._create_menu_items()
    self._children = self.menu.get_components()

    if anvil.designer.in_designer:
      self._design_name = anvil.designer.get_design_name(self)
      if not self.label_text:
        self.selection_field.dom_nodes['anvil-m3-label-text'].innerText = self._design_name

  def _create_menu_items(self):
    p = MenuItem()
    p.text = self.placeholder if self.placeholder else "Clear Selection"
    p.italic = self.italic_items
    p.underline = self.underline_items
    p.text_color = self.items_text_color
    p.background = self.items_background
    p.font = self.items_font
    p.font_size = self.items_font_size
    p.hide_leading_icon = True

    def _handle_select_placeholder(**e):
      if self.allow_none: self.selected_value = None

    if not self.allow_none:
      p.enabled = False

    if self.allow_none or self.placeholder:
      p.add_event_handler('click', _handle_select_placeholder)
      self.menu.add_component(p, slot="anvil-m3-menu-slot")

    for item in self.items:
      selection = MenuItem()
      selection.hide_leading_icon = True

      selection.bold = self.bold_items
      selection.italic = self.italic_items
      selection.underline = self.underline_items
      selection.text_color = self.items_text_color
      selection.background = self.items_background
      selection.font = self.items_font
      selection.font_size = self.items_font_size

      if type(item) is list:
        selection.text = item[0]
      else:
        selection.text = item

      def _handle_selection_click(value = item, menuItem = selection, **e):
        self.selected_value = value
        self._selected_menuItem = menuItem

      selection.add_event_handler('click', _handle_selection_click)
      self.menu.add_component(selection, slot="anvil-m3-menu-slot")

# DESIGNER INTERACTIONS
  def _anvil_get_interactions_(self):
    return [
      {
      "type": "whole_component",
      "title": "Edit Label",
      "icon": "edit",
      "default": True,
      "callbacks": {
        "execute": lambda: anvil.designer.start_inline_editing(self, "label_text", self.selection_field.dom_nodes['anvil-m3-label-text'])
      }
    }]
