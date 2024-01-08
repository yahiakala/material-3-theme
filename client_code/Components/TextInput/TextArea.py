import anvil.server
from . import TextInput
import anvil.designer
from ...Functions import property_with_callback, theme_color_to_css

class TextArea(TextInput):
  def __init__(self, **properties):
    super().__init__(**properties)
    self.init_components(**properties)
    hiddenInput = self.dom_nodes['textfield']
    self.dom_nodes['input-container'].removeChild(hiddenInput)
    
    
    # todo: add id attribute to input 
    
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
    self.dom_nodes["textarea"].id = value
    self.dom_nodes["label-text"].setAttribute("for", value)
    self.dom_nodes["supporting-text"].setAttribute("for", value)
    self.dom_nodes["character-amount"].setAttribute("for", value)

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