init python:

    def Laura_enjoying_being_girlfriend():
        label = "Laura_enjoying_being_girlfriend"

        conditions = [
            "Laura in Partners",
            
            "approval_check(Laura, threshold = [275, 300])",

            "day - EventScheduler.Events['Laura_boyfriend'].completed_when >= 3",

            "Player.location == Player.home and not Present",

            "Laura.is_in_normal_mood()"]
            
        waking = True

        priority = 99

        return EventClass(label, conditions, waking = waking, priority = priority)

label Laura_enjoying_being_girlfriend:
    $ ongoing_Event = True

    "You wake up, but as you're getting out of bed, you notice something flash by your window."
    "A quick peek outside doesn't show anything out of the ordinary, so you get ready for the day as usual."

    call receive_text(Kurt, "Morning bruder") from _call_receive_text_294
    call receive_text(Kurt, "Seems like you have a visitor waiting for you") from _call_receive_text_692
    call open_texts(Kurt) from _call_open_texts_5
    call send_text(Kurt, "I do?") from _call_send_text_82
    call send_text(Kurt, "But nobody knocked") from _call_send_text_83
    call receive_text(Kurt, "Your girlfriend, zee small angry one, is pacing by your door") from _call_receive_text_693
    call receive_text(Kurt, "What did you do???") from _call_receive_text_694
    call send_text(Kurt, "nothing!") from _call_send_text_84
    call send_text(Kurt, "I think. . .") from _call_send_text_85
    call send_text(Kurt, "thanks for letting me know") from _call_send_text_86
    call send_text(Kurt, "I'll go see what's up") from _call_send_text_87
    call receive_text(Kurt, "Of course") from _call_receive_text_695
    call receive_text(Kurt, "Also") from _call_receive_text_696
    call receive_text(Kurt, "Nein, never mind", delay = 5.0) from _call_receive_text_697
    call receive_text(Kurt, "Good luck") from _call_receive_text_698

    pause 2.0

    hide screen phone_screen
    
    "You get dressed, prepare for the worst, and open the door."

    call remove_Characters(location = "bg_hallway") from _call_remove_Characters_113
    call send_Characters(Laura, "bg_hallway", behavior = False) from _call_send_Characters_6
    call set_the_scene(location = "bg_hallway") from _call_set_the_scene_329
    
    $ Laura.change_face("furious", eyes = "right")

    pause 1.0

    $ Laura.change_face("appalled3")

    # $ Laura.left_arm_pose = 2

    "Once she notices you, [Laura.name] jumps back in surprise, getting into a fighting stance."

    $ Laura.change_face("neutral", eyes = "squint")

    ch_Laura "Sorry. . ."

    # $ Laura.left_arm_pose = 1

    ch_Laura "You surprised me."
    ch_Player "Me?"
    ch_Player "Surprised you?"

    $ Laura.change_face("angry1", eyes = "right")

    ch_Laura "I was. . . preoccupied."

    $ Laura.change_face("angry1")

    ch_Player "[Kurt.name] said you've been pacing around for a while."
    ch_Player "Everything okay?"

    $ Laura.change_face("confused1")

    ch_Laura "The blue elf?"
    ch_Player "He's not an elf. . ."

    $ Laura.change_face("confused1", eyes = "squint")

    ch_Laura "Logan disagrees."

    $ Laura.change_face("neutral")

    ch_Laura "And, I am fine."
    ch_Laura "How did you sleep last night?" 
    ch_Player "Fine, thanks."
    ch_Player "Why?"

    $ Laura.change_face("suspicious1")

    ch_Laura "Are you telling me the truth?"
    ch_Laura "You were tossing and turning more than usual last night."
    ch_Player "Wha. . . how do you know that?!"

    $ Laura.change_face("confused1")

    ch_Laura "I watch you sleep sometimes to make sure you're unharmed."

    $ Laura.change_face("neutral")

    ch_Laura "It is not difficult to climb up to your window."

    $ temp = Laura.petname.capitalize()

    menu:
        extend ""
        "[temp], I appreciate the concern, but you shouldn't just watch me sleep. . . (discourage_quirk)":
            $ Laura.change_face("confused1")

            pause 1.0

            $ Laura.change_face("neutral", eyes = "right") 
            
            ch_Laura "Fine. . ." 
            ch_Laura "I will stop." 
            
            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_932

            $ Laura.History.update("quirk_discouraged")
        "That's. . . actually really sweet, and it's not that I want you to stop, but I don't want you losing sleep for my sake. (encourage_quirk)":
            ch_Laura "I don't need as much sleep as you do." 
            
            $ Laura.change_face("angry1", eyes = "right", blush = 1) 
            
            ch_Laura "And. . . it brings me comfort. . . knowing you're safe. . ." 
            
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_933

            $ Laura.History.update("quirk_encouraged")

    $ Laura.change_face("neutral", eyes = "squint")

    ch_Player "I can tell you're also dodging the real reason for being here."
    ch_Laura "Fine."

    $ Laura.change_face("angry1", eyes = "right")

    ch_Laura "I'm only here because [Rogue.name] said it was a good idea to. . ."
    ch_Player "To?"

    $ Laura.change_face("furious")

    ch_Laura "{i}Grrrrrr{/i}. . ."

    $ Laura.change_face("furious", eyes = "right")

    ch_Laura "{size=-5}She said it would be easy{/size}. . ."

    $ Laura.change_face("suspicious2")

    ch_Laura "I. . ."
    ch_Laura ". . ."

    $ Laura.change_face("furious", eyes = "right")

    ch_Laura ". . . very much enjoy being your girlfriend."

    $ Laura.change_face("suspicious2")

    ch_Player "That's sw-"
    ch_Laura "That is all, bye."

    call remove_Characters(Laura) from _call_remove_Characters_114

    ch_Player "-eet."

    $ ongoing_Event = False

    return