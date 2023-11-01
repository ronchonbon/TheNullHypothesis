init -2:

    define work_unit = 50

label work(Character):
    hide screen interactions_screen

    $ temp_dialogue_hidden = dialogue_hidden
    $ temp_phone_interactable = phone_interactable
    $ temp_choice_disabled = choice_disabled
    $ temp_Character_picker_disabled = Character_picker_disabled
    $ temp_belt_disabled = belt_disabled

    $ dialogue_hidden = False
    $ phone_interactable = False
    $ choice_disabled = False
    $ Character_picker_disabled = True
    $ belt_disabled = True

    if Character in [Charles] and Character.location != Player.location:
        $ Character.telepathic = True

        if Character.History.check("Player_contacted_telepathically"):
            ch_Player "Hey, [Character.name], any jobs for me today?"
        else:
            ch_Player "Uhm. . . testing, testing, one two three. . ."
            ch_Player "[Character.name]? Can you hear me?"

            pause 1.0

            ch_Charles "I can."
            ch_Charles "What can I do for you, [Player.first_name]?"
            ch_Player "!!!" with small_screenshake
            ch_Player "No way."
            ch_Player "I uh. . . are you just. . . always listening?"
            ch_Charles "It might be best not to think about it too much, [Player.first_name]."
            ch_Player "Okay. . ."
            ch_Player "Well. . ."
            ch_Player "I don't suppose you have any jobs for me today?"

            $ Character.History.update("Player_contacted_telepathically")
    else:
        ch_Player "Hey, [Character.name], any jobs for me today?"

    if time_index < 3:
        if Character.has_jobs:
            $ Character.has_jobs = False

            call expression f"{Character.tag}_ask_for_job" from _call_expression_371

            $ Character.electronic = False
            $ Character.telepathic = False

            $ Player.sweaty = True

            $ income = Player.level*int(work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15))

            $ Player.cash += income

            $ update_messages.append("{color=%s}%s{/color} gained {color=%s}$%s{/color}" % ("#feba00", Player.first_name, "#feba00", income))

            $ clock -= 1

            call set_the_scene(location = Player.home) from _call_set_the_scene_354
            call move_location(Player.home) from _call_move_location_53
        else:
            if Character.History.check("said_no_jobs", tracker = "recent") >= 2:
                call expression f"{Character.tag}_no_jobs_asked_twice" from _call_expression_372
            elif Character.History.check("said_no_jobs", tracker = "recent") == 1:
                call expression f"{Character.tag}_no_jobs_asked_once" from _call_expression_373
            else:
                call expression f"{Character.tag}_no_jobs" from _call_expression_374

            $ Character.History.update("said_no_jobs")
    else:
        if Character.History.check("said_too_late_to_work", tracker = "recent") >= 2:
            call expression f"{Character.tag}_too_late_to_work_asked_twice" from _call_expression_375
        elif Character.History.check("said_too_late_to_work", tracker = "recent") == 1:
            call expression f"{Character.tag}_too_late_to_work_asked_once" from _call_expression_376
        else:
            call expression f"{Character.tag}_too_late_to_work" from _call_expression_377

        $ Character.History.update("said_too_late_to_work")

    $ dialogue_hidden = temp_dialogue_hidden
    $ phone_interactable = temp_phone_interactable
    $ choice_disabled = temp_choice_disabled
    $ Character_picker_disabled = temp_Character_picker_disabled
    $ belt_disabled = temp_belt_disabled

    if Character.location == Player.location:
        show screen interactions_screen(Character)

    return