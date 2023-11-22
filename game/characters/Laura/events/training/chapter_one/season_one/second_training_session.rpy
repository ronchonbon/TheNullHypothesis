init python:

    def Laura_chapter_one_season_one_second_training_session():
        label = "Laura_chapter_one_season_one_second_training_session"

        conditions = [
            "chapter == 1 and season == 1",

            "Laura.History.check('trained_with_Player', tracker = 'season') == 1",
            
            "Player.behavior == 'training' and Laura in Player.behavior_Partners and Laura.behavior == 'training'"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Laura_chapter_one_season_one_second_training_session:
    $ ongoing_Event = True
        
    ch_Player "Ready to warm up?" 

    $ Laura.change_face("confused1")

    ch_Laura "Of course."

    $ fade_to_black(0.4)

    "Just like last time, [Laura.name] puts you through a 'warm up' that would make any athlete beg for mercy."
    "When it's finally over, you have to take a few minutes just to catch your breath."

    $ fade_in_from_black(0.4)

    $ Laura.change_face("neutral")

    ch_Player "*huff* How is this. . . *huff* a warmup. . ." 

    $ Laura.change_face("confused1")

    "[Laura.name] doesn't even look like she broke a sweat."
    ch_Laura "For you? It's not."
    ch_Laura "Learning technique while exhausted is part of the training."
    ch_Laura "For me, that was a slow walk." 

    $ Laura.change_face("neutral")

    ch_Player "You're. . . *huff*. . . a monster. . ." 

    $ Laura.change_face("sly")

    "[Laura.name] doesn't take pity on you and, after the fastest few minutes of your life, she gets right into teaching you simple defensive techniques."

    $ Laura.change_face("smirk2")

    $ fade_to_black(0.4)

    "She's lightning fast and throws you on your ass more than once while demonstrating how to defend yourself." 
    "Her 'lessons' are quick. . . and painful." 
    "But they're very effective at ensuring you don't make the same mistake twice. Especially when you faceplant after each one."

    pause 1.0

    with small_screenshake

    $ fade_in_from_black(0.4)

    $ Laura.change_face("angry1")

    ch_Player "Oof. . . shit." 
    "That last throw felt more forceful than usual."
    ch_Player "Can't we move on to offensive stuff or something?" 

    $ Laura.change_face("confused1")

    ch_Player "Ya'know. . . techniques where I don't always end up on my ass?"
    ch_Laura "Why would we move on to something more advanced when you're obviously still inept?" 

    $ Laura.change_face("angry2")

    ch_Laura "When you can defend yourself satisfactorily, then we will move on." 
    "She proceeds to teach you 'how to defend yourself' for the next few hours."

    $ Laura.change_face("surprised2")

    pause 1.0

    $ Laura.change_face("angry1")

    "You can tell she's getting increasingly irritated the more she has to touch you, either to correct your form or to give you a beating."

    $ Laura.change_face("angry1", blush = 1)

    "Seems like this only makes her want to beat you even more. . ."

    $ Laura.change_face("furious", blush = 1)

    ". . ."

    pause 1.0

    with small_screenshake

    ch_Laura "Alright, that's enough." 

    $ Laura.change_face("angry1")

    ch_Laura "You can barely keep your hands up." 
    ch_Player "{size=-5}Thank god{/size}. Alright, I'll se. . ." 

    $ Laura.change_face("confused1")

    ch_Laura "Did you think we were done?"
    ch_Player "Wha. . ." 

    $ Laura.change_face("neutral")

    "Apparently the 'warm up' at the start wasn't enough, and she pushes you through more calisthenic exercises and repetitions than you can count."
    ch_Player "*huff* This can't be healthy. . . *huff* "
    ch_Player "*huff* Isn't there something called rhabdomyol-" 
    "Your legs give out and you hit the floor." with small_screenshake

    $ Laura.change_face("smirk2")

    ch_Player "*huff* Shit. . . *huff*"
    ch_Laura "Okay, now we're done."
    "She just watches, amused, as you struggle to stand up."
    ch_Player "Were you just waiting for my legs to give out before ending the session?" 

    $ Laura.change_face("neutral")

    ch_Laura "Yes." 
    ch_Player "At least you're honest. . ."
    ch_Player "We're actually done? Because I can barely walk." 
    ch_Laura "Yes, your form and technique are still atrocious, but there was. . . progress."
    ch_Player "Thanks. . ."
    ch_Laura "You can leave now, I will stay for a while longer."
    ch_Player "You're not done?!" 

    $ Laura.change_face("confused1")

    ch_Laura "No. . . it was at least a decent warm up in the end." 

    $ Laura.change_face("neutral")
    
    call remove_Characters(Laura) from _call_remove_Characters_131

    "With that, she walks away and gets right into more training."

    $ ongoing_Event = False

    return