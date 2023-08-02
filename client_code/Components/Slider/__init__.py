from ._anvil_designer import SliderTemplate
from anvil import *
from anvil.js.window import document
import anvil.js

class Slider(SliderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.dom_nodes["anvil-m3-slider-input"].addEventListener("input", self.on_input)
    self.dom_nodes["anvil-m3-slider-input"].addEventListener("mousedown", self.on_mouse_down)
    
    self.label_container = document.createElement('div')
    self.label_container.classList.add('anvil-m3-slider-label-container')
    self.label = document.createElement('div')
    self.label.classList.add('anvil-m3-slider-label')
    self.label_container.appendChild(self.label)


    # Any code you write here will run before the form opens.
  def on_input(self, event):
    self.update_progress()

  def on_mouse_down(self, event):
    self.do_show_label()
    document.addEventListener("mouseup", self.on_mouse_up)

  def on_mouse_up(self, event):
    self.do_hide_label()
    document.removeEventListener("mouseup", self.on_mouse_up)
    
  def update_progress(self):
    slider = self.dom_nodes["anvil-m3-slider-input"]
    progress = self.dom_nodes["anvil-m3-slider-progress"]
    range = float(slider.max) - float(slider.min)
    abs_value = float(slider.value) - float(slider.min)
    percent = (abs_value / range) * 100;
    progress.style.width = str(percent) + "%"
    progress_right, progress_top = self.check_position()
    self.label.textContent = slider.value
    self.label_container.style.left = str(progress_right) + "px"
    self.label_container.style.top = str(progress_top) + "px"

  def get_track_width(self):
    input = self.dom_nodes["anvil-m3-slider-input"]
    input_width = input.getBoundingClientRect().width
    return str(input_width - 20) + "px"

  def check_position(self):
    progress_rect = self.dom_nodes["anvil-m3-slider-progress"].getBoundingClientRect()
    progress_right = progress_rect.right
    progress_top = progress_rect.top
    return progress_right, progress_top

  def do_show_label(self):
    if self.has_label:
      self.label_container.remove()
      document.body.appendChild(self.label_container)

  def do_hide_label(self):
    self.label_container.remove()
    
  # TODO: rename to show_label
  @property
  def has_label(self):
    return self._has_label

  @has_label.setter
  def has_label(self, value):
    self._has_label = value

  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    self.dom_nodes['anvil-m3-slider-track-container'].style.width = self.get_track_width()



  