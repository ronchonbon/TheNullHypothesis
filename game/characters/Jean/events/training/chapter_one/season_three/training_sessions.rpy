init python:

    def Jean_chapter_one_season_three_training_sessions():
        label = "Jean_chapter_one_season_three_training_sessions"

        conditions = [
            "season == 3",
            "Jean.History.check('trained_with_Player', tracker = 'season') >= 2",
            "Player.training == Jean and Jean.training"]

        priority = 99
        repeatable = True

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label Jean_chapter_one_season_three_training_sessions:
    $ ongoing_Event = True

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("smirk2")

        ch_Jean "Hurry up, [Jean.Player_petname]."
        ch_Jean "Let's start."

        $ Jean.change_face("smirk2", mouth = "lipbite")

        ch_Player "Wha-"

        call Jean_activate_psychic from _call_Jean_activate_psychic_21

        $ fade_to_black(0.4)

        "[Jean.name] blind sides you with a tennis ball." 

        $ Player.power = 25

        "It flies towards you so fast that by the time you activate the nullification, it's only a foot from your face."

        show expression "images/effects/zing.webp" as zing onlayer effects:
            anchor (0.5, 0.5) pos (0.5, 0.5)

            zoom 0.0
            alpha 0.0
            ease 0.1 zoom 1.0 alpha 1.0
            ease 1.0 alpha 0.0

        "The ball loses some momentum in the instant before it hits you. . . but not much." 

        $ fade_in_from_black(0.4)

        $ Jean.change_face("sly")

        pause 1.0

        if Laura.History.check("trained_with_Player", tracker = "season") >= 2:
            $ Jean.change_face("surprised3") 
            
            "Training with [Laura.name] has not only gotten you used to surprises, but also forced your reaction time and senses to improve." 
            "Instead of just letting the ball hit you in the face, you twist and block just in time." 
            
            $ Jean.change_face("confused1", eyes = "squint", mouth = "smirk") 
            
            ch_Jean "Show off."
        else:
            $ Jean.change_face("worried1", mouth = "smirk") 
            
            "Despite all the strength and speed, you still aren't quite used to your body." 
            "You intended to move out of the way and block, but instead managed to smack yourself, while still letting the tennis ball hit you." 
            
            ch_Jean "That was. . . less than graceful. . ."

        $ Player.power = 0

        call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_21

        $ Jean.change_face("smirk2")

        "After a proper warm up, [Jean.name] has you work on turning your nullification on and off as fast as you can."
        "Getting caught unaware can be very dangerous, and you need to be able to react fast enough."
        "It gives you a pretty bad headache, so you leave it off during sparring."

        call Jean_activate_psychic from _call_Jean_activate_psychic_22

        "[Jean.name] works on her powers for a bit, and while you don't have to step in, it gets pretty close a couple times."

        call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_22

        $ Jean.change_face("worried1") 

        ch_Jean "I hate how I can barely tell when I'm taking it too far."
        ch_Jean "It always creeps up on me." 
        ch_Player "Want to take a break?"

        $ Jean.change_face("worried1", mouth = "smirk") 

        ch_Jean "Yeah. . . thanks for always being here for me, [Jean.Player_petname]."
    elif dice_roll == 2:
        $ Jean.change_face("sly")

        ch_Jean "Come on, let's get started."

        call Jean_activate_psychic from _call_Jean_activate_psychic_23

        $ Player.power = 25

        "This seems to be a thing now, where she tries to blindside you with a tennis ball at the start of every session."

        show expression "images/effects/zing.webp" as zing onlayer effects:
            anchor (0.5, 0.5) pos (0.5, 0.5)

            zoom 0.0
            alpha 0.0
            ease 0.1 zoom 1.0 alpha 1.0
            ease 1.0 alpha 0.0

        "You know that look in her eye, so you had already activated your nullification by the time you feel the ball coming from behind."
        "You manage to get out of the way."

        $ Jean.change_face("worried1")
        
        $ Player.power = 0

        call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_23

        ch_Jean "You're getting too good at this."

        $ Jean.change_face("confused1")

        ch_Jean "Maybe I'm just becoming too predictable."

        $ Jean.change_face("smirk2")

        ch_Jean "Whatever, let's just warm up." 
        "After a quick warmup, you spend a couple hours trying to improve your power control."
        "It still takes a bit of effort, but you can pretty much enable or disable your nullification at will."
        "Still not as quickly as you'd like, but progress is progress."

        $ Jean.change_face("sly")

        "You spar a bit with [Jean.name], and she uses her powers to narrow the widening gap between your physical prowess."

        call Jean_activate_psychic from _call_Jean_activate_psychic_24

        "She doesn't go big and flashy while practicing her own stuff today, instead focusing more on introspection."

        call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_24

        $ Jean.change_face("worried1")

        ch_Jean "I still don't even know what's wrong with me. . ."

        $ Jean.change_face("worried1", eyes = "right")

        ch_Jean "Am I even looking in the right place?"
        ch_Player "I wish I could do more to help."

        $ Jean.change_face("worried1", mouth = "smirk")

        ch_Jean "Just knowing you're here for me is enough. . ."
        ch_Jean "I gotta take a break."
        ch_Jean "See you later."
    elif dice_roll == 3:
        $ Jean.change_face("worried1", mouth = "smirk")

        ch_Jean "Ready to go?"
        ch_Player "Yeah, but is something wrong?"

        call Jean_activate_psychic from _call_Jean_activate_psychic_25

        show expression "images/effects/green_smack.webp" as smack onlayer effects:
            anchor (0.5, 0.5) pos (0.5, 0.4)

            zoom 0.0
            alpha 0.0
            ease 0.1 zoom 1.0 alpha 1.0
            ease 1.0 alpha 0.0

        with small_screenshake

        "Before you can even react, a tennis ball smacks into your butt from behind."
        "It stings a bit. . ."

        $ Jean.change_face("sly")

        call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_25

        ch_Jean "Gotcha."
        ch_Player "Wow, that's just cruel."
        ch_Player "I was worried about you."

        $ Jean.change_face("smirk2")

        ch_Jean "As you should be."

        if Jean.petname == "big sis'":
            ch_Jean "Like a good little bro'."

        ch_Jean "Now, let's get started for real."
        "One quick warm up later, and the stinging in your ass is gone."
        "[Jean.name] has you work on your powers as usual, running through various exercises, constantly turning it on and off again."
        "You're getting better at it, but still have zero control over how strongly your power expresses itself."

        $ Jean.change_face("worried1")

        "After a quick sparring session where neither of you use any powers, she focuses on herself." 

        call Jean_activate_psychic from _call_Jean_activate_psychic_26

        "You can tell she's also gotten better, and her power is just about completely stable if she doesn't try and push it too far."

        call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_26

        $ Jean.change_face("worried1", mouth = "smirk")

        ch_Jean "I think I'd rather not ruin my day by losing control. . ."
        ch_Jean "Let's call it there."
        ch_Player "That sounds like a good idea."
        ch_Player "You should actually give yourself a break for once, though."

        $ Jean.change_face("worried1")

        ch_Jean "I can't just skip studying, [Jean.Player_petname]."
        ch_Jean "I'll see you later. . ."

    call remove_Characters(Jean) from _call_remove_Characters_59

    $ ongoing_Event = False

    return