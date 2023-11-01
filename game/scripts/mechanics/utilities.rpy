init python:
     
    def get_Present(location = None):
        global all_Characters
        global all_Girls

        global Player

        global Party
        
        global focused_Girl

        Present = Party[:] if Party else []

        location = Player.location if not location else location

        for C in all_Characters:
            if C not in Party:
                if C not in Present and C.location == location:
                    Present.append(C)
                elif C in Present and C.location != location:
                    Present.remove(C)
                    
        if focused_Girl not in Present:
            randomized_present_Girls = []

            for C in Present:
                if C in all_Girls:
                    randomized_present_Girls.append(C)

            if randomized_present_Girls:
                focused_Girl = renpy.random.choice(randomized_present_Girls)
                        
        return Present

label reset_all_interfaces:
    call stop_all_Actions(automatic = True) from _call_stop_all_Actions_6
    call closing_Action_interface from _call_closing_Action_interface_6

    hide screen Wardrobe_screen
    hide screen phone_screen
    hide screen interactions_screen
    show screen belt_screen()

    $ current_phone_screen = "home"

    if current_phone_Character:
        $ current_phone_Character.electronic = False
        $ current_phone_Character = None

    $ ongoing_Event = False
    $ phone_interactable = True
    $ choice_disabled = False
    $ Character_picker_active = True
    $ Character_picker_disabled = False
    $ belt_hidden = False
    $ belt_disabled = False

    return