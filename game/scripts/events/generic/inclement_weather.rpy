init python:

    def inclement_weather():
        label = "inclement_weather"

        conditions = [
            "False"]

        waiting = True
        repeatable = True

        return EventClass(label, conditions, waiting = waiting, repeatable = repeatable)

label inclement_weather:
    if weather == "rain":
        "Without warning, the skies open up."

        menu:
            extend ""
            "Run inside":
                if Present:
                    if len(Present) == 1:
                        "You and [Present[0].name] rush inside before you get completely drenched."
                    else:
                        "You and the others rush inside before you get completely drenched."

                    $ temp_running_Characters = Present[:]

                    call send_Characters(temp_running_Characters, location = "bg_hallway") from _call_send_Characters_225
                    call set_the_scene(location = "bg_hallway") from _call_set_the_scene_286
            "Stay outside":
                if Present and renpy.random.random() > 0.5:
                    if len(Present) == 1:
                        "[Present[0].name] rushes inside."
                    else:
                        "The others rush inside."

                    $ temp_running_Characters = Present[:]

                    call send_Characters(temp_running_Characters, location = "bg_hallway") from _call_send_Characters_226
    elif weather == "snow":
        "It starts to snow!"

    # if Player.location not in ["bg_campus", "bg_pool"]:
    #     call move_location(Player.location) from _call_move_location_39

    return