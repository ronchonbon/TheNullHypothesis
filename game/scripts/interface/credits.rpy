style message is default

style message_frame:
    background Frame("images/interface/box1.webp", 30, 30)

    minimum (100, 0)
    xmaximum 400

screen disclaimer():
    style_prefix "message"

    modal True

    add "images/interface/disclaimer.webp" align (0.5, 0.5)

    text "DISCLAIMER: This is a fictional {color=#ffb100}parody{/color} made for adults. All characters depicted are at least 18 years old. All game assets are either created by the Null Hypothesis team or authorized via creative commons license." anchor (0.5, 0.5) pos (0.5, 0.8):
        size 42

        color "#ffffff"

        xmaximum 1500

    frame anchor (0.5, 0.5) pos (0.5, 0.915):
        style_prefix "confirm"
        
        padding (15, 15, 15, 15)

        background None

        vbox:
            spacing 15

            text _("Are you at least 18 years old?"):
                size 40
                
                color "#ffffff"
                
            hbox:
                spacing 100

                textbutton _("Yes"): 
                    hover_sound None

                    action Return()

                    text_size 36

                textbutton _("No"): 
                    hover_sound None
                    
                    action Quit(confirm = False)

                    text_size 36
                    
screen credits():
    style_prefix "message"

    frame anchor (0.5, 0.5) pos (0.5, 0.2):
        background None

        padding (25, 25, 25, 25)

        text "This game would not exist if the creators had not played and been inspired by Oni's Rogue-Like: Evolution.":
            size 40

            color "#ffffff"

    frame anchor (0.5, 0.5) pos (0.5, 0.65) xysize (1000, 600):
        background None

        padding (25, 25, 25, 25)

        text "{color=#ffb100}Creative{/color}\n\nMaddening\nShiny Boots\nButtholder" anchor (0.5, 0.0) pos (0.15, 0.02):
            size 36

            color "#ffffff"

        text "{color=#ffb100}Writing{/color}\n\nMaddening\nButtholder" anchor (0.5, 0.0) pos (0.5, 0.02):
            size 36

            color "#ffffff"

        text "{color=#ffb100}Design{/color}\n\nNarukamiCharge\n\n" anchor (0.5, 0.0) pos (0.85, 0.02):
            size 36

            color "#ffffff"

        text "{color=#ffb100}Art{/color}\n\nAB\nL\nD" anchor (0.5, 0.0) pos (0.15, 0.6):
            size 36

            color "#ffffff"

        text "{color=#ffb100}Development{/color}\n\nRon Chon" anchor (0.5, 0.0) pos (0.5, 0.6):
            size 36

            color "#ffffff"

        text "{color=#ffb100}Music{/color}\n\nRoss Whitby" anchor (0.5, 0.0) pos (0.85, 0.6):
            size 36

            color "#ffffff"