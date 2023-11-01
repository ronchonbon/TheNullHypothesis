init python:

    def Jean_chapter_one_season_four_training_sessions():
        label = "Jean_chapter_one_season_four_training_sessions"

        conditions = [
            "season == 4",
            "Jean.History.check('trained_with_Player', tracker = 'season') >= 1",
            "Player.training == Jean and Jean.training"]

        priority = 99
        repeatable = True

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label Jean_chapter_one_season_four_training_sessions:
    $ ongoing_Event = True

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("smirk2")

        ch_Jean "C'mon, [Jean.Player_petname]."
        ch_Jean "Let's start."

        $ Jean.change_face("smirk2", mouth = "lipbite")

        ch_Jean "I'm gonna need some help stretching." 
        "You start with a warm up, for your bodies but also for your powers."

        $ Player.power = 50

        call Jean_activate_psychic from _call_Jean_activate_psychic_1

        "You can enable and disable your power with relative ease, but still not nearly as well as [Jean.name]."  
        "Afterwards, she helps you focus and work on controlling just how much of your powers you use at a time."
        "It's not easy and takes a lot of effort, but you're getting better, slowly but surely."

        $ Jean.change_face("sly")

        ch_Jean "Now, I wanna see how much progress you've made with [Laura.name] so far."
        ch_Jean "No power for you this time, but I'm special so I can use mine." 
        "You show her what you can do."

        pause 1.0

        if Laura.History.check("trained_with_Player", tracker = "season") >= 15:
            $ Jean.change_face("surprised3") 
            
            "You've been just as dedicated to training with [Laura.name] as you were with [Jean.name], if not more so." 
            "It shows, and you're unrecognizable when compared to your old self." 
            "Of course, all the training in the world can't overcome the advantages [Jean.name]'s power gives her." 
            
            $ Jean.change_face("confused1", eyes = "squint", mouth = "smirk") 
            
            ch_Jean "Impressive."
        else:
            $ Jean.change_face("worried1", mouth = "smirk") 
            
            "You've trained with [Laura.name] a lot, but maybe haven't been quite as dedicated as you could've been." 
            "Nevertheless, your body is now capable of some pretty impressive things during a fight." 
            "It's still not nearly enough to overcome all the advantages [Jean.name]'s power gives her." 
            ch_Jean "You're getting much better. . ."

        $ Player.power = 0

        call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_1

        $ Jean.change_face("smirk2")

        ch_Jean "My turn."

        call Jean_activate_psychic from _call_Jean_activate_psychic_2

        "[Jean.name] moves to show off all that she's now capable off."
        "If she used even a fraction of this much power just a few months ago, she wouldn't have a chance of keeping control."

        call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_2

        $ Jean.change_face("worried1", mouth = "smirk") 

        ch_Jean "I think I've gotten pretty far. . . right?" 
        ch_Player "You really have."
        ch_Player "More impressive than ever."

        $ Jean.change_face("smirk2") 

        ch_Jean "Thanks, [Jean.Player_petname]."
        ch_Jean "That goes for you too."
        ch_Jean "I'll see you later."
    elif dice_roll == 2:
        $ Jean.change_face("smirk2") 

        ch_Player "Ready to start, [Jean.petname]?"
        ch_Jean "Yep!"
        ch_Jean "C'mon, help me stretch."

        $ fade_to_black(0.4)

        "You do help her stretch, and the warm up is both for your bodies and your powers."

        $ Player.power = 25

        "The control exercises have been getting easier, and turning your power on and off is becoming second nature."
        "Your progress towards controlling the amount, however, is much slower."
        "It's possible, but much more of a strain on your mind, and you can only handle doing it for minutes at a time."
        "After a quick sparring session, while simultaneously trying to do it, is pretty exhausting."

        $ Player.power = 0

        $ fade_in_from_black(0.4)

        $ Jean.change_face("worried1", mouth = "smirk")

        ch_Jean "Don't worry, that was better than last time."
        ch_Jean "I can tell."
        ch_Player "Thanks. . ."

        $ Jean.change_face("smirk2")

        call Jean_activate_psychic from _call_Jean_activate_psychic_3

        ch_Jean "My turn."
        "She spends a while flaunting her own powers and her masterful control over them."
        "It's a shame there isn't much crossover between how she describes her power working."
        "You're content to sit back and watch [Jean.name] do her thing."

        $ Jean.change_face("worried2")

        $ Player.power = 25

        with small_screenshake

        "And stop things when it goes too far. . ."

        $ Player.power = 0

        call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_3

        $ Jean.change_face("worried1", mouth = "smirk")

        ch_Jean "Thanks. . ."
        ch_Jean "Got a bit carried away there."
        ch_Player "Still wish I had even ten percent as much mastery over my powers as you do."

        $ Jean.change_face("sly") 

        ch_Jean "You little brown noser."

        $ Jean.change_face("smirk2") 

        ch_Jean "Not saying you should stop the flattery. . ."
        ch_Jean "But that's enough for today."
        ch_Jean "See ya later, [Jean.Player_petname]."
    elif dice_roll == 3:
        $ Jean.change_face("smirk2") 

        ch_Jean "Wanna start, [Jean.Player_petname]?"
        ch_Player "Yep, I'm good to go."

        $ Jean.change_face("sly")

        ch_Jean "Good, now help me stretch out."

        $ fade_to_black(0.4)

        "You do, and she gets a bit handsy while returning the favor. . ."
        "The warm up is quick, and then you get into the actual training."

        $ Player.power = 25

        "You can feel your connection with the powers inside you strengthening by the day."
        "Unfortunately, while that makes it easier to access and activate them, it doesn't do much to help your control over them."
        "It still takes quite a bit of mental effort to control how much you use at a time."

        $ fade_in_from_black(0.4)

        $ Player.power = 0

        $ Jean.change_face("worried1")

        "After giving yourself a proper headache, [Jean.name] thinks it's probably a good idea to skip sparring for today, so you don't strain yourself too much."
        "Also so you'll be able to stop her from going out of control, because you can tell she's still fairly insecure about it."

        call Jean_activate_psychic from _call_Jean_activate_psychic_4

        "Despite her concerns, she manages to keep things under control and doesn't actually need your help anyway."

        $ Jean.change_face("worried1", mouth = "smirk")

        ch_Jean "Sorry. . . just felt a bit off today."
        ch_Jean "Worried something was gonna go wrong."
        ch_Player "Don't worry about it."
        ch_Player "You know I'm happy to help."

        $ Jean.change_face("smirk2") 

        ch_Jean "Thanks again, [Jean.Player_petname]."
        ch_Jean "That's enough for today."
        ch_Jean "I'll see you later." 

        call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_4

    call remove_Characters(Jean) from _call_remove_Characters_51

    call change_Girl_stat(Jean, "trust", 10) from _call_change_Girl_stat_160

    $ ongoing_Event = False

    return