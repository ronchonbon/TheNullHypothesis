label Kurt_texting(message):
    if weekday == 6 and time_index == 0:
        $ Kurt.History.update("texted_Sunday_morning")

        if message == "how's it going?":
            $ Kurt.History.update("sent_how_are_you_text")

        return
    
    if message == "how's it going?":
        $ selected_Event = EventScheduler.choose_Event(texting = True)

        if selected_Event:
            call start_Event(selected_Event) from _call_start_Event_2
        else:
            if time_index == 3:
                if Kurt.History.check("said_too_late_to_text", tracker = "recent") == 1:
                    call Kurt_text_how_are_you_late_reject_asked_once from _call_Kurt_text_how_are_you_late_reject_asked_once
                elif Kurt.History.check("said_too_late_to_text", tracker = "recent") > 1:
                    call Kurt_text_how_are_you_late_reject_asked_twice from _call_Kurt_text_how_are_you_late_reject_asked_twice
                else:
                    call Kurt_text_how_are_you_late_reject from _call_Kurt_text_how_are_you_late_reject

                $ Kurt.History.update("said_too_late_to_text")
            else:
                call Kurt_text_how_are_you from _call_Kurt_text_how_are_you

        $ Kurt.History.update("sent_how_are_you_text")

    if message == "what the heck is a 'BAMF taxi'?":
        call Kurt_text_bamf_taxi from _call_Kurt_text_bamf_taxi

        $ Kurt.text_options.remove("what the heck is a 'BAMF taxi'?")

    if message == "got any tips about this damn phone?":
        call Kurt_text_phone_tips from _call_Kurt_text_phone_tips

    if message == "hey, about that comic book store in town":
        $ EventScheduler.Events["ch1_mutant_hate"].start()

    return

label Kurt_text_how_are_you:
    if chapter == 1 and season < 4:
        $ dice_roll = renpy.random.randint(1, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        call receive_text(Kurt, "Hello") from _call_receive_text_222
        call receive_text(Kurt, "Good") from _call_receive_text_223
        call receive_text(Kurt, "Made $75 today") from _call_receive_text_224
        call send_text(Kurt, "doing what???") from _call_send_text_13
        call receive_text(Kurt, ";)") from _call_receive_text_225
    elif dice_roll == 2:
        call receive_text(Kurt, "Ausreden finden, nicht zu lernen. Nicht, dass du das verstehen könntest") from _call_receive_text_226
        call send_text(Kurt, "english???") from _call_send_text_14
        call receive_text(Kurt, ">:)") from _call_receive_text_227
        call send_text(Kurt, ">:(") from _call_send_text_15
    elif dice_roll == 3:
        call receive_text(Kurt, "Been catching up with the comic") from _call_receive_text_228
        call receive_text(Kurt, "Good fun") from _call_receive_text_229
        call send_text(Kurt, "what comic?") from _call_send_text_16
        call receive_text(Kurt, "The one I helped with") from _call_receive_text_230
        call send_text(Kurt, "you helped make a comic???") from _call_send_text_17
        call receive_text(Kurt, ">:)") from _call_receive_text_231

    return

label Kurt_text_how_are_you_late_reject:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Kurt, "I go bed") from _call_receive_text_232
        call receive_text(Kurt, "Schlaf gut") from _call_receive_text_233
    elif dice_roll == 2:
        call receive_text(Kurt, "So sleepy") from _call_receive_text_49
    elif dice_roll == 3:
        call receive_text(Kurt, "Very tired")

    return

label Kurt_text_how_are_you_late_reject_asked_once:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Kurt, "Shush, go sleep") from _call_receive_text_234
    elif dice_roll == 2:
        call receive_text(Kurt, "Later!") from _call_receive_text_50
    elif dice_roll == 2:
        call receive_text(Kurt, "Talk later, it's time for bed")

    return

label Kurt_text_how_are_you_late_reject_asked_twice:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        call receive_text(Kurt, "Geh schlafen >:(") from _call_receive_text_235
    elif dice_roll == 2:
        call receive_text(Kurt, ". . .") from _call_receive_text_51
    elif dice_roll == 3:
        call receive_text(Kurt, "Gute Nacht!!!")

    return

label Kurt_text_bamf_taxi:
    call receive_text(Kurt, "I am zee bamf taxi >:)") from _call_receive_text_236
    call send_text(Kurt, "which is?") from _call_send_text_18
    call receive_text(Kurt, "Sometimes I 'port people around") from _call_receive_text_237
    call receive_text(Kurt, "For a fee of course") from _call_receive_text_238
    call send_text(Kurt, "naturally") from _call_send_text_19
    call send_text(Kurt, "and I get a friend's discount, right?") from _call_send_text_20
    call receive_text(Kurt, "Nein") from _call_receive_text_239
    call receive_text(Kurt, ">:)") from _call_receive_text_240
    call receive_text(Kurt, "Equality is important to zee taxi") from _call_receive_text_241

    return

label Kurt_text_phone_tips:
    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        call receive_text(Kurt, "I don't know why it gives you so much trouble") from _call_receive_text_242
        call receive_text(Kurt, "I know zere are some cool ringtones you can buy") from _call_receive_text_243
        call receive_text(Kurt, "Gotta unlock some of zem first") from _call_receive_text_244
        call send_text(Kurt, "how do I do that?") from _call_send_text_21
        call receive_text(Kurt, "Just progress zee story") from _call_receive_text_245
        call send_text(Kurt, "what story?") from _call_send_text_22
    elif dice_roll == 2:
        call receive_text(Kurt, "You can at least make zee phone look prettier") from _call_receive_text_246
        call receive_text(Kurt, "Can customize it in zee config app") from _call_receive_text_247
        call send_text(Kurt, "do I have to pay for that?") from _call_send_text_23
        call receive_text(Kurt, ">:)") from _call_receive_text_248
    elif dice_roll == 3:
        call receive_text(Kurt, "Having trouble again???") from _call_receive_text_249
        call receive_text(Kurt, "Don't worry about all zee fancy stuff") from _call_receive_text_250
        call receive_text(Kurt, "Just focus on your own progress") from _call_receive_text_251
        call receive_text(Kurt, "Can find zee updated info in the menu") from _call_receive_text_252
    elif dice_roll == 4:
        call receive_text(Kurt, "What? Trying to talk to a girl but can't find her?") from _call_receive_text_253
        call receive_text(Kurt, "Just look at zee damn map >:)") from _call_receive_text_255

    return