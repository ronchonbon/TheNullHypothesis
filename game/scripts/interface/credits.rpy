style message is default

style message_frame:
    minimum (100, 0)
    xmaximum 400

style message_text:
    font "agency_fb.ttf"

    size 36

screen disclaimer():
    modal True

    style_prefix "message"

    add "images/interface/disclaimer.webp"

    text "DISCLAIMER: This is a fictional {color=#ffb100}parody{/color} made for adults. All characters depicted are at least 18 years old. All game assets are either created by the Null Hypothesis team or authorized via creative commons license." anchor (0.5, 0.5) pos (0.5, 0.8):
        xmaximum 1500

        size 42

    frame anchor (0.5, 0.5) pos (0.5, 0.915):
        style_prefix "confirm"

        background None

        vbox:
            spacing 10

            text _("Are you at least 18 years old?"):
                font "agency_fb.ttf"
                
                size 40
                
            hbox:
                spacing 100

                textbutton _("YES"):
                    text_size 36

                    text_color "#ffffff"

                    action Return()

                textbutton _("NO"):
                    text_size 36

                    text_color "#ffffff"

                    action Quit()
                    
screen credits():
    style_prefix "message"

    frame anchor (0.5, 0.5) pos (0.5, 0.2):
        text "This game would not exist if the creators had not played and been inspired by Oni's Rogue-Like: Evolution.":
            size 40

    frame anchor (0.5, 0.5) pos (0.5, 0.65) xysize (0.5, 0.5):
        text "{color=#ffb100}Creative{/color}\n\nMaddening\nShiny Boots\nButtholder" anchor (0.5, 0.0) pos (0.15, 0.02)
        
        text "{color=#ffb100}Writing{/color}\n\nMaddening\nButtholder" anchor (0.5, 0.0) pos (0.5, 0.02)

        text "{color=#ffb100}Design{/color}\n\nNarukamiCharge\n\n" anchor (0.5, 0.0) pos (0.85, 0.02)
        
        text "{color=#ffb100}Art{/color}\n\nAB\nL\nD" anchor (0.5, 0.0) pos (0.15, 0.6)

        text "{color=#ffb100}Development{/color}\n\nRon Chon" anchor (0.5, 0.0) pos (0.5, 0.6)

        text "{color=#ffb100}Music{/color}\n\nRoss Whitby" anchor (0.5, 0.0) pos (0.85, 0.6)