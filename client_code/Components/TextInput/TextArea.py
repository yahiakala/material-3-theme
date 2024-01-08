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
    # self.dom_nodes['textarea'].classList.remove('anvil-m3-hide-tag')
    
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