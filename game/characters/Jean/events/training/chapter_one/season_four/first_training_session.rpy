init python:

    def Jean_chapter_one_season_four_first_training_session():
        label = "Jean_chapter_one_season_four_first_training_session"

        conditions = [
            "chapter == 1 and season == 4",

            "not Jean.History.check('trained_with_Player', tracker = 'season')",
            
            "Player.behavior == 'training'"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Jean_chapter_one_season_four_first_training_session:
    $ ongoing_Event = True
    
    if Jean not in Player.behavior_Partners:
        "You want to train, but after everything that's happened, you have to change up the status quo."
        "Nearly beating people to death has a way of changing one's perspective on things."
        "You need to consult [Jean.name] and learn to control how strongly your power expresses itself."
        "As if on cue, [Jean.name] appears in the doorway."

        call send_Characters(Jean, "bg_danger", behavior = "training") from _call_send_Characters_56

        $ Player.behavior = "training"
        $ Player.behavior_Partners = [Jean]

        call remove_everyone_but(Jean) from _call_remove_everyone_but

    $ Jean.change_face("worried1") 
    $ Jean.change_arms("crossed")

    ch_Player "Something has to change."
    ch_Player "I was strong enough this time. . . but too strong. . ."

    $ Jean.change_face("worried2")

    pause 1.0

    $ Jean.change_face("angry1")
    $ Jean.change_arms("angry")

    ch_Jean "Better than not strong enough, [Jean.Player_petname]. . ."

    $ Jean.change_face("worried1") 

    ch_Jean "I'm just glad you're okay and didn't almost die again. . ."
    
    $ Jean.change_arms("neutral")

    ch_Jean "And nobody else died anyway."

    $ temp = Jean.petname.capitalize()

    menu:
        extend ""
        "[temp]. . . you only feel that way because you care about me so much.":
            call change_Character_stat(Jean, "love", small_stat) from _call_change_Character_stat_185
            call change_Character_stat(Jean, "trust", medium_stat) from _call_change_Character_stat_186

            $ Jean.change_face("angry1", eyes = "right")
            $ Jean.change_arms("crossed")

            ch_Jean "Ugh, I know. . ." 
            
            $ Jean.change_face("angry1") 
            
            ch_Jean "Don't know what I would've done if I saw you in that infirmary again." 
        "I'm more glad than anyone. . . but it can't stay like this.":
            call change_Character_stat(Jean, "trust", medium_stat) from _call_change_Character_stat_187

            $ Jean.change_face("worried2")
            $ Jean.change_arms("crossed")

            ch_Jean "What do you mean?" 
            ch_Jean "Any stronger and you definitely would've killed someone." 
        "Trust me, it feels great finally being powerful. . . but even I know there's something missing.":
            call change_Character_stat(Jean, "trust", small_stat) from _call_change_Character_stat_188

            $ Jean.change_face("confused1") 
            $ Jean.change_arms("crossed")

            ch_Jean "What are you talking about?" 
            ch_Jean "You still don't think you're strong enough?"
            
    ch_Player "I need more control."

    $ Jean.change_face("confused1")

    ch_Player "Both of my abilities. . . it's still all or nothing."
    ch_Player "I don't know if it's a problem with my mindset, or the fact that I barely know what I'm doing, but. . ."

    menu:
        extend ""
        "If I can't control myself, I'll be just as bad as them. . . I need to focus, so I don't go overboard.":
            $ Jean.change_face("confused2")

            if Player.History.check("told_Jean_angry_at_protesters_during_mutant_hate"):
                call change_Character_stat(Jean, "love", medium_stat) from _call_change_Character_stat_189
                call change_Character_stat(Jean, "trust", small_stat) from _call_change_Character_stat_191
                
                pause 1.0
                
                $ Jean.change_face("worried1") 
                
                ch_Jean "You do need to be careful. . ."
                ch_Jean "But regardless of what happened, I know you. . . you'll never be as bad as them." 
            else:
                call change_Character_stat(Jean, "love", medium_stat) from _call_change_Character_stat_192
                call change_Character_stat(Jean, "trust", medium_stat) from _call_change_Character_stat_193
                
                ch_Jean "No, you won't be." 
                ch_Jean "I know you, [Jean.Player_petname]." 
                ch_Jean "You're an infinitely better person than them, regardless of what happened." 
        "It's scary. . . not being able to control myself. . . I might go too far. . .":
            $ Jean.change_face("worried2")

            if Player.History.check("told_Jean_was_scared_during_mutant_hate"):
                call change_Character_stat(Jean, "love", medium_stat) from _call_change_Character_stat_194
                call change_Character_stat(Jean, "trust", medium_stat) from _call_change_Character_stat_195
                
                ch_Jean "Are you okay?" 
                ch_Jean "You know I'm always here, to help you through it all." 
            else:
                call change_Character_stat(Jean, "love", medium_stat) from _call_change_Character_stat_198
                call change_Character_stat(Jean, "trust", small_stat) from _call_change_Character_stat_199
                
                ch_Jean "I know it's scary, but that's why you have me." 
                ch_Jean "I'll help you through it all." 
                ch_Jean "Make sure nothing happens." 
        "Maybe those people deserved worse than I gave them, but that should be my choice, not my power's.":
            $ Jean.change_face("angry1")

            $ temp = Jean.Player_petname.capitalize()
            
            if Player.History.check("told_Jean_angry_at_protesters_during_mutant_hate"):
                call change_Character_stat(Jean, "love", -small_stat) from _call_change_Character_stat_200
                call change_Character_stat(Jean, "trust", -small_stat) from _call_change_Character_stat_201
                
                ch_Jean "[temp], don't be like that." 
                ch_Jean "Don't stoop to their level." 
            else:
                call change_Character_stat(Jean, "love", -medium_stat) from _call_change_Character_stat_202
                call change_Character_stat(Jean, "trust", -medium_stat) from _call_change_Character_stat_203

                ch_Jean "What's gotten into you?" 
                ch_Jean "You can't let what happened affect you this much. . ." 
                
    $ Jean.change_face("angry1")
    $ Jean.change_arms("angry")

    ch_Jean ". . ."
    ch_Jean "Then let's do it."
    ch_Player "What?"

    $ Jean.change_arms("angry", left_arm = "extended")

    ch_Jean "You need more control?"

    $ Jean.change_arms("sass")

    ch_Jean "That's what we'll do today."
    ch_Jean "Turn your power on."
    ch_Jean "Both of them."
    ch_Player "Wait, but-"

    $ Jean.change_face("neutral")
    $ Jean.change_arms("hips")

    ch_Jean "I'll be fine, as long as you don't keep it on for too long."

    $ Jean.change_face("angry1", mouth = "smirk")

    ch_Jean "Plus, this is the perfect opportunity to see if your power is more like [Rogue.name]'s than we thought."

    $ Jean.change_arms("psychic1")

    $ Player.power = 50

    call Jean_activate_psychic from _call_Jean_activate_psychic

    $ fade_to_black(0.4)

    "She looks determined, and you're confident in your ability to turn the power off if things go too far, so you go for it."

    $ count = 7

    while count > 0:
        $ dice_roll = renpy.random.randint(1, 3)

        $ x = renpy.random.random()*0.7 + 0.15
        $ y = renpy.random.random()*0.7 + 0.15

        if dice_roll == 1:
            show expression "images/effects/zing.webp" as zing onlayer effects:
                anchor (0.5, 0.5) pos (x, y)

                zoom 0.0
                alpha 0.0
                ease 0.1 zoom 1.0 alpha 1.0
                ease 1.0 alpha 0.0
        elif dice_roll == 2:
            show expression "images/effects/crash.webp" as crash onlayer effects:
                anchor (0.5, 0.5) pos (x, y)

                zoom 0.0
                alpha 0.0
                ease 0.1 zoom 1.0 alpha 1.0
                ease 1.0 alpha 0.0
        elif dice_roll == 3:
            show expression "images/effects/pow.webp" as pow onlayer effects:
                anchor (0.5, 0.5) pos (x, y)

                zoom 0.0
                alpha 0.0
                ease 0.1 zoom 1.0 alpha 1.0
                ease 1.0 alpha 0.0

        $ renpy.pause(renpy.random.random(), hard = True)

        $ count -= 1

    "You've never directly confronted [Jean.name] like this before, using the full extent of your abilities."
    "Of course, she isn't using the full extent of {i}her{/i} abilities, but then it wouldn't even be a fight."
    "It's one thing engaging [Laura.name] in hand-to-hand combat, but this is a completely new kind of fighting."
    "It ends up being a stalemate with her keeping you at a distance, and your powers nullifying and absorbing everything she throws at you."
    "You spend a while like this, both struggling against [Jean.name] and against your own powers."
    "Eventually something changes."

    $ fade_in_from_black(0.4)

    $ Jean.change_face("surprised2")

    $ Player.power = 25

    "You're both pushing against [Jean.name]'s power, while also trying to pull your own power back without fully turning it off."

    show expression "images/effects/green_smack.webp" as smack onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.4)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    "All of the sudden, a tennis ball going way too fast, smacks you right in the face."

    $ Jean.change_face("pleased2")

    call Jean_deactivate_psychic from _call_Jean_deactivate_psychic

    $ Jean.change_arms("sass")

    "With much mental effort, you managed to lower your powers just enough that she was able to overcome the stalemate."
    "You have a pounding headache, but it worked."

    $ Player.power = 0

    $ Jean.change_face("smirk2")

    ch_Jean "Heh, well I guess it worked."

    $ Jean.change_face("worried1", mouth = "smirk")
    $ Jean.change_arms("neutral", left_arm = "rub_neck")

    ch_Jean "Didn't mean to hit you so hard. . ."
    ch_Player "It's fine, I was gonna have a headache anyway."
    
    $ Jean.change_arms("sass")

    ch_Player "But yeah, it worked."
    ch_Player "I think I can do it again. . . maybe after a bit of rest."

    $ Jean.change_face("confused1")

    ch_Jean "And it doesn't feel like you could copy my power after absorbing all that energy?"
    ch_Player "Not at all."
    ch_Player "It only felt like it gave me a little power boost."

    $ Jean.change_face("angry1")
    $ Jean.change_arms("crossed")

    ch_Jean "Well if your power is really all about inspiration and stuff, your next one better be about me."

    $ Jean.change_face("angry1", eyes = "right")

    ch_Jean "Not fair those other girls got one before I did. . ."
    ch_Player "I'll try. . ."
    ch_Player "But hey, I could tell you went pretty hard with your powers."
    ch_Player "Didn't feel like you got unstable at all."

    $ Jean.change_face("worried1", mouth = "smirk")
    $ Jean.change_arms("sass")

    ch_Jean "Yeah. . . I think being so focused on helping you ended up making me a bit better too."
    ch_Player "Thanks, [Jean.petname]."
    ch_Player "You know how much I appreciate all the help you've given me so far."

    $ Jean.change_face("happy")

    ch_Jean "You better appreciate it."

    $ Jean.change_face("smirk2")

    ch_Jean "And you've helped me a lot too. . . thanks."
    
    $ Jean.change_arms("hips")

    ch_Jean "But it sounds like you could use a break."

    $ Jean.change_face("sly")

    ch_Jean "Don't want poor [Jean.Player_petname] to suffer from his headache for too long."

    $ Jean.change_face("smirk2")

    ch_Jean "Go take it easy, I'll see you later."

    call remove_Characters(Jean) from _call_remove_Characters_50

    $ ongoing_Event = False

    return