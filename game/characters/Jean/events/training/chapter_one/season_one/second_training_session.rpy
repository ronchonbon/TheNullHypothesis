init python:

    def Jean_chapter_one_season_one_second_training_session():
        label = "Jean_chapter_one_season_one_second_training_session"

        conditions = [
            "season == 1",
            "Jean.History.check('trained_with_Player', tracker = 'season') == 1",
            "Player.training == Jean and Jean.training"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Jean_chapter_one_season_one_second_training_session:
    $ ongoing_Event = True

    $ Jean.change_face("smirk2")

    ch_Jean "Ready?"
    ch_Jean "Let's get warmed up."

    $ fade_to_black(0.4)

    "You both go through a series of mobility exercises to get ready for the session."

    $ fade_in_from_black(0.4)

    $ Jean.change_face("neutral")

    ch_Player "I was hoping we could work more on control today." 
    ch_Player "I can reliably feel whenever my power reacts to something."

    $ Jean.change_face("smirk1")

    ch_Player "But I still can't control that reaction at all." 

    $ Jean.change_face("sly")

    ch_Jean "That's what I was thinking." 
    ch_Jean "Usually I'm the mind reader."

    $ Jean.change_face("smirk2")

    call Jean_activate_psychic from _call_Jean_activate_psychic_9

    "Jean starts with tennis balls again today, at least this time she's not trying to kill you with them."
    "She slowly guides them to the edge of your nullification range."
    "You're prepared, and you try reigning in your power to actually let the tennis ball touch you."
    ". . ."

    $ Jean.change_face("worried1")

    "The tennis ball hits the floor."
    "After probably 50 failures, something finally changes when you close your eyes for another attempt."

    $ fade_to_black(0.4)

    "The tennis ball gets close, and you feel some feedback in your mind."

    show expression "images/effects/zing.webp" as zing onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0
        
    "!!!"
    "You try with every fiber of your being to not react to the stimulus and imagine just letting the tennis ball touch you."
    ". . ."
    "You hear the tennis ball drop to the floor."

    $ fade_in_from_black(0.4)

    call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_9

    $ Jean.change_face("surprised1")

    ch_Player "Goddamnit, this is fucking impossible."
    ch_Jean "But it kinda worked that time!"
    ch_Player "Really?" 

    $ Jean.change_face("smirk2")

    ch_Jean "Well sorta. . ."
    ch_Jean "It did get a couple inches closer to you." 

    $ Jean.change_face("worried1")

    ch_Player "I guess that's something. . ." 

    $ Jean.change_face("neutral")

    call Jean_activate_psychic from _call_Jean_activate_psychic_10

    $ fade_to_black(0.4)

    "You continue trying for another 45 minutes without success."
    "The rest of the session is spent lightly sparring with [Jean.name], after which she exercises her own powers."
    "This time she restrains herself and is able to stop before things get out of control."

    $ fade_in_from_black(0.4)

    call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_10

    $ Jean.change_face("worried1")

    ch_Player "You alright? Need any help?"
    ch_Jean "No, I'm okay."
    ch_Jean "I thought it would be fine if I just limited myself. . ."
    ch_Jean "But that got pretty close."
    ch_Jean "That's enough for today, I need a break." 

    $ Jean.change_face("neutral")

    ch_Player "Sounds good."
    ch_Jean "Bye, [Player.first_name]."

    call remove_Characters(Jean) from _call_remove_Characters_54

    $ ongoing_Event = False

    return