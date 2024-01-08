import anvil.server
from . import TextInput
import anvil.designer
import anvil.js
from anvil.js.window import ResizeObserver
from ...Functions import property_with_callback, theme_color_to_css

class TextArea(TextInput):
  def __init__(self, **properties):
    super().__init__(**properties)
    self.init_components(**properties)
    hiddenInput = self.dom_nodes['textfield']
    self.dom_nodes['input-container'].removeChild(hiddenInput)

    self.update_height = self.update_height
    
    

    # now the the page is loaded, apply your resize observer
    
  def set_placeholder(self, value):
    input = self.dom_nodes['textarea']
    if value:
      input.placeholder = value
      input.classList.add('anvil-m3-has-placeholder')
    else:
      input.placeholder = " "
      input.classList.remove('anvil-m3-has-placeholder')
  placeholder = property_with_callback('placeholder', set_placeholder)

  def set_label(self, value):
      self.dom_nodes['label-text'].innerText = value or ""
      if value:
        self.dom_nodes['textarea'].classList.toggle('has_label_text', True)
      else:
        self.dom_nodes['textarea'].classList.toggle('has_label_text', anvil.designer.in_designer);
  label_text = property_with_callback("label_text", set_label)
  
  def set_enabled(self, value):
    supporting_text = self.dom_nodes['subcontent']
    if value:
      self.dom_nodes['textarea'].removeAttribute("disabled")
      supporting_text.classList.remove("anvil-m3-textinput-disabled")
    else:
      self.dom_nodes['textarea'].setAttribute("disabled", " ")
      supporting_text.classList.add("anvil-m3-textinput-disabled")
  enabled = property_with_callback("enabled", set_enabled)

  def set_id(self, value):
    super().set_id(value)
    self.dom_nodes["textarea"].id = value

  
  def update_height(self, entries, observer = None):
    for entry in entries:
      print(entry)
  resizeObserver = anvil.js.new(ResizeObserver, update_height)

    
  
  

  

"""

const h1Elem = document.querySelector("h1");
const pElem = document.querySelector("p");
const divElem = document.querySelector("body > div");
const slider = document.querySelector('input[type="range"]');
const checkbox = document.querySelector('input[type="checkbox"]');

divElem.style.width = "600px";

slider.addEventListener("input", () => {
  divElem.style.width = `${slider.value}px`;
});

const resizeObserver = new ResizeObserver((entry) => {
    if (entry.contentBoxSize) {
      const contentBoxSize = entry.contentBoxSize[0];
      h1Elem.style.fontSize = `${Math.max(
        1.5,
        contentBoxSize.inlineSize / 200,
      )}rem`;
      pElem.style.fontSize = `${Math.max(
        1,
        contentBoxSize.inlineSize / 600,
      )}rem`;
    } else {
      h1Elem.style.fontSize = `${Math.max(
        1.5,
        entry.contentRect.width / 200,
      )}rem`;
      pElem.style.fontSize = `${Math.max(1, entry.contentRect.width / 600)}rem`;
    }
  console.log("Size changed");
});

resizeObserver.observe(divElem);

checkbox.addEventListener("change", () => {
  if (checkbox.checked) {
    resizeObserver.observe(divElem);
  } else {
    resizeObserver.unobserve(divElem);
  }
});


self.handle_click = self.handle_click
    self.add_event_handler("x-anvil-page-added", self.on_mount)
    self.add_event_handler("x-anvil-page-removed", self.on_cleanup)

  def on_mount(self, **event_args):
    self.dom_nodes['anvil-m3-button'].addEventListener("click", self.handle_click)
  def on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-button'].removeEventListener("click", self.handle_click)
"""

"""
<script type="text/javascript">
        textarea = document.querySelector("#autoresizing");
        textarea.addEventListener('input', autoResize, false);
 
        function autoResize() {
            this.style.height = 'auto';
            this.style.height = this.scrollHeight + 'px';
        }
    </script>
"""