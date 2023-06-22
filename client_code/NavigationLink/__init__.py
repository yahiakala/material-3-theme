from ._anvil_designer import NavigationLinkTemplate
from anvil import *

class NavigationLink(NavigationLinkTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

      
  @property
  def url(self):
    return self._url

  @url.setter
  def url(self, value):
    self._url = value

  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    print('form show', self.url)
    self.call_js('setHref', self.url)


    
    
