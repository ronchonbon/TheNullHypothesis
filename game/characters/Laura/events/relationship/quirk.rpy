init python:

    def Laura_penultimate_quirk():
        label = "Laura_penultimate_quirk"

        conditions = [
            "Laura in Partners",
            "approval_check(Laura, threshold = [550, 600])",
            "EventScheduler.Events['Laura_enjoying_being_girlfriend'].completed",
            "day - EventScheduler.Events['Laura_enjoying_being_girlfriend'].completed >= 3",
            "Laura.location != Player.location",
            "Player.location in public_locations",
            "not Player.date_planned or time_index < 2"]

        waiting = True
        traveling = True

        priority = 99

        return EventClass(label, conditions, waiting = waiting, traveling = traveling, priority = priority)

label Laura_penultimate_quirk:
    $ ongoing_Event = True

    if Laura.History.check("quirk_encouraged") >= Laura.History.check("quirk_discouraged"):
        call send_Characters(Laura, Player.location, behavior = False) from _call_send_Characters_114

        $ Laura.change_face("angry1")

        ch_Laura "Come."

        $ Laura.change_face("angry1", eyes = "left")

        "After suddenly appearing in front of you, [Laura.name] grabs your wrist and starts dragging you along."
        ch_Player "What the. . ."
        ch_Player "What's going on?"

        $ Laura.change_face("furious", blush = 1)

        ch_Laura "I said '{i}come{/i}.'"
        "She tightens her grip and pulls harder."

        $ Laura.change_face("furious", eyes = "right")

        $ fade_to_black(0.4)

        if Player.location != "bg_girls_hallway":
            "You follow along. . . as if you have any choice. . ."
                
            call remove_Characters(location = "bg_girls_hallway") from _call_remove_Characters_255
            call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_343
            call send_Characters(Laura, "bg_girls_hallway", behavior = False) from _call_send_Characters_126

        "She unlocks her door, before shoving you inside."

        call remove_Characters(location = Laura.home) from _call_remove_Characters_256
        call set_the_scene(location = Laura.home) from _call_set_the_scene_344
        call send_Characters(Laura, Laura.home, behavior = False) from _call_send_Characters_127

        $ Laura.change_face("angry1")

        $ temp = Laura.petname.capitalize()

        ch_Player "[temp], what the hell is going on?"

        $ Laura.change_face("suspicious2")

        ch_Laura "I have several questions you need to answer."

        $ Laura.change_face("confused1")

        ch_Player "Why didn't you just ask, instead of dragging me here?"

        $ Laura.change_face("angry1", eyes = "right")

        ch_Laura "You didn't seem to mind when I was so assertive in the past. . ."

        $ Laura.History.update("started_penultimate_quirk_encouraged")
    else:
        call receive_text(Laura, "I need to ask you questions") from _call_receive_text_725
        call receive_text(Laura, "Come to my room") from _call_receive_text_726
        call open_texts(Laura) from _call_open_texts_27
        call receive_text(Laura, "Now") from _call_receive_text_727
        call receive_text(Laura, "Please") from _call_receive_text_728

        pause 1.0

        call send_text(Laura, "did you just say please?") from _call_send_text_97
        call send_text(Laura, "that's new") from _call_send_text_98
        call receive_text(Laura, "Shut up") from _call_receive_text_729
        call receive_text(Laura, "Come now or I will find you") from _call_receive_text_730
        call send_text(Laura, "on my way") from _call_send_text_99
        
        pause 2.0

        hide screen phone_screen

        "You don't dally and head right over."

        call remove_Characters(location = "bg_girls_hallway") from _call_remove_Characters_257
        call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_345
        call knock_on_door(times = 2) from _call_knock_on_door_43

        "You knock on [Laura.name]'s door."
        ch_Player "It's me!"

        $ fade_to_black(0.4)

        "Before you can even finish knocking, the door whips open, and [Laura.name] yanks you inside."

        call send_Characters(Laura, Laura.home, behavior = False) from _call_send_Characters_134
        call set_the_scene(location = Laura.home) from _call_set_the_scene_346

        $ Laura.change_face("angry1")

        ch_Player "So, what's up?"
        ch_Player "You're saying 'please' now?"

        $ Laura.change_face("suspicious2")

        ch_Laura "Don't make me cut you."

        $ Laura.change_face("furious", eyes = "right")

        ch_Laura "And. . . you don't seem to like when I'm. . . so assertive. . ."

    $ Laura.change_face("angry1")

    ch_Player "That's. . . true."
    ch_Player "But, what's this all about?"

    $ Laura.change_face("suspicious2")

    ch_Laura "I was talking to [Rogue.name] earlier. . ."
    ch_Player "About?"

    $ Laura.change_face("angry1", eyes = "right")

    ch_Laura "About my relationship with you."

    $ Laura.change_face("neutral")

    ch_Laura "She is a very useful resource."
    ch_Laura "Has helped answer many questions I've had regarding 'romance.'"
    ch_Player "She really is a great friend. . ."

    $ Laura.change_face("confused1")

    ch_Laura "But, she mentioned a concept the other day, yet refused to elaborate when I wanted to know more." 
    ch_Laura "It was regarding relationships, and how they are generally two-sided."
    ch_Laura "Where each person has an equal say."

    $ Laura.change_face("neutral", eyes = "squint")

    ch_Laura "However, for some people, they may prefer to make it. . . more one-sided. . ."

    if Rogue in Partners:
        ch_Laura "She mentioned her own relationship with you." 
        ch_Laura "And how she wants to 'give herself to you' and prefers to allow you to make decisions for her. . ."
    else:
        ch_Laura "She said certain people find it fulfilling to. . . allow the other person to make decisions for them. . ."

    $ Laura.change_face("confused1")

    ch_Laura "I wanted to know more, but she turned red and changed the subject."

    $ Laura.change_face("angry1")

    ch_Laura "It made me think about my relationship with you."

    if Laura.History.check("started_penultimate_quirk_encouraged"):
        $ Laura.change_face("neutral", eyes = "squint", mouth = "smirk") 

        ch_Laura "I recall you seem to enjoy it when I am. . . forceful. . ."

        $ Laura.change_face("neutral", eyes = "squint", mouth = "lipbite", blush = 1)

        ch_Laura "When I make decisions for you. . ."

        menu:
            extend ""
            "I will admit. . . I do enjoy it when you are assertive like that. . . (encourage_quirk)":
                call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_1061

                $ Laura.change_face("sexy", eyes = "squint", blush = 2) 
                
                ch_Laura "Good." 
                ch_Laura "Because I haven't been able to stop thinking about it." 
                ch_Laura "Thinking about you being. . . {i}mine{/i}. . . making decisions for you. . ." 
                ch_Laura "You are {i}mine{/i}, right?"

                menu:
                    extend ""
                    "I am. . . but let's not jump into this blindly. (encourage_quirk)":
                        call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_1062

                        while Laura.History.check("quirk_encouraged") < Laura.History.check("quirk_discouraged"):
                            $ Laura.History.update("quirk_encouraged")
                    "I don't know. . . let's not take this too far. (discourage_quirk)":
                        $ Laura.change_face("confused1")

                        while Laura.History.check("quirk_encouraged") >= Laura.History.check("quirk_discouraged"):
                            $ Laura.History.update("quirk_discouraged")
            "Yeah. . . but maybe you could tone it down, be less assertive in the future? (discourage_quirk)":
                $ Laura.change_face("confused1")

                ch_Laura "Less assertive?"

                while Laura.History.check("quirk_encouraged") >= Laura.History.check("quirk_discouraged"):
                    $ Laura.History.update("quirk_discouraged")
    else:
        $ Laura.change_face("neutral", eyes = "squint")

        ch_Laura "I've noticed you pushing back when I am forceful. . ."
        ch_Laura "When I try to make decisions for you."

        menu:
            extend ""
            "I have. . . but I don't mind if you're a little assertive. . . (encourage_quirk)":
                $ Laura.change_face("confused1")

                ch_Laura "So, you do want me to be assertive?"

                while Laura.History.check("quirk_encouraged") < Laura.History.check("quirk_discouraged"):
                    $ Laura.History.update("quirk_encouraged")
            "That's true. . . I don't know if I like it when you're so assertive. (discourage_quirk)":
                $ Laura.change_face("confused1")

                ch_Laura "So, I should be less assertive?"

                while Laura.History.check("quirk_encouraged") >= Laura.History.check("quirk_discouraged"):
                    $ Laura.History.update("quirk_discouraged")

    pause 1.0
        
    $ Laura.change_face("confused1", eyes = "squint")

    ch_Player "Yes, but I don't know if you really understand. . ."
    ch_Laura "What is there to understand?"

    $ Laura.change_face("angry1", blush = 1)

    ch_Laura "I know how it makes me feel."

    $ Laura.change_face("angry1", mouth = "lipbite", blush = 1)

    ch_Laura "The thought of you being mine makes me. . . very excited."
    ch_Laura "Telling you what to do. . . making you do things to me. . . doing things to you whenever I want. . ."

    $ Laura.change_face("angry1", mouth = "lipbite", blush = 2)

    ch_Laura "Following my instincts. . ."

    $ Laura.change_face("angry1", eyes = "squint", mouth = "lipbite", blush = 1)

    ch_Player "That's. . . well. . . {i}ahem{/i}."

    $ Laura.change_face("confused1", eyes = "squint", blush = 1)

    ch_Player "Whichever way we end up taking our relationship. . . you need to realize that's still what this is: a relationship."

    $ Laura.change_face("confused1", eyes = "squint", mouth = "lipbite", blush = 1)

    ch_Player "Even if I did. . . let you 'use me'. . ."
    ch_Player "And whenever I do things to you, we both still have the choice to stop things whenever we want."

    $ Laura.change_face("confused1")

    ch_Laura "This is that 'consent' thing?"
    ch_Player "Yes."
    ch_Laura "So, even if you want me to be forceful, you'd still have the choice to stop me?"
    ch_Player "Exactly."
    ch_Player "But, let's not jump into anything right now."

    $ Laura.change_face("neutral")

    ch_Player "Let's give it some time, think about how we feel, and revisit this discussion later, okay?"
    ch_Laura "Fine."

    if Laura.History.check("started_penultimate_quirk_encouraged"):
        $ Laura.change_face("sly", mouth = "lipbite", blush = 1) 
        
        ch_Laura "But that doesn't mean I will stop. . . certain things you have already been encouraging. . ."

    ch_Player "Good."

    $ Laura.change_face("suspicious1")

    ch_Laura "Now, leave. . ."

    if not Laura.History.check("started_penultimate_quirk_encouraged"):
        ch_Laura ". . . please."

    ch_Laura "I need to get ready for training." 

    $ fade_to_black(0.4)

    "[Laura.name] doesn't shove, but she isn't quite gentle when she guides you out the door."

    call remove_Characters(location = "bg_girls_hallway") from _call_remove_Characters_258
    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_347
    call send_Characters(Laura, "bg_danger", behavior = "training") from _call_send_Characters_135

    $ ongoing_Event = False

    return