from anvil import *

def m3_alert(title=None, content=None, buttons="OK", icon=None, dividers=False, centered=False):
  pass

def theme_color_to_css(color:str):
  if color.startswith('theme:'):
    color = color.strip('theme:')
    return app.theme_colors[color]
  else:
    return color