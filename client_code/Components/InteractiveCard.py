import anvil.server
from .Card import Card
import anvil.designer
from ..Functions import property_with_callback

click_event = {"name": "click", "default_event": True, "description": "When the component is clicked"}
class InteractiveCard(Card):
  _anvil_events_ = [click_event, *Card._anvil_events_]
  def __init__(self, **properties):
    super().__init__(**properties)
    self.init_components(**properties)
    