init python:

    def Jean_chapter_one_season_three_second_training_session():
        label = "Jean_chapter_one_season_three_second_training_session"

        conditions = [
            "chapter == 1 and season == 3",
            
            "Jean.History.check('trained_with_Player', tracker = 'season') == 1",

            "Player.behavior == 'training' and Jean in Player.behavior_Partners and Jean.behavior == 'training'"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Jean_chapter_one_season_three_second_training_session:
    $ ongoing_Event = True

    $ Jean.change_face("worried1")
    $ Jean.change_arms("neutral", left_arm = "rub_neck")

    ch_Jean "So, [Jean.Player_petname]. . ."

    $ Jean.change_face("confused1", mouth = "smirk")
    $ Jean.change_arms(right_arm = "extended", left_arm = "rub_neck")

    ch_Jean "You're not mad about the end of our last training session. . . right?"

    menu:
        extend ""
        "Not at all. I feel bad about all the stress you're going through.":
            $ Jean.change_face("worried1", mouth = "smirk")
            $ Jean.change_arms("crossed")

            ch_Jean "Thanks for being so understanding. . ." 
            
            call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_191
            call change_Character_stat(Jean, "trust", 0) from _call_change_Character_stat_192
        "It made me a little sad to have you upset at me. . . But don't worry, I understand.":
            $ Jean.change_face("worried2")
            $ Jean.change_arms("crossed")

            ch_Jean "I don't like it when you're sad, [Jean.Player_petname]." 
            
            call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_193
        "A little bit to be honest. . . it was pretty uncalled for. But it's fine, I'd be frustrated too if I were in your shoes.":
            $ Jean.change_face("confused2")
            $ Jean.change_arms("crossed")

            ch_Jean "At least you get it. . . I guess." 
            
            call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_194
            call change_Character_stat(Jean, "trust", 0) from _call_change_Character_stat_195

    $ Jean.change_face("worried1")

    ch_Jean "I am sorry, though."

    $ Jean.change_face("smirk1")
    $ Jean.change_arms("sass")

    ch_Jean "But on a different note, I've been thinking about your powers since last time."
    ch_Jean "If it really is some inspirational power thing. . ."

    $ Jean.change_face("suspicious1")
    $ Jean.change_arms("hips")

    ch_Jean "How come you haven't been inspired by me yet?"
    ch_Player "Uh. . . I. . . don't know. . ."

    $ Jean.change_face("sly")

    ch_Jean "I'm {i}mostly{/i} messing with you."

    $ Jean.change_face("confused1", mouth = "smirk")
    $ Jean.change_arms("crossed")

    ch_Jean "But seriously, I wonder if it really does only work in times of need. . ."

    $ Jean.change_face("sly")

    ch_Jean "Like if I made you think you were about to die, could you use it again right now. . . ?"
    ch_Player "That doesn't sound like a good idea. . ."
    ch_Player "I mean what if there's some kind of cooldown."
    ch_Player "It was months in between each time I got a new ability."
    ch_Player "What if it doesn't work and I really do die. . ."

    $ Jean.change_face("worried1")
    $ Jean.change_arms("sass")

    ch_Jean "Good point. . ."
    ch_Player "Not to mention how shitty it made me feel each time."

    $ Jean.change_face("confused1")

    ch_Player "Felt like it was rearranging my insides. . . made me feel physically ill."

    $ Jean.change_face("worried1")

    ch_Jean "Okay, yeah, let's not do that to you."

    $ Jean.change_face("smirk2")
    $ Jean.change_arms("sass", right_arm = "extended")

    ch_Jean "Let's just focus on improving the abilities you currently have."

    $ Jean.change_face("worried3")
    $ Jean.change_arms("angry")

    ch_Jean "Wait, what if your old abilities start going away since your body doesn't need them to survive anymore?!"
    ch_Player "No, if anything, it feels like they're even more a part of me than ever."

    $ Jean.change_face("worried1")
    $ Jean.change_arms("neutral")

    ch_Jean "Okay good."

    $ Jean.change_face("smirk1")

    ch_Jean "Now, onto the training. . ."

    $ Player.power = 25

    $ fade_to_black(0.4)

    "She has you go through a bunch of power control exercises, but there's still one problem."
    "You can turn your nullification on and off, but that's it. . . you lack any finer control."
    "It's all or nothing."
    "She has you focus on one thing at a time, and having any control over it at all is still very new to you."
    "After a quick sparring session, where she makes you constantly turn your nullification on and off, you have quite the headache."

    $ Player.power = 0

    $ fade_in_from_black(0.4)

    $ Jean.change_face("sly")

    ch_Jean "Alright, turn it back on."

    $ Jean.change_arms("psychic2")

    ch_Jean "I'm gonna mess with my powers for a bit."

    $ Jean.change_face("worried1")

    ch_Jean "Might need your help. . ."

    $ Player.power = 25

    call Jean_activate_psychic from _call_Jean_activate_psychic_20

    "Despite her worries - and throwing around some serious weight with her mind - she doesn't actually need your help today."
    "You can tell she's improved, quite a lot."
    "Her power is just about completely stable up to moderate outputs, but higher ones are still iffy."

    $ Jean.change_face("worried1", mouth = "smirk")

    call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_20

    $ Jean.change_arms("crossed")
    
    ch_Jean "I think that'll do it."
    ch_Jean "Don't want to keep pushing it and just end up ruining my day."
    ch_Player "I getcha."
    ch_Player "See you later?"

    $ Jean.change_face("smirk2")

    ch_Jean "Yeah."
    ch_Jean "Bye, for now."

    call remove_Characters(Jean) from _call_remove_Characters_58

    $ ongoing_Event = False

    return