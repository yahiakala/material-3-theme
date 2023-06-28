from ._anvil_designer import StandardPageLayoutTemplate
from anvil import *

class StandardPageLayout(StandardPageLayoutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def navigation_link_2_click(self, **event_args):
    """This method is called when the component is clicked"""
    alert("clicked!")


