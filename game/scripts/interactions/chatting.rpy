label chat(Character):
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

    if renpy.get_screen("phone_screen"):
        $ counter = 0

        $ number_of_rings = renpy.random.randint(1, 4)

        while counter < number_of_rings:
            if counter == 0:
                "."
            elif counter == 1:
                ". ."
            elif counter == 2:
                ". . ."
            elif counter == 3:
                ". . . ."
            elif counter == 4:
                ". . . . ."

            $ counter += 1

        call expression f"{Character.tag}_answering_phone" from _call_expression_123

        ch_Player "Hey, [Character.name], how's it going?"

        if time_index == 3 and not approval_check(Character, threshold = "talk_late"):
            if Character.History.check("said_too_late_to_talk", tracker = "recent") >= 2:
                if Character in all_Girls:
                    call change_Girl_stat(Character, "love", -5) from _call_change_Girl_stat_1091
                    call change_Girl_stat(Character, "trust", -5) from _call_change_Girl_stat_1092
                
                call expression f"{Character.tag}_busy_late_asked_twice" from _call_expression_125
            elif Character.History.check("said_too_late_to_talk", tracker = "recent") == 1:
                if Character in all_Girls:
                    call change_Girl_stat(Character, "love", -2) from _call_change_Girl_stat_1093

                call expression f"{Character.tag}_busy_late_asked_once" from _call_expression_126
            else:
                call expression f"{Character.tag}_busy_late" from _call_expression_127

            $ Character.History.update("said_too_late_to_talk")

            $ dialogue_hidden = temp_dialogue_hidden
            $ phone_interactable = temp_phone_interactable
            $ choice_disabled = temp_choice_disabled
            $ Character_picker_disabled = temp_Character_picker_disabled
            $ belt_disabled = temp_belt_disabled

            if current_phone_screen == "call":
                $ Character.electronic = False

                $ current_phone_screen = "call_choice"

            return

    $ chatting = True

    while chatting:        
        if Character in all_Girls:
            $ status = Character.get_status()
        else:
            $ status = None

        menu:
            "[Character.chat_options[0]]" if len(Character.chat_options) >= 1 and not status:
                call expression f"{Character.tag}_chatting" pass (Character.chat_options[0]) from _call_expression_116
            "[Character.chat_options[0]] (locked)" if len(Character.chat_options) >= 1 and status:
                pass
            "[Character.chat_options[1]]" if len(Character.chat_options) >= 2 and not status:
                call expression f"{Character.tag}_chatting" pass (Character.chat_options[1]) from _call_expression_117
            "[Character.chat_options[1]] (locked)" if len(Character.chat_options) >= 2 and status:
                pass
            "[Character.chat_options[2]]" if len(Character.chat_options) >= 3 and not status:
                call expression f"{Character.tag}_chatting" pass (Character.chat_options[2]) from _call_expression_118
            "[Character.chat_options[2]] (locked)" if len(Character.chat_options) >= 3 and status:
                pass
            "[Character.chat_options[3]]" if len(Character.chat_options) >= 4 and not status:
                call expression f"{Character.tag}_chatting" pass (Character.chat_options[3]) from _call_expression_119
            "[Character.chat_options[3]] (locked)" if len(Character.chat_options) >= 4 and status:
                pass
            "[Character.chat_options[4]]" if len(Character.chat_options) >= 5 and not status:
                call expression f"{Character.tag}_chatting" pass (Character.chat_options[4]) from _call_expression_120
            "[Character.chat_options[4]] (locked)" if len(Character.chat_options) >= 5 and status:
                pass
            "Tell her you would like to date. . ." if not status and Character in Partners and Character.History.check("told_wants_multiple_partners"):
                menu:
                    "Tell her you would like to date. . ."
                    "[Rogue.name]" if Character != Rogue and Rogue not in Character.knows_about:
                        $ EventScheduler.Events[f"{Character.tag}_disclosing_wants_to_date_Rogue"].start()
                    "[Laura.name]" if Character != Laura and Laura not in Character.knows_about:
                        $ EventScheduler.Events[f"{Character.tag}_disclosing_wants_to_date_Laura"].start()
                    "[Jean.name]" if Character != Jean and Jean not in Character.knows_about:
                        $ EventScheduler.Events[f"{Character.tag}_disclosing_wants_to_date_Jean"].start()
                    "Back":
                        pass
            "Tell her you would like to date. . . (locked)" if status and Character in Partners and Character.History.check("told_wants_multiple_partners"):
                pass
            "Tell her you would like to date other people" if not status and Character in Partners and not Character.History.check("told_wants_multiple_partners"):
                $ EventScheduler.Events[f"{Character.tag}_disclosing_wants_to_date_others"].start()
            "Tell her you would like to date other people (locked)" if status and Character in Partners and not Character.History.check("told_wants_multiple_partners"):
                pass
            "Ask her to change her pubic hair" if not status and Character.History.check("seen_pussy") and not Character.customizable_pubes:
                call expression f"{Character.tag}_pubic_hair_discussion" from _call_expression_121
            "Ask her to change her pubic hair (locked)" if status and Character.History.check("seen_pussy") and not Character.customizable_pubes:
                pass
            "Ask on date" if Character in all_Girls and Player.cash >= 40 and not Player.date_planned and 2 not in Player.schedule.keys() and 3 not in Player.schedule.keys() and time_index < 3 and not Character.History.check("said_no_to_date", tracker = "daily") and Character.History.check("went_on_date_with_Player"):
                call expression f"{Character.tag}_ask_on_date" from _call_expression_122
            "Ask on date (locked)" if Character in all_Girls and Character.History.check("went_on_date_with_Player") and (Player.cash < 40 or Player.date_planned or 2 in Player.schedule.keys() or 3 in Player.schedule.keys() or time_index > 2 or Character.History.check("said_no_to_date", tracker = "daily")):
                pass
            "Flirt" if Character in all_Girls and not Character.History.check("flirted_with", tracker = "daily"):
                call flirt(Character) from _call_flirt
            # "How's it going?":
            #     $ selected_Event = EventScheduler.choose_Event(chatting = True)

            #     if selected_Event:
            #         call start_Event(selected_Event) from _call_start_Event_7
            #     else:
            #         if Character in all_Girls:
            #             if time_index == 3 and not approval_check(Character, threshold = "talk_late"):
        #                     if Character.History.check("said_too_late_to_talk", tracker = "recent") >= 2:
        #                         if Character in all_Girls:
        #                             call change_Girl_stat(Character, "love", -5) from _call_change_Girl_stat_931
        #                             call change_Girl_stat(Character, "trust", -5) from _call_change_Girl_stat_932
                                
        #                         call expression f"{Character.tag}_busy_late_asked_twice" from _call_expression_124
        #                     elif Character.History.check("said_too_late_to_talk", tracker = "recent") == 1:
        #                         if Character in all_Girls:
        #                             call change_Girl_stat(Character, "love", -2) from _call_change_Girl_stat_933

        #                         call expression f"{Character.tag}_busy_late_asked_once" from _call_expression_125
        #                     else:
        #                         call expression f"{Character.tag}_busy_late" from _call_expression_126

            #                 $ Character.History.update("said_too_late_to_talk")
            #             else:
            #                 $ status = Character.get_status()

            #                 if status:
            #                     call expression f"{Character.tag}_busy_{status}" from _call_expression_127
            #                 elif approval_check(Character, threshold = "love"):
            #                     call expression f"{Character.tag}_busy_love" from _call_expression_128
            #                 elif Character in Partners:
            #                     call expression f"{Character.tag}_busy_relationship" from _call_expression_129
            #                 else:
        #                         if Character.History.check("asked_how_are_you", tracker = "recent") >= 2:
        #                             if Character in all_Girls:
        #                                 call change_Girl_stat(Character, "love", -5) from _call_change_Girl_stat_934
        #                                 call change_Girl_stat(Character, "trust", -5) from _call_change_Girl_stat_935
                                    
        #                             call expression f"{Character.tag}_busy_asked_twice" from _call_expression_131
        #                         elif Character.History.check("asked_how_are_you", tracker = "recent") == 1:
        #                             if Character in all_Girls:
        #                                 call change_Girl_stat(Character, "love", -2) from _call_change_Girl_stat_936

        #                             call expression f"{Character.tag}_busy_asked_once" from _call_expression_132
        #                         else:
        #                             call expression f"{Character.tag}_busy" from _call_expression_133
            #         else:
            #             if time_index == 3:
            #                 if Character.History.check("said_too_late_to_talk", tracker = "recent") >= 2:
            #                     if Character in all_Girls:
            #                         call change_Girl_stat(Character, "love", -5) from _call_change_Girl_stat_937
            #                         call change_Girl_stat(Character, "trust", -5) from _call_change_Girl_stat_938

            #                     call expression f"{Character.tag}_busy_late_asked_twice" from _call_expression_134
            #                 elif Character.History.check("said_too_late_to_talk", tracker = "recent") == 1:
            #                     if Character in all_Girls:
            #                         call change_Girl_stat(Character, "love", -2) from _call_change_Girl_stat_939

            #                     call expression f"{Character.tag}_busy_late_asked_once" from _call_expression_135
            #                 else:
            #                     call expression f"{Character.tag}_busy_late" from _call_expression_136

            #                 $ Character.History.update("said_too_late_to_talk")
            #             else:
            #                 if Character.History.check("asked_how_are_you", tracker = "recent") >= 2:
            #                     if Character in all_Girls:
            #                         call change_Girl_stat(Character, "love", -5) from _call_change_Girl_stat_940
            #                         call change_Girl_stat(Character, "trust", -5) from _call_change_Girl_stat_941

            #                     call expression f"{Character.tag}_busy_asked_twice" from _call_expression_137
            #                 elif Character.History.check("asked_how_are_you", tracker = "recent") == 1:
            #                     if Character in all_Girls:
            #                         call change_Girl_stat(Character, "love", -2) from _call_change_Girl_stat_942
                                
            #                     call expression f"{Character.tag}_busy_asked_once" from _call_expression_138
            #                 else:
            #                     call expression f"{Character.tag}_busy" from _call_expression_139

            #         $ Character.History.update("asked_how_are_you")
            "What do you think about. . . ?" if not status and Character in all_Girls:
                menu:
                    "What do you think about. . . ?"
                    "[Rogue.name]?" if Character != Rogue and Rogue.History.check("met"):
                        call expression f"{Character.tag}_ask_about_Rogue" from _call_expression_140
                    "[Laura.name]?" if Character != Laura and Laura.History.check("met"):
                        call expression f"{Character.tag}_ask_about_Laura" from _call_expression_141
                    "[Jean.name]?" if Character != Jean and Jean.History.check("met"):
                        call expression f"{Character.tag}_ask_about_Jean" from _call_expression_142
                    "Never mind.":
                        pass
            "What do you think about. . . ? (locked)" if status and Character in all_Girls:
                pass
            "Dismiss" if Character.location == Player.location and (Character in all_Girls or Character == Kurt):
                call dismiss(Character) from _call_dismiss
            "Talk to you later.":
                if Character in all_Girls:
                    if status:
                        call expression f"{Character.tag}_talk_later_{status}" from _call_expression_143
                    elif approval_check(Character, threshold = "love"):
                        call expression f"{Character.tag}_talk_later_love" from _call_expression_144
                    elif Character in Partners:
                        call expression f"{Character.tag}_talk_later_relationship" from _call_expression_145
                    else:
                        call expression f"{Character.tag}_talk_later" from _call_expression_146
                else:
                    call expression f"{Character.tag}_talk_later" from _call_expression_147

                $ chatting = False

    $ dialogue_hidden = temp_dialogue_hidden
    $ phone_interactable = temp_phone_interactable
    $ choice_disabled = temp_choice_disabled
    $ Character_picker_disabled = temp_Character_picker_disabled
    $ belt_disabled = temp_belt_disabled

    if current_phone_screen == "call":
        $ Character.electronic = False

        $ current_phone_screen = "call_choice"

    $ Character.History.update("talked_with_Player")

    if Character.location == Player.location:
        show screen interactions_screen(Character)

    return