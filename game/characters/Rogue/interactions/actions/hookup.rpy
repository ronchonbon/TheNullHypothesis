label Rogue_rejects_hookup:
    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue "Sorry, [Rogue.Player_petname]."

    if Rogue.History.check("hooked_up"):
        ch_Rogue "Not now."
    else:
        ch_Rogue "Ah'm just not ready to be intimate with you yet. . ."

    return

label Rogue_rejects_hookup_later:

    return

label Rogue_rejects_hookup_mad:
    $ Rogue.change_face("appalled2")

    pause 1.0

    $ Rogue.change_face("angry1")

    ch_Rogue "Ah think you should stop while yer ahead."

    $ Rogue.change_face("furious", eyes = "right")

    ch_Rogue "Ah reckon yer just tryin' to get a rise out of me."
    ch_Rogue "Cause if not, there's gotta be somethin' wrong with ya."

    return

label Rogue_rejects_hookup_public:
    $ Rogue.change_face("perplexed", blush = 1)

    pause 1.0

    $ Rogue.change_face("worried3", eyes = "right", blush = 1)

    ch_Rogue "Yer jokin' right, [Rogue.Player_petname]?"

    $ Rogue.change_face("confused1", eyes = "squint", blush = 1)

    ch_Rogue "Ain't no way we're foolin' around in a place like this."

    return

label Rogue_rejects_hookup_threesome:
    $ Rogue.change_face("perplexed", eyes = "right", blush = 1)

    python:
        for C in Present:
            if C in all_Companions and C != Rogue:
                C.change_face("suspicious1", blush = 1)

    pause 1.0

    $ Rogue.change_face("confused2", blush = 1)

    ch_Rogue "Ah know yer aware we're not alone. . ."

    call change_Character_stat(Rogue, "love", 0) from _call_change_Character_stat_684
    call change_Character_stat(Rogue, "trust", 0) from _call_change_Character_stat_685

    $ Rogue.change_face("suspicious1")

    ch_Rogue "Ah reckon you should reconsider what you were just fixin' to try."

    return

label Rogue_accepts_hookup_first_time:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Ah guess we can fool around. . ." 

    $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Rogue "Only a little bit though."

    return

label Rogue_accepts_hookup_second_time:

    return

label Rogue_accepts_hookup:
    if Rogue.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sexy", blush = 1)

        ch_Rogue "Ah could go for some foolin' around. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "Yer in the mood. . . ?" 

        $ Rogue.change_face("sexy", blush = 1)

        ch_Rogue "What do ya wanna do to me?"

    return

label Rogue_accepts_hookup_love:

    return

label Rogue_rejects_Action_asked_once:
    $ Rogue.change_face("angry1") 

    ch_Rogue "Ah already said no, stop askin'."

    return

label Rogue_rejects_Action_asked_twice:
    $ Rogue.change_face("furious") 

    ch_Rogue "That's it, you're done."

    if Player.location == Rogue.home:
        "She pushes you out of the room, locking the door behind you."
    else:
        "She storms out of the room."
        
    call getting_kicked_out(Rogue) from _call_getting_kicked_out_44

    return

label Rogue_accepts_Action_again:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "Want to go again. . . ?"

        $ Rogue.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Rogue "You know ah'm always down."
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

        ch_Rogue "Ah'm gonna get worn out. . ."

        $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1) 

        ch_Rogue "Not that ah'm complainin' or nothin'!"
    elif dice_roll == 3:
        $ Rogue.change_face("sexy", blush = 1)

        ch_Rogue "Wanna do it again?"

        $ Rogue.change_face("sexy", blush = 2)

        ch_Rogue "Won't have to convince me. . ."

    return

label Rogue_bored_by_Action(Action):

    return

label Rogue_not_warmed_up_for_Action(Action):

    return

label Rogue_hookup_summary(total_Character_orgasms, total_Player_orgasms, total_unique_Actions, score):

    return

label Rogue_weekly_summary(average_score):

    return