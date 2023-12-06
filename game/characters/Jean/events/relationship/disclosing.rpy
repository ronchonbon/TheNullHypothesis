init python:

    def Jean_disclosing_wants_to_date_others():
        label = "Jean_disclosing_wants_to_date_others"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_disclosing_wants_to_date_others:
    $ ongoing_Event = True

    ch_Player "I need to tell you something. . ." 

    $ Jean.change_face("confused1")

    ch_Jean "What's up?"
    ch_Player "Well. . . to be completely honest. . ."

    $ Jean.change_face("appalled3")

    ch_Player "I'm interested in having multiple girlfriends."
    ch_Jean "You're interested in what?!" 
    ch_Player ". . ."

    $ Jean.change_face("appalled2")

    ch_Player "In having multiple girlfriends. . ." 

    $ Jean.change_face("suspicious2")

    ch_Player "I just wanted to make sure you knew. . . before we got more involved. . ."

    $ Jean.change_face("suspicious2", eyes = "right")

    ch_Jean "I guess it makes sense. . ."

    $ Jean.change_face("confused1", eyes = "squint")

    ch_Jean "I mean, look at you. . ." 

    $ Jean.change_face("confused1", eyes = "down")

    pause 1.0

    $ Jean.change_face("suspicious1")

    ch_Jean "Hmm. . ."

    $ Jean.change_face("neutral")

    ch_Jean "Fine, I'll let you have your fun. . ."
    ch_Player "Fine?"

    $ Jean.change_face("confused1")

    ch_Jean "But only under a few conditions."

    $ Jean.change_face("suspicious1")

    ch_Jean "As long as your. . . 'other girls' know I'm the main one. . ." 

    $ Jean.change_face("worried2")

    ch_Player "[Jean.name], I'm not just talking about having casual relationships with other girls. . ."
    ch_Player "I mean to take my relationships with them as seriously as I do with ours."

    $ Jean.change_face("worried1", eyes = "right")

    ch_Jean "Oh. . ."

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Jean "Well, you better at least tell me before you try dating another girl."
    ch_Player "I can do that."

    $ Jean.change_face("confused1", mouth = "smirk")

    ch_Jean "I won't have anyone playing with my man's heart. . ."

    $ Jean.change_face("sly")

    ch_Jean "And they better not hog all of your attention."
    ch_Jean "Thanks for letting me know. . ."

    call change_Character_stat(Jean, "trust", 0) from _call_change_Character_stat_949

    $ Jean.History.update("told_wants_multiple_partners")

    $ ongoing_Event = False

    return

init python:

    def Jean_disclosing_wants_to_date_Rogue():
        label = "Jean_disclosing_wants_to_date_Rogue"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_disclosing_wants_to_date_Rogue:
    $ ongoing_Event = True

    $ Jean.change_face("confused1", mouth = "smirk")

    ch_Jean "Rogue?" 

    $ Jean.change_face("smirk2")

    ch_Player "Yeah, is that okay?" 
    ch_Player "I really like her, and I think she feels the same way." 
    ch_Player "Plus, she's just a really nice person in general."
    ch_Jean "That's true." 

    $ Jean.change_face("confused1", eyes = "squint", mouth = "smirk")

    ch_Jean "And duh, it's kinda obvious she's super into you." 

    $ Jean.change_face("sly")

    ch_Jean "Not to mention, you're basically the only person she can date."

    $ Jean.change_face("smirk2")

    ch_Jean "But I have a feeling she'd be into you even if that wasn't the case. . ."
    ch_Player "So you don't mind if I start spending more time with her?"  

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Jean "Nope." 
    ch_Jean "And. . . thanks for asking." 

    call change_Character_stat(Jean, "trust", 0) from _call_change_Character_stat_950

    $ Jean.knows_about.append(Rogue)

    $ ongoing_Event = False

    return

init python:

    def Jean_disclosing_wants_to_date_Laura():
        label = "Jean_disclosing_wants_to_date_Laura"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_disclosing_wants_to_date_Laura:
    $ ongoing_Event = True

    $ Jean.change_face("perplexed", blush = 1)

    ch_Jean "Her?!" 

    $ Jean.change_face("confused1")

    ch_Jean "I know she's like, obsessed with you." 

    if Laura.History.check("encouraged_quirk") >= Laura.History.check("quirk_discouraged"):
        ch_Jean "Doesn't she, like, stalk you. . . ?"
    
    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Jean "And, isn't she kinda mean?"

    $ Jean.change_face("worried1")

    ch_Player "She's not mean on purpose." 
    ch_Player "She's just been through a lot and isn't great at social interactions yet."

    $ Jean.change_face("sly")

    ch_Jean "Well, she is really cute. . . in a dangerous kinda way." 

    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Jean "I guess you like the aggressive ones, huh?"
    ch_Player "{i}Ahem{/i}. . ." 

    $ Jean.change_face("smirk2")

    ch_Player "So, is it okay if I start to spend more time with her?"
    ch_Jean "Yeah, I guess it's fine." 

    $ Jean.change_face("confused1", mouth = "smirk")

    ch_Jean "Just try not to get clawed." 

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Jean "And. . . thanks for asking first." 

    call change_Character_stat(Jean, "trust", 0) from _call_change_Character_stat_951

    $ Jean.knows_about.append(Laura)
    
    $ ongoing_Event = False

    return