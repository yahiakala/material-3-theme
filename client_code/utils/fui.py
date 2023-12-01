from anvil.js import import_from

fui = import_from("https://cdn.jsdelivr.net/npm/@floating-ui/dom@1.5.3/+esm")

def get_update(target, element, placement="bottom", strategy="absolute", offset=6, padding=5):
  def update(*args):
    rv = fui.computePosition(target, element, {
        'placement': placement,
        'strategy': strategy,
        'middleware': [
            fui.offset(offset),
            fui.flip(),
            fui.shift({'paddidng': padding}),
            # fui.arrow({'element': arrowElement}),
        ],
    })
    element.style.left = f"{rv.x}px"
    element.style.top = f"{rv.y}px"
  return update


autoUpdate = fui.autoUpdate
