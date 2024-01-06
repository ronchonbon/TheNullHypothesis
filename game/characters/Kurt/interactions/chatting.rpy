label Kurt_chatting(line):
    if line == "Can you tell me anything about. . . ?":
        menu:
            "Can you tell me anything about. . . ?"
            "[Rogue.name]?" if Rogue.History.check("met"):
                if approval_check(Rogue, threshold = "dating") and Rogue not in Partners:
                    $ Kurt.change_face("confused1") 
                    
                    ch_Kurt "Zat one?" 
                    
                    $ Kurt.change_face("happy") 
                    
                    ch_Kurt "I sink she has quite zee crush on you." 
                    ch_Kurt "Everyone can tell." 
                    ch_Kurt "Vould be a nice pairing in my opinion."
                else:
                    $ Kurt.change_face("confused1") 

                    ch_Kurt "Vat about her?" 
                    
                    $ Kurt.change_face("neutral") 
                    
                    ch_Kurt "I'd say vee are friends, not terribly close." 
                    ch_Kurt "She started here around zee same time as me." 
                    
                    $ Kurt.change_face("sad") 

                    ch_Kurt "She vas not so friendly viz anyone in zee beginning."
            "[Laura.name]?" if Laura.History.check("met"):
                if approval_check(Laura, threshold = "dating") and Laura not in Partners:
                    $ Kurt.change_face("confused1") 
                    
                    ch_Kurt "Vell, she is quite formidable." 
                    
                    $ Kurt.change_face("happy") 
                    
                    ch_Kurt "Alzough I'm sure you're already avare of zat." 
                    
                    $ Kurt.change_face("sad") 
                    
                    ch_Kurt "Many people vere not happy when she vas brought here. . ." 
                    ch_Kurt "On account of. . . zee people she killed. . ."
                else:
                    $ Kurt.change_face("confused1") 
                    
                    ch_Kurt "Can't say I know much about zat one." 
                    ch_Kurt "She hasn't been at zee mansion for very long, only a month or two longer zan you." 
                    
                    $ Kurt.change_face("sad") 

                    ch_Kurt "She is not very friendly. . ." 
                    ch_Kurt "Doesn't let anyone get close." 
            "[Jean.name]?" if Jean.History.check("met"):
                if approval_check(Jean, threshold = "dating") and Jean not in Partners:
                    $ Kurt.change_face("confused1") 
                    
                    ch_Kurt "Apparently she dated the leader of zee X-Men, Scott, several years ago. . ." 
                    
                    $ Kurt.change_face("happy") 
                    
                    ch_Kurt "I hear it vas quite zee drama." 
                    ch_Kurt "Don't sink she has tried again since." 
                else:
                    $ Kurt.change_face("confused1") 
                    
                    ch_Kurt "Vell, she is not our age." 
                    ch_Kurt "A few years older I believe." 
                    
                    $ Kurt.change_face("neutral") 
                    
                    ch_Kurt "Everbody knows she is top of her class." 
                    
                    $ Kurt.change_face("confused1") 
                    
                    ch_Kurt "Being smart seems to be a large part of her personality. . ."

    if line == "Any tips regarding. . . ?":
        menu:
            "Any tips regarding. . . ?"
            "The mall?":
                if EventScheduler.Events["ch1_Sentinel_attack"].completed and not EventScheduler.Events["ch1_mutant_hate"].completed:
                    $ Kurt.change_face("sad") 
                    
                    ch_Kurt "Zee mall is. . ." 
                    ch_Kurt "Viz everysing zat has happened lately." 
                    ch_Kurt "Someone who looks like a mutant, being seen in public. . ." 
                    ch_Kurt "I vill just say zee harassment has been getting vorse." 
                    ch_Kurt "Be careful mein Bruder."
                else:
                    $ dice_roll = renpy.random.randint(1, 2)

                    if dice_roll == 1:
                        $ Kurt.change_face("happy") 
                        
                        ch_Kurt "If you veren't avare, zee clothing shops get re-stocked seasonally." 
                        ch_Kurt "If zere is a particular outfit you are looking for, you may have to vait until zee next quarter."
                    elif dice_roll == 2:
                        $ Kurt.change_face("happy") 
                        
                        ch_Kurt "I have heard rumors zat zee mall may get renovations soon." 
                        ch_Kurt "Vee both know vat 'soon' really means."
                        ch_Kurt "But, it iz nice to know zere are plans for new locations." 
            "Dates?":
                $ Kurt.change_face("confused1", mouth = "smile") 
                
                ch_Kurt "Vell, I have shown you zee popular locations." 
                
                $ Kurt.change_face("happy") 
                
                ch_Kurt "I suspect different girls may prefer different sings." 
                ch_Kurt "Vether it may be date locations, movie genres, types of cuisine." 
                ch_Kurt "Just keep zeir preferences in mind, I have faiz in you mein Bruder."

    if line == "Hey, about that comic book store in town.":
        $ EventScheduler.Events["ch1_mutant_hate"].start()
        
    return

label Kurt_busy:
    if Kurt.behavior == "in_class":
        $ Kurt.change_face("neutral") 
        
        ch_Kurt "Not good." 
        ch_Kurt "I vill never get used to zese lectures." 
        ch_Kurt "Vish I could just 'port avay."
    elif Kurt.behavior == "training":
        $ Kurt.change_face("happy") 

        ch_Kurt "Good, sanks." 
        ch_Kurt "Training alvays feels good."

        $ Character_picker_disabled = True
        
        call Kurt_teleports_out from _call_Kurt_teleports_out_3
        call move_location(Player.location) from _call_move_location_21
    else:
        if EventScheduler.Events["ch1_Sentinel_attack"].completed and not EventScheduler.Events["ch1_mutant_hate"].completed:
            $ Kurt.change_face("sad") 
            
            ch_Kurt "I am okay." 
            ch_Kurt "But sings are getting vorse." 
            ch_Kurt "People are angry, and zey blame us." 
            ch_Kurt "Especially zose of us who. . . look different." 
        else:
            $ Kurt.change_face("confused1") 
            
            ch_Kurt "I am good, sanks." 
            
            $ Kurt.change_face("neutral") 
            
            ch_Kurt "So busy ven I could be reading comics. . ."

    return

label Kurt_busy_asked_once:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Kurt.change_face("worried1") 
        
        ch_Kurt "You alright, Bruder?" 
    
        $ Kurt.change_face("confused1") 

        ch_Kurt "I sink you just asked me zat."
    elif dice_roll == 2:
        $ Kurt.change_face("confused1")

        ch_Kurt "Uh. . . you just asked me zat?"
    elif dice_roll == 3:
        $ Kurt.change_face("confused1")

        ch_Kurt "Hmm?"

    return

label Kurt_busy_asked_twice:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Kurt.change_face("angry1") 
        
        ch_Kurt "It is no longer funny." 

        if Player.location == Kurt.location:
            $ Character_picker_disabled = True
                
            call Kurt_teleports_out from _call_Kurt_teleports_out_4
            call move_location(Player.location) from _call_move_location_24
    elif dice_roll == 2:
        $ Kurt.change_face("confused1") 
        
        ch_Kurt "Dude. . ."
    elif dice_roll == 3:
        $ Kurt.change_face("angry1")

        ch_Kurt "Okay, enough now. . ."

    return

label Kurt_busy_late:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Kurt.change_face("smirk1") 

        ch_Kurt "I am doing fine." 
        ch_Kurt "Tired." 
        ch_Kurt "I sink I vill go to bed, gute Nacht."
    elif dice_roll == 2:
        $ Kurt.change_face("smirk1") 

        ch_Kurt "Good, just off to bed."
        ch_Kurt "Gute Nacht."
    elif dice_roll == 3:
        $ Kurt.change_face("smirk1")

        ch_Kurt "About to go to sleep, gute Nacht!"

    return

label Kurt_busy_late_asked_once:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Kurt.change_face("confused1") 
        
        ch_Kurt "I said I'm going to bed."
    elif dice_roll == 2:
        $ Kurt.change_face("confused1") 

        ch_Kurt "I. . . are you messing viz me again?"
    elif dice_roll == 3:
        $ Kurt.change_face("confused1") 

        ch_Kurt "You seem pretty tired too, [Player.first_name]."

    return

label Kurt_busy_late_asked_twice:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Kurt.change_face("angry1") 
        
        ch_Kurt "Stop joking around."

        if Player.location == Kurt.location:
            $ Character_picker_disabled = True
                
            call Kurt_teleports_out from _call_Kurt_teleports_out_5
            call move_location(Player.location) from _call_move_location_25
    elif dice_roll == 2:
        $ Kurt.change_face("angry1", eyes = "closed") 

        ch_Kurt "Man, it is too late for zis."

        if Player.location == Kurt.location:
            $ Character_picker_disabled = True
                
            call Kurt_teleports_out from _call_Kurt_teleports_out_8
            call move_location(Player.location) from _call_move_location_1
    elif dice_roll == 3:
        $ Kurt.change_face("angry1") 

        ch_Kurt "I sink you need to go to bed too."

        if Player.location == Kurt.location:
            $ Character_picker_disabled = True
                
            call Kurt_teleports_out from _call_Kurt_teleports_out_9
            call move_location(Player.location) from _call_move_location_63

    return

label Kurt_talk_later:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Kurt.change_face("smirk2")

        ch_Kurt "Later dude."
    elif dice_roll == 2:
        $ Kurt.change_face("pleased1") 

        ch_Kurt "Talk to you later!"
    elif dice_roll == 3:
        $ Kurt.change_face("smirk1") 

        ch_Kurt "See you around!"

    return

label Kurt_dismiss:
    $ Kurt.change_face("confused1")

    if len(Present) >= 2:
        ch_Player "Hey [Kurt.name], could you give us some room?"
    else:
        ch_Player "Hey [Kurt.name], could you give me some room?"

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Kurt.change_face("smirk2") 

        ch_Kurt "Later dude."
    elif dice_roll == 2:
        $ Kurt.change_face("pleased1") 

        ch_Kurt "Sure, talk to you later!"
    elif dice_roll == 3:
        $ Kurt.change_face("smirk1") 

        ch_Kurt "Okay, see you around!"

    return True

label Kurt_answering_phone:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        ch_Kurt "Hallo?"
    elif dice_roll == 2:
        ch_Kurt "Hey [Player.first_name]!"
    elif dice_roll == 3:
        ch_Kurt "Vat's up?"

    return