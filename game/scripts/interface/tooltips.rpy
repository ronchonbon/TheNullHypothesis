screen tooltips():
    layer "interface"
    
    $ tooltip = GetTooltip()

    if tooltip:
        nearrect:
            # focus "tooltip"
            rect (get_mouse_position()[0], get_mouse_position()[1], 0, 0)

            prefer_top True

            frame anchor (0.5, 0.5):
                background Frame("images/interface/text_boxes/white.webp")

                text tooltip:
                    size 24

                    color "#000000"