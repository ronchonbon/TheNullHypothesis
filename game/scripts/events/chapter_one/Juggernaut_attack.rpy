init python:

    def ch1_season_one_main_Quest():
        name = "Chapter I: Fall"

        string = "ch1_season_one_main_Quest"

        Quest_type = "main"

        chapter = 1

        description = "Explore your new home and get to know its students"

        objectives = {
            "Increase your level": ["Player.level", 2],

            "Complete [Rogue.name]'s Fall Quest": ["QuestPool.Quests['Rogue_ch1_season_one_Quest'].completed", None],
            "Complete [Laura.name]'s Fall Quest": ["QuestPool.Quests['Laura_ch1_season_one_Quest'].completed", None],
            "Complete [Jean.name]'s Fall Quest": ["QuestPool.Quests['Jean_ch1_season_one_Quest'].completed", None],

            "Gain Trust across all characters": ["Rogue.trust + Laura.trust + Jean.trust", 375]}

        optional_objectives = {}

        rewards = [
            "New Available Actions",
            "New Shop Items"]

        criteria = [
            "chapter == 1 and season == 1"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)

init python:

    def ch1_season_one_complete():
        label = "ch1_season_one_complete"

        conditions = [
            "QuestPool.Quests['ch1_season_one_main_Quest'].completed"]

        automatic = True

        return EventClass(label, conditions, automatic = automatic)

label ch1_season_one_complete:
    "You have met all the requirements to progress the main story. Check your journal for more information."

    $ season_completed = True

    return

init python:

    def ch1_season_one_progress():
        label = "ch1_season_one_progress"

        conditions = [
            "EventScheduler.Events['ch1_season_one_complete'].completed",
            "not EventScheduler.Events['ch1_Juggernaut_attack'].completed",
            "weekday == 4",
            "not Present",
            "Player.location == Player.home"]

        sleeping = True

        priority = 99
        repeatable = True

        return EventClass(label, conditions, sleeping = sleeping, priority = priority, repeatable = repeatable)

label ch1_season_one_progress:
    $ ongoing_Event = True

    "You feel especially tired tonight and fall asleep as soon as you hit the sheets."

    menu:
        "Progress the main story":
            $ EventScheduler.Events["ch1_Juggernaut_attack"].start()
        "Postpone story progress":
            pass

    $ ongoing_Event = False

    return

init python:

    def ch1_Juggernaut_attack():
        label = "ch1_Juggernaut_attack"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label ch1_Juggernaut_attack:
    $ ongoing_Event = True

    $ reset_behavior()

    "It's been a long week."
    "You decide to sleep in a bit later than usual."
    
    call start_new_day from _call_start_new_day_1

    $ weather = None

    play music "sounds/music/Disconnect.ogg" fadeout 1.0

    show expression "images/effects/crash.webp" as crash onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.25 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    pause 1.0

    show expression "images/effects/crash.webp" as crash onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.5 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    pause 1.0

    show expression "images/effects/crash.webp" as crash onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    with big_screenshake

    $ lights_on = True

    $ fade_in_from_black(0.4)

    "You awake with a start as loud crashing sounds echo across campus."
    ch_Player "What the fu. . ."

    call phone_buzz(times = 3, intensity = 1.5) from _call_phone_buzz_4

    "An alarm goes off on your phone."

    $ phone_interactable = False
    
    $ emergency_broadcast = True

    show screen phone_screen()

    ch_Player "Holy shit."

    hide screen phone_screen
    
    $ emergency_broadcast = False

    show expression "images/effects/crash.webp" as crash onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    "You hear more crashes, but whatever's going on doesn't sound close."

    call remove_Characters(location = "bg_hallway") from _call_remove_Characters_210
    call set_the_scene(location = "bg_hallway") from _call_set_the_scene_227

    "You peek out into the hallway and see a bunch of people running to their dorms."
    "You notice [Jean.name], however, is running right towards you."

    $ temp = Jean.Player_petname.capitalize()

    ch_Jean "[temp]!"
    
    $ Jean.change_face("worried3") 

    call send_Characters(Jean, location = "bg_hallway", behavior = False) from _call_send_Characters_285

    ch_Jean "Thank god you're okay." 

    $ Jean.change_face("worried1") 

    ch_Player "What are you doing here?"
    ch_Jean "I was nearby - had to make sure you were okay."

    $ Jean.change_face("worried1", mouth = "smirk") 

    ch_Player "Do you know what's going on?"
    ch_Jean "No. . . it's probably some stray mutant attacking the school for whatever reason." 

    $ Jean.change_face("smirk2") 

    ch_Jean "Now that I know you're safe, I'll just head over and help deal with them real quick." 

    $ Jean.change_face("worried1", eyes = "right") 

    $ temp = Jean.petname.capitalize()

    menu:
        extend ""
        "We both know that's not a good idea. You're more than powerful enough, but the instability. . .":
            call change_Companion_stat(Jean, "love", small_stat) from _call_change_Companion_stat_837
            call change_Companion_stat(Jean, "trust", medium_stat) from _call_change_Companion_stat_838
        "[temp], are you sure. . . ? What if you lose control again?":
            call change_Companion_stat(Jean, "love", -small_stat) from _call_change_Companion_stat_839
        "Don't act all confident, you need to face reality. You and I both know you're not stable enough for that.":
            call change_Companion_stat(Jean, "love", -medium_stat) from _call_change_Companion_stat_840  
            call change_Companion_stat(Jean, "trust", small_stat) from _call_change_Companion_stat_841

    $ Jean.change_face("angry1") 

    ch_Jean "Oh don't start."
    ch_Jean "I'll be fine, I won't lose control." 

    $ Jean.change_face("angry1", eyes = "right") 

    ch_Player "[Jean.name]. . ."

    $ Jean.change_face("worried1", eyes = "right")

    pause 1.0 

    $ Jean.change_face("angry1")  

    ch_Jean "Goddamnit."

    $ Jean.change_face("worried1", eyes = "right") 

    ch_Jean "I know. . ."
    ch_Player "I'm sure somebody's handling it already."

    $ Jean.change_face("worried1") 

    ch_Player "I'll just go try and find [Laura.name] and [Rogue.name]."

    $ Jean.change_face("appalled1") 

    ch_Jean "Absolutely not, you're staying right here where it's safe."

    menu:
        extend ""
        "I won't sit around while they could be getting hurt. (determined)":
            $ Jean.change_face("worried1")

            $ Player.History.update("Determined")
        "It's not like I want to run out into danger. . . but I have to make sure. . . (reluctant)":
            $ Jean.change_face("worried1", eyes = "right")

            $ Player.History.update("Reluctant")
        "That's not gonna happen. If they're in danger, I will do something about it. (bitter)":
            $ Jean.change_face("worried2")

            $ Player.History.update("Bitter")

    ch_Jean "Fine. . ."

    $ Jean.change_face("angry1") 

    ch_Jean "You better be careful."

    $ Jean.change_face("worried1", eyes = "right") 

    ch_Jean "I'll try to find Charles and see if I can help him somehow."

    $ Jean.change_face("kiss1")

    "She gives you a kiss on the cheek, before running off." 

    call remove_Characters(Jean) from _call_remove_Characters_211

    "You start heading towards the girl's dormitory."

    $ fade_to_black(0.4)
    
    $ Player.location = "traveling"

    $ fade_in_from_black(0.4)

    call make_call(Rogue) from _call_make_call

    "On the way, you try calling [Rogue.name], but she doesn't pick up."

    call end_call(Rogue) from _call_end_call_2

    call remove_Characters(location = "bg_girls_hallway") from _call_remove_Characters_212
    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_228
    call knock_on_door(times = 4) from _call_knock_on_door_23

    "You knock on [Rogue.name]'s door as well, but there's no answer."

    call knock_on_door(times = 4) from _call_knock_on_door_24

    "You try [Laura.name]'s room next, but again, no answer."

    call make_call(Laura) from _call_make_call_1

    "You call [Laura.name]."

    ch_Laura "Where are you, are you safe?"
    "You hear screaming in the background."
    ch_Player "I'm fine, but [Rogue.name] isn't picking up her phone."
    ch_Player "I'm outside your room right now."
    ch_Player "What about you?"
    ch_Player "Are you okay?"
    ch_Laura "I'm helping evacuate some of the wounded, stay where you are."
    ch_Laura "I'll come protect you when I'm done."

    $ choice_disabled = False

    menu:
        extend ""
        "I think [Rogue.name] might be in trouble, I need to find her.":
            call change_Companion_stat(Laura, "love", medium_stat) from _call_change_Companion_stat_1080
            call change_Companion_stat(Laura, "trust", small_stat) from _call_change_Companion_stat_1086

            ch_Player "She always picks up her phone." 
            ch_Laura "Part of being a friend is to tell you when you're being an idiot, right?" 
            ch_Player "Ha! Now you're getting it." 
            ch_Laura "You're still weak, you'll just get yourself hurt." 
            ch_Player "I'm sorry, but I'm going. She's our friend too."
            ch_Player "I might be able to help, they won't be expecting my power."
        "I'm not going to sit around - I'll be fine. With all the training you've put me through, I can handle it.":
            call change_Companion_stat(Laura, "trust", -small_stat) from _call_change_Companion_stat_1087

            ch_Laura "You're being an idiot." 
            ch_Laura "Scenarios are nothing like the real thing." 
            ch_Player "I'll be fine." 
            ch_Player "Plus, you know [Rogue.name] would pick up her phone if she could." 
            ch_Laura "You're still weak, you'll just get yourself hurt." 
            ch_Player "Even if I'm not ready, they won't be expecting my power." 
            ch_Player "I have to try."

    ch_Laura "You're still an idiot."
    ch_Player "Just come back me up when you're done over there." 
    ch_Laura "{i}Grrrrrrrrr{/i}. . . If you get hurt, I'll kill you."

    $ _skipping = False

    "She hangs up."

    call end_call(Laura) from _call_end_call_3

    $ fade_to_black(0.4)

    show expression "images/effects/crash.webp" as crash onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.25 alpha 1.0
        ease 1.0 alpha 0.0

    show screen disable_click(22.0)

    play music "sounds/cinematic/Juggernaut No Vox.ogg" fadeout 0.25 fadein 0.5

    "You start heading towards the crashing sounds. . .{w=3}{nw}"

    show expression "images/effects/crash.webp" as crash onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.5 alpha 1.0
        ease 1.0 alpha 0.0

    "They're starting to get louder, and you're pretty sure it's coming from the Danger Room.{w=3}{nw}"
    "You pick up the pace.{w=3}{nw}"

    show expression "images/effects/crash.webp" as crash onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    with big_screenshake

    "Right as you're about to enter, you hear a massive crash, much louder than all the others.{w=3}{nw}" 

    show expression "images/backgrounds/ch1/bg_ch1_danger_lights.webp" as lights onlayer master zorder 5:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/backgrounds/ch1/bg_ch1_danger_destruction2.webp" as destruction2 onlayer master zorder 6:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/backgrounds/ch1/bg_ch1_danger_hole.webp" as hole onlayer master zorder 8:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/backgrounds/ch1/bg_ch1_danger_destruction1.webp" as destruction1 onlayer master zorder 10:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show top_bar onlayer master zorder 10:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/backgrounds/ch1/bg_ch1_danger_Rogue1.webp" as Rogue onlayer master zorder 12:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/backgrounds/ch1/bg_ch1_danger_Juggernaut.webp" as Juggernaut onlayer master zorder 15:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    call remove_Characters(location = "bg_danger") from _call_remove_Characters_213
    call set_the_scene(location = "bg_danger") from _call_set_the_scene_229

    "You burst through the door and end up face-to-face with a giant of a man.{w=4}{nw}"
    ch_Player "Holy shi-{w=2}{nw}"

    $ danger_red_alert = True

    show expression "images/backgrounds/ch1/bg_ch1_danger_lights_red.webp" as lights onlayer master zorder 5:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/backgrounds/ch1/bg_ch1_danger_lights_red2.webp" as lights2 onlayer master zorder 7:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/backgrounds/ch1/bg_ch1_danger_Juggernaut_red_blur.webp" as Juggernaut onlayer master zorder 15:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    $ Cain.name = "???"

    if flashing_lights:
        ch_Cain "AAAAAAAAAAAAAH!!!" with rumble
    else:
        ch_Cain "AAAAAAAAAAAAAH!!!"
    
    ch_Cain "OUT THE WAY, BITCH!"

    with small_screenshake

    pause 0.2

    with small_screenshake

    pause 0.2

    with small_screenshake

    pause 0.2

    "He's barreling right towards you, his footfalls causing the ground to shake."
    "Before you can react, shit your pants, or even move out of the way. . ."

    $ Piotr.name = "???"

    ch_Piotr "OY!"
    ch_Piotr "Vy don't you pick on someone your own size?!"

    show expression "images/effects/clang.webp" as clang onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.2)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    "A massive piece of rubble smacks into the giant's metal dome, causing him to turn around and face the other person in the room."

    hide Juggernaut onlayer master

    show expression "images/backgrounds/ch1/bg_ch1_danger_punches1.webp" as punches onlayer master zorder 13:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/effects/pow.webp" as pow onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.75 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    ch_Cain "AIN'T NOBODY HERE MY OWN SIZE."

    show expression "images/backgrounds/ch1/bg_ch1_danger_punches2.webp" as punches onlayer master zorder 13:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/effects/pow.webp" as pow onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.75 alpha 1.0
        ease 1.0 alpha 0.0

    with big_screenshake

    "The behemoth pays back the attack in kind, with a massive punch."
    "You stand there, too shocked to move, when you see her. . ."

    with small_screenshake

    show comic_cutout1 onlayer master zorder 99:
        anchor (0.5, 0.5) pos (0.25, 0.7) xysize (800, 600)
    
    show expression "images/backgrounds/base/bg_danger_red.webp" as background onlayer comic_cutout1 zorder 0:
        transform_anchor True

        anchor (0.5, 0.5) pos (1.95, -0.85)
        zoom 2.0*background_adjustment
    
    show expression "images/backgrounds/base/bg_danger_lights_red.webp" as background_lights onlayer comic_cutout1 zorder 1:
        transform_anchor True

        anchor (0.5, 0.5) pos (1.95, -0.85)
        zoom 2.0*background_adjustment
    
    show expression "images/backgrounds/ch1/bg_ch1_danger_lights_red.webp" as lights onlayer comic_cutout1 zorder 5:
        transform_anchor True

        anchor (0.5, 0.5) pos (1.95, -0.85)
        zoom 2.0*background_adjustment

    show expression "images/backgrounds/ch1/bg_ch1_danger_destruction2.webp" as destruction2 onlayer comic_cutout1 zorder 6:
        transform_anchor True

        anchor (0.5, 0.5) pos (1.95, -0.85)
        zoom 2.0*background_adjustment
    
    show expression "images/backgrounds/ch1/bg_ch1_danger_lights_red2.webp" as lights2 onlayer comic_cutout1 zorder 7:
        transform_anchor True

        anchor (0.5, 0.5) pos (1.95, -0.85)
        zoom 2.0*background_adjustment

    show expression "images/backgrounds/ch1/bg_ch1_danger_hole.webp" as hole onlayer comic_cutout1 zorder 8:
        transform_anchor True

        anchor (0.5, 0.5) pos (1.95, -0.85)
        zoom 2.0*background_adjustment

    show expression "images/backgrounds/ch1/bg_ch1_danger_destruction1.webp" as destruction1 onlayer comic_cutout1 zorder 10:
        transform_anchor True

        anchor (0.5, 0.5) pos (1.95, -0.85)
        zoom 2.0*background_adjustment

    show expression "images/backgrounds/ch1/bg_ch1_danger_Rogue1.webp" as Rogue onlayer comic_cutout1 zorder 12:
        transform_anchor True

        anchor (0.5, 0.5) pos (1.95, -0.85)
        zoom 2.0*background_adjustment

    "It's [Rogue.name], laying in a pile of rubble."
    "She's struggling to pull herself up, and it looks like she's bleeding from a head wound."
    "From all the debris around her, it looks like the collapsed ceiling hit her on the way down. . ."

    show expression "images/backgrounds/ch1/bg_ch1_danger_Rogue2.webp" as Rogue onlayer master zorder 12:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/backgrounds/ch1/bg_ch1_danger_Rogue2.webp" as Rogue onlayer comic_cutout1 zorder 12:
        transform_anchor True

        anchor (0.5, 0.5) pos (1.95, -0.8)
        zoom 2.0*background_adjustment

    with {"master": dissolve, "comic_cutout1": dissolve}

    "She collapses and stops moving, save for her chest rising and falling."

    $ _skipping = False

    "You're about to yell out and run over. . ."

    hide comic_cutout1 

    show expression "images/backgrounds/ch1/bg_ch1_danger_punches1.webp" as punches onlayer master zorder 13:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/effects/pow.webp" as pow onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.75 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    show screen disable_click(9.0)

    play music "sounds/cinematic/Juggernaut Bitch.ogg" fadeout 0.1 fadein 0.25
    queue music "sounds/cinematic/Juggernaut End.ogg"
    queue music "sounds/cinematic/Juggernaut No Vox.ogg"

    "Your tunnel vision is suddenly shattered by the other occupants of the room.{w=2.0}{nw}"
    ch_Piotr "Cyka.{w=2.0} Who da hell even are you?!{w=2.0}{nw}"

    $ renpy.pause(1.65, hard = True)

    $ Cain.name = "Juggernaut"

    show expression "images/effects/juggernaut.webp" as juggernaut onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.5 alpha 1.0
        ease 5.0 alpha 0.0

    show expression "images/effects/bitch.webp" as bitch onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.65)

        zoom 0.0
        alpha 0.0
        pause 0.85
        ease 0.1 zoom 1.0 alpha 1.0
        ease 4.5 alpha 0.0

    ch_Cain "I'm{w=0.2} the{w=0.2} Juggernaut{w=0.4}, bitch!!"
    "You stare, mouth agape, at the men across the room."

    hide juggernaut onlayer effects
    hide bitch onlayer effects

    with dissolve

    "One you recognize from photos as an upperclassman, and one of the X-Men, Colossus."
    
    $ Piotr.name = "Colossus"

    "An imposing man of nearly 2 meters tall, he looks like a living statue carved out of steel."
    "Yet even he looks like a child. . ."
    ". . . compared to that nearly 3 meter tall behemoth with a dome of metal covering his head."

    show expression "images/backgrounds/ch1/bg_ch1_danger_punches2.webp" as punches onlayer master zorder 13:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/effects/clash.webp" as clash onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    ch_Cain "If ya just tell me what I want to know, maybe I won't melt you down into a cock ring."
    ch_Cain "Now, where. . ."

    show expression "images/effects/pow.webp" as pow onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.75 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    ch_Cain ". . . the fuck is Charles?!"

    show expression "images/effects/pow.webp" as pow onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.75 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    ch_Cain "Tell me, ya commie bastard!"
    "[Piotr.name] doesn't respond. He lunges."

    show expression "images/backgrounds/ch1/bg_ch1_danger_punches1.webp" as punches onlayer master zorder 13:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/effects/pow.webp" as pow onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.75 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    menu:
        "Don't draw attention to yourself (reluctant)":
            call ch1_Juggernaut_attack_path_1A from _call_ch1_Juggernaut_attack_path_1A

            $ Player.History.update("ch1_Juggernaut_attack_path_1A")
            $ Player.History.update("Reluctant")
        "Try to help [Piotr.name] (determined)":
            call ch1_Juggernaut_attack_path_1B from _call_ch1_Juggernaut_attack_path_1B

            $ Player.History.update("ch1_Juggernaut_attack_path_1B")
            $ Player.History.update("Determined")

    camera:
        block:
            ease 1.5 blur 15
            ease 1.5 blur 0
            repeat

    "You hold on to [Rogue.name] for dear life, but the pain in your head and ribs finally overcomes you."

    $ fade_to_black(0.4)

    camera
    
    play music "sounds/music/Almost an Ending.ogg" fadeout 5.0

    "You black out. . ."

    hide lights onlayer master
    hide destruction2 onlayer master
    hide lights2 onlayer master
    hide hole onlayer master
    hide top_bar onlayer master
    hide destruction1 onlayer master
    hide Rogue onlayer master
    hide Juggernaut onlayer master
    hide punches onlayer master
    hide wall_damage onlayer master
    hide Piotr onlayer master
    hide Laura onlayer master
    hide claws onlayer master
    hide Ororo onlayer master
    
    hide background onlayer comic_cutout1
    hide lights onlayer comic_cutout1
    hide destruction2 onlayer comic_cutout1
    hide lights2 onlayer comic_cutout1
    hide hole onlayer comic_cutout1
    hide destruction1 onlayer comic_cutout1
    hide Rogue onlayer comic_cutout1

    $ danger_red_alert = False

    pause 2.0

    "You have a deep, dreamless sleep that feels like it drags on forever."

    python:
        for C in all_Characters:
            C.timed_text_options = {}

    $ counter = 0

    while counter < 2:
        call start_new_day from _call_start_new_day_2

        python:
            for C in all_Characters:
                C.timed_text_options = {}

        $ counter += 1

    $ season = 2

    $ season_day = 0

    python:
        for C in all_Characters:
            C.History.manually_reset("event")
            C.History.manually_reset("season")

    $ Player.History.manually_reset("event")
    $ Player.History.manually_reset("season")

    $ time_index = 2
    
    $ lighting = "evening"

    $ infirmary_in_bed = True

    camera:
        blur 15

    call remove_Characters(location = "bg_infirmary") from _call_remove_Characters_214
    call set_the_scene(location = "bg_infirmary") from _call_set_the_scene_230

    "You wake up to a room you've never seen before."

    camera:
        ease 2.0 blur 0

    "You sit up in the bed, a jolt of pain in your side reminding you what just happened."

    $ Cecilia.name = "???"

    show expression "images/backgrounds/base/bg_infirmary_doctor.webp" as Cecilia onlayer master:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    ch_Cecilia "[Player.full_name]?! You're awake already?"
    ch_Player "Uh, hey. . . yeah? How long has it been?"
    ch_Player "Sure felt like forever."
    ch_Player "Who are you?"

    $ Cecilia.name = "Dr. Reyes"

    ch_Cecilia "My name is Dr. Reyes."
    ch_Cecilia "It's only been two days."
    ch_Cecilia "With a head injury as bad as yours, we were worried you might not wake up at all. . ."
    ch_Cecilia "But we certainly didn't expect this."
    ch_Player "Where's [Rogue.name]? Is she okay?"
    ch_Cecilia "Yes, don't worry. She woke up yesterday, she'll be just fine."
    ch_Player "I'm gonna go see her."
    ch_Cecilia "Not in your current condition you won't."
    ch_Cecilia "You broke two ribs and cracked a third!"
    ch_Cecilia "Not to mention a severe concussion."
    ch_Player "Oh come on, it doesn't feel that bad."

    $ infirmary_in_bed = False

    "You swing your feet off the bed and try standing up."
    "It hurts like hell and you have to grab the doctor to stay upright."
    ch_Cecilia "Sit back down young man."
    ch_Player "I'm going to see [Rogue.name] even if I have to crawl my way over."
    ch_Cecilia "All you kids are the same. . . reckless idiots."
    ch_Cecilia "Fine! But only after we take another set of tests."

    $ fade_to_black(0.4)

    "You humor the doctor, the tests and X-rays are quick anyway."

    pause 2.0

    $ fade_in_from_black(0.4)

    ch_Cecilia "This is very bizarre."
    ch_Cecilia "To already have callus formation and remodeling. . ."
    ch_Cecilia "Are you sure you didn't have a prior rib injury?"
    ch_Cecilia "Maybe we misread the prior X-rays. . ."
    ch_Player "I think it would've been pretty obvious."
    ch_Cecilia "Alright you can go see her if you feel up to it."
    ch_Cecilia "But be careful! I don't want to see you unconscious again."
    ch_Player "Yes ma'am!"

    hide Cecilia onlayer master
    
    "You leave the infirmary and head to [Rogue.name]'s room."

    $ fade_to_black(0.4)

    "On the way there, you're suddenly accosted."

    call remove_Characters(location = "bg_girls_hallway") from _call_remove_Characters_215
    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_231
    call send_Characters(Laura, "bg_girls_hallway") from _call_send_Characters_170

    $ Laura.change_face("angry1", eyes = "closed", blush = 1)

    "[Laura.name] leaps at you, pulling you into a bear hug and causing a jolt of pain in your ribs."
    ch_Laura "How are you awake already?!"

    $ Laura.blush = 2

    ch_Laura "I just checked on you an hour ago, the doctor said it might be days!"

    $ Laura.change_face("angry1", eyes = "closed", blush = 2)

    camera:
        block:
            ease 1.5 blur 5
            ease 1.5 blur 0
            repeat

    "She's squeezing too hard and the pain sucks the breath out of your lungs."
    $ Laura.change_face("furious", eyes = "closed", blush = 3)

    ch_Laura "You idiot, what were you thinking?!" 
    ch_Laura "I'm never letting you out of my sight again."
    ch_Player "[Laura.name]. . . can't. . . breathe. . ."

    $ Laura.change_face("angry1", blush = 2)

    "She lets go and collects herself."

    camera

    $ Laura.change_face("furious", blush = 1)

    ch_Laura "Suck it up, you did this to yourself."

    if Player.History.check("ch1_Juggernaut_attack_path_1A"):
        ch_Player ". . . don't know what the hell happened."
    else:
        ch_Player "I didn't expect my power to be completely useless. . ."

    $ Laura.change_face("confused1")

    menu:
        extend ""
        "I'd still do it all over again, I had to help [Rogue.name].":
            call change_Companion_stat(Laura, "love", medium_stat) from _call_change_Companion_stat_1587
            call change_Companion_stat(Laura, "trust", medium_stat) from _call_change_Companion_stat_1588

            $ Laura.change_face("angry1", eyes = "right") 
            
            ch_Player "She's our friend, remember?"
            ch_Player "And don't tell me you weren't getting ready to fight that behemoth in order to protect me." 

            $ Laura.change_face("furious", blush = 1) 
            
            ch_Laura "Then I'll have to keep an even closer eye on you."
        "Yeah. . . I don't know what I was thinking.":
            call change_Companion_stat(Laura, "love", small_stat) from _call_change_Companion_stat_1589

            $ Laura.change_face("suspicious2") 
            
            ch_Player "But [Rogue.name] is our friend, I couldn't just run away." 
            
            $ Laura.change_face("angry1", eyes = "right") 
            
            ch_Player "And don't tell me you weren't ready to fight that behemoth in order to protect me." 

            $ Laura.change_face("furious", blush = 1) 
            
            ch_Laura "Next time, just stay behind me."
        "Oh come on, I'm fine!":
            call change_Companion_stat(Laura, "trust", -small_stat) from _call_change_Companion_stat_1590

            $ Laura.change_face("suspicious2") 
            
            ch_Player "I was gonna help [Rogue.name] either way." 
            
            $ Laura.change_face("angry1", eyes = "right") 
            
            ch_Player "And don't tell me you weren't getting ready to fight that behemoth in order to protect me." 

            $ Laura.change_face("furious", blush = 1) 
            
            ch_Laura "You're an idiot, you could've died." 
            
    $ Laura.change_face("suspicious1", blush = 1)
            
    ch_Laura "This whole 'friends' thing keeps getting more confusing."

    $ Laura.change_face("confused2")

    ch_Laura "Why would a friend want you to almost die to save them?" 

    $ Laura.change_face("appalled2")

    ch_Laura "It makes no sense!" 

    $ Laura.change_face("furious")

    ch_Player "It doesn't work like that, it's the other way around." 

    $ Laura.change_face("confused2")

    ch_Player "Of course you wouldn't want your friend to die trying to save you."

    $ Laura.change_face("angry1")

    ch_Player "What makes someone a real friend - or more - is the willingness to go that far." 
    ch_Player "Even when the other person wouldn't ask for it."

    $ Laura.change_face("worried1")

    ch_Player "That's how I know you're a real friend even if you don't understand it." 

    $ Laura.change_face("worried1", eyes = "right")

    ch_Player "We both know you were ready to die trying to protect me too."
    ch_Player "And I obviously wouldn't want that."

    $ Laura.change_face("angry1", eyes = "right")

    ch_Laura "I. . . see."

    $ Laura.change_face("angry1")

    ch_Player "I'm gonna go check on [Rogue.name] now, okay, [Laura.name]?" 
    ch_Laura "Fine, but I'll be watching you."

    $ Laura.change_face("suspicious2") 

    pause 1.0

    $ Laura.change_face("worried1", eyes = "right", blush = 1)

    ch_Laura "And you can call me Laura. . . if you want."

    $ Laura.names.append("Laura")

    call remove_Characters(Laura) from _call_remove_Characters_216

    "She doesn't let you respond before leaving."

    menu:
        extend ""
        "Keep calling her 'X-23'":
            pass
        "Call her 'Laura'":
            $ Laura.name = "Laura"

    if Laura.petname == "X-23":
        $ Laura.petname = Laura.name

    "You're about to head to [Rogue.name]'s room when you get nearly tackled. . . again!"

    call send_Characters(Jean, "bg_girls_hallway") from _call_send_Characters_171

    $ Jean.change_face("worried3", eyes = "closed", blush = 1)

    "[Jean.name] wraps you in another bear hug."

    if Jean.quirk or Jean.quirk is None:
        ch_Jean "Little bro'!!!"

    ch_Jean "Thank god you're alright." 
    ch_Jean "I heard you got hurt, but I guess it wasn't as bad as they said." 

    $ Jean.change_face("angry2", eyes = "closed", blush = 1)

    ch_Jean "You idiot, you're not allowed to die on me."

    $ Jean.change_face("worried2", blush = 1)

    ch_Player "{i}Jean{/i}. . . {i}ribs{/i}. . . {i}hurt{/i}. . ."
    "She lets go."
    ch_Player ". . . I've been called an idiot at least a couple times today already."

    if Jean.quirk is None:
        $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

        ch_Player "And did you just call me 'little bro'?" 

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "Yes. . ."
        ch_Jean "I mean, you are my little bro'. . ."

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 2)

        pause 1.0

        $ Jean.blush = 1

        ch_Jean "It's not a problem. . . if I keep calling you that, right?"

        menu:
            extend ""
            "No, you can. . . I just wasn't expecting it. (encourage_quirk)":
                call change_Companion_stat(Jean, "love", medium_stat) from _call_change_Companion_stat_1591
                
                $ Jean.change_face("worried2", mouth = "lipbite", blush = 2)

                pause 1.0

                $ Jean.change_face("sexy", eyes = "right", blush = 2) 
                
                ch_Jean "Good. . ." 
                
                $ Jean.Player_petname = "little bro'"

                $ Jean.History.update("quirk_encouraged")
            "I'd rather you just use my name. (discourage_quirk)":
                $ Jean.change_face("angry1", blush = 1)

                ch_Jean "Ugh, fine."

                $ Jean.Player_petname = Player.first_name

                $ Jean.History.update("quirk_discouraged")

        $ Jean.change_face("suspicious1")

        ch_Jean "Anyways." 

    ch_Jean "I told you to not die!" 

    $ Jean.change_face("angry1")

    ch_Player "But. . . I. . ."
    ch_Jean "Tell me everything, what happened?"
    "You explain the situation."

    if Player.History.check("ch1_Juggernaut_attack_path_1A"):
        $ Jean.change_face("worried2")

        menu:
            extend ""
            "I saw [Rogue.name], but then I saw that. . . [Cain.name]. . .":
                $ Jean.change_face("worried1") 
                
                ch_Player "I just froze up." 
                
                $ Jean.change_face("sad") 
                
                ch_Player "Eventually I snapped out of it, but maybe if I acted sooner things would've been different."
                
                call change_Companion_stat(Jean, "love", medium_stat) from _call_change_Companion_stat_1592
                call change_Companion_stat(Jean, "trust", small_stat) from _call_change_Companion_stat_1593

                ch_Jean "I'm glad she's okay." 
                ch_Jean "But she was already hurt by the time you got there." 
                
                $ Jean.change_face("worried1", mouth = "smirk") 
                
                ch_Jean "Don't worry, I'll back you up next time." 
                ch_Jean "Then you won't have anything to worry about. . ." 
                
                $ Jean.change_face("furious", eyes = "right") 
                
                ch_Jean "Once my power cooperates. . ."
            "Maybe if I tried helping Colossus instead, things would've been different.":
                call change_Companion_stat(Jean, "love", small_stat) from _call_change_Companion_stat_1594
                call change_Companion_stat(Jean, "trust", -small_stat) from _call_change_Companion_stat_1595
                
                $ Jean.change_face("angry1")
                
                ch_Jean "No, [Jean.Player_petname]." 
                ch_Jean "Don't be reckless."
                
                $ Jean.change_face("worried1", mouth = "smirk") 
                
                ch_Jean "Next time I'll be there to back you up and you won't have to worry about anything. . ." 
                
                $ Jean.change_face("furious", eyes = "right") 
                
                ch_Jean "If my power cooperates. . ."
    else:
        menu:
            extend ""
            "Well, when I got there I saw [Rogue.name]. . .":
                $ Jean.change_face("worried2") 
                
                ch_Player "She was unconscious, looked hurt pretty bad." 
                ch_Player "I couldn't just stand around." 
                
                call change_Companion_stat(Jean, "love", medium_stat) from _call_change_Companion_stat_1596
                call change_Companion_stat(Jean, "trust", medium_stat) from _call_change_Companion_stat_1597

                $ Jean.change_face("sad") 

                ch_Jean "I'm glad she's okay." 
                
                $ Jean.change_face("worried1") 
                
                ch_Player "I tried nullifying the big guy, but it didn't work for some reason. . ."
            "When I got there, sure the guy looked big, but I thought I could just nullify him.":
                call change_Companion_stat(Jean, "trust", -medium_stat) from _call_change_Companion_stat_1602

                $ Jean.change_face("appalled1") 
                
                ch_Player "It didn't really work out for some reason. . ." 
                
                $ Jean.change_face("angry1") 
                
                $ temp = Jean.Player_petname.capitalize()

                ch_Jean "[temp]. . . you are SUCH an idiot!" 
                
                $ Jean.change_face("appalled1") 
                
                ch_Jean "Running in recklessly like that, what the hell were you thinking?!" 
                
                $ Jean.change_face("confused2") 

                ch_Player "It was kinda stupid. . ." 
                
        ch_Jean "If I was there things would've gone differently." 
        
        $ Jean.change_face("angry1", eyes = "right") 
        
        ch_Jean "I wouldn't have let you get hurt." 
        
        $ Jean.change_face("furious", eyes = "right") 
        
        ch_Jean "If only my goddamn power would cooperate. . ."

    $ Jean.change_face("worried1")

    ch_Player "Don't worry, I'm sure we can figure it out." 

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Jean "Of course I. . . we will." 

    $ Jean.change_face("smirk2", blush = 1)

    ch_Jean "Thanks. . ."
    ch_Player "I'm gonna go check on [Rogue.name] now, I'll see you later."

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Jean "Bye."

    call remove_Characters(Jean) from _call_remove_Characters_217

    "You finally make your way to [Rogue.name]'s room."

    call knock_on_door(times = 2) from _call_knock_on_door_25

    ch_Player "[Rogue.name], can I come in?"

    $ temp = Rogue.Player_petname.capitalize()

    ch_Rogue "[temp]?! Is that you?"

    call send_Characters(Rogue, "bg_girls_hallway", behavior = False) from _call_send_Characters_172

    $ Rogue.change_face("worried3")

    "She opens the door and pulls you inside. . ."

    call set_the_scene(location = Rogue.home) from _call_set_the_scene_232
    call send_Characters(Rogue, location = Rogue.home, behavior = False) from _call_send_Characters_286

    $ Rogue.change_face("worried2", eyes = "closed", blush = 1)

    "Into {i}another{/i} bear hug."
    "She's squeezing so hard you think you hear your tender ribs start cracking again."

    $ Rogue.change_face("worried2", blush = 1)

    ch_Player "{i}[Rogue.name]{/i}. . . {i}squeezing{/i}. . ." 
    ch_Rogue "Sorry, hon'."
    "She lets go."

    $ Rogue.change_face("worried1")

    ch_Rogue "Ah thought you were. . . a lot worse off." 
    ch_Player "It hurt pretty bad in the moment, but I guess it wasn't serious."

    $ Rogue.change_face("worried1", eyes = "right", blush = 1)

    ch_Rogue "And, ah heard what you did for me. . . " 

    $ Rogue.change_face("sad", blush = 1)

    ch_Rogue "Ah'm real sorry you got hurt cuz of me." 

    menu:
        extend ""
        "Don't worry about me. I'd do it again, no question.":
            call change_Companion_stat(Rogue, "love", medium_stat) from _call_change_Companion_stat_855 
            call change_Companion_stat(Rogue, "trust", medium_stat) from _call_change_Companion_stat_856

            $ Rogue.change_face("worried2", blush = 2) 
            
            ch_Player "Maybe if I was faster you wouldn't have gotten hurt in the first place." 
            
            $ Rogue.change_face("sad", blush = 1) 
            
            ch_Rogue "Ah hope ya never have to again. . ." 
            
            $ Rogue.change_face("angry1", eyes = "right", blush = 1) 
            
            ch_Rogue "And next time, ah'll be right there fightin' alongside ya."
        "It's not your fault.":
            call change_Companion_stat(Rogue, "trust", medium_stat) from _call_change_Companion_stat_635

            $ Rogue.change_face("worried1", blush = 1) 
            
            ch_Player "Maybe if I was faster you wouldn't have gotten hurt in the first place." 
            ch_Rogue "Don't blame yerself." 
            
            $ Rogue.change_face("angry1", eyes = "right", blush = 1) 
            
            ch_Rogue "Next time, ah'll be right there fightin' alongside ya."
        "Yeah. . . it wasn't fun.":
            call change_Companion_stat(Rogue, "love", -small_stat) from _call_change_Companion_stat_636

            $ Rogue.change_face("worried1", eyes = "down", blush = 1) 
            
            ch_Player "But we're both okay now." 
            ch_Rogue "Ah really am sorry. . ." 
            
            $ Rogue.change_face("worried1", blush = 1) 
            
            ch_Rogue "Next time, ah'll be right there fightin' alongside ya."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Player "Thanks [Rogue.petname], I'll be counting on you. . ."

    $ Contacts.append(Charles)

    call receive_text(Charles, "Please come to my office.") from _call_receive_text_651
    call open_texts(Charles) from _call_open_texts_9
    call receive_text(Charles, "I would like to explain a few things regarding the incident the other day.") from _call_receive_text_652

    pause

    call send_text(Charles, "I'll be right there") from _call_send_text_48

    pause 2.0

    hide screen phone_screen

    ch_Player "Hey, why would [Charles.name] text me when he can just talk in my head?" 

    $ Rogue.change_face("confused1")

    ch_Rogue "The Professor makes an effort to respect our privacy."
    ch_Rogue "Avoids usin' his powers inside our bedrooms 'cept for special circumstances."
    ch_Rogue "Not to mention, our rooms are able to block mutant powers when needed."

    $ Rogue.change_face("confused1", mouth = "smirk")

    ch_Rogue "For security reasons."
    ch_Rogue "Ah reckon you can guess why it would be a problem if someone like [Kurt.name] just popped up in the middle of someone's room."
    ch_Player "I. . . never thought of that."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Cause yer a gentleman, you'd never try somethin' untoward." 

    $ Rogue.change_face("smirk2")

    ch_Player "Thanks. . . I gotta go talk to [Charles.name], I'll see you later."
    ch_Rogue "Bye." 

    $ fade_to_black(0.4)

    "You head to [Charles.name]'s study."

    call remove_Characters(location = "bg_study") from _call_remove_Characters_218
    call send_Characters(Charles, "bg_study") from _call_send_Characters_173
    call set_the_scene(location = "bg_study") from _call_set_the_scene_233

    $ Charles.change_face("happy")

    ch_Charles "Hello [Player.first_name], I am glad to see you doing so well."
    ch_Player "Better than expected apparently."

    $ Charles.change_face("confused")

    ch_Charles "Yes, I spoke to Cecilia. She was quite surprised by your condition."

    $ Charles.change_face("neutral")

    ch_Charles "It seems there may be another, previously unknown, aspect to your abilities." 

    menu:
        extend ""
        "Wait a minute. . . so I might actually be able to fly one day???":
            $ Charles.change_face("happy") 
            
            ch_Charles "I promise nothing, but there is always a possibility. . ."
            ch_Player "Yesss!"
        "I hope it's a good one.":
            ch_Charles "I think you will find this to be good news."
        "Great. . . more complications.":
            ch_Charles "Not a complication, a boon if anything."

    $ Charles.change_face("sad")

    ch_Charles "By all accounts, when you were brought to the infirmary, your injuries were quite severe."

    $ Charles.change_face("confused")

    ch_Charles "That was only two days ago."
    ch_Charles "Radiography from just this morning shows callus formation and even remodeling around your previously fractured ribs."

    $ Charles.change_face("neutral")

    ch_Charles "In other words, it is as if they have been healing for several weeks and not just two days."

    $ Charles.change_face("confused")

    ch_Charles "And I have still neglected to mention your head injury, which was more critical than you think."
    ch_Player "Damn. . . I just thought my injuries weren't as bad as people thought."
    ch_Player "So you think it's part of my powers?"

    $ Charles.change_face("neutral")

    ch_Charles "Potentially."
    ch_Charles "Robust constitutions are a common by-product of mutation. Look at Colossus for example."

    $ Charles.change_face("confused")

    ch_Charles "Do not take this as an invitation for recklessness."
    ch_Charles "I recommend you continue carefully exploring your abilities with [Jean.name]."

    if Player.History.check("ch1_Juggernaut_attack_path_1A"):
        $ Charles.change_face("sad")

        ch_Charles "I also wanted to warn you."
        ch_Charles "Do not rely too heavily on your nullification power."

        $ Charles.change_face("neutral")

        ch_Charles "Had you tried using it on Cain Marko, aka 'The Juggernaut', we expect the effect would have been naught."
    else:
        ch_Charles "However, that is not the main reason for this visit."

        $ Charles.change_face("neutral")

        ch_Charles "As you know all too well, your nullification did not have an effect on Cain Marko aka 'The Juggernaut.'"
        ch_Player "Am I just not strong enough?"

        $ Charles.change_face("confused")

        ch_Charles "Hardly."

        $ Charles.change_face("neutral")

    ch_Charles "You see, Cain is not a mutant like you and I."
    ch_Charles "His powers are derived from. . . something else."

    $ Charles.change_face("sad")

    ch_Charles "We have an unfortunate history."
    ch_Charles "My X-Men were fortuitous in their timing, but only able to drive him away as a team."

    $ Charles.change_face("neutral")

    ch_Charles "This is all to say, there are beings in the world with unimaginable powers who are not 'mutants.'"
    ch_Charles "Be very careful with who you try using your power on in the future."
    ch_Player "Thanks for the warning."
    ch_Player "I'm not gonna lie, this is all pretty daunting. . ."

    $ Charles.change_face("sad")

    ch_Charles "This is why we all must help each other whenever possible."
    ch_Charles "I am sorry your 'introduction' to our world has been. . . quite deadly." 
    ch_Player "It's alright, thanks for the insight."

    $ Charles.change_face("happy")

    ch_Player "And thank you for everything you've done for me so far." 
    ch_Charles "You are a good person, [Player.first_name]."
    ch_Charles "You made this evident these past months, and especially two days ago."
    ch_Charles "With trustworthy friends - and a bit of ambition - I think you will become quite capable."

    $ fade_to_black(0.4)

    "You leave [Charles.name]'s study with a lot to think about."
    "Not to mention the sharp pain in your side whenever you try to breathe."

    $ lights_on = True

    $ time_index = 3
    
    $ lighting = "night"

    call set_the_scene(location = Player.home) from _call_set_the_scene_234

    pause 1.0

    call knock_on_door(times = 2) from _call_knock_on_door_26

    "As you're getting ready to finally go to bed, someone knocks on your door."
    "Too tired to even see who it is, you let them in."

    # $ Ororo.right_arm = 2

    # call change_Outfit(Ororo, Ororo.Wardrobe.Outfits["Hero (Chapter I)"], instant = True) from _call_change_Outfit_28
    call add_Characters(Ororo) from _call_add_Characters_49

    $ Ororo.change_face("worried1")

    ch_Player "Professor?!"
    ch_Ororo "I apologize for bothering you at such a late hour. . ."

    # $ Ororo.right_arm = 1
    $ Ororo.change_face("worried1", eyes = "down")

    pause 1.0

    $ Ororo.change_face("worried1", mouth = "smirk")

    ch_Ororo "Are you alright?" 
    ch_Ororo "I heard your injuries were severe."
    ch_Ororo "You look quite exhausted."

    menu:
        extend ""
        "I've been better. . . but don't apologize, I wanted to thank you.":
            $ Ororo.change_face("worried2") 
            
            call change_Companion_stat(Ororo, "love", 0) from _call_change_Companion_stat_858 
            call change_Companion_stat(Ororo, "trust", 0) from _call_change_Companion_stat_859
        
            ch_Ororo "I do not deserve your thanks." 
            
            $ Ororo.change_face("worried1", eyes = "right") 
            
            ch_Ororo "Had we stopped him sooner. . ."
        "I am exhausted, the past few days have really done a number on me. . .":
            $ Ororo.change_face("worried1", eyes = "right") 
            
            call change_Companion_stat(Ororo, "love", 0) from _call_change_Companion_stat_860
        
            ch_Ororo "That is why I am here. . ."
        "I was about to go to bed, this can't wait?":
            $ Ororo.change_face("confused1", eyes = "squint") 
            
            call change_Companion_stat(Ororo, "love", 0) from _call_change_Companion_stat_861

            ch_Ororo "It cannot. . ."

    $ Ororo.change_face("worried1")

    ch_Ororo "I heard about your condition, and the circumstances of the attack before I arrived."

    $ Ororo.change_face("sad")

    ch_Ororo "I deeply regret not being swift enough to prevent your injuries. . ."

    $ Ororo.change_face("worried1")

    ch_Ororo "Thus, I felt it necessary to apologize."
    ch_Ororo "I also apologize for not coming to check on you sooner."
    ch_Ororo "I hope you understand, I had other responsibilities to take care of." 

    menu:
        extend ""
        "None of this is your fault, but I still really appreciate it.":
            $ Ororo.change_face("worried1", mouth = "smirk") 
            
            call change_Companion_stat(Ororo, "love", 0) from _call_change_Companion_stat_862 
        "Well, luckily I wasn't too badly injured. . .":
            $ Ororo.change_face("worried1", mouth = "smirk")
        "Yeah. . . I was wondering what the hell took you so long. . .": 
            $ Ororo.change_face("worried1", eyes = "right") 
            
            call change_Companion_stat(Ororo, "love", 0) from _call_change_Companion_stat_863

    $ Ororo.change_face("worried1")

    ch_Player "But why couldn't you come see me in the morning?" 
    ch_Player "Are you not gonna be sticking around?"
    ch_Ororo "Unfortunately, no."
    ch_Ororo "This attack was a surprise to us all, and we had to abandon our current mission in order to thwart it."

    $ Ororo.change_face("neutral")

    ch_Ororo "We will be heading back out in the morning." 

    $ Ororo.change_face("smirk2")

    ch_Ororo "This reminds me, Colossus also wanted to express his well wishes."
    ch_Ororo "He was not badly injured and appreciates what you did, regardless of the outcome." 

    $ Ororo.change_face("worried1", mouth = "smirk")

    ch_Ororo "Now, I shall let you get some rest."

    $ Ororo.change_face("worried1", eyes = "right")

    ch_Ororo "Unfortunately, I will be gone for a while longer. . ." 

    $ Ororo.change_face("worried1")

    ch_Ororo "I hope you. . ."

    $ Ororo.change_face("worried1", eyes = "right")

    ch_Ororo "{size=-5}Bright lady spare me from this childish embarrassment{/size}. . ."

    $ Ororo.change_face("worried1", mouth = "lipbite")

    ch_Ororo "I will see you when I return. Please, sleep soundly."

    call send_Characters(Ororo, "hold") from _call_send_Characters_174

    "She leaves, gently closing the door behind her."

    $ lights_on = False

    $ lighting = "moonlight"

    call set_the_scene(fade = False, fade_Characters = False) from _call_set_the_scene_235

    pause 2.0

    $ fade_to_black(0.4)

    "You gingerly get into bed and fall asleep as soon as your head hits the pillow."

    call refresh_season_content from _call_refresh_season_content_1

    $ Player.date_planned = {}
    $ Player.schedule = {}

    python:
        for C in all_Companions:
            C.wants_alone_time = 0
            C.schedule = {}

    $ unlocked_Characters.append(Cain)
    $ unlocked_Characters.append(Piotr)
    $ unlocked_Characters.append(Cecilia)

    pause 2.0

    $ season_completed = False

    $ ongoing_Event = False

    return

label ch1_Juggernaut_attack_path_1A:
    show expression "images/backgrounds/ch1/bg_ch1_danger_punches2.webp" as punches onlayer master zorder 13:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/effects/pow.webp" as pow onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.75 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    "You watch the two titans clash, feeling a mixture of both awe and horror."
    "Any thoughts of helping [Rogue.name] are driven from your mind."
    "Practicing scenarios in the Danger Room is one thing. . ."
    "Seeing such monstrous strength on display roots your feet to the ground."

    show expression "images/backgrounds/ch1/bg_ch1_danger_punches1.webp" as punches onlayer master zorder 13:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/effects/pow.webp" as pow onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.75 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    "[Piotr.name] is more agile, but obviously not as strong."
    "It's clear [Cain.name] is just toying with him."

    show expression "images/backgrounds/ch1/bg_ch1_danger_punches2.webp" as punches onlayer master zorder 13:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/effects/pow.webp" as pow onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.75 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    ch_Cain "HAHAHA, YOU HIT LIKE A BITCH TOO!"

    "With each thunderous clash, new bits of the ceiling fall to the ground. . ."
    "Wait. . . Ceiling. . ."
    ch_Player "Shit! [Rogue.name]!" 
    "You finally shake out of the stupor and dash over to her."

    # call change_Outfit(Laura, Laura.Wardrobe.Outfits["Hero (Chapter I)"], instant = True) from _call_change_Outfit_29

    call show_Character(Laura, x = stage_far_far_right, sprite_layer = 16, color_transform = red_lights, fade = False) from _call_show_Character_3

    $ Laura.change_face("furious")

    ch_Laura "[Player.first_name], where are you goi. . ."

    $ Laura.change_face("appalled3")

    pause 1.0

    $ Laura.change_face("appalled3", eyes = "right")

    "She notices [Rogue.name]."

    # $ Laura.left_arm = 2

    pause 0.2

    $ Laura.left_claws = True
    $ Laura.right_claws = True
    $ Laura.unsheathing_claws = True

    show expression "images/effects/snikt.webp" as snikt onlayer effects:
        anchor (0.5, 0.5) pos (0.9, 0.1)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.5 alpha 1.0
        ease 2.0 alpha 0.0

    $ renpy.pause(0.1, hard = True)

    $ Laura.unsheathing_claws = False

    ch_Laura "What the. . ."

    $ Laura.change_face("worried4")

    show expression "images/backgrounds/ch1/bg_ch1_danger_punches1.webp" as punches onlayer master zorder 13:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/effects/pow.webp" as pow onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.75 alpha 1.0
        ease 1.0 alpha 0.0

    with big_screenshake

    $ Laura.change_face("appalled1", eyes = "right")

    "You get to [Rogue.name] just as more debris is about to fall on her."
    "Without thinking, you shield [Rogue.name] with your body."
    "Most of it misses. . ."

    $ Laura.change_face("worried4")

    pause 1.0

    show expression "images/effects/bone_crack.webp" as bone_crack onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    pause 1.0

    camera:
        block:
            ease 1.5 blur 15
            ease 1.5 blur 0
            repeat

    "One chunk hits you, {i}hard{/i}, glancing off of your ribcage."
    "Another, smaller one, hits you in the head."

    $ Laura.left_claws = False
    $ Laura.right_claws = False
    $ Laura.sheathing_claws = True

    show expression "images/effects/snakt.webp" as snakt onlayer effects:
        anchor (0.5, 0.5) pos (0.9, 0.1)

        zoom 0.5
        alpha 0.0
        ease 0.01 alpha 1.0
        ease 0.5 zoom 0.0 alpha 0.0

    $ renpy.pause(0.51, hard = True)

    $ Laura.sheathing_claws = False

    pause 0.5
    
    $ Laura.change_face("worried2")
    $ Laura.change_arms("neutral")

    ch_Laura "[Player.first_name]!"
    "It feels like somebody just stabbed you in the side while simultaneously hitting you in the head with a baseball bat."

    $ Laura.change_face("worried1")

    "Almost blacking out from the pain, you look over and see [Laura.name]."
    "For the first time, she actually looks worried instead of angry."
    ch_Player "Fuuuuuck. . . I'd give anything to have a healing factor like [Laura.name] right about now. . ."

    with small_screenshake

    camera

    $ Player.power = 50

    "The pain from your ribs suddenly envelops your entire body for a split second."
    "Then comes the nausea."
    "Your comment only makes you feel even more like shit."
    "Still, you grit your teeth and slowly try to drag [Rogue.name] out of harm's way."
    "[Laura.name] is about to come help. . ."

    $ Player.power = 0

    hide Rogue onlayer master

    with dissolve

    call hide_Character(Laura) from _call_hide_Character_30

    show expression "images/backgrounds/ch1/bg_ch1_danger_punches1.webp" as punches onlayer master zorder 13:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/effects/pow.webp" as pow onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.75 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    ch_Cain "Oh come on Ivan, it's useless." 
    ch_Cain "Ain't nobody can stop me when I get goin'."
    ch_Cain "Ah fuck it."

    hide punches onlayer master

    show expression "images/backgrounds/ch1/bg_ch1_danger_headbutt.webp" as Juggernaut onlayer master zorder 13:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/backgrounds/ch1/bg_ch1_danger_wall_damage.webp" as wall_damage onlayer master zorder 11:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/backgrounds/ch1/bg_ch1_danger_Piotr.webp" as Piotr onlayer master zorder 11:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/effects/clang.webp" as clang onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    with big_screenshake

    "You look over to see [Cain.name] headbutt [Piotr.name] hard enough to send him flying across the room. . ."

    show expression "images/effects/crash.webp" as crash onlayer effects:
        anchor (0.5, 0.5) pos (0.2, 0.7)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    hide Piotr onlayer master

    with faster_dissolve

    ". . . and through the goddamn wall."

    show expression "images/backgrounds/ch1/bg_ch1_danger_Juggernaut_Null.webp" as Juggernaut onlayer master zorder 14:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    with dissolve

    "Then, [Cain.name] turns in your direction."
    ch_Cain "So, shithead, maybe you can give me some answers. . ."

    show expression "images/backgrounds/ch1/bg_ch1_danger_Juggernaut_Laura.webp" as Juggernaut onlayer master zorder 14:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    with dissolve

    ch_Laura "{i}Grrrrrr{/i}. . ."

    show expression "images/backgrounds/ch1/bg_ch1_danger_Laura_hand.webp" as Laura onlayer master zorder 16:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    pause 0.5

    show expression "images/backgrounds/ch1/bg_ch1_danger_Laura_claws.webp" as claws onlayer master zorder 17:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/effects/snikt.webp" as snikt onlayer effects:
        anchor (0.5, 0.5) pos (0.6, 0.65)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.5 alpha 1.0
        ease 2.0 alpha 0.0

    pause 2.0

    hide Laura onlayer master
    hide claws onlayer master

    show expression "images/backgrounds/ch1/bg_ch1_danger_Laura.webp" as Laura onlayer master zorder 16:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    with dissolve

    "Before he can get any closer, [Laura.name] leaps to get in between you and [Cain.name]."

    show expression "images/backgrounds/ch1/bg_ch1_danger_hole_Ororo.webp" as hole onlayer master zorder 8:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    with dissolve

    pause 1.0

    show expression "images/backgrounds/ch1/bg_ch1_danger_hole_Ororo_lightning.webp" as hole onlayer master zorder 8:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    with fastest_dissolve

    show expression "images/backgrounds/ch1/bg_ch1_danger_hole_Ororo.webp" as hole onlayer master zorder 8:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    with fastest_dissolve

    show expression "images/effects/kaboom.webp" as kaboom onlayer effects:
        anchor (0.5, 0.5) pos (0.32, 0.3)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.75 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    "A sudden clap of thunder draws everyone's attention to the hole in the ceiling."

    show expression "images/backgrounds/ch1/bg_ch1_danger_Juggernaut_Ororo.webp" as Juggernaut onlayer master zorder 14:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    with dissolve

    ch_Cain "What the fuck now. . ."

    pause 1.0

    show expression "images/backgrounds/ch1/bg_ch1_danger_Ororo.webp" as Ororo onlayer master zorder 11:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/backgrounds/ch1/bg_ch1_danger_hole_Ororo_lightning.webp" as hole onlayer master zorder 8:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    with fastest_dissolve

    show expression "images/backgrounds/ch1/bg_ch1_danger_hole_Ororo.webp" as hole onlayer master zorder 8:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    with fastest_dissolve

    show expression "images/effects/kaboom.webp" as kaboom onlayer effects:
        anchor (0.5, 0.5) pos (0.32, 0.3)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.75 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    "A furious [Ororo.name] descends from the sky."
    ch_Cain "FUCK OFF!"

    hide Laura onlayer master

    "[Laura.name] uses the distraction to start dragging you and [Rogue.name] out of the room."

    return

label ch1_Juggernaut_attack_path_1B:
    show expression "images/backgrounds/ch1/bg_ch1_danger_punches2.webp" as punches onlayer master zorder 13:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment
        
    show expression "images/effects/pow.webp" as pow onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.75 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    "With each thunderous clash, new bits of the ceiling fall to the ground. . ."
    "You realize more of the ceiling might fall and hit [Rogue.name]."

    show expression "images/backgrounds/ch1/bg_ch1_danger_punches1.webp" as punches onlayer master zorder 13:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/effects/pow.webp" as pow onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.75 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    "If you can just nullify this guy's powers, the fight will be over."
    "Then you can get [Rogue.name] out of here."

    show expression "images/backgrounds/ch1/bg_ch1_danger_punches2.webp" as punches onlayer master zorder 13:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/effects/pow.webp" as pow onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.75 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    "[Piotr.name] is more agile, but obviously not as strong."
    "It's clear [Cain.name] is just toying with him."
    "You slowly sneak around until you're directly behind [Cain.name]."
    "[Piotr.name] notices, and you briefly lock eyes with him."

    show expression "images/backgrounds/ch1/bg_ch1_danger_punches1.webp" as punches onlayer master zorder 13:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/effects/pow.webp" as pow onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.75 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    "He knows what you're about to do and provides a distraction."
    ch_Piotr "Ha! My babushka hits harder than that."
    ch_Cain "Commie motherfucker. . ."

    show expression "images/backgrounds/ch1/bg_ch1_danger_punches2.webp" as punches onlayer master zorder 13:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/effects/pow.webp" as pow onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.75 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    "You start running, full tilt, at [Cain.name]'s back."

    # call change_Outfit(Laura, Laura.Wardrobe.Outfits["Hero (Chapter I)"], instant = True) from _call_change_Outfit_30

    call show_Character(Laura, x = stage_far_far_right, sprite_layer = 16, color_transform = red_lights, fade = False) from _call_show_Character_4

    $ Laura.change_face("furious")

    ch_Laura "[Player.first_name], where are you goi. . ."

    $ Laura.change_face("appalled3")

    pause 1.0

    $ Laura.change_face("appalled3", eyes = "right")

    "She notices [Rogue.name]."

    # $ Laura.left_arm = 2

    pause 0.2

    $ Laura.left_claws = True
    $ Laura.right_claws = True
    $ Laura.unsheathing_claws = True

    show expression "images/effects/snikt.webp" as snikt onlayer effects:
        anchor (0.5, 0.5) pos (0.9, 0.1)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.5 alpha 1.0
        ease 2.0 alpha 0.0

    $ renpy.pause(0.1, hard = True)

    $ Laura.unsheathing_claws = False

    ch_Laura "What the. . ."

    $ Laura.change_face("worried4")

    "[Cain.name] barely notices as you slam into him."

    $ Laura.change_face("appalled1")

    "It's like running into a brick wall, but you hope that by nullifying his power. . ."
    ". . . nothing happens."
    "He casually throws you off, like waving away an annoying bug."

    $ fade_to_black(0.4)

    "You go flying into the nearest wall." with small_screenshake

    show expression "images/effects/bone_crack.webp" as bone_crack onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    pause 1.0

    camera:
        block:
            ease 1.5 blur 15
            ease 1.5 blur 0
            repeat

    $ fade_in_from_black(0.4)

    $ Laura.change_face("worried4")

    show expression "images/backgrounds/ch1/bg_ch1_danger_punches1.webp" as punches onlayer master zorder 13:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/effects/pow.webp" as pow onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.75 alpha 1.0
        ease 1.0 alpha 0.0

    with big_screenshake

    "[Piotr.name] manages to get a hit in thanks to you, but to very little effect."

    $ Laura.left_claws = False
    $ Laura.right_claws = False
    $ Laura.sheathing_claws = True

    show expression "images/effects/snakt.webp" as snakt onlayer effects:
        anchor (0.5, 0.5) pos (0.9, 0.1)

        zoom 0.5
        alpha 0.0
        ease 0.01 alpha 1.0
        ease 0.5 zoom 0.0 alpha 0.0

    $ renpy.pause(0.51, hard = True)

    $ Laura.sheathing_claws = False

    pause 0.5
    
    $ Laura.change_face("worried2")
    $ Laura.change_arms("neutral")

    "You're too busy laying on the floor with a splitting headache, vision swimming, gasping for air."
    "Feels like you broke a rib or two when you hit the wall. . ."
    ". . . and like someone hit your head with a baseball bat."
    "Almost blacking out from the pain, you look over and see [Laura.name]."

    $ Laura.change_face("worried1")

    "For the first time, she actually looks worried instead of angry."

    ch_Player "Fuuuuuck. . . I'd give anything to have a healing factor like [Laura.name] right about now. . ."

    with small_screenshake

    camera

    $ Player.power = 50

    "The pain from your ribs suddenly envelops your entire body for a split second."
    "Then comes the nausea."
    "Your comment only makes you feel even more like shit."
    "Still, you grit your teeth and slowly crawl over to [Rogue.name]."
    "[Laura.name] is about to come help. . ."

    $ Player.power = 0

    call hide_Character(Laura) from _call_hide_Character_31

    show expression "images/backgrounds/ch1/bg_ch1_danger_punches2.webp" as punches onlayer master zorder 13:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/effects/pow.webp" as pow onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.75 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    ch_Cain "Oh come on Ivan, it's useless." 
    ch_Cain "Ain't nobody can stop me when I get goin'."
    ch_Cain "Ah fuck it."

    hide punches onlayer master

    show expression "images/backgrounds/ch1/bg_ch1_danger_headbutt.webp" as Juggernaut onlayer master zorder 13:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/backgrounds/ch1/bg_ch1_danger_wall_damage.webp" as wall_damage onlayer master zorder 11:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/backgrounds/ch1/bg_ch1_danger_Piotr.webp" as Piotr onlayer master zorder 11:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/effects/clang.webp" as clang onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    with big_screenshake

    "You look over to see [Cain.name] headbutt [Piotr.name] hard enough to send him flying across the room. . ."

    show expression "images/effects/crash.webp" as crash onlayer effects:
        anchor (0.5, 0.5) pos (0.2, 0.7)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    hide Piotr onlayer master

    with faster_dissolve

    ". . . and through the goddamn wall."

    show expression "images/backgrounds/ch1/bg_ch1_danger_Juggernaut_Null.webp" as Juggernaut onlayer master zorder 14:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    with dissolve

    "Then, [Cain.name] turns in your direction."
    ch_Cain "Heh that was pretty fuckin' dumb, shithead."
    ch_Cain "Brave, but dumb."
    "He starts moving towards you."

    show expression "images/backgrounds/ch1/bg_ch1_danger_Juggernaut_Laura.webp" as Juggernaut onlayer master zorder 14:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    with dissolve

    ch_Cain "Maybe you can give me some answers. . ."
    ch_Laura "{i}Grrrrrr{/i}. . ."

    show expression "images/backgrounds/ch1/bg_ch1_danger_Laura_hand.webp" as Laura onlayer master zorder 16:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    pause 0.5

    show expression "images/backgrounds/ch1/bg_ch1_danger_Laura_claws.webp" as claws onlayer master zorder 17:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/effects/snikt.webp" as snikt onlayer effects:
        anchor (0.5, 0.5) pos (0.6, 0.65)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.5 alpha 1.0
        ease 2.0 alpha 0.0

    pause 2.0

    hide Laura onlayer master
    hide claws onlayer master

    show expression "images/backgrounds/ch1/bg_ch1_danger_Laura.webp" as Laura onlayer master zorder 16:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    with dissolve

    "Before he can get any closer, [Laura.name] leaps to get in between you and [Cain.name]."

    show expression "images/backgrounds/ch1/bg_ch1_danger_hole_Ororo.webp" as hole onlayer master zorder 8:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    with dissolve

    pause 1.0

    show expression "images/backgrounds/ch1/bg_ch1_danger_hole_Ororo_lightning.webp" as hole onlayer master zorder 8:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    with fastest_dissolve

    show expression "images/backgrounds/ch1/bg_ch1_danger_hole_Ororo.webp" as hole onlayer master zorder 8:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    with fastest_dissolve

    show expression "images/effects/kaboom.webp" as kaboom onlayer effects:
        anchor (0.5, 0.5) pos (0.32, 0.3)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.75 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    "A sudden clap of thunder draws everyone's attention to the hole in the ceiling."

    show expression "images/backgrounds/ch1/bg_ch1_danger_Juggernaut_Ororo.webp" as Juggernaut onlayer master zorder 14:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    with dissolve

    ch_Cain "What the fuck now. . ."

    pause 1.0

    show expression "images/backgrounds/ch1/bg_ch1_danger_Ororo.webp" as Ororo onlayer master zorder 9:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    show expression "images/backgrounds/ch1/bg_ch1_danger_hole_Ororo_lightning.webp" as hole onlayer master zorder 8:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    with fastest_dissolve

    show expression "images/backgrounds/ch1/bg_ch1_danger_hole_Ororo.webp" as hole onlayer master zorder 8:
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    with fastest_dissolve

    show expression "images/effects/kaboom.webp" as kaboom onlayer effects:
        anchor (0.5, 0.5) pos (0.32, 0.3)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.75 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    "A furious [Ororo.name] descends from the sky."
    "You use the distraction to crawl the last few feet to [Rogue.name] and grab onto her."
    ch_Player "[Laura.name], drag us!"
    "Yelling like that just makes your head hurt like hell. . . and feel like you're about to throw up."
    "The wind starts picking up."
    ch_Cain "FUCK OFF!"

    hide Laura onlayer master

    "[Laura.name] begins to drag you and [Rogue.name] out of the room."

    return