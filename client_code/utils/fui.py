from anvil.js import import_from

# https://floating-ui.com/
fui = import_from("https://cdn.jsdelivr.net/npm/@floating-ui/dom@1.5.3/+esm")

def auto_update(
  reference_el,
  floating_el,
  *,
  placement="bottom",
  strategy="absolute",
  offset=6,
  shift={"paddidng": 5},
  hide={"padding": 15},
):
  """starts auto updating position of floating element to a reference element
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
        fui.shift(shift),
        fui.hide(hide)
      ],
    })
    floating_el.style.left = f"{rv.x}px"
    floating_el.style.top = f"{rv.y}px"

    middlewareData = rv.middlewareData
    if "hide" in middlewareData:
      hidden = middlewareData.hide.referenceHidden
      floating_el.style.visibility = "hidden" if hidden else "visible"


  return fui.autoUpdate(reference_el, floating_el, update)
