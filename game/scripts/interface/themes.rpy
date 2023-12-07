init -1 python hide:
    
    theme.tv(
        widget = "#6a7183",
        widget_hover = "#1a2b47",
        widget_text = "#ffffff",
        widget_selected = "e3e3e4",
        disabled = "#4448",
        disabled_text = "#4448",
        
        rounded_window = False)

style default:
    font "agency_fb_bold.ttf"

style fixed:
    align (0.5, 0.5)

style frame:
    align (0.5, 0.5)

    background None

style hbox:
    align (0.5, 0.5)

style vbox:
    align (0.5, 0.5)

style button:
    align (0.5, 0.5)

    # hover_sound "sounds/interface/hover.ogg"
    activate_sound "sounds/interface/press.ogg"

style image_button:
    align (0.5, 0.5)

    # hover_sound "sounds/interface/hover.ogg"
    activate_sound "sounds/interface/press.ogg"

    focus_mask True

style text:
    align (0.5, 0.5)

    text_align 0.5
    
    color "#ffffff"