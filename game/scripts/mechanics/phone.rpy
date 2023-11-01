label receive_call(Character, dialogue = None):
    play sound f"sounds/ringtones/{Player.ringtone}.ogg"

    call phone_buzz(times = 3) from _call_phone_buzz_9

    if dialogue:
        "[dialogue]"

    $ Character.electronic = True

    $ current_phone_Character = Character
    $ current_phone_screen = "call"

    $ phone_disabled = True

    show screen phone_screen()

    return

label make_call(Character):
    $ Character.electronic = True

    $ current_phone_Character = Character
    $ current_phone_screen = "call"

    $ phone_disabled = True

    show screen phone_screen()

    return

label end_call(Character):
    hide screen phone_screen

    $ current_phone_screen = "call_choice"

    $ phone_disabled = False

    $ Character.electronic = False

    return

label update_texts:
    $ unread_messages = {}

    python:
        for C in Contacts:
            for i in range(len(C.text_history)):
                Owner, content, status = C.text_history[i]

                if status == "unread":
                    unread_messages[C] = True
                elif status == "recently_read" and current_phone_Character != C:
                    C.text_history[i] = (Owner, content, "read")

    return

label read_texts(Character, override = False):
    if Character:
        python:
            for i in range(len(Character.text_history)):
                Owner, content, status = Character.text_history[i]

                if (status == "recently_read" and current_phone_Character != Character) or override:
                    Character.text_history[i] = (Owner, content, "read")

        call update_texts from _call_update_texts

    return

label send_text(Character, message, delay = 2.0):
    $ phone_disabled = True

    $ Character.mandatory_text_options = []

    $ Character.text_history.append((Player, message, "current"))

    play sound "sounds/interface/message.ogg"
    
    pause delay

    $ Character.text_history[-1] = (Player, message, "recently_read")

    if not ongoing_Event:
        call expression f"{Character.tag}_texting" pass (message) from _call_expression_379

    $ Character.History.update("texted_with_Player")
    
    $ phone_disabled = False
    
    return

label receive_text(Character, message, buzz = True, delay = 2.0):
    $ phone_disabled = True

    if renpy.get_screen("phone_screen") and current_phone_screen == "text" and Character == current_phone_Character:
        $ Character.text_history.append((Character, message, "current"))

        play sound "sounds/interface/message.ogg"

        pause delay

        $ Character.text_history[-1] = (Character, message, "recently_read")

        call read_texts(Character) from _call_read_texts
    else:
        if buzz:
            call phone_buzz from _call_phone_buzz_10

        $ Character.text_history.append((Character, message, "unread"))
    
        call update_texts from _call_update_texts_1

    $ Character.History.update("texted_with_Player")

    $ phone_disabled = False

    return

label open_texts(Character):
    pause 1.0

    $ phone_interactable = False

    $ current_phone_Character = Character
    $ current_phone_screen = "text"

    show screen phone_screen()

    call read_texts(Character) from _call_read_texts_1

    pause 2.0

    return