from ._anvil_designer import AnotherPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class AnotherPage(AnotherPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Notification("This is a notification", timeout=None, title="Notification!", style="info").show()
    # Notification("This is a notification", timeout=None, title="Notification!", style="success").show()
    # Notification("This is a notification", timeout=None, title="Notification!", style="danger").show()
    # Notification("This is a notification", timeout=None, title="Notification!", style="warning").show()

