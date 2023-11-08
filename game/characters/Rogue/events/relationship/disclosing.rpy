init python:

    def Rogue_disclosing_wants_to_date_others():
        label = "Rogue_disclosing_wants_to_date_others"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_disclosing_wants_to_date_others:
    $ ongoing_Event = True

    $ Rogue.change_face("worried2")

    ch_Player "I wanted to tell you something."

    $ Rogue.change_face("worried1")

    ch_Rogue "What's got ya all bothered, [Rogue.Player_petname]?"

    $ Rogue.change_face("perplexed")

    ch_Player "Well. . . I know it's unconventional, but I'm interested in having multiple girlfriends." 

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Player "Of course we'd still be together as well."
    ch_Player "Are you okay with that?"

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Ah guess ah don't really mind. . ." 
    ch_Player "You don't?"
    ch_Rogue "Ah don't."

    $ Rogue.change_face("worried1", eyes = "right", mouth = "smirk")

    ch_Rogue "Ah saw this comin' anyway."
    ch_Rogue "It ain't no secret that yer a real hot commodity 'round here."

    $ Rogue.change_face("confused1", eyes = "right")

    ch_Player "'Hot commodity'?"
    ch_Rogue "Ya don't have to pretend 'round me, [Rogue.Player_petname]."
    ch_Player "Wha-"

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "You can have all the girlfriends ya want, so long as ya don't forget about me."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "But, ah'd really appreciate it if you could tell me who you plan on datin', before you go after 'em."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Player "Of course."

    call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_1141

    $ Rogue.History.update("told_wants_multiple_partners")

    $ ongoing_Event = False

    return

init python:

    def Rogue_disclosing_wants_to_date_Laura():
        label = "Rogue_disclosing_wants_to_date_Laura"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_disclosing_wants_to_date_Laura:
    $ ongoing_Event = True

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Ah knew you had a thing for her." 

    $ Rogue.change_face("worried1", mouth = "lipbite")

    ch_Rogue "And she's constantly askin' me questions about you."
    ch_Player "Wait, really?" 

    $ Rogue.change_face("confused1", mouth = "smirk")

    ch_Rogue "Well, sure, it's obvious yer her first crush." 

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Ah've been tryin' to help her. . . manage those feelin's." 
    ch_Player "Well, I do want to spend more time with her." 

    $ Rogue.change_face("smirk2")

    ch_Player "Is that okay with you?" 
    ch_Rogue "Ah don't mind, it'll be good for her." 

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Thanks for askin', [Rogue.Player_petname]." 

    call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_1142

    $ Rogue.knows_about.append(Laura)
    
    $ ongoing_Event = False

    return

init python:

    def Rogue_disclosing_wants_to_date_Jean():
        label = "Rogue_disclosing_wants_to_date_Jean"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_disclosing_wants_to_date_Jean:
    $ ongoing_Event = True

    $ Rogue.change_face("worried1")

    ch_Rogue "Jean?" 

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "She is real pretty, ah can see why you like her. . ."

    $ Rogue.change_face("worried1")

    ch_Player "It's not just because she's pretty." 
    ch_Player "She's been helping me out a lot lately."
    ch_Player "Both with my powers and with tutoring."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "She is super smart."
    ch_Rogue "Ain't top of her class for nothin'." 

    $ Rogue.change_face("worried2")

    ch_Rogue "Just promise you'll still be studyin' with me too sometimes." 

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Player "Of course." 
    ch_Player "You're a better tutor anyway. . ." 

    $ Rogue.change_face("smirk2")

    ch_Player "But you're okay with me spending more time with her?" 
    ch_Rogue "Ah don't mind." 

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "And, thanks for askin'. . ." 

    call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_1143

    $ Rogue.knows_about.append(Jean)

    $ ongoing_Event = False

    return