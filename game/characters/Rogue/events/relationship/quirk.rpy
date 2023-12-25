init python:

    def Rogue_penultimate_penultimate_quirk():
        label = "Rogue_penultimate_penultimate_quirk"

        conditions = [
            "Rogue in Partners",

            "approval_check(Rogue, threshold = [525, 525])",
            
            "day - EventScheduler.Events['Rogue_enjoying_being_girlfriend'].completed_when >= 3",

            "Rogue.location != Player.location and Player.location in public_locations",
            "not Player.date_planned or time_index < 2",

            "Rogue.is_in_normal_mood()"]

        waiting = True
        traveling = True

        priority = 99

        return EventClass(label, conditions, waiting = waiting, traveling = traveling, priority = priority)

label Rogue_penultimate_penultimate_quirk:
    $ ongoing_Event = True

    call send_Characters(Rogue, Player.location, behavior = False) from _call_send_Characters_280 

    if Rogue.History.check("quirk_encouraged") >= Rogue.History.check("quirk_discouraged"):
        $ Rogue.change_face("worried2", mouth = "smirk")

        pause 1.0

        $ Rogue.change_face("worried1", mouth = "smirk")

        "[Rogue.name] sees you but doesn't walk over, just standing there patiently."
        "You wait for a moment, and she still keeps her distance."

        $ Rogue.change_face("worried2", blush = 1)

        "You walk over to her instead."

        $ temp = Rogue.petname.capitalize()

        ch_Player "[temp], why are you standing so far away?"

        $ Rogue.change_face("worried1")

        ch_Rogue "Ah'm sorry, ah just. . ."

        $ Rogue.change_face("worried1", eyes = "down")

        ch_Rogue "Was just wonderin' if we could talk in private when you got a chance."

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "But ah didn't wanna interrupt, so ah was waitin'. . ."

        menu:
            extend ""
            "I really appreciate that, how considerate you are, but we've talked about this before. You need to tell me if you want to talk first, and I'll be the one to decide, okay? (encourage_quirk)":
                $ Rogue.change_face("worried1")

                ch_Rogue "Ah'm sorry." 
                
                $ Rogue.change_face("worried1", eyes = "down") 
                
                ch_Rogue "Ah promise ah will, from now on." 
                ch_Player "Good, then there's nothing to worry about." 
                
                call change_Character_stat(Rogue, "love", 0) from _call_change_Character_stat_1164
            "You don't need to do that. If there's something you want to talk about, don't worry about interrupting me. (discourage_quirk)":
                $ Rogue.change_face("worried1", mouth = "smirk")
                
                ch_Rogue "Oh, alright, if you say so. . ." 
                ch_Player "Really, there's nothing to worry about." 
                
                call change_Character_stat(Rogue, "trust", 0) from _call_change_Character_stat_1165

        $ Rogue.change_face("worried1")

        ch_Player "But, you wanted to go talk in private?"

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Ah do, if you don't mind."
        ch_Rogue "It ain't about nothin' big, but. . ."
        ch_Player "C'mon, let's go."
    else:
        $ Rogue.change_face("worried2", mouth = "smirk")

        pause 1.0

        $ Rogue.change_face("worried1", mouth = "smirk")

        "[Rogue.name] sees you, and walks right over."
        ch_Rogue "Hey, [Rogue.Player_petname]."

        $ Rogue.change_face("worried1")

        ch_Rogue "Was wonderin' if ya had time to talk. . . in private. . ."

        menu:
            extend ""
            "I'm glad you let me know something is bothering you, but I'm kind of in the middle of something. . . (encourage_quirk)":
                $ Rogue.change_face("worried2")

                ch_Rogue "Ah'm sorry. . ." 
                
                $ Rogue.change_face("worried1", eyes = "down") 
                
                ch_Rogue "Ah promise ah won't interrupt ya next time." 
                
                call change_Character_stat(Rogue, "love", 0) from _call_change_Character_stat_1166
            "Of course we can talk. (discourage_quirk)":
                $ Rogue.change_face("smirk2")
                
                ch_Rogue "Nothin's botherin' me, per se. . ." 
                
                call change_Character_stat(Rogue, "trust", 0) from _call_change_Character_stat_1167

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "What ah wanna talk to ya about is a good thing."

        $ Rogue.change_face("worried1")

        ch_Rogue "Can we head to yer room for some privacy?"
        ch_Player "Okay, sure."

    $ fade_to_black(0.4)

    "You lead [Rogue.name] to your room."

    call remove_Characters(location = Player.home) from _call_remove_Characters_306
    call set_the_scene(location = Player.home) from _call_set_the_scene_381
    call send_Characters(Rogue, location = Player.home, behavior = False) from _call_send_Characters_281

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Player "So, what's up?"
    ch_Rogue "Ah just felt like you'd 'ppreciate hearin' what ah had to say."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "Before ya came, ah had a couple friends, sure, and people were nice to me. . ."

    $ Rogue.change_face("worried1")

    ch_Rogue "But ah was pretty lonely by all accounts."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "Tried not to get too close with anyone. . . for. . . reasons. . ."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Ah just wanted to thank you. . . for bein' a real great friend. . . and a real great boyfriend."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Our relationship, it's made me real happy."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "Happier. . . than ah can remember feelin'. . ."

    $ Rogue.change_face("worried1")

    ch_Rogue "And ah really hope it's been makin' you happy too. . ."

    menu:
        extend ""
        "It really, {i}really{/i} has. You're such a beacon of light.":
            $ Rogue.change_face("worried2")

            pause 1.0

            $ Rogue.change_face("worried1") 
            
            ch_Rogue "Thank you for sayin' that. . ." 
            
            $ Rogue.change_face("worried1", mouth = "smirk") 
            
            ch_Rogue "It means a whole lot." 
            
            call change_Character_stat(Rogue, "love", 0) from _call_change_Character_stat_1168 
            call change_Character_stat(Rogue, "trust", 0) from _call_change_Character_stat_1169
        "You have no idea how happy it's made me, especially with everything else going on. . .":
            $ Rogue.change_face("worried2")

            pause 1.0

            $ Rogue.change_face("worried1", mouth = "smirk") 
            
            ch_Rogue "Ah'm glad. . ."
            ch_Rogue "You've been goin' through a lot, and it's the least ah could do." 
            
            call change_Character_stat(Rogue, "love", 0) from _call_change_Character_stat_1170
        "Well, yeah, I guess you could say that. Definitely hasn't been the worst thing I've been through since coming here.":
            $ Rogue.change_face("worried2")

            pause 1.0

            $ Rogue.change_face("worried1") 
            
            ch_Rogue "Ah'm glad. . ." 
            ch_Rogue "Ah know it hasn't been easy for you." 
            
            call change_Character_stat(Rogue, "love", 0) from _call_change_Character_stat_1171 
            call change_Character_stat(Rogue, "trust", 0) from _call_change_Character_stat_1172

    $ Rogue.change_face("worried1")

    pause 1.0

    $ Rogue.change_face("worried1", eyes = "closed", blush = 1)

    "[Rogue.name] tentatively walks up to you, pulling you into a hug."
    "She doesn't say anything, she doesn't have to, as she buries her face in your chest, squeezing you tightly."
    "Minutes go by, and you lose track of how long the hug lasts, as you gently caress her hair."

    $ Rogue.change_face("worried1", eyes = "right", blush = 1)

    "Finally, she pulls away and takes a moment to collect herself."

    $ Rogue.change_face("worried1")

    ch_Rogue "Sorry. . . ah. . . just really needed that."

    $ ongoing_Event = False

    return

init python:

    def Rogue_penultimate_quirk_encouraged():
        label = "Rogue_penultimate_quirk_encouraged"

        conditions = [
            "Rogue in Partners",
            
            "approval_check(Rogue, threshold = [825, 825])",
            
            "not EventScheduler.Events['Rogue_penultimate_quirk_discouraged'].completed",
            "EventScheduler.Events['Rogue_penultimate_penultimate_quirk'].completed",
            
            "day - EventScheduler.Events['Rogue_penultimate_penultimate_quirk'].completed_when >= 3",
            
            "Rogue.History.check('quirk_encouraged') >= Rogue.History.check('quirk_discouraged')",
            
            "Rogue.location != Player.location and Player.location == Player.home",
            "not Player.date_planned or time_index < 2",

            "Rogue.is_in_normal_mood()"]

        sleeping = True

        priority = 99

        return EventClass(label, conditions, sleeping = sleeping, priority = priority)

label Rogue_penultimate_quirk_encouraged:
    $ ongoing_Event = True

    call start_new_day from _call_start_new_day_13

    call receive_text(Rogue, f"Morning {Rogue.Player_petname}") from _call_receive_text_811
    call receive_text(Rogue, "Im real sorry for textin you so early") from _call_receive_text_812

    if Present:
        $ temp = Present[0].name

        call remove_Characters(fade = False) from _call_remove_Characters_307
    else:
        $ temp = None

    $ fade_in_from_black(0.4)

    "Your phone startles you awake."

    if temp:
        "It also looks like [temp] is already gone. . . that's odd."

    "After rubbing the sleep from your eyes, you pick it up."

    call open_texts(Rogue) from _call_open_texts_37
    call receive_text(Rogue, "But I was really hopin youd let me come over") from _call_receive_text_813
    call receive_text(Rogue, "Theres somethin I need to tell you") from _call_receive_text_814

    $ Rogue.mandatory_text_options = ["sure, you can come over. I'll get ready while you're on the way", "you really had to wake me up so early? fine, you might as well. I'm up now anyways"]
    $ temp = Rogue.mandatory_text_options[:]

    while Rogue.mandatory_text_options:
        pause

    if Rogue.text_history[-1][1] == temp[0]:
        call receive_text(Rogue, "Thank you") from _call_receive_text_815
        call receive_text(Rogue, "I'll go slow to give ya extra time") from _call_receive_text_816

        call change_Character_stat(Rogue, "love", 0) from _call_change_Character_stat_1173
    elif Rogue.text_history[-1][1] == temp[1]:
        call receive_text(Rogue, "Im sorry") from _call_receive_text_817
        call receive_text(Rogue, "I can wait") from _call_receive_text_818
        call send_text(Rogue, "no, it's fine") from _call_send_text_105
        call receive_text(Rogue, "I'll go slow to give ya extra time") from _call_receive_text_819
        call send_text(Rogue, "thanks") from _call_send_text_106

        call change_Character_stat(Rogue, "love", 0) from _call_change_Character_stat_1174

    call send_text(Rogue, "see you soon") from _call_send_text_107

    pause 2.0

    hide screen phone_screen
    
    "You hop out of bed, get dressed, and head to the bathroom to brush your teeth."
    "After a few minutes, you hear a soft knocking at your door."

    call knock_on_door(times = 2, intensity = 0.4) from _call_knock_on_door_69

    "You open it."

    call send_Characters(Rogue, Player.home, behavior = False) from _call_send_Characters_282

    $ Rogue.change_face("worried1")

    pause 1.0

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Thanks for lettin' me over so early. . ."
    ch_Rogue "Ah know ya like to sleep in, but ah just couldn't get this out of my mind."

    menu:
        extend ""
        "Really, it's okay. If something's bothering you that much, then it's a good thing you didn't wait.":
            ch_Rogue "Thank you. . ." 
            
            $ Rogue.change_face("worried1") 
            
            ch_Rogue "Ah still feel bad 'bout it, though." 
            
            call change_Character_stat(Rogue, "love", 0) from _call_change_Character_stat_1175 
            call change_Character_stat(Rogue, "trust", 0) from _call_change_Character_stat_1176
        "Don't worry about it. I know how it feels to have something nagging at you, and waiting never helps. . .":
            $ Rogue.change_face("worried1")

            ch_Rogue "Ah appreciate how considerate ya are. . ." 
            ch_Rogue "But ah still feel bad." 
            
            call change_Character_stat(Rogue, "love", 0) from _call_change_Character_stat_1177
        "Better to get this out of the way as soon as possible. Don't want you waking me up like this every morning. . .":
            $ Rogue.change_face("worried1")

            ch_Rogue "Ah promise ah won't make this a regular thing. . ." 
            
            $ Rogue.change_face("worried1", eyes = "down") 
            
            ch_Rogue "It was just really botherin' me." 
            
            call change_Character_stat(Rogue, "love", 0) from _call_change_Character_stat_1178

    $ Rogue.History.update("started_penultimate_quirk_encouraged")

    $ EventScheduler.Events["Rogue_penultimate_quirk"].start()

    $ ongoing_Event = False

    return

init python:

    def Rogue_penultimate_quirk_discouraged():
        label = "Rogue_penultimate_quirk_discouraged"

        conditions = [
            "Rogue in Partners",
            
            "approval_check(Rogue, threshold = [825, 825])",
            
            "not EventScheduler.Events['Rogue_penultimate_quirk_encouraged'].completed",
            "EventScheduler.Events['Rogue_penultimate_penultimate_quirk'].completed",
            
            "day - EventScheduler.Events['Rogue_penultimate_penultimate_quirk'].completed_when >= 3",
            
            "Rogue.History.check('quirk_encouraged') < Rogue.History.check('quirk_discouraged')",
            
            "Rogue.location != Player.location and Player.location in public_locations",
            "not Player.date_planned or time_index < 2",

            "Rogue.is_in_normal_mood()"]

        waiting = True
        traveling = True

        priority = 99

        return EventClass(label, conditions, waiting = waiting, traveling = traveling, priority = priority)

label Rogue_penultimate_quirk_discouraged:
    $ ongoing_Event = True

    call send_Characters(Rogue, Player.location, behavior = False) from _call_send_Characters_283 

    $ Rogue.change_face("worried1")

    pause 1.0

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "There ya are. . ."

    $ Rogue.change_face("worried1")

    ch_Rogue "Ah'm sorry for springin' this on ya, but could we go to yer room. . ."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "Was hopin' we could have a chat in private."

    $ Rogue.change_face("worried1", mouth = "smirk")

    menu:
        extend ""
        "Of course we can. Follow me.":
            $ Rogue.change_face("smirk2")

            ch_Rogue "Thanks, [Rogue.Player_petname]." 
            ch_Rogue "Ah really appreciate it." 
            
            call change_Character_stat(Rogue, "love", 0) from _call_change_Character_stat_1179
        "Really, it has to be right now? Fine, let's get this over with.":
            $ Rogue.change_face("worried1", eyes = "down")

            ch_Rogue "Ah'm sorry. . ." 
            ch_Rogue "Somethin's just been botherin' me lately. . ." 
            
            call change_Character_stat(Rogue, "love", 0) from _call_change_Character_stat_1180

    $ fade_to_black(0.4)

    "You lead [Rogue.name] to your room."

    call remove_Characters(location = Player.home) from _call_remove_Characters_308
    call set_the_scene(location = Player.home) from _call_set_the_scene_382
    call send_Characters(Rogue, Player.home, behavior = False) from _call_send_Characters_284

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Thanks for hearin' me out."
    ch_Rogue "Ah know yer real busy 'n stuff. . . but ah've been thinkin'. . . and somethin's been botherin' me."

    menu:
        extend ""
        "Really, it's okay. If something's bothering you that much, then it's a good thing you didn't wait.":
            ch_Rogue "Thank you. . ." 
            
            $ Rogue.change_face("smirk2") 
            
            ch_Rogue "Yer always so considerate." 
            ch_Rogue "It's why ah like ya." 
            
            call change_Character_stat(Rogue, "love", 0) from _call_change_Character_stat_1181 
            call change_Character_stat(Rogue, "trust", 0) from _call_change_Character_stat_1182
        "Don't worry about it. I know how it feels to have something nagging at you, and waiting never helps. . .":
            ch_Rogue "Ah really appreciate how considerate ya are. . ." 
            
            $ Rogue.change_face("smirk2") 
            
            ch_Rogue "It's why ah like ya." 
            
            call change_Character_stat(Rogue, "love", 0) from _call_change_Character_stat_1183
        "Better to get this stuff out of the way as soon as possible. Don't want you dragging me away all the time. . .":
            $ Rogue.change_face("worried1") 
            
            ch_Rogue "This won't be a regular thing. . ." 
            
            call change_Character_stat(Rogue, "love", 0) from _call_change_Character_stat_1184

    $ EventScheduler.Events["Rogue_penultimate_quirk"].start()

    $ ongoing_Event = False

    return

init python:

    def Rogue_penultimate_quirk():
        label = "Rogue_penultimate_quirk"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_penultimate_quirk:
    $ ongoing_Event = True

    $ Rogue.change_face("worried2", mouth = "lipbite")

    ch_Player "So, what did you want to talk about?"

    $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

    ch_Rogue "It's about how our relationship's been progression'. . ."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    if Rogue.History.check("started_penultimate_quirk_encouraged"):
        ch_Rogue "And how you've started takin' control of things."
    else:
        ch_Rogue "And how you don't seem to like takin' control of things."

    $ Rogue.change_face("worried1", eyes = "right", blush = 1)

    ch_Rogue "It's a bit embarrassin', and it ain't nothin' bad, but before ah get to it. . ."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

    ch_Rogue "Ah never really thought ah'd be like this, was always independent, tryin' not to rely on no one."
    ch_Rogue "But since you came along. . . ah couldn't help but feel a different type of way."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Ya probably already started noticin'."
    ch_Rogue "Noticin' how ah like to defer to you for the decision makin'."

    $ Rogue.change_face("worried1", eyes = "right", blush = 1)

    ch_Rogue "How ah. . . tend to let you take charge."

    $ Rogue.change_face("worried1", blush = 2)

    ch_Rogue "What ah'm tryin' to say is, ah really like it when yer. . . the dominant one in our relationship. . ."

    if Rogue.History.check("started_penultimate_quirk_encouraged"):
        ch_Rogue "And ah don't me to presume, but. . ."

        $ Rogue.change_face("worried1", blush = 1)

        ch_Rogue "It seems like ya enjoy takin' charge anyways."

        menu:
            extend ""
            "I will admit. . . I do enjoy wearing the pants in this relationship. . . (encourage_quirk)":
                call change_Character_stat(Rogue, "love", 0) from _call_change_Character_stat_1185

                $ Rogue.change_face("worried2", mouth = "lipbite", blush = 2) 
                
                ch_Rogue "Good." 
                
                $ Rogue.change_face("sexy", blush = 1) 
                
                ch_Rogue "Because you don't know how much ah like it when ya boss me 'round. . ." 
                
                ch_Rogue "Feelin' like ah'm truly. . . yours. . ." 
                ch_Rogue "It's a real good feelin'."

                menu:
                    extend ""
                    "I like it too. . . but let's not jump into this blindly. (encourage_quirk)":
                        $ Rogue.change_face("worried1", blush = 1)

                        call change_Character_stat(Rogue, "love", 0) from _call_change_Character_stat_1186

                        while Rogue.History.check("quirk_encouraged") < Rogue.History.check("quirk_discouraged"):
                            $ Rogue.History.update("quirk_encouraged")

                        $ Rogue.History.update("penultimate_quirk_encouraged")
                    "I don't know. . . let's not take this too far. (discourage_quirk)":
                        $ Rogue.change_face("worried2", blush = 1)

                        while Rogue.History.check("quirk_encouraged") >= Rogue.History.check("quirk_discouraged"):
                            $ Rogue.History.update("quirk_discouraged")
            "Yeah. . . but to be honest it's been making me a bit uncomfortable. I think I want to be less assertive in the future. (discourage_quirk)":
                $ Rogue.change_face("worried2")

                ch_Rogue "Ya wanna be. . . less assertive?"

                while Rogue.History.check("quirk_encouraged") >= Rogue.History.check("quirk_discouraged"):
                    $ Rogue.History.update("quirk_discouraged")
    else:
        $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Rogue "But, ah reckon you don't seem too keen on it. . ."
        ch_Rogue "Like ya don't care much for takin' charge of me."

        menu:
            extend ""
            "I haven't been. . . but I guess I wouldn't mind being a little more assertive. . . (encourage_quirk)":
                $ Rogue.change_face("worried1", blush = 1)

                ch_Rogue "So ya do wanna take charge?"

                while Rogue.History.check("quirk_encouraged") < Rogue.History.check("quirk_discouraged"):
                    $ Rogue.History.update("quirk_encouraged")

                $ Rogue.History.update("penultimate_quirk_encouraged")
            "That's true. . . I don't know if I like being so assertive. (discourage_quirk)":
                $ Rogue.change_face("worried1", blush = 1)

                ch_Rogue "So ya really don't wanna take charge?"

                while Rogue.History.check("quirk_encouraged") >= Rogue.History.check("quirk_discouraged"):
                    $ Rogue.History.update("quirk_discouraged")

    pause 1.0

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    if Rogue.History.check("penultimate_quirk_encouraged"):
        ch_Player "Look, I'm all for exploring this stuff more with you. . ."
        ch_Player "But let's not dive right into the deep end."
    else:
        ch_Player "Look, I'm not really sure about this whole dominant thing right now. . ." 
        ch_Player "But either way, let's not dive right into the deep end."
        
    ch_Player "This is a pretty significant aspect of our relationship, and we should give it the consideration is deserves."

    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue "Ah know, yer right."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Ah just know how much it's been botherin' me, not lettin' ya know how ah feel about it."
    ch_Player "I'm not saying anything needs to change just yet, but let's both take some more time to consider how we feel."

    $ Rogue.change_face("smirk2")

    ch_Rogue "That sounds real wise."

    if Rogue.History.check("penultimate_quirk_encouraged"):
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 
        
        ch_Player "Now, come here."
    else:
        $ Rogue.change_face("worried1", blush = 1) 
        
        ch_Rogue "Ya better still give me a kiss right now. . ."

    $ Rogue.change_face("kiss2", blush = 1)

    "You pull [Rogue.name] into your embrace, pressing your lips against hers."

    $ Rogue.change_face("kiss2", blush = 2)

    "She melts into your arms, and even starts using some tongue."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    "You pull away before things escalate too far."

    $ Rogue.History.update("kiss")

    ch_Rogue "Ah should go."
    ch_Rogue "Hopefully you'll come find me later."

    call remove_Characters(Rogue) from _call_remove_Characters_309

    $ ongoing_Event = False

    return