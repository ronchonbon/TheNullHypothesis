screen tooltips():
    layer "interface"
    
    $ tooltip = GetTooltip()

    if tooltip:
        nearrect:
            rect (get_mouse_position()[0], get_mouse_position()[1], 0, 0)

            prefer_top True

            frame:
                background Frame("images/interface/text_boxes/white.webp", 10, 10)

                text tooltip:
                    font "agency_fb.ttf"
                    
                    size 24

                    color "#000000"