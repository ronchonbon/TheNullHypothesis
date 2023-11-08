init python:

    def Jean_enjoying_being_girlfriend():
        label = "Jean_enjoying_being_girlfriend"

        conditions = [
            "Jean in Partners",
            "approval_check(Jean, threshold = [300, 275])",
            "day - EventScheduler.Events['Jean_boyfriend'].completed >= 3",
            "Player.location in public_locations"]
            
        waiting = True
        traveling = True

        priority = 99

        return EventClass(label, conditions, waiting = waiting, traveling = traveling, priority = priority)

label Jean_enjoying_being_girlfriend:
    $ ongoing_Event = True

    call send_Characters(Jean, Player.location, behavior = False) from _call_send_Characters_231

    $ Jean.change_face("happy", eyes = "wide")

    $ temp = Jean.Player_petname.capitalize()

    ch_Jean "[temp]!"

    $ Jean.change_face("smirk2", eyes = "closed")

    $ temp_Characters = Present[:]
    $ temp_Characters.remove(Jean)

    while temp_Characters:
        if temp_Characters[0] in all_Girls:
            $ temp_Characters[0].change_face("confused2")
        else:
            $ temp_Characters[0].change_face("confused")

        $ temp_Characters.remove(temp_Characters[0])
        
    "Before you can even react, [Jean.name] smothers you with a hug."

    $ Jean.change_face("smirk2", eyes = "closed", blush = 1)

    $ temp_Characters = Present[:]
    $ temp_Characters.remove(Jean)

    while temp_Characters:
        $ temp_Characters[0].change_face("confused1", blush = 1)

        $ temp_Characters.remove(temp_Characters[0])
        
    ch_Jean "Mmm. . ."
    "[Jean.name] just squeezes harder, thoroughly enjoying the moment."

    menu:
        extend ""
        "Uhm. . . [Jean.petname], what did I do to deserve this?":
            $ Jean.change_face("worried2", mouth = "smirk", blush = 1)

            ch_Jean "Oh. . . heh, sorry." 
            
            $ Jean.change_face("worried1", mouth = "smirk") 
            
            ch_Jean "Got a bit carried away when I saw you." 
            
            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1094
        "Gently extricate yourself from her":
            $ Jean.change_face("worried1")

            ch_Jean "Awww, we're done already?"

    $ Jean.change_face("worried1", mouth = "smirk", eyes = "right")

    ch_Jean "It's not that you did anything. . . I just. . ."

    $ Jean.change_face("worried2")

    pause 1.0

    $ Jean.change_face("worried1", eyes = "left")

    pause 1.0

    $ Jean.change_face("worried1", mouth = "smirk")

    "It seems like she finally realizes where she is."
    ch_Jean "Can we, like. . . have a quick talk in private. . ."
    ch_Player "Sure."
    
    if Player.location != "bg_hallway":
        "You lead [Jean.name] to your room."

        call remove_Characters(location = "bg_hallway") from _call_remove_Characters_263
        call set_the_scene(location = "bg_hallway") from _call_set_the_scene_358
        call send_Characters(Jean, "bg_hallway", behavior = False) from _call_send_Characters_232

    $ Jean.change_face("kiss2")

    pause 1.0

    $ Jean.change_face("worried1", mouth = "lipbite")

    "She can't help herself apparently, and gives you a kiss on the cheek before following you inside."

    call remove_Characters(location = Player.home) from _call_remove_Characters_264
    call set_the_scene(location = Player.home) from _call_set_the_scene_359
    call send_Characters(Jean, Player.home, behavior = False) from _call_send_Characters_233

    $ Jean.change_face("worried1")

    $ temp = Jean.petname.capitalize()

    ch_Player "[temp], what's really going on?"

    $ Jean.change_face("pleased2")

    ch_Jean "Nothing's going on!"

    $ Jean.change_face("worried1", mouth = "smirk", eyes = "right")

    ch_Jean "I just. . . I dunno. . ."

    $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Jean "Seeing you. . . thinking about you. . . about us. . ."

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Jean "It makes me really happy, and I just can't help it."

    $ Jean.change_face("worried1", mouth = "lipbite", eyes = "right", blush = 1)

    ch_Jean "Finally being together. . ."
    ch_Player "'Finally'?"

    $ Jean.change_face("smirk2")

    ch_Jean "Whenever I'm really stressed out, I just think about us, and it makes me feel better."

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Jean "The idea of being there for you. . ."

    $ Jean.change_face("worried2", mouth = "lipbite", blush = 1)

    pause 1.0

    $ Jean.change_face("worried1", mouth = "lipbite", eyes = "right", blush = 1)

    ch_Jean "Gah! It just makes me want to smother you with attention and spoil you for being such a good little bro'. . ."

    $ Jean.change_face("worried1", mouth = "smirk")

    menu:
        extend ""
        "I won't say no to having my beautiful big sis' spoil me. . . (encourage_quirk)":
            $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 
            
            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1095 
            call change_Girl_stat(Jean, "desire", 0) from _call_change_Girl_stat_1096

            ch_Jean "Of course you wouldn't." 
            ch_Jean "You should be super thankful."

            $ Jean.History.update("called_big_sis")
            $ Jean.History.update("quirk_encouraged")
        "I prefer it when you don't call me that. . . (discourage_quirk)":
            $ Jean.change_face("worried1")

            ch_Jean "Oh alriiight. . ." 
            
            $ Jean.change_face("worried1", eyes = "right") 
            ch_Jean ". . . spoilsport."

            $ Jean.History.update("quirk_discouraged")

    $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Player "But, it makes me glad to hear that you're so happy. . ."
    ch_Jean "Good, but. . . are you happy?"

    menu:
        extend ""
        "Of course I am. I know we haven't been together all that long, but you're a wonderful girlfriend. . .":
            $ Jean.change_face("worried2", mouth = "lipbite", blush = 1) 
            
            if Jean.History.check("called_big_sis"):
                ch_Player ". . . and 'big sis''."

            $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 

            ch_Jean "Good. . . that makes me even happier. . ." 
            
            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1097 
            call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_1098
        "Are you kidding me? I couldn't ask for a better girlfriend. . .":
            $ Jean.change_face("worried2", mouth = "lipbite", blush = 1) 
            
            if Jean.History.check("called_big_sis"):
                ch_Player ". . . and 'big sis''."

            $ Jean.change_face("worried1", mouth = "lipbite", eyes = "right", blush = 1) 
            
            ch_Jean "I really am the best. . ." 
            
            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1099
        "Well. . . yeah, it's not too bad. . .":
            $ Jean.change_face("confused2", blush = 1)
            
            if Jean.History.check("called_big_sis"):
                ch_Player ". . . you are a pretty good 'big sis'' too."

            $ Jean.change_face("worried1", blush = 1) 
            
            ch_Jean "Oh come on, don't be like that." 
            
            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1100

    $ Jean.change_face("sexy", blush = 1)

    ch_Jean "Well. . . c'mere."

    $ Jean.change_face("kiss2", blush = 1)

    "[Jean.name] pulls you into a tender kiss. . ."

    $ Jean.change_face("sexy", eyes = "closed", blush = 1)

    "Your lips part after a moment, but she holds the embrace, squeezing you tightly, leaning her head on your shoulder."
    "Finally, she let's go."

    $ Jean.History.update("kiss")

    $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Jean "I'm gonna head out. . ."
    ch_Jean "Don't miss me too much."

    call remove_Characters(Jean) from _call_remove_Characters_265

    $ ongoing_Event = False

    return