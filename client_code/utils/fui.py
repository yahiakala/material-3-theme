from anvil.js import import_from

# https://floating-ui.com/
fui = import_from("https://cdn.jsdelivr.net/npm/@floating-ui/dom@1.5.3/+esm")

def auto_update(reference_el, floating_el, *, placement="bottom", strategy="absolute", offset=6, padding=5):
  """starts auto updating position of element to target
  returns a cleanup function
  call this function in x-anvil-page-added
  call the cleanup in x-anvil-page-removed"""

  def update(*args):
    rv = fui.computePosition(reference_el, floating_el, {
      'placement': placement,
      'strategy': strategy,
      'middleware': [
        fui.offset(offset),
        fui.flip(),
        fui.shift({'paddidng': padding}),
        # fui.arrow({'element': arrowElement}),
      ],
    })
    floating_el.style.left = f"{rv.x}px"
    floating_el.style.top = f"{rv.y}px"

  return fui.autoUpdate(reference_el, floating_el, update)
