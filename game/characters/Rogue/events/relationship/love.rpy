init python:

    def Rogue_I_love_you_encouraged():
        label = "Rogue_I_love_you_encouraged"

        conditions = [
            "Rogue in Partners",

            "approval_check(Rogue, threshold = Rogue_thresholds['love'])",

            "day - EventScheduler.Events['Rogue_penultimate_quirk'].completed_when >= 3",

            "Rogue.History.check('quirk_encouraged') >= Rogue.History.check('quirk_discouraged')",

            "Player.location == Player.home and Player.destination in public_locations",
            "not Player.date_planned or time_index < 2",

            "Rogue.is_in_normal_mood()"]

        traveling = True

        priority = 99

        return EventClass(label, conditions, traveling = traveling, priority = priority)

label Rogue_I_love_you_encouraged:
    $ ongoing_Event = True

    call remove_Characters(location = "bg_hallway") from _call_remove_Characters_304
    call send_Characters(Rogue, "bg_hallway", behavior = False) from _call_send_Characters_278
    call set_the_scene(location = "bg_hallway") from _call_set_the_scene_380

    $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite")

    "As you enter the hallway, you notice [Rogue.name] standing off to the side, looking a bit sheepish."

    $ Rogue.change_face("worried2", blush = 1)

    pause 1.0

    $ Rogue.change_face("worried1", mouth = "smirk")

    $ temp = Rogue.petname.capitalize()

    ch_Player "[temp]?"

    $ Rogue.change_face("worried1", eyes = "closed")

    "[Rogue.name] walks right up to you, pulling you into a fierce hug."
    ch_Player "Uh, hey?"

    $ Rogue.change_face("worried1")

    ch_Rogue "Howdy, [Rogue.Player_petname]."

    $ Rogue.change_face("worried1", eyes = "closed")

    ch_Rogue "Ah'm sorry. . . ah just couldn't help myself. . ."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "If yer free, ah was hopin' we could have a talk."

    $ Rogue.change_face("worried1")

    ch_Player "Have you just been waiting around for me to leave my room?"
    ch_Rogue "Yes. . ."
    ch_Rogue "Didn't want to interrupt ya."

    $ Rogue.change_face("worried2", blush = 1)

    ch_Player "For how long?!"
    ch_Rogue "Please, don't worry yerself none. . ."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "It ain't been that long."
    ch_Player "Okay. . . well come on in, let's have that chat."

    call remove_Characters(location = Player.home) from _call_remove_Characters_313
    call send_Characters(Rogue, Player.home, behavior = False) from _call_send_Characters_290
    call set_the_scene(location = Player.home) from _call_set_the_scene_386

    $ EventScheduler.Events["Rogue_I_love_you"].start()

    $ Rogue.History.update("started_love_encouraged")

    $ ongoing_Event = False

    return

init python:

    def Rogue_I_love_you_discouraged():
        label = "Rogue_I_love_you_discouraged"

        conditions = [
            "Rogue in Partners",

            "approval_check(Rogue, threshold = Rogue_thresholds['love'])",

            "day - EventScheduler.Events['Rogue_penultimate_quirk'].completed_when >= 3",

            "Rogue.History.check('quirk_encouraged') < Rogue.History.check('quirk_discouraged')",

            "Player.location == Player.home and not Present",
            "time_index != 2 or not Player.date_planned"]

        sleeping = True

        priority = 99

        return EventClass(label, conditions, sleeping = sleeping, priority = priority)

label Rogue_I_love_you_discouraged:
    $ ongoing_Event = True

    call knock_on_door(times = 2, intensity = 0.25) from _call_knock_on_door_64
    call knock_on_door(times = 2, intensity = 0.5) from _call_knock_on_door_65
    call knock_on_door(times = 2, intensity = 0.75) from _call_knock_on_door_66

    if Present:
        $ temp = Present[0].name

        call remove_Characters(fade = False) from _call_remove_Characters_305

        $ fade_in_from_black(0.4)

        "You're startled awake by someone knocking on your door."

        call knock_on_door(times = 4, intensity = 0.75) from _call_knock_on_door_67

        "They seem quite determined, and just keep knocking."
        "You glance around - it looks like [temp] is already gone. . . odd."
    else:
        $ fade_in_from_black(0.4)

        "You're startled awake by someone knocking on your door."

        call knock_on_door(times = 4, intensity = 0.75) from _call_knock_on_door_68

        "They seem quite determined, and just keep knocking."

    ch_Player "I'll be right there!"
    "You jump out of bed, throw some clothes on, and open the door."

    call send_Characters(Rogue, Player.home, behavior = False) from _call_send_Characters_279

    $ Rogue.change_face("worried1", mouth = "smirk")

    pause 1.0

    $ Rogue.change_face("worried1", eyes = "closed")

    "[Rogue.name] walks in, and pulls you right into a fierce hug."
    ch_Player "Uh, good morning?"

    $ Rogue.change_face("worried1")

    ch_Rogue "Good mornin'. . ."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Ah'm sorry for wakin' ya, but ah really needed to have a chat with you."
    ch_Player "Okay. . . what's up?"

    $ EventScheduler.Events["Rogue_I_love_you"].start()

    $ ongoing_Event = False

    return

init python:

    def Rogue_I_love_you():
        label = "Rogue_I_love_you"

        conditions = [
            "False"]
            
        return EventClass(label, conditions)

label Rogue_I_love_you:
    $ ongoing_Event = True

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "It's. . . about 'us'. . . and how things have been going'."
    
    if Rogue.History.check("started_love_encouraged"):
        $ Rogue.change_face("worried1") 
        
        "She glances at you nervously, as if waiting for permission to keep going." 
        "You just give her a nod."
    else:
        $ Rogue.change_face("neutral", eyes = "right") 
        
        pause 1.0 
        
        $ Rogue.change_face("neutral") 
        
        "[Rogue.name] seems to resolve herself, and presses on."

    $ Rogue.change_face("worried1")

    ch_Rogue "Ah reckon this has been a long time comin'. . ."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "Been sortin' through my feelin's lately, really makin' sure. . ."

    $ Rogue.change_face("worried1")

    ch_Rogue "Ah know this ain't no fancy ceremony or nothin', but ah'm ready to say it."
    ch_Rogue "Have been for a long while, ah reckon."

    $ Rogue.change_face("neutral")

    "[Rogue.name]'s piercing green eyes stare right into your soul."
    ch_Rogue "This might be a bit out of character from what yer used to out of me. . ."

    $ Rogue.change_face("worried1")

    ch_Rogue "But please don't say nothin' till ah'm done."

    $ Rogue.change_face("worried1", eyes = "right")

    "You just stay silent as she pauses for a moment."

    $ Rogue.change_face("angry1", eyes = "right")

    pause 1.0

    $ Rogue.change_face("neutral")

    ch_Rogue "[Player.first_name], ah'm in love with you."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "Maybe ya do understand, but maybe ya don't. . ."

    $ Rogue.change_face("worried1")

    ch_Rogue "Ah've tried makin' my appreciation clear to ya, but it ain't easy tryin' to convey the gravity of things."
    ch_Rogue "You've been the best thing that's. . ."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue ". . . ever happened to me."

    $ Rogue.change_face("worried1")

    ch_Rogue "Our relationship makes me so darn happy, and ah want nothin' more than to spend every wakin' moment with you."

    if Rogue.History.check("started_love_encouraged"):
        $ Rogue.give_trait("quirk")

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "And, ah want nothin' more than to truly be {i}yours{/i}. . ."
        ch_Rogue "Ah love you, and ah want to give myself to you. . . fully, both body and soul."

        $ Rogue.change_face("worried1", eyes = "right")

        ch_Rogue "Ah'm sorry for takin' the lead there for a moment, ah was a bad girl. . ."

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "But it was just real important to me, gettin' all that out."

        menu:
            extend ""
            "I understand - I feel the exact same way. I love you too. I want nothing more than for you to be mine.":
                call change_Character_stat(Rogue, "love", massive_stat) from _call_change_Character_stat_240
                                
                $ Rogue.change_face("worried2", mouth = "smirk", blush = 1)

                pause 1.0

                $ Rogue.change_face("worried1", mouth = "smirk", blush = 1) 
                
                ch_Rogue "You have no idea how happy ah am hearin' you say that. . ." 
            "It's okay, I know how much this matters to you. I love you too. Of course I want you to be mine.":
                call change_Character_stat(Rogue, "love", large_stat) from _call_change_Character_stat_241
                call change_Character_stat(Rogue, "trust", medium_stat) from _call_change_Character_stat_242
                                
                $ Rogue.change_face("worried2", mouth = "smirk", blush = 1)

                pause 1.0

                $ Rogue.change_face("worried1", mouth = "smirk", blush = 1) 
                
                ch_Rogue "It matters a whole lot, and nothin' makes me happier than hearin' you say that. . ." 
            "You were a bad girl, but I'll forgive you this one time. I know how much this means to you - I love you too. You are {i}mine{/i}.":
                call change_Character_stat(Rogue, "love", large_stat) from _call_change_Character_stat_243
                                
                $ Rogue.change_face("worried2", blush = 1)

                pause 1.0

                $ Rogue.change_face("worried1", eyes = "down", blush = 1) 
                
                ch_Rogue "Ah'm sorry. . ." 
                
                $ Rogue.change_face("worried1", blush = 1) 
                
                ch_Rogue "But you have no idea how glad ah am that you feel the same way. . ." 

        $ Rogue.change_face("kiss2", blush = 1)

        "Without another word, you pull [Rogue.name] into a kiss."
        "She grabs onto you, holding on for dear life, as your lips connect."

        $ Rogue.History.update("kiss")

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "Hearin' you say those words back to me, makes me the happiest girl in the world. . ."

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

        ch_Rogue "And, now. . . now that ah'm truly yours. . ."
        ch_Rogue "Ah think ah'm ready to give myself to you."
        ch_Rogue "Ah want to make love with you."
        ch_Rogue "Ah'm on the pill 'n everythin', so it ain't a problem."

        $ Rogue.give_trait("birth_control")

        $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

        ch_Rogue "But. . . if ah may. . ."

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "Could we do it after we go on a nice date?"
        ch_Rogue "Ah want it to be a special occasion."

        $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Player "Sure, that can be arranged."
    else:
        $ Rogue.remove_trait("quirk")

        $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Rogue "And ah want nothin' more than for us to be together. . . for a very long time. . ."
        ch_Rogue "Ah love you, and ah want us to give ourselves to each other. . . fully, both body and soul."

        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "Ah'd say ah'm sorry for takin' the lead there for a minute. . ."

        $ Rogue.change_face("sly")

        ch_Rogue "But ah ain't sorry."

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "It was real important to me, gettin' all that out."

        menu:
            extend ""
            "I know how much all of this means to you. . . I love you too - I want nothing more than for us to be together.":
                call change_Character_stat(Rogue, "love", large_stat) from _call_change_Character_stat_244
                call change_Character_stat(Rogue, "trust", medium_stat) from _call_change_Character_stat_255

                $ Rogue.change_face("worried2", blush = 1)

                pause 1.0

                $ Rogue.change_face("worried1", mouth = "smirk", blush = 1) 
                
                ch_Rogue "You make it so easy to love ya. . ." 
            "I love you too. . . so much. . . you have no idea how happy you make me. I want us to be together for a very long time.":
                call change_Character_stat(Rogue, "love", massive_stat) from _call_change_Character_stat_256
                                
                $ Rogue.change_face("worried2", blush = 1)

                pause 1.0

                $ Rogue.change_face("worried1", mouth = "smirk", blush = 1) 
                
                ch_Rogue "Ah'm glad yer happy. . . you have no idea how glad. . ." 
            "I don't know how I feel about you 'taking charge'. . . but yeah, I love you too. Don't worry, it's not like I want to break up or anything.":
                call change_Character_stat(Rogue, "love", -large_stat) from _call_change_Character_stat_257
                call change_Character_stat(Rogue, "trust", -medium_stat) from _call_change_Character_stat_260
                
                $ Rogue.change_face("confused1", blush = 1)

                pause 1.0

                $ Rogue.change_face("worried1", blush = 1) 
                
                ch_Rogue "It ain't gonna be a frequent thing if ya don't want. . ." 
                
                $ Rogue.change_face("worried1", mouth = "smirk") 
                
                ch_Rogue "But ah'm glad ya feel the same way. . ." 
                
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "Hearin' you say those words back to me, makes me the happiest girl in the world. . ."

        $ Rogue.change_face("sexy", blush = 1)

        ch_Rogue "And, now. . . now that we've said the words. . ."
        ch_Rogue "Ah think ah'm ready to make love with you."
        ch_Rogue "Ah'm on the pill 'n everythin', so it ain't a problem."

        $ Rogue.give_trait("birth_control")

        $ Rogue.change_face("worried1")

        ch_Rogue "But. . . could we do it after we go on a nice date?"

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Ah want it to be a special occasion."
        ch_Player "Sure, that can be arranged."

    $ Rogue.change_face("smirk2")

    ch_Rogue "Ah'd like to hang around, if that's alright with you."

    $ Rogue.change_face("sexy")

    ch_Rogue "Say 'I love you' a few more times. . ."
    ch_Rogue "Makes me giddy just thinkin' 'bout it. . ."

    $ ongoing_Event = False

    return