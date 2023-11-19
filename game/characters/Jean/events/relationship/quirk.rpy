init python:

    def Jean_penultimate_quirk():
        label = "Jean_penultimate_quirk"

        conditions = [
            "Jean in Partners",

            "approval_check(Jean, threshold = [600, 550])",

            "day - EventScheduler.Events['Jean_enjoying_being_girlfriend'].completed_when >= 3",

            "Jean.location != Player.location and Player.location in public_locations",

            "Jean.is_in_normal_mood()"]

        waiting = True
        traveling = True

        priority = 99

        return EventClass(label, conditions, waiting = waiting, traveling = traveling, priority = priority)

label Jean_penultimate_quirk:
    $ ongoing_Event = True

    call send_Characters(Jean, Player.location, behavior = False) from _call_send_Characters_250
    
    $ Jean.change_face("happy")

    pause 1.0

    $ Jean.change_face("smirk2", eyes = "closed", blush = 1)

    "[Jean.name] comes up to you, wrapping you in a tight hug."
    "She holds it for a moment before letting go."

    if Jean.History.check("quirk_encouraged") >= Jean.History.check("quirk_discouraged"):
        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "Let's go, [Jean.Player_petname]."

        $ Jean.change_face("smirk2", eyes = "right", blush = 1)

        "She takes your hand, expecting you to follow along."

        menu:
            extend ""
            "Where are we going, [Jean.petname]?":
                $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

                ch_Jean "Shush, just follow your big sis'."
            "Hold on, tell me where we're going first.":
                call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_1133

                ch_Jean "Oh c'mon, it's like you don't trust me or something." 
                
                $ Jean.change_face("worried1", blush = 1)

        $ Jean.change_face("smirk2", eyes = "squint", blush = 1)
        
        show expression "images/effects/smack.webp" as smack onlayer effects:
            anchor (0.5, 0.5) pos (0.5, 0.7)

            zoom 0.0
            alpha 0.0
            ease 0.1 zoom 1.0 alpha 1.0
            ease 1.0 alpha 0.0

        with small_screenshake

        "She gives your ass a light spank, before squeezing your hand and pulling you along."
        ch_Jean "We're going to have a chat."

        $ Jean.change_face("smirk2", eyes = "right", blush = 1)

        ch_Jean "Now, c'mon!"

        call remove_Characters(location = "bg_girls_hallway") from _call_remove_Characters_285
        call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_370
        call send_Characters(Jean, "bg_girls_hallway", behavior = False) from _call_send_Characters_251

        "She unlocks the door, and ushers you inside."

        call remove_Characters(location = Jean.home) from _call_remove_Characters_286
        call set_the_scene(location = Jean.home) from _call_set_the_scene_371
        call send_Characters(Jean, Jean.home, behavior = False) from _call_send_Characters_252

        $ Jean.change_face("confused1", eyes = "squint", mouth = "smirk", blush = 1)

        ch_Player "A chat?"
        ch_Player "Did something happen?"

        $ Jean.change_face("confused1", eyes = "squint", mouth = "lipbite", blush = 1)

        ch_Jean "I said shush. . ."

        $ Jean.change_face("kiss2", blush = 1)

        "She doesn't let you respond, before dragging you into her embrace and planting her lips on yours."

        $ Jean.change_face("kiss2", blush = 1)

        call change_Girl_stat(Jean, "desire", 0) from _call_change_Girl_stat_1134

        "One hand cups your face, while her other wanders its way across your body before settling on your ass."

        $ Jean.change_face("sexy", blush = 1)

        "Your lips part, but she squeezes and holds you close."
        ch_Jean "I know you like it when your big sis' takes control of things."

        $ Jean.History.update("started_penultimate_quirk_encouraged")
    else:
        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Player "That was nice. . ."
        ch_Jean "Hey, [Jean.Player_petname]."

        $ Jean.change_face("smirk2", blush = 1)

        ch_Jean "I wanna have a chat."

        $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

        ch_Jean "Let's head over to my room. . ."

        $ Jean.change_face("worried1", eyes = "left", mouth = "lipbite", blush = 1)

        ch_Jean "So we can do it in private."

        $ Jean.change_face("smirk2", blush = 1)

        menu:
            extend ""
            "Okay, sure. Is everything okay?":
                $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

                ch_Jean "It's nothing bad."
            "Do we have to right now? Can't this wait?":
                $ Jean.change_face("angry1", blush = 1) 

                ch_Jean "Oh c'mon, this is important!"
                
                call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_1135

        $ Jean.change_face("worried1", blush = 1)

        ch_Jean "Let's go."

        $ Jean.change_face("smirk2", eyes = "right", blush = 1)

        call remove_Characters(location = "bg_girls_hallway") from _call_remove_Characters_287
        call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_372
        call send_Characters(Jean, "bg_girls_hallway", behavior = False) from _call_send_Characters_253

        "She unlocks the door and ushers you inside."

        call remove_Characters(location = Jean.home) from _call_remove_Characters_288
        call set_the_scene(location = Jean.home) from _call_set_the_scene_373
        call send_Characters(Jean, Jean.home, behavior = False) from _call_send_Characters_254

        $ Jean.change_face("confused1", eyes = "squint", mouth = "smirk", blush = 1)

        ch_Jean "Before we talk. . ."

        $ Jean.change_face("kiss2", blush = 1)

        "She drags you into her embrace and plants her lips on yours."

        $ Jean.change_face("kiss2", blush = 1)

        call change_Girl_stat(Jean, "desire", 0) from _call_change_Girl_stat_1136

        "One hand cups your face, while her other wanders its way across your body before settling on your ass."

        $ Jean.change_face("sexy", blush = 1)

        "Your lips part, but she squeezes and holds you close."
        ch_Jean "I can never get enough of you. . ."

    $ Jean.History.update("kiss")

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Jean "I wanted to have a chat about us. . ."

    $ Jean.change_face("kiss2", blush = 1)

    "She gives you another quick kiss."

    $ Jean.change_face("sexy", blush = 1)

    ch_Jean "About how our relationship is gonna go from now on. . ."
    ch_Player "Wh-"

    if Jean.History.check("started_penultimate_quirk_encouraged"):
        $ Jean.change_face("kiss2", blush = 1) 
        
        "She kisses you before you can say anything." 
        
        $ Jean.change_face("sly", blush = 1) 
        
        ch_Jean "Shush, it's still my turn to talk."

        $ Jean.History.update("kiss")
    else:
        "She gently puts a finger over your mouth." 
        
        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 
        
        ch_Jean "Please, let me say my peace first. . ."

    $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Jean "It's not anything bad."

    $ Jean.change_face("worried1", eyes = "right", blush = 1)

    ch_Jean "But, I don't really know what's going on. . ."

    $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Jean "It started out all innocent, ya'know? Making you my 'little sib'' on campus."

    $ Jean.change_face("worried2", blush = 1)

    ch_Jean "Plenty of colleges have that sort of thing!"

    menu:
        extend ""
        "That's true, my old school had something like it.":
            $ Jean.change_face("worried2", mouth = "smirk", blush = 1)

            ch_Jean "See! It's not that weird. . ." 
            
            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1137
        "I guess you're right. . . but this isn't really a normal college. . .":
            $ Jean.change_face("worried2", blush = 1)

            ch_Jean "So?! It's not that weird. . ."
        "I think I see where this is going. . . and that doesn't make it not weird. . .":
            $ Jean.change_face("appalled2", blush = 1)

            ch_Jean "It's not weird!" 
            
            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1138

    $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Jean "Look, all I'm saying is that making you my little sibling was the greatest idea."

    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Jean "And, since we officially got together. . ." 
    ch_Jean "I started to realize that I really enjoy treating you like my. . . little brother. . ." 
    ch_Jean "Smothering you with affection, and taking control. . ." 

    $ Jean.change_face("sexy", blush = 2)

    ch_Jean "Teasing you until you can't take it anymore. . ." 

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Jean "Just the thought of it. . ."

    if Jean.History.check("started_penultimate_quirk_encouraged"):
        $ Jean.change_face("sly", blush = 1)

        ch_Jean "Plus, it seems like you enjoy it too."

        $ Jean.change_face("confused1", mouth = "smirk", eyes = "squint", blush = 1)

        ch_Jean "Isn't that right, [Jean.Player_petname]?"

        menu:
            extend ""
            "Yeah. . . I think I do enjoy it. . . being your little brother. . .":
                call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1139

                $ Jean.change_face("sexy", eyes = "squint", blush = 2) 
                
                ch_Jean "Good." 
                ch_Jean "You better like it."
                ch_Jean "You're lucky to have such a nice big sister. . ."

                menu:
                    extend ""
                    "I really, really am. . . (encourage_quirk)":
                        call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1140

                        while Jean.History.check("quirk_encouraged") < Jean.History.check("quirk_discouraged"):
                            $ Jean.History.update("quirk_encouraged")

                        $ Jean.History.update("penultimate_quirk_encouraged")
                    "I am, but. . . maybe we shouldn't lean into it so heavily. (discourage_quirk)":
                        $ Jean.change_face("worried1")

                        while Jean.History.check("quirk_encouraged") >= Jean.History.check("quirk_discouraged"):
                            $ Jean.History.update("quirk_discouraged")
            "I don't know. . . maybe you could tone it down a little bit? (discourage_quirk)":
                $ Jean.change_face("confused1")

                ch_Jean "Tone it down?"

                while Jean.History.check("quirk_encouraged") >= Jean.History.check("quirk_discouraged"):
                    $ Jean.History.update("quirk_discouraged")
    else:
        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "And. . . I know you don't seem to be the biggest fan of it. . ."

        $ Jean.change_face("worried2", mouth = "smirk", blush = 1)

        ch_Jean "I mean. . . unless. . . ?"

        menu:
            extend ""
            "You know. . . the idea has been growing on me. . . (encourage_quirk)":
                $ Jean.change_face("sly", blush = 1)

                ch_Jean "I knew it. . ."

                while Jean.History.check("quirk_encouraged") < Jean.History.check("quirk_discouraged"):
                    $ Jean.History.update("quirk_encouraged")

                $ Jean.History.update("penultimate_quirk_encouraged")
            "No. . . I'm still not a fan of it. (discourage_quirk)":
                $ Jean.change_face("worried1")

                ch_Jean "Aw, are you sure?"

                while Jean.History.check("quirk_encouraged") >= Jean.History.check("quirk_discouraged"):
                    $ Jean.History.update("quirk_discouraged")

    $ Jean.change_face("worried1", mouth = "smirk")

    if Jean.History.check("penultimate_quirk_encouraged"):
        ch_Player "Look, I'm all for exploring this stuff more with you. . ." 
        ch_Player "But let's not dive right into the deep end."
    else:
        ch_Player "Look, I'm not really sure about this whole sibling thing right now. . ." 
        ch_Player "But either way, let's not dive right into the deep end."

    ch_Jean "I know, you're right."

    $ Jean.change_face("worried1", mouth = "lipbite", eyes = "right")

    ch_Jean "I just know it makes me. . ."

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Jean "{i}Ahem{/i}. . ."

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Jean "Of course it's not like I'll force you to do anything if you don't want to."

    $ Jean.change_face("smirk2")

    ch_Jean "But I guess we could both use some time to think about how we feel."
    ch_Player "I think it's a good idea."

    $ Jean.change_face("sly")

    ch_Jean "I'm still gonna smother you with affection, though. . ."

    $ Jean.change_face("kiss2", blush = 1)

    "[Jean.name] pulls you into another deep kiss."

    $ Jean.change_face("kiss2", blush = 2)

    "Her tongue starts getting involved, and you enjoy each other for a few long moments."

    $ Jean.change_face("sexy", blush = 1)

    ch_Jean "Yum."

    $ Jean.History.update("kiss")

    $ ongoing_Event = False

    return