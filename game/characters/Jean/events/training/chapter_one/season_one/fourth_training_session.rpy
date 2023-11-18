init python:

    def Jean_chapter_one_season_one_fourth_training_session():
        label = "Jean_chapter_one_season_one_fourth_training_session"

        conditions = [
            "chapter == 1 and season == 1",
            "Jean.History.check('trained_with_Player', tracker = 'season') == 3",
            "Player.training == Jean and Jean.training"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Jean_chapter_one_season_one_fourth_training_session:
    $ ongoing_Event = True

    $ Jean.change_face("worried1")

    ch_Player "Everything okay?"
    ch_Jean "I'm just worried. . ."
    ch_Jean "Doesn't feel like I've made all that much progress with my. . . situation." 

    $ Jean.change_face("sad")

    menu:
        extend ""
        "But you have been making progress, that's all that matters.":
            $ Jean.change_face("worried1") 
            
            ch_Player "Like you said to me last time, these things can take a while." 
           
            $ Jean.change_face("neutral")

            ch_Jean "I know. . . " 
            
            $ Jean.change_face("smirk1") 
            
            ch_Jean "Slow and steady wins the race, right?" 
            ch_Jean "And you've been a big help, thanks." 
            
            $ Jean.change_face("smirk2") 
            
            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_176 
            call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_177
        "I'm sure it'll work out. . .":
            $ Jean.change_face("worried1", eyes = "right")

            ch_Jean "Yeah. . ." 
            
            $ Jean.change_face("neutral") 
            
            ch_Jean "You're right, it will." 
            
            $ Jean.change_face("smirk1") 
            
            ch_Jean "Of course it will." 
            ch_Jean "Thanks." 
            
            $ Jean.change_face("smirk2") 
            
            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_178
        "Yeah. . . I'd be worried too.":
            $ Jean.change_face("angry1", eyes = "right")

            ch_Jean "That's not very reassuring. . ." 
            
            $ Jean.change_face("neutral") 
            
            ch_Jean "Whatever." 
            ch_Jean "I'll figure it out." 
            
            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_179

    $ Jean.change_face("smirk1")

    ch_Jean "Alright, time to get warmed up."

    $ fade_to_black(0.4)

    "You both go through a quick warmup."
    "She seems to find excuses for you to 'help her stretch out.'"

    $ fade_in_from_black(0.4)

    $ Jean.change_face("smirk1", blush = 1)

    ch_Player "It seems like your idea last time worked pretty well, should we start with that again?" 

    $ Jean.change_face("confused1")

    ch_Jean "Hmm." 

    $ Jean.change_face("neutral")

    ch_Jean "Yeah, let's start with what we know works."

    call Jean_activate_psychic from _call_Jean_activate_psychic_7

    $ fade_to_black(0.4)

    "You spend the next hour or so with [Jean.name], trying to wrangle your power under control, so the ball doesn't fall on your head."
    "This time you're successful maybe 30\% of the time. . ."

    $ fade_in_from_black(0.4)

    call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_7

    $ Jean.change_face("smirk2")

    ch_Jean "Good job!" 
    ch_Jean "That was definitely better than last time."
    ch_Player "Thanks."
    ch_Player "Doesn't feel any different. . ."
    ch_Player "But it's working I guess."

    $ Jean.change_face("worried1")

    ch_Jean "Don't worry, you'll get there."

    $ Jean.change_face("smirk1")

    ch_Jean "Now try without touching me."
    ch_Jean "See if you can let the ball come to you."

    call Jean_activate_psychic from _call_Jean_activate_psychic_8

    $ fade_to_black(0.4)

    "This continues to be much more difficult for whatever reason."
    "After many tries, you only manage to let the ball get within a foot of yourself before it falls."
    "You develop a pretty killer headache."
    "The rest of the session is spent lightly sparring with [Jean.name] before she starts working her own powers."
    "She's making some progress too and even manages to maintain control the entire time."

    $ fade_in_from_black(0.4)

    call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_8

    $ Jean.change_face("worried1")

    ch_Player "Nice! I could tell that was more than last time, and you didn't even need my help." 

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Jean "I still almost lost it at the end there. . ." 

    $ Jean.change_face("smirk1")

    ch_Jean "But thanks." 
    ch_Jean "I still don't even know why it's happening." 

    $ Jean.change_face("worried1", eyes = "right")

    ch_Player "Don't worry, we'll figure it out." 

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "You're right, together. . ." 

    $ Jean.change_face("smirk2", blush = 1) 

    ch_Jean "Okay, that's it for today." 
    ch_Jean "I gotta go, bye!"

    call remove_Characters(Jean) from _call_remove_Characters_53
    
    $ ongoing_Event = False

    return