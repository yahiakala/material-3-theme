from ._anvil_designer import SliderTemplate
from anvil import *
from anvil.js.window import document, ResizeObserver
import anvil.js
from ...Functions import enabled_property

class Slider(SliderTemplate):
  def __init__(self, **properties):
    self._props = properties
    self.init_components(**properties)
    self.add_event_handler("x-anvil-page-added", self.on_mount)
    self.add_event_handler("x-anvil-page-removed", self.on_cleanup)
    
    self.label_container = document.createElement('div')
    self.label_container.classList.add('anvil-m3-slider-label-container')
    self.label = document.createElement('div')
    self.label.classList.add('anvil-m3-slider-label')
    self.label_container.appendChild(self.label)

  def on_mount(self, **event_args):
    self.dom_nodes["anvil-m3-slider-input"].addEventListener("input", self.on_input)
    self.dom_nodes["anvil-m3-slider-input"].addEventListener("mousedown", self.on_mouse_down)
    self.resize_observer = ResizeObserver(self.on_window_resize)
    self.resize_observer.observe(self.dom_nodes['anvil-m3-slider'])
  
  def on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-slider-input'].removeEventListener('input', self.on_input)
    self.dom_nodes['anvil-m3-slider-input'].removeEventListener('mousedown', self.on_mouse_down)
    self.resize_observer.unobserve(self.dom_nodes['anvil-m3-slider'])
    
  def on_input(self, event):
    self.update_progress()

  def on_mouse_down(self, event):
    self.do_show_label()
    document.addEventListener("mouseup", self.on_mouse_up)

  def on_mouse_up(self, event):
    self.do_hide_label()
    document.removeEventListener("mouseup", self.on_mouse_up)

  def on_window_resize(self, *args):
    self.dom_nodes['anvil-m3-slider-track-container'].style.width = self.get_track_width()
    
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
    if self.show_label:
      self.label_container.remove()
      document.body.appendChild(self.label_container)
      self.update_progress()

  def do_hide_label(self):
    self.label_container.remove()
    
  @property
  def show_label(self):
    return self._show_label

  @show_label.setter
  def show_label(self, value):
    self._show_label = value

  @property
  def enabled(self):
    return self._enabled

  @enabled.setter
  def enabled(self, value):
    self._enabled = value
    full_slider = self.dom_nodes['anvil-m3-slider']
    input = self.dom_nodes['anvil-m3-slider-input']
    if value:
      input.removeAttribute("disabled")
      full_slider.classList.remove("anvil-m3-slider-disabled")
    else:
      input.setAttribute("disabled", " ")
      full_slider.classList.add("anvil-m3-slider-disabled")


  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    self.dom_nodes['anvil-m3-slider-track-container'].style.width = self.get_track_width()




  