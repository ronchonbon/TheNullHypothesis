init python:

    def Rogue_enjoying_being_girlfriend():
        label = "Rogue_enjoying_being_girlfriend"

        conditions = [
            "Rogue in Partners",

            "approval_check(Rogue, threshold = [275, 275])",

            "day - EventScheduler.Events['Rogue_boyfriend'].completed_when >= 3",

            "Player.location == Player.home and not Present",

            "Rogue.is_in_normal_mood()"]
            
        waking = True

        priority = 99

        return EventClass(label, conditions, waking = waking, priority = priority)

label Rogue_enjoying_being_girlfriend:
    $ ongoing_Event = True

    call receive_text(Rogue, "Good mornin! :)") from _call_receive_text_787
    call receive_text(Rogue, "Are ya awake yet?") from _call_receive_text_788

    "You wake up to your phone going off."

    call receive_text(Rogue, "Sorry") from _call_receive_text_789
    call receive_text(Rogue, "Yer probably still sleepin this early") from _call_receive_text_790

    "The messages are coming in quickly, and by the time you rub the sleep out of your eyes, a few more come in."

    call open_texts(Rogue) from _call_open_texts_34
    call receive_text(Rogue, "Just wanted") from _call_receive_text_791
    call receive_text(Rogue, "Was wonderin") from _call_receive_text_792
    call receive_text(Rogue, "Could I please come over real quick?") from _call_receive_text_793
    call receive_text(Rogue, "Somethin's been botherin me") from _call_receive_text_794
    call receive_text(Rogue, "It ain't yer fault") from _call_receive_text_795
    call receive_text(Rogue, "But still") from _call_receive_text_796

    $ Rogue.mandatory_text_options = ["it's okay, this seems important", "are you okay? yeah, come on over", "what the hell? it's way too early for this. . . come over and let's get this over with"]
    $ temp = Rogue.mandatory_text_options[:]

    while Rogue.mandatory_text_options:
        pause

    if Rogue.text_history[-1][1] == temp[0]:
        call receive_text(Rogue, "Thank you") from _call_receive_text_797
        call receive_text(Rogue, "I wouldnt bother ya if it wasnt") from _call_receive_text_798
    elif Rogue.text_history[-1][1] == temp[1]:
        call receive_text(Rogue, "Im alright") from _call_receive_text_799
        call receive_text(Rogue, "Just somethin Ive been a bit worried bout") from _call_receive_text_800
    elif Rogue.text_history[-1][1] == temp[2]:
        call receive_text(Rogue, "Im sorry") from _call_receive_text_801
        call receive_text(Rogue, "Itll be quick") from _call_receive_text_802
        call receive_text(Rogue, "Ill be right over") from _call_receive_text_803

    call receive_text(Rogue, "Omw") from _call_receive_text_804

    pause 2.0

    hide screen phone_screen
    
    "You hop out of bed, throw some clothes on, and only get midway through brushing your teeth before someone knocks."

    call knock_on_door(times = 2) from _call_knock_on_door_55

    "That was quick. . ."
    "You finish up and open the door."

    call send_Characters(Rogue, location = Player.home, behavior = False) from _call_send_Characters_266
    
    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Hey. . ."

    $ Rogue.change_face("worried1")

    ch_Rogue "Again, ah'm real sorry for wakin' ya so early."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "Just really needed to make sure of somethin'. . ."

    $ Rogue.change_face("worried2")

    ch_Player "Make sure of something?"

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "Ah've had this worry in the back of my head for a while now. . ."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "It sure ain't like ah don't love bein' yer girlfriend."

    $ Rogue.change_face("worried1")

    ch_Rogue "But ah was worried about bringin' this up because ah thought it might upset ya. . ."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Player "[Rogue.name], what is it?"

    $ Rogue.change_face("worried2")

    pause 1.0

    $ Rogue.change_face("worried1", eyes = "down")

    ch_Rogue "It's about our relationship. . ."
    ch_Rogue "Ah've been worried. . . worried you think ah'm only with ya because yer my only choice. . ."

    $ Rogue.change_face("worried3")

    ch_Rogue "And it ain't the truth!"
    ch_Rogue "Not one bit!"

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "Ah feel like ah found somethin' even more important than a person ah can touch. . ."

    $ Rogue.change_face("worried1")

    ch_Rogue "Even if yer powers weren't like they are, you'd still be the same person."
    ch_Rogue "And that person is the one ah'm here for, not just 'cause ah can touch ya."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Player "Okay, firstly. . ."

    menu:
        extend ""
        "If something was bothering me, you need to trust that I would let you know about it, okay? You're {i}my{/i} girlfriend - tell me whenever something's worrying you. (encourage_quirk)":
            call change_Character_stat(Rogue, "trust", medium_stat) from _call_change_Character_stat_234

            $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

            ch_Rogue "Ah'm sorry. . ." 
            ch_Rogue "Ah was just worried. . ." 
            
            $ Rogue.change_face("worried1", blush = 1) 
            
            ch_Rogue "In the future, ah will make sure you know sooner." 
        "Hey, don't bottle stuff up because you're afraid it might upset me. We're in this together. (discourage_quirk)": 
            call change_Character_stat(Rogue, "love", medium_stat) from _call_change_Character_stat_235
            call change_Character_stat(Rogue, "trust", small_stat) from _call_change_Character_stat_236

            $ Rogue.change_face("worried2")

            ch_Rogue "Ah know, ah'm sorry. . ." 
            
            $ Rogue.change_face("worried1", mouth = "smirk") 
            
            ch_Rogue "Yer right." 
            
    $ Rogue.change_face("worried1")

    ch_Player "And, secondly, that's what you were so worried about?"
    ch_Rogue "Yeah. . ."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "Ah just heard some people gossipin'. . ."

    $ Rogue.change_face("worried2")

    ch_Player "You don't need to worry."
    ch_Player "I know you're not that kind of person."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Player "You're sweet as pie on the outside. . ."

    $ Rogue.change_face("confused1", mouth = "smirk")

    ch_Player "But you're also a hopeless romantic, no way you'd settle for anything less than the dream boyfriend."

    $ Rogue.change_face("confused1", eyes = "squint", mouth = "smirk")

    ch_Rogue "And that's what you are, huh?" 

    $ Rogue.change_face("sly")

    ch_Rogue "Then ah'd sure appreciate a kiss from my 'dream boyfriend.'"
    ch_Player "Happy to oblige."

    $ Rogue.change_face("kiss2", blush = 1)

    "You pull [Rogue.name] into a gentle kiss, and hold her close for a while."

    $ Rogue.change_face("smirk2", eyes = "closed")

    "She pulls away from the kiss and into a hug, leaning her head on your shoulder."

    $ Rogue.History.update("kiss")

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Thanks for listenin' to my concerns. . ."
    ch_Rogue "Ah really appreciate it."
    ch_Rogue "Ah think ah'd like to stick by you for a little while."

    $ Party.append(Rogue)

    $ ongoing_Event = False

    return