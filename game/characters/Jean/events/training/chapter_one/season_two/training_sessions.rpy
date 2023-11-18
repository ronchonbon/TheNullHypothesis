init python:

    def Jean_chapter_one_season_two_training_sessions():
        label = "Jean_chapter_one_season_two_training_sessions"

        conditions = [
            "chapter == 1 and season == 2",
            "Jean.History.check('trained_with_Player', tracker = 'season') >= 2",
            "Player.training == Jean and Jean.training"]

        priority = 99
        repeatable = True

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label Jean_chapter_one_season_two_training_sessions:
    $ ongoing_Event = True

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("happy")

        ch_Jean "Ready to start?"

        $ Jean.change_face("smirk2")

        ch_Player "Yep!"

        call Jean_activate_psychic from _call_Jean_activate_psychic_31

        "[Jean.name] helps you through a quick warm up, making sure you're properly stretched out." 
        "Afterwards, she puts you through some fairly complicated power control exercises."
        "By the end, you have a pretty bad headache, but also felt closer than ever to actually taking control."

        call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_31

        if Laura.History.check("trained_with_Player") >= 2:
            $ Jean.change_face("appalled1", mouth = "smirk") 
            
            "All the training with [Laura.name], as well as your new boosts to strength and speed, allows you an edge during sparring."
        else:
            $ Jean.change_face("worried1", mouth = "smirk") 
            
            "Despite this new boosts to strength and speed, your technique is still a bit sloppy." 
            "You don't have quite as much of an advantage during sparring as you expected."

        $ Jean.change_face("sly")

        ch_Jean "Watch this."

        call Jean_activate_psychic from _call_Jean_activate_psychic_32

        "If you thought you were impressed by what abilities she's already shown off, today was something else."
        "She shows off just how much she's improved. . ."

        $ Jean.change_face("worried3") 

        "And then goes too far."
        "You rush over to help and things calm down quickly."

        call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_32

        $ Jean.change_face("worried1") 

        ch_Jean "Thanks, [Jean.Player_petname]."
        ch_Jean "Got a bit too excited there."
        "Her progress since last time might be even slower than yours, but of course you don't say that."
        ch_Player "Of course."
        ch_Player "We should probably call it there, yeah?"

        $ Jean.change_face("worried1", mouth = "smirk") 

        ch_Jean "Yeah. . . I'll see you later."
    elif dice_roll == 2:
        $ Jean.change_face("worried1")

        ch_Player "Are you okay?"
        ch_Player "Ready to go?"

        $ Jean.change_face("smirk2")

        ch_Jean "I am, thanks."
        ch_Jean "C'mon, follow my lead."
        "She runs you through a quick warm up, and you help each other stretch out."

        $ Player.power = 25

        "Today she has you try a bunch more small experiments with your power, to try and define its current limitations."
        "It's hard to really quantify, since you're constantly getting better and getting ever closer to properly controlling it."

        $ Jean.change_face("sly")

        "Then you go through some quick sparring, during which [Jean.name] cheats by using her powers to distract you."

        $ Jean.change_face("smirk2")

        "Then she starts on her own powers, but instead of being flashy, she has you do mostly introspective exercises with her."
        "You can feel the power inside you, still just barely out of reach."

        $ Jean.change_face("worried1")

        $ Player.power = 0

        ch_Player "It feels like I'm getting super close."
        ch_Player "You okay?"

        $ Jean.change_face("worried2")

        ch_Jean "I am. . . just doesn't feel like much is different for me, on the inside." 

        $ Jean.change_face("worried1", eyes = "right")

        ch_Jean "I need a break."

        $ Jean.change_face("worried1")

        ch_Jean "I'll see you later, okay?"

        $ Jean.change_face("worried1")

        ch_Player "Yeah, sure." 
    elif dice_roll == 3:
        $ Jean.change_face("happy")

        ch_Jean "You feeling good today? I know I am."
        ch_Player "Ye-"

        $ Jean.change_face("smirk2")

        "She doesn't even wait for an answer and pulls you over to start the warm up."
        ch_Jean "Let's go."
        "One quick warm up later, and she runs through some power exercises with you."

        $ Player.power = 25

        "The closer you get to actually controlling your power, the more effective these exercises seem to get."

        $ Jean.change_face("surprised1")

        "You get into a bit of sparring, feeling proud of the one thing you might be better at than [Jean.name]." 

        $ Jean.change_face("confused1", mouth = "smirk")

        "She starts working on her own powers, and although the lack of stability is palpable at times, she manages to maintain control of herself."

        $ Jean.change_face("worried1")

        $ Player.power = 0

        ch_Jean "That got pretty close a couple times. . ."
        ch_Player "Hey, at least you managed to keep it together." 

        $ Jean.change_face("smirk1")

        ch_Jean "You're right. . . thanks."

        $ Jean.change_face("worried1")

        ch_Jean "Now, I really gotta go study."

        $ Jean.change_face("smirk2")

        ch_Jean "I'll see you later, [Jean.Player_petname]."

    call remove_Characters(Jean) from _call_remove_Characters_62

    $ ongoing_Event = False

    return