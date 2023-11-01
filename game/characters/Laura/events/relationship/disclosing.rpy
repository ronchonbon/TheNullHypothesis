init python:

    def Laura_disclosing_wants_to_date_others():
        label = "Laura_disclosing_wants_to_date_others"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Laura_disclosing_wants_to_date_others:
    $ ongoing_Event = True

    $ Laura.change_face("confused1")

    ch_Player "There's something I think you should know." 
    ch_Player "I'm interested in having multiple girlfriends. . ." 

    $ Laura.change_face("confused3")

    ch_Laura "Is this a common thing?" 
    ch_Player "Not really. . ." 

    $ Laura.change_face("confused1") 

    ch_Laura "Is this because you're the most attractive male at the Institute and are expecting other women to also want a relationship with you?"
    ch_Player "No, I. . . wait, 'the most attractive'?"

    $ Laura.change_face("neutral") 

    ch_Laura "Yes, it's obvious."
    ch_Player "Wh-"
    ch_Laura "Regardless, I don't care."
    ch_Player "You don't?"
    ch_Laura "No." 

    $ Laura.change_face("smirk2")

    ch_Laura "I only care that you're mine." 

    $ Laura.change_face("confused1", mouth = "smirk")

    ch_Laura "As long as you're here when I want, and tell me who you plan on dating." 
    ch_Player "I can do that."

    # $ Laura.change_face("sly")

    # ch_Laura "And, I'm only interested in having {i}one{/i} boyfriend." 

    $ Laura.change_face("neutral", eyes = "right")

    ch_Laura ". . . thank you for letting me know." 

    $ Laura.change_face("smirk2")

    ch_Player "You're welcome."

    call change_Girl_stat(Laura, "trust", 5) from _call_change_Girl_stat_642

    $ Laura.History.update("told_wants_multiple_girlfriends")

    $ ongoing_Event = False

    return

init python:

    def Laura_disclosing_wants_to_date_Rogue():
        label = "Laura_disclosing_wants_to_date_Rogue"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Laura_disclosing_wants_to_date_Rogue:
    $ ongoing_Event = True

    $ Laura.change_face("confused1")

    ch_Laura "You're interested in Rogue?" 
    ch_Player "I am, and I plan on spending more time with her." 

    $ Laura.change_face("smirk2")

    ch_Player "Is that okay with you?" 
    ch_Laura "Yes."

    $ Laura.change_face("smirk2", eyes = "right", blush = 1)

    call change_Girl_stat(Laura, "trust", 5) from _call_change_Girl_stat_643

    ch_Laura "Thank you for asking. . ." 

    $ Laura.change_face("smirk2", blush = 1)

    ch_Laura "It makes sense, she is very attractive." 

    $ Laura.change_face("confused1", mouth = "smirk", blush = 1)

    ch_Laura "It's clear she's infatuated with you as well." 

    $ Laura.change_face("sly", blush = 1)

    ch_Laura "I don't expect you'll have a difficult time making her yours." 

    $ Laura.change_face("confused1")

    ch_Player "I don't know if I'd phrase it like that. . ." 

    $ Laura.knows_about.append(Rogue)
    
    $ ongoing_Event = False

    return

init python:

    def Laura_disclosing_wants_to_date_Jean():
        label = "Laura_disclosing_wants_to_date_Jean"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Laura_disclosing_wants_to_date_Jean:
    $ ongoing_Event = True

    $ Laura.change_face("confused1")

    ch_Laura "The annoying one with the red hair?"

    $ Laura.change_face("neutral") 

    ch_Player ". . . I don't think she's annoying." 
    ch_Player "But yes, red hair." 
    ch_Player "I plan on spending more time with her." 

    $ Laura.change_face("smirk2") 

    ch_Player "Is that okay?" 
    ch_Laura "Fine."

    $ Laura.change_face("smirk2", eyes = "right", blush = 1)

    call change_Girl_stat(Laura, "trust", 5) from _call_change_Girl_stat_931

    ch_Laura "Thank you for asking. . ." 

    $ Laura.change_face("neutral")

    ch_Laura "But I don't fully understand why you're interested in her." 

    $ Laura.change_face("confused1", blush = 1)

    ch_Laura "Is it just because you're attracted to her body?" 

    $ Laura.change_face("angry1")

    ch_Laura "Her personality makes me angry. . ." 

    $ Laura.change_face("confused1")

    ch_Player "No, it's more than just physical." 

    $ Laura.change_face("neutral", eyes = "squint")

    ch_Player "And cut her some slack, she has a lot going on. . ."

    $ Laura.knows_about.append(Jean)

    $ ongoing_Event = False

    return