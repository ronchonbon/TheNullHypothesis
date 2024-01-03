define ch_protest_leader = Character("Protest Leader")
define ch_protester = Character("Protester")
define ch_unknown = Character("???")

init python:

    def ch1_season_three_main_Quest():
        name = "Chapter I: Spring"

        string = "ch1_season_three_main_Quest"

        Quest_type = "main"

        chapter = 1

        description = "Explore your new home and get to know its students"

        objectives = {
            "Increase your level": ["Player.level", 4],

            "Complete [Rogue.name]'s Spring Quest": ["QuestPool.Quests['Rogue_ch1_season_three_Quest'].completed", None],
            "Complete [Laura.name]'s Spring Quest": ["QuestPool.Quests['Laura_ch1_season_three_Quest'].completed", None],
            "Complete [Jean.name]'s Spring Quest": ["QuestPool.Quests['Jean_ch1_season_three_Quest'].completed", None],

            "Gain Trust across all characters": ["Rogue.trust + Laura.trust + Jean.trust", 750]}

        optional_objectives = {}

        rewards = {
            "unlock": ["love", "trust", "actions", "shop"]}
            
        criteria = [
            "chapter == 1 and season == 3"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)

init python:

    def ch1_season_three_complete():
        label = "ch1_season_three_complete"

        conditions = [
            "QuestPool.Quests['ch1_season_three_main_Quest'].completed"]

        automatic = True

        return EventClass(label, conditions, automatic = automatic)

label ch1_season_three_complete:
    "You have met all requirements to progress the main story. Check your journal for more information."

    $ season_completed = True

    return

init python:

    def ch1_season_three_progress():
        label = "ch1_season_three_progress"

        conditions = [
            "EventScheduler.Events['ch1_season_three_complete'].completed",
            "time_index == 2",
            "not EventScheduler.Events['ch1_mutant_hate'].completed"]

        waiting = True
        traveling = True

        priority = 99

        return EventClass(label, conditions, waiting = waiting, traveling = traveling, priority = priority)

label ch1_season_three_progress:
    $ ongoing_Event = True

    call receive_text(Kurt, "Hallo :D") from _call_receive_text_673
    call receive_text(Kurt, "Ever been to zee comic book store in town???") from _call_receive_text_674
    call open_texts(Kurt) from _call_open_texts_18

    pause

    call send_text(Kurt, "there's a comic book store?") from _call_send_text_65
    call send_text(Kurt, "and a town?!?!") from _call_send_text_66
    call receive_text(Kurt, "Ja") from _call_receive_text_675
    call receive_text(Kurt, "New issue of X-Men comic releases zis week") from _call_receive_text_676
    call send_text(Kurt, "X-Men comic?") from _call_send_text_67
    call receive_text(Kurt, "Ja") from _call_receive_text_677
    call receive_text(Kurt, "Guy named Stan owns zee store") from _call_receive_text_678
    call receive_text(Kurt, "He hears stories about the X-Men and writes comics on zem") from _call_receive_text_679
    call send_text(Kurt, "okay, wait") from _call_send_text_68
    call send_text(Kurt, "first things first") from _call_send_text_69
    call send_text(Kurt, "why do you always write 'zee' instead of 'the' over text?") from _call_send_text_70
    call receive_text(Kurt, "So people hear my accent in their heads. . .") from _call_receive_text_680
    call receive_text(Kurt, "Just go along with it dude.") from _call_receive_text_681
    call send_text(Kurt, "lol okay") from _call_send_text_71
    call receive_text(Kurt, "Anyway, wanna come with me and grab a copy of zee new issue?") from _call_receive_text_682

    $ choice_disabled = False

    menu:
        "Progress the main story":
            call send_text(Kurt, "I'm down, wanna head into town right now?") from _call_send_text_72
            call receive_text(Kurt, "Ja") from _call_receive_text_683
            call receive_text(Kurt, "I'll meet you in the hallway") from _call_receive_text_684

            $ EventScheduler.Events["ch1_mutant_hate"].start()
        "Postpone story progress":
            call send_text(Kurt, "yeah! I'll let you know when I'm free") from _call_send_text_73

            if "Hey, about that comic book store in town." not in Kurt.chat_options:
                $ Kurt.chat_options.insert(0, "Hey, about that comic book store in town.")
                $ Kurt.text_options.insert(0, "hey, about that comic book store in town")

            $ choice_disabled = True

    $ phone_interactable = True

    $ ongoing_Event = False

    return

init python:

    def ch1_mutant_hate():
        label = "ch1_mutant_hate"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label ch1_mutant_hate:
    $ phone_interactable = False

    if weather == "rain":
        $ weather = None
        
    if time_index != 2:
        if Kurt.text_history[-1][1] == "hey, about that comic book store in town":
            call receive_text(Kurt, "Vee should go in zee afternoon") from _call_receive_text_685
        else:
            $ Kurt.change_face("confused1")

            ch_Kurt "Better to go in zee afternoon, I sink."

        $ EventScheduler.Events["ch1_mutant_hate"].completed = False
        $ EventScheduler.Events["ch1_mutant_hate"].completed_when = 1e8

        $ EventScheduler.Events["ch1_mutant_hate"].counter = 0

        $ phone_interactable = True
        
        return

    call remove_Characters(Party) from _call_remove_Characters_224

    $ ongoing_Event = True

    if Kurt.text_history[-1][1] == "I'll meet you in the hallway":
        pass
    elif Kurt.text_history[-1][1] == "hey, about that comic book store in town":
        call send_text(Kurt, "I'm ready to go, wanna head into town right now?") from _call_send_text_74
        call receive_text(Kurt, "Ja") from _call_receive_text_686
        call receive_text(Kurt, "I'll meet you in the hallway") from _call_receive_text_687
    else:
        ch_Player "I'm ready to go, wanna head into town right now?"

        $ Kurt.change_face("happy")

        ch_Kurt "Ja, I have a couple sings to do, then I'll meet you in the hallway."

        call send_Characters(Kurt, "hold") from _call_send_Characters_218

    pause 2.0

    hide screen phone_screen
        
    "After checking the weather, you put on a hoodie before leaving."
    "It's a bit chilly out."

    play music "sounds/music/Disconnect.ogg" fadeout 1.0

    call remove_Characters(location = "bg_hallway") from _call_remove_Characters_225
    call set_the_scene(location = "bg_hallway") from _call_set_the_scene_279

    if Laura.History.check("quirk_encouraged") >= Laura.History.check("quirk_discouraged"):
        call receive_text(Laura, "Where are you going?") from _call_receive_text_688
        call open_texts(Laura) from _call_open_texts_19
        call send_text(Laura, "into town") from _call_send_text_75
        call receive_text(Laura, "Why?") from _call_receive_text_689
        call send_text(Laura, "I'm going to check out a comic book store") from _call_send_text_76
        call send_text(Laura, "[Kurt.name] asked me to go with him") from _call_send_text_77
        call receive_text(Laura, "Fine") from _call_receive_text_690
        call receive_text(Laura, "You're allowed") from _call_receive_text_691
        call send_text(Laura, "I'm 'allowed'") from _call_send_text_78

        ". . ."
        "She doesn't respond."

        pause 2.0

        hide screen phone_screen

    $ reset_behavior(Kurt)

    $ Kurt.outfit = "casual"

    call Kurt_teleports_in from _call_Kurt_teleports_in_6

    $ Kurt.change_face("happy")

    ch_Player "Ya'know, I'm starting to get used to that." 

    $ Kurt.change_face("sad")

    ch_Kurt "I am becoming too predictable?"

    $ Kurt.change_face("stunned")

    ch_Player "Heh, just a bit."
    ch_Kurt "{size=-5}Scheiße. . .{/size}"

    $ Kurt.change_face("neutral")

    ch_Kurt "Just follow me, Bruder."
    "[Kurt.name] leads the way."

    call hide_Character(Kurt) from _call_hide_Character_44
    call remove_Characters(location = "bg_campus") from _call_remove_Characters_226
    call set_the_scene(location = "bg_campus") from _call_set_the_scene_280
    call add_Characters(Kurt) from _call_add_Characters_75

    ch_Player "You're not just gonna poof us into town?" 

    $ Kurt.change_face("happy")

    ch_Kurt "Where is zee fun in that?"
    ch_Kurt "It's nice to actually walk somevere for a change."

    $ Kurt.change_face("neutral")

    ch_Player "Fine by me, it's not too chilly out anyway."

    $ fade_to_black(0.4)

    call hide_Character(Kurt) from _call_hide_Character_45

    "You walk to town with [Kurt.name] and get to know each other a bit better."
    "Apparently, this Stan guy gives him free comics in exchange for story ideas."

    show expression "images/backgrounds/base/bg_town_people.webp" as townspeople onlayer master zorder 4:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

    show top_bar onlayer master zorder 4:
        transform_anchor True

        align (0.5, 0.5)

    call set_the_scene(location = "bg_town") from _call_set_the_scene_281
    call show_Character(Kurt, x = stage_center - 0.1, sprite_layer = 5, fade = True) from _call_show_Character_10

    "As you walk into the town proper, you see [Kurt.name] put his hood up."

    $ Kurt.outfit = "casual_hood"
    $ Kurt.give_trait("tail_hidden")

    ch_Player "C'mon man, it's not that cold out."

    $ Kurt.change_face("sad")

    if Player.check_traits("visible_mutation"):
        ch_Kurt "Put yours up too, mein Bruder."
        ch_Kurt "Zee harassment has only been getting worse lately. . ."

        $ Kurt.change_face("neutral")

        "You know he's right and put your hood up as well."
    else:
        ch_Kurt "I'm not cold."
        ch_Kurt "Zee harassment has only been getting worse lately. . ." 

        $ Kurt.change_face("neutral")

        ch_Player "It's gotten that bad?"
        ch_Kurt "Much worse. . ."

    "You both continue on, [Kurt.name] leading the way since he's been to the comic book store before."

    play music "sounds/music/Rain.ogg" fadeout 1.0

    show expression "images/backgrounds/ch1/bg_ch1_town_mob1.webp" as mob onlayer master zorder 4:
        subpixel True
        transform_anchor True

        anchor (0.496, 0.810) pos (0.496, 0.810)
        zoom 0.5*cinematic_adjustment

        ease 30.0 zoom 0.8*cinematic_adjustment

    "Walking down the main road, you start hearing shouts off in the distance."

    ch_Player "Can you hear that?"

    $ Kurt.change_face("confused1")

    ch_Kurt "Nein."
    ch_Kurt "Your hearing has gotten quite good. . ."
    ch_Player "It sounds like a bunch of people shouting."
    "The shouting only gets louder, and eventually you see a large gathering down the road. . ."
    
    show expression "images/backgrounds/ch1/bg_ch1_town_mob1.webp" as mob onlayer master zorder 4:
        subpixel True
        transform_anchor True

        anchor (0.496, 0.810) pos (0.496, 0.810)
        zoom 0.8*cinematic_adjustment

        ease 20.0 zoom cinematic_adjustment
    
    "They're moving towards you."
    "There is one man walking in front of them all, preaching anti-mutant gospel to the zealous horde."
    ch_protest_leader "Mutants are a cancer to our society!"
    ch_protest_leader "They are an affront to god! Malformations, created by the devil himself to spit in the face of all that is holy!"

    $ Kurt.change_face("angry1")

    "[Kurt.name] becomes visibly upset by these remarks, and you see him shake as he tries to reel in his emotions."

    $ Kurt.change_face("sad")

    menu:
        extend ""
        "I'm not happy either. We have to be better than people like this. (determined)": 
            $ Kurt.change_face("neutral")

            ch_Kurt "You are right, vee must be better." 
            
            $ Kurt.change_face("happy") 
            
            ch_Kurt "Heh, zey make it quite easy to do so. . ."

            $ Player.History.update("Determined")
        "I. . . don't understand why they hate us so much. . . (reluctant)":
            ch_Player ". . . just for existing." 
            
            $ Kurt.change_face("neutral")

            ch_Kurt "Zey are just sad people, looking for a scapegoat." 
            ch_Kurt "It iz not personal."

            $ Player.History.update("Reluctant")
        "What the fuck is wrong with these people? (bitter)":
            ch_Player "If they start messing with mutants. . . they deserve the consequences." 
            
            $ Kurt.change_face("angry1")

            ch_Kurt "I am upset too, mein Bruder." 
            
            $ Kurt.change_face("neutral") 
            
            ch_Kurt "Don't take it too far. . ."

            $ Player.History.update("Bitter")

    $ Kurt.change_face("neutral")

    show expression "images/backgrounds/ch1/bg_ch1_town_mob2.webp" as mob onlayer master zorder 4:
        subpixel True
        transform_anchor True

        anchor (0.496, 0.810) pos (0.496, 0.810)
        zoom 0.8*cinematic_adjustment

        ease 20.0 zoom cinematic_adjustment

    hide townspeople onlayer master

    with dissolve

    "As they get closer, the vulgarity they're spouting only gets more vile."
    ch_protest_leader "Mutants are inhuman abominations! They do not deserve the rights granted to us by god!"
    "As the crowd draws near, you notice some of them have weapons. . ."

    $ Kurt.change_face("angry1")

    ch_Player "Maybe we should go a different way. . ."
    "[Kurt.name] doesn't seem to hear you and keeps walking, trying to ignore them."
    "The sermonic tone of the protest leader takes a sharp turn, and his true feelings of hate and revulsion against mutants becomes abundantly clear."
    "His voice becomes hushed, and the entire crowd is silent, in rapt attention."
    ch_protest_leader "Man, woman, or child. They are all equally disgusting."
    ch_protest_leader "They are less than human, yet think they are better than us because of it. God weeps due to their continued existence."
    ch_protest_leader "We must purge their kind from our world."
    "With each sentence, his zeal only deepens."
    ch_Kurt "{size=-5}Unglaublich{/size}. . . using religion as an excuse for bigotry."
    "You tense up and hope nobody overheard what [Kurt.name] just said."
    "Thankfully, the mob is too distracted by their leader's words, but, unfortunately, so is [Kurt.name]."
    "*WOOOOSH*"
    "The wind picks up."

    if Player.check_traits("visible_mutation"):
        "You hold on to your hood so it doesn't get blown off."

    $ Kurt.outfit = "casual"

    "[Kurt.name] isn't paying attention, and his hood gets blown off by the wind. . ."

    $ Kurt.change_face("sad")

    pause 1.0

    $ Kurt.change_face("surprised1")

    "He snaps out of it and quickly puts the hood back up."

    play music "sounds/music/Once and for All.ogg" fadeout 1.0

    ch_protester "HEY! LOOK, A FUCKING MUTIE!"
    ch_Kurt "{size=-5}Scheiße{/size}. . ."
    ch_protester "You think you can just watch from the fucking sidelines like you're better than us?"
    "The entire crowd turns their attention to you and [Kurt.name]."
    "They start surrounding you."

    show expression "images/backgrounds/ch1/bg_ch1_town_mob3.webp" as mob onlayer master zorder 4:
        transform_anchor True

        anchor (0.496, 0.810) pos (0.496, 0.810)
        zoom cinematic_adjustment

    with dissolve

    ch_Player "[Kurt.name]! We need to go, now."
    ch_protest_leader "The audacity."
    ch_protest_leader "Let's make an example out of them. . ." 
    "The closest ones brandish their weapons and tentatively move towards you both."

    $ Kurt.change_face("sad")

    "You can hear footsteps behind you as well."
    ch_Kurt "[Player.first_name], take my ha. . ."

    show expression "images/backgrounds/ch1/bg_ch1_town_fight2.webp" as protest_leader onlayer master zorder 4:
        transform_anchor True

        anchor (0.5, 0.5) pos (0.5, 0.5)
        zoom cinematic_adjustment

    with faster_dissolve

    ch_Player "Watch out!"

    show expression "images/effects/crack.webp" as crack onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    show expression "images/backgrounds/ch1/bg_ch1_town_fight1.webp" as protest_leader onlayer master zorder 7:
        transform_anchor True

        anchor (0.5, 0.5) pos (0.5, 0.5)
        zoom cinematic_adjustment

    show expression "images/backgrounds/ch1/bg_ch1_town_Kurt.webp" as Kurt_sprite onlayer master zorder 8:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

    with small_screenshake

    "[Kurt.name] gets interrupted mid-sentence, as someone breaks a baseball bat over his back."
    ch_Kurt "FUCK."

    show expression "images/effects/bamf.webp" as bamf onlayer effects:
        anchor (0.5, 0.5) pos (0.4, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    show expression "images/backgrounds/ch1/bg_ch1_town_purple_smoke.webp" as smoke onlayer master zorder 9:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 3.0 alpha 0.0

    $ renpy.pause(0.1, hard = True)

    hide Kurt_sprite onlayer master

    with None

    show expression "images/backgrounds/ch1/bg_ch1_town_fight2.webp" as protest_leader onlayer master zorder 7:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

    with faster_dissolve

    "He's forced to teleport away before they can do any more damage."
    "Leaving you alone. . ."
    "Surrounded."

    hide protest_leader onlayer master

    with dissolve

    if Player.check_traits("visible_mutation"):
        "Your hood doesn't do you any good this close."
        ch_protester "Hey, this guy's a fuckin' mutie too."
    else:
        ch_protester "Is this guy a mutie too?"
        ch_protester "I don't give a shit, he was hangin' out with one."

    $ fade_to_black(0.4)

    "You don't have time to respond before the first attacker is upon you."
    "Thanks to all of [Laura.name]'s training, and whatever the mutation did to your body, you're faster and stronger than ever."
    "You make quick work of disarming and incapacitating him, using all your accumulated skills."

    $ x = clamp(renpy.random.random(), 0.3, 0.7)
    $ y = clamp(renpy.random.random(), 0.3, 0.7)

    show expression "images/effects/green_smack.webp" as smack onlayer effects:
        anchor (0.5, 0.5) pos (x, y)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    $ fade_in_from_black(0.4)

    "He falls to the ground, unconscious."
    "You can hear more fighting in the distance, it's [Kurt.name] trying to make his way back to you."
    "The other attackers pause for a moment and look at each other."
    "You think they might back down for a moment, until you realize what's about to happen. . ."
    "The mob doesn't conveniently start attacking you one-by-one."
    "This isn't a video game or some choreographed movie fight scene."
    "There's one thing all the skills in the world can't make up for, and the mob clearly knows they have what they need."
    ch_protest_leader "Kill him!"

    $ fade_to_black(0.4)

    "They all attack at once, abruptly and ruthlessly."
    "*WOOOSH*"
    "Someone swings a lead pipe at your head from behind, which you manage to duck under. . ."

    $ x = clamp(renpy.random.random(), 0.3, 0.7)
    $ y = clamp(renpy.random.random(), 0.3, 0.7)

    show expression "images/effects/green_smack.webp" as smack onlayer effects:
        anchor (0.5, 0.5) pos (x, y)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    with small_screenshake

    "And put your face right into someone else's knee."
    "It doesn't really phase you, until the pipe comes down again. . ."

    $ x = clamp(renpy.random.random(), 0.3, 0.7)
    $ y = clamp(renpy.random.random(), 0.3, 0.7)

    show expression "images/effects/bone_crack.webp" as bone_crack onlayer effects:
        anchor (0.5, 0.5) pos (x, y)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    with small_screenshake

    ". . . barely missing your head, straight into your collar bone."
    "You feel the bone crack and wince from a lance of pain. . ."

    $ x = clamp(renpy.random.random(), 0.3, 0.7)
    $ y = clamp(renpy.random.random(), 0.3, 0.7)

    show expression "images/effects/pow.webp" as pow onlayer effects:
        anchor (0.5, 0.5) pos (x, y)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    with small_screenshake

    "Someone takes the opportunity to punch you in the gut."
    "You try to fight back, throwing punches and kicks. . ."
    "But for everything you give, you get twice as much back."
    "You're more resilient than normal, so you can take a beating."
    "You're not too worried. . ."

    $ fade_in_from_black(0.4)

    "*THUNK*"
    ". . . until someone embeds a knife in between your ribs."
    ch_protester "You're dead now, asshole!"
    "You've never been stabbed before, and it fucking hurts."
    "It makes you feel. . ."

    menu:
        extend ""
        "Pissed off (bitter)":
            call ch1_mutant_hate_path_1A from _call_ch1_mutant_hate_path_1A

            $ Player.History.update("ch1_mutant_hate_path_1A")
            $ Player.History.update("Bitter")
        "Scared (reluctant)":
            call ch1_mutant_hate_path_1B from _call_ch1_mutant_hate_path_1B

            $ Player.History.update("ch1_mutant_hate_path_1B")
            $ Player.History.update("Reluctant")
        "Determined (determined)":
            call ch1_mutant_hate_path_1C from _call_ch1_mutant_hate_path_1C

            $ Player.History.update("ch1_mutant_hate_path_1C")
            $ Player.History.update("Determined")

    play music "sounds/music/Uncertain Ending.ogg" fadeout 1.0

    $ Player.power = 0

    $ Kurt.remove_trait("tail_hidden")

    call Kurt_teleports_in from _call_Kurt_teleports_in_7

    $ Kurt.change_face("surprised1")

    ch_Kurt "Heilige scheiße. . ."
    ch_Kurt "Are you. . . okay?"
    "You feel exhausted, and as you look down at yourself, you feel the stab wound slowly finish closing up."
    ch_Player "Physically? Yes."

    $ Kurt.change_face("sad")

    ch_Player "Mentally? Not so much. . ."
    ch_Kurt "Bruder, we have to go."
    "[Kurt.name] tentatively walks over to you and puts a hand on your shoulder."
    ch_Player "Yeah. . . let's go."

    show expression "images/effects/bamf.webp" as bamf onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    show solid_black onlayer cinematic

    $ fade_to_black(0.4)

    pause 2.0

    ". . ."

    hide mob onlayer master
    hide solid_black onlayer cinematic

    $ infirmary_bed = False
    $ infirmary_in_bed = False

    call remove_Characters(location = "bg_infirmary") from _call_remove_Characters_227
    call set_the_scene(location = "bg_infirmary") from _call_set_the_scene_282

    play music "sounds/music/Disconnect.ogg" fadeout 1.0

    $ Kurt.outfit = "casual"

    call add_Characters(Kurt) from _call_add_Characters_76

    $ Kurt.change_face("neutral")

    ch_Kurt "Let zee doctor check you over, I'll tell Xavier vat happened."
    ch_Player "Okay, thanks man."

    call Kurt_teleports_out from _call_Kurt_teleports_out_6

    pause 1.0

    show expression "images/backgrounds/base/bg_infirmary_doctor.webp" as Cecilia onlayer master zorder 0:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

    with dissolve

    ch_Cecilia "[Player.first_name]?!"
    ch_Cecilia "What happened?! Your clothes are a mess!"
    "You explain the situation, and she does a quick physical exam to make sure you're alright."

    $ Laura.temp = Laura.name
    $ Laura.name = "???"

    ch_Laura "I know he's in there."

    $ Laura.name = Laura.temp

    ch_unknown "Wait!"

    show expression "images/effects/clang.webp" as clang onlayer effects:
        anchor (0.5, 0.5) pos (0.65, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    "[Laura.name] forces the door open and manages to break the door handle off."

    call send_Characters(Laura, "bg_infirmary", behavior = False) from _call_send_Characters_219

    $ Laura.change_face("angry1")

    ch_Cecilia "I'll give you two some privacy. . ."

    hide Cecilia onlayer master

    ch_Laura "I knew it, I could smell you."
    ch_Player "H-"

    $ Laura.change_face("furious", blush = 1)

    ch_Laura "Shirt off, now."
    ch_Player "Wait what?!"

    $ Laura.change_face("suspicious1", blush = 1)

    ch_Laura "I smell blood."
    ch_Laura "You are injured." 

    $ Laura.change_face("suspicious2", blush = 1)

    ch_Laura "Shirt. Off."

    menu:
        extend ""
        "Fine. . . (encourage_quirk)":
            ch_Player "But the doctor said I was okay. . ." 
            
            $ Laura.change_face("angry1", blush = 1)

            ch_Laura "I will make sure of that myself."

            call change_Character_stat(Laura, "love", small_stat) from _call_change_Character_stat_574

            "You do as she says and take your shirt off."

            $ Laura.change_face("angry1", eyes = "down", blush = 1)

            "She closely inspects your body to look for injuries."
            "So she says. . ."

            ch_Laura "Right here." 
            "She touches the exact spot where you got stabbed."

            $ Laura.change_face("angry1", eyes = "squint", blush = 1)

            ch_Laura "I know you were injured, your power must've healed it."

            $ Laura.change_face("furious", blush = 1)

            ch_Laura "You are going to explain exactly what happened."

            $ Laura.History.update("quirk_encouraged")
        "[Laura.name], that's a bit too far. (discourage_quirk)":
            call change_Character_stat(Laura, "love", -small_stat) from _call_change_Character_stat_575
            call change_Character_stat(Laura, "trust", small_stat) from _call_change_Character_stat_576

            ch_Player "The doctor said I was okay." 
            
            $ Laura.change_face("angry1")

            ch_Laura "Fine." 
            ch_Laura "But you are going to explain exactly what happened."

            $ Laura.History.update("quirk_discouraged")

    $ Laura.change_face("confused1")

    "You tell her what happened, how you got stabbed, and how things ended up."

    $ Laura.change_face("appalled1")

    ch_Laura "Good, they got what they fucking deserved for hurting you. . ."

    $ Laura.change_face("angry1")

    menu:
        extend ""
        "I did what I had to do, I just wish they hadn't force my hand like that. . . (determined)":
            call change_Character_stat(Laura, "love", medium_stat) from _call_change_Character_stat_577
            call change_Character_stat(Laura, "trust", large_stat) from _call_change_Character_stat_578

            ch_Laura "Don't feel pity for degenerates like that." 
            
            $ Laura.change_face("neutral", eyes = "right") 
            
            ch_Laura "Your empathy is. . . admirable. . . but it doesn't make what you did, wrong."

            $ Player.History.update("Determined")
        "I was scared shitless. . . would probably be dead without your training. . . (reluctant)":
            call change_Character_stat(Laura, "love", small_stat) from _call_change_Character_stat_579
            call change_Character_stat(Laura, "trust", small_stat) from _call_change_Character_stat_581

            ch_Laura "This is exactly why you need more training."
            
            $ Laura.change_face("suspicious2") 
            
            ch_Laura "You tie your emotions too strongly to it." 
            ch_Laura "Were you expecting pity?"

            $ Player.History.update("Reluctant")
        "You're right, they tried to fucking kill me afterall. (bitter)":
            call change_Character_stat(Laura, "love", large_stat) from _call_change_Character_stat_582
            call change_Character_stat(Laura, "trust", small_stat) from _call_change_Character_stat_583

            ch_Player "But. . . I still feel like shit about it."
            ch_Laura "Because you are a better person than them." 
            
            $ Laura.change_face("neutral", eyes = "right") 
            
            ch_Laura "That doesn't make it wrong, what you had to do."

            $ Player.History.update("told_Laura_protesters_got_what_they_deserved_during_mutant_hate")
            $ Player.History.update("Bitter")

    $ Laura.change_face("angry1")

    ch_Laura "Either way, expect your training to become even more difficult."

    $ Laura.change_face("confused1")

    ch_Player "Is that even possible. . ."
    ch_Laura "Of course it's possible."

    $ Laura.change_face("neutral")

    if Laura.History.check("quirk_encouraged") >= Laura.History.check("quirk_discouraged"):
        ch_Laura "From now on, you're letting me know before you leave campus."

        $ Laura.change_face("furious")

        ch_Player "Wai. . ."
        ch_Laura "{i}You{/i} are my number one priority. I will not let you get hurt again." 

        $ Laura.change_face("furious", eyes = "right", blush = 1)

        ch_Player "I. . . wait, 'number one priority'?" 

        $ Laura.change_face("worried1", eyes = "right", blush = 1)

        ch_Player "No that should'n. . ."
    else:
        $ Laura.change_face("furious")

        ch_Laura "And, you {i}will{/i} stop getting hurt." 

        $ Laura.change_face("suspicious2")

        ch_Player "It's not like I do it on purpose. . ."

        $ Laura.change_face("worried1", eyes = "right", blush = 1)

        ch_Laura "I don't care. Stop it. . . it makes me. . ."

    call remove_Characters(Laura) from _call_remove_Characters_228

    "Without elaborating, she leaves."
    ch_Player "Fuck. . ."
    "You feel a presence in your mind and hear [Charles.name]'s voice."

    $ Charles.give_trait("telepathic")

    ch_Charles "[Player.first_name], please meet me in my study."
    ch_Charles "Kurt told me what happened."
    ch_Player "I'll be right there."

    $ Charles.remove_trait("telepathic")
    
    "The presence disappears."
    "You leave the infirmary and head to [Charles.name]'s study."

    $ fade_to_black(0.4)

    "You only get so far, before. . ."

    call remove_Characters(location = "bg_campus") from _call_remove_Characters_229
    call set_the_scene(location = "bg_campus") from _call_set_the_scene_283
    call send_Characters(Jean, "bg_campus", behavior = False) from _call_send_Characters_220

    $ Jean.change_face("worried3")

    $ temp = Jean.Player_petname.capitalize()

    ch_Jean "[temp]!"

    if Jean.History.check("quirk_encouraged") >= Jean.History.check("quirk_discouraged"):
        $ Jean.change_face("worried1")

        ch_Jean "Come here."

        $ Jean.change_face("worried1", eyes = "closed", blush = 1)
        $ Jean.change_arms("crossed")

        "She wraps her arms around you in a tight hug."
        ch_Jean "Word's been spreading about what happened."
        ch_Jean "I know it must've been scary, but don't worry, I'm here now."

        menu:
            extend ""
            "Lean into her for comfort":
                call change_Character_stat(Jean, "love", large_stat) from _call_change_Character_stat_584
                
                "You squeeze her back, tightly, realizing she's right."
                "Regardless of how you reacted at the time, you were terrified deep down."
                "An angry mob of normal people just tried to murder you."

                $ Jean.change_face("sad")

                "She finally lets go."
            "You're okay":
                "You squeeze her back, before letting go."
                
        $ Jean.change_arms("neutral")
    else:
        $ Jean.change_face("worried1")

        ch_Jean "Come here."

        $ Jean.change_face("worried1", eyes = "closed", blush = 1)
        $ Jean.change_arms("crossed")

        "She hugs you tightly for a moment before letting go."

        $ Jean.change_face("worried1")
        $ Jean.change_arms("neutral")

        ch_Jean "You're okay, right?"
        ch_Player "Physically I am. . ."
        ch_Jean "I can't imagine what it must've been like, probably terrifying. I'm so sorry."
        "You realize, regardless of your reaction at the time, you were terrified deep down."
        "An angry mob of normal people just tried to murder you."

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Player "Thanks, [Jean.petname]. I needed that." 

    $ Jean.change_face("smirk2")

    if Jean.History.check("quirk_encouraged") >= Jean.History.check("quirk_discouraged"):
        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 
        
        ch_Jean "My little bro' gets hugs whenever he wants."
    else:
        $ Jean.change_face("worried1", mouth = "smirk") 
        
        ch_Jean "Just ask if you want another one. . ." 

    menu:
        extend ""
        "I just don't get it, they were willing to go so far. . . (determined)":
            call change_Character_stat(Jean, "love", medium_stat) from _call_change_Character_stat_585

            $ Jean.change_face("worried1")

            ch_Jean "Not everybody is good, like we are. . ." 
            
            $ Jean.change_face("sad") 
            
            ch_Jean "Some people will find any excuse for violence."

            $ Player.History.update("Determined")
        "I really was terrified. . . they didn't even hesitate to try and kill me. . . (reluctant)":
            call change_Character_stat(Jean, "love", medium_stat) from _call_change_Character_stat_586

            $ Jean.change_face("worried1")

            ch_Jean "Some people just like to find any excuse for violence. . ." 
            
            $ Jean.change_face("worried1", mouth = "smirk")
            
            ch_Jean "But don't worry, I'm always here to help."

            $ Player.History.update("told_Jean_was_scared_during_mutant_hate")
            $ Player.History.update("Reluctant")
        "In retrospect, I'm more pissed off than scared. (bitter)":
            call change_Character_stat(Jean, "love", small_stat) from _call_change_Character_stat_587

            $ Jean.change_face("worried1")

            ch_Jean "I know it's frustrating, but you can't let them make you angry." 
            ch_Jean "That's exactly what they want."

            $ Player.History.update("told_Jean_angry_at_protesters_during_mutant_hate")
            $ Player.History.update("Bitter")

    $ Jean.change_face("worried1")

    ch_Jean "I know it's hard, but you have to try to understand where they're coming from." 
    ch_Jean "Not all mutants are good." 

    $ Jean.change_face("confused1", mouth = "smirk")

    ch_Jean "You can imagine the ego some people get when they realize they're special." 
    ch_Player "I know, you're right. . ."

    call send_Characters(Rogue, "bg_campus", behavior = False) from _call_send_Characters_221

    $ Jean.change_face("confused1", eyes = "left")

    $ Rogue.change_face("worried3")

    $ temp = Rogue.Player_petname.capitalize()

    ch_Rogue "[temp]! Thank goodness you're alright."
    ch_Jean "Oh, hey Rogue."
    "[Jean.name] moves closer to you, putting a hand on your shoulder."

    $ Jean.change_face("confused1", mouth = "smirk")
    $ Rogue.change_face("worried1", eyes = "right")

    ch_Jean "You better come find me later, we're going to have a lot to work on so you stop getting yourself hurt." 

    $ Rogue.change_face("worried2")

    ch_Jean "Got it?"
    ch_Player "Got it. . ." 

    $ Jean.change_face("sly")

    ch_Jean "Good, now. . ."

    $ Jean.change_face("sly", eyes = "left")
    $ Rogue.change_face("worried1", eyes = "right")

    ch_Jean "I'll leave you two to catch up."

    if Rogue in Partners and Jean in Partners and Jean in Rogue.knows_about and Rogue in Jean.knows_about:
        "[Jean.name] gives [Rogue.name] a pointed look. . ."

        $ Jean.change_face("kiss2", blush = 1)

        $ Rogue.change_face("worried2", mouth = "lipbite")

        ". . . before forcefully pulling you into a kiss."

        $ Rogue.change_face("worried2", eyes = "down", mouth = "lipbite", blush = 1)

        "She holds you there for a long moment before letting go."

        $ Jean.History.update("kiss")

        $ Jean.change_face("sexy", eyes = "left", blush = 1)
        $ Rogue.change_face("worried1", mouth = "lipbite")

        ch_Jean "Mmm."

        $ Jean.change_face("sexy", blush = 1)

        ch_Jean "See you later, [Jean.Player_petname]." 

        $ Rogue.change_face("worried1", mouth = "smirk")
    else:
        "[Jean.name] gives [Rogue.name] a pointed look. . ."

        $ Jean.change_face("smirk2", eyes = "closed", blush = 1)
        $ Rogue.change_face("worried2", mouth = "lipbite")

        ". . . before forcefully pulling you into another hug."

        $ Jean.change_face("kiss2", blush = 1)
        $ Rogue.change_face("worried2", eyes = "down", mouth = "lipbite", blush = 1)

        "She holds you there for a long moment before giving you a kiss on the cheek and letting go."

        $ Rogue.change_face("worried1", mouth = "lipbite")
        $ Jean.change_face("neutral", eyes = "left", blush = 1)

        pause 1.0

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "You're a good hugger."
        ch_Jean "See you later, [Jean.Player_petname]."

        $ Rogue.change_face("worried1", mouth = "smirk")

    call remove_Characters(Jean) from _call_remove_Characters_230

    ch_Player "{i}Ahem{/i}. . . Hey, [Rogue.petname]."
    ch_Rogue "Hey. . . [Rogue.Player_petname]."

    $ Rogue.change_face("worried1")

    ch_Rogue "Ah came as soon as ah heard what happened." 

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Seems like ah was a bit slow. . ."
    ch_Player "Don't worry about it, I'm just glad you're here now." 

    $ Rogue.change_face("confused1", mouth = "smirk")

    ch_Rogue "Ah only heard bits about what happened, but yer alright?" 

    $ Rogue.change_face("worried1")

    ch_Player "Yeah. . . for the most part."
    "You explain what happened. . ."

    menu:
        extend ""
        "I did what I had to do. . . but I don't feel good about it. (determined)":
            call change_Character_stat(Rogue, "trust", large_stat) from _call_change_Character_stat_487

            $ Rogue.change_face("worried1", eyes = "right")

            $ Player.History.update("told_Rogue_did_what_had_to_do_during_mutant_hate")
            $ Player.History.update("Determined")
        "To be honest, it was scarier than when those Sentinels attacked. . . (reluctant)":
            call change_Character_stat(Rogue, "trust", large_stat) from _call_change_Character_stat_488
            
            $ Rogue.change_face("worried1")

            $ Player.History.update("told_Rogue_was_scared_during_mutant_hate")
            $ Player.History.update("Reluctant")
        "They had it coming. Imagine if I didn't have my power. . . (bitter)":
            call change_Character_stat(Rogue, "trust", -small_stat) from _call_change_Character_stat_489

            $ Rogue.change_face("appalled1", eyes = "right")

            $ Player.History.update("told_Rogue_protesters_had_it_coming_during_mutant_hate")
            $ Player.History.update("Bitter")

    $ Rogue.change_face("furious", eyes = "right")

    "You're surprised to see [Rogue.name] get angry."
    ch_Rogue "Those bastards."

    $ Rogue.change_face("confused1")

    ch_Rogue ". . ."
    ch_Rogue "Why are ya lookin' at me like that?"
    ch_Player "Sorry, just didn't expect that kind of reaction. . ."

    $ Rogue.change_face("angry1")

    ch_Rogue "Well. . . ah can't help it when they try to hurt {i}you{/i} like that. . ."

    if Rogue.History.check("quirk_encouraged") >= Rogue.History.check("quirk_discouraged"):
        $ Rogue.change_face("worried1")

        ch_Rogue "Can ah. . . come with ya from now on?" 

        $ Rogue.change_face("worried2")

        ch_Rogue "Please? Ah want to be there with you for once." 
        ch_Player "I don't plan on getting into a situation like that again."

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Player "But yeah, I want you by my side next time."
    else:
        $ Rogue.change_face("neutral")

        ch_Rogue "Hon', ah know [Kurt.name] was with ya. . ."

        $ Rogue.change_face("worried1")

        ch_Rogue "You shouldn't be goin' around without more than a couple people backin' ya up."
        ch_Rogue "Ah should probably be with ya from now on. . ."

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Player "You're right, I'd feel better with you around." 

    $ Rogue.change_face("smirk2")

    ch_Rogue "Thanks. . ."
    ch_Player "And thank you for checking up on me, I gotta go have a talk with Charles."
    ch_Rogue "Alright, ah'll see ya later. You know where to find me."

    call remove_Characters(Rogue) from _call_remove_Characters_231

    pause 1.0

    $ fade_to_black(0.4)

    "You head to [Charles.name]'s study."

    call send_Characters(Charles, location = "bg_study") from _call_send_Characters_222
    call remove_everyone_but(Charles, location = "bg_study") from _call_remove_everyone_but_6
    call set_the_scene(location = "bg_study") from _call_set_the_scene_284

    $ Charles.change_face("happy")

    ch_Charles "Hello, [Player.first_name]. I am glad to see you are well."

    $ Charles.change_face("sad")

    ch_Player "Hey Professor. I'm guessing Kurt told you what happened?" 
    ch_Charles "He did."

    $ Charles.change_face("neutral")

    ch_Charles "I trust Kurt will want to speak to you himself, he was very repentant about what happened."
    ch_Player "What, why? It's not his fault."

    $ Charles.change_face("confused1")

    ch_Charles "He does not feel that way."

    $ Charles.change_face("neutral")

    ch_Charles "But it is also because of what you were forced to do."

    if Player.History.check("ch1_mutant_hate_path_1C"):
        ch_Charles "Despite the situation, he tells me you handled things calmly and with as much restraint as was possible."
        ch_Player "I tried."
        ch_Player "But. . . maybe I still went too far. . . I couldn't help but injure them so badly."
        ch_Player "My power control wasn't good enough. . ."
        ch_Charles "That is not your fault, [Player.first_name]."
        ch_Charles "And do not worry, nobody was killed, we have made sure of that."
    elif Player.History.check("ch1_mutant_hate_path_1B"):
        ch_Player "What I was forced to do. . ."
        ch_Player "I probably killed someone!"
        ch_Player "What am I becoming?! That I can just break someone like that so easily. . ."
        ch_Charles "Rest assured, [Player.first_name], nobody was killed."

        $ Charles.change_face("happy")

        ch_Charles "And the fact you are so worried about their wellbeing means you are not becoming a monster."
    elif Player.History.check("ch1_mutant_hate_path_1A"):
        ch_Charles "He also told me what happened."

        $ Charles.change_face("stunned", eyes = "wide")

        ch_Charles "How. . . angry. . . you became."
        ch_Player "They tried to kill me!"
        ch_Player "I think that warrants a bit of anger. . ."

        $ Charles.change_face("neutral")

        ch_Charles "Maybe it does, but you {i}must not{/i} let it get out of control."
        ch_Charles "Thankfully, nobody was killed today. But, with such power. . . controlling our emotions is paramount."

    $ Charles.change_face("neutral")

    ch_Charles "Nevertheless, I am sorry you had to face the worst of humanity."

    if Player.History.check("Determined", tracker = "event") >= 5 or Player.History.check("Reluctant", tracker = "event") >= 5 or Player.History.check("Bitter", tracker = "event") >= 5:
        ch_Charles "You seem to have your wits about you, all things considered."
        ch_Player "You think so? I don't feel very calm and collected. . ."
    elif Player.History.check("Determined", tracker = "event") >= 3 or Player.History.check("Reluctant", tracker = "event") >= 3 or Player.History.check("Bitter", tracker = "event") >= 5:
        ch_Charles "I suggest you take some time to collect yourself and rest, after all that has happened."
        ch_Charles "Today was understandably stressful for you."
        ch_Player "Yeah. . . I need some time to think about all that's happened."
    else:
        ch_Charles "I know today was very. . . disconcerting for you."
        ch_Charles "Please remember you are not alone, and there are many people at this school who would be happy to help you talk things through."
        ch_Player "Thanks. . . talking to someone might be helpful."

    ch_Charles "I am afraid you can find enemies, not just in high places, but within the ranks of normal citizenry as well."
    ch_Player "It's. . . terrifying."

    $ Charles.change_face("sad")

    ch_Player "The number of enemies is only going to increase, isn't it?"
    ch_Charles "Sadly, you are probably correct."

    $ Charles.change_face("neutral")

    ch_Charles "But that is why this school exists. To help young mutants like yourself become responsible with their powers and prove that humanity and mutantkind can co-exist."
    ch_Charles "Now please, talk to Kurt. He is waiting for you in the dorms."
    ch_Player "I will, thanks Professor."

    $ fade_to_black(0.4)

    pause 2.0

    call remove_Characters(location = "bg_hallway") from _call_remove_Characters_232
    call set_the_scene(location = "bg_hallway") from _call_set_the_scene_285
    call send_Characters(Kurt, "bg_hallway") from _call_send_Characters_223

    $ Kurt.change_face("surprised1")

    ch_Kurt "[Player.first_name]!"
    ch_Player "Hey man."

    $ Kurt.change_face("confused1")

    ch_Player "Xavier told me you wanted to say sorry, but I won't let you."
    ch_Kurt "Eh?"

    $ Kurt.change_face("sad")

    ch_Player "What happened isn't your fault or mine."
    ch_Kurt "Bu. . ."

    $ Kurt.change_face("neutral")

    ch_Player "And don't tell me you feel bad for teleporting away."
    ch_Player "I heard you fighting tooth and nail trying to get back to me."
    ch_Player "It would've been really stupid to try and fight alongside me." 

    $ Kurt.change_face("confused1")

    "You put your arm out."

    $ Kurt.change_face("neutral")

    ch_Kurt "Thank you. . . mein Bruder."
    "He grabs your forearm."
    ch_Player "Any time, brother."

    $ Kurt.change_face("happy")

    ch_Player "Although. . . I think you owe me a comic book now."

    call send_Characters(Kurt, Kurt.home) from _call_send_Characters_224

    if "Hey, about that comic book store in town." in Kurt.chat_options:
        $ Kurt.chat_options.remove("Hey, about that comic book store in town.")
        $ Kurt.text_options.remove("hey, about that comic book store in town")

    $ season = 4

    $ season_day = 0

    python:
        for C in all_Characters:
            C.History.manually_reset("event")
            C.History.manually_reset("season")

    $ Player.History.manually_reset("event")
    $ Player.History.manually_reset("season")

    call refresh_season_content from _call_refresh_season_content_4

    $ Player.date_planned = {}
    $ Player.schedule = {}

    python:
        for C in all_Companions:
            C.wants_alone_time = 0
            C.schedule = {}

    pause 2.0

    $ clock = 0

    $ season_completed = False

    call move_location(Player.home) from _call_move_location_38

    $ ongoing_Event = False

    return

label ch1_mutant_hate_path_1:
    $ Player.power = 75

    $ x = clamp(renpy.random.random(), 0.3, 0.7)
    $ y = clamp(renpy.random.random(), 0.3, 0.7)

    show expression "images/effects/clang.webp" as clang onlayer effects:
        anchor (0.5, 0.5) pos (x, y)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    "This time, the pipe connects with your temple, but it rings as if it just struck steel."
    "It only stings, instead of caving your skull in. You can tell their attacks are getting weaker."

    $ x = clamp(renpy.random.random(), 0.3, 0.7)
    $ y = clamp(renpy.random.random(), 0.3, 0.7)

    show expression "images/effects/green_smack.webp" as smack onlayer effects:
        anchor (0.5, 0.5) pos (x, y)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    "A wooden bat splinters as it impacts your shoulder."

    $ x = clamp(renpy.random.random(), 0.3, 0.7)
    $ y = clamp(renpy.random.random(), 0.3, 0.7)

    show expression "images/effects/crack.webp" as crack onlayer effects:
        anchor (0.5, 0.5) pos (x, y)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    "A knife shatters as the tip fails to penetrate your skin."
    ch_protester "*huff* What the fuck. . . did this freak do to us?! *huff*"
    ch_protest_leader "Must I do it myself?"

    show expression "images/backgrounds/ch1/bg_ch1_town_fight3a.webp" as protest_leader onlayer master zorder 7:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

    with faster_dissolve

    "It's like everything is in slow motion, as your brain starts processing stimuli almost instantaneously."
    "You respond without a word."

    show expression "images/effects/crack.webp" as crack onlayer effects:
        anchor (0.5, 0.5) pos (0.4, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    show expression "images/backgrounds/ch1/bg_ch1_town_fight3b.webp" as punch onlayer master zorder 7:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

    with small_screenshake

    "You throw your arm up to block the leader's strike."
    "With minimal effort, you parry the attack."

    show expression "images/effects/pow.webp" as pow onlayer effects:
        anchor (0.5, 0.5) pos (0.6, 0.55)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    hide punch onlayer master

    show expression "images/backgrounds/ch1/bg_ch1_town_fight4a.webp" as protest_leader onlayer master zorder 7:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

    show expression "images/backgrounds/ch1/bg_ch1_town_fight4b.webp" as punch onlayer master zorder 7:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

    with fastest_dissolve

    "Your jab connects, and you feel his jaw break against your fist."

    show expression "images/backgrounds/ch1/bg_ch1_town_fight4c.webp" as teeth onlayer master zorder 7:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

    with fastest_dissolve

    "His teeth go flying."

    hide punch onlayer master
    hide teeth onlayer master

    show expression "images/backgrounds/ch1/bg_ch1_town_fight5.webp" as protest_leader onlayer master zorder 7:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

    with fastest_dissolve

    "The man is lifted off his feet, the power from such a low effort strike surprising you."

    hide protest_leader onlayer master

    with fastest_dissolve

    "Trying to capitalize on your momentary lapse in concentration, another man tries to stab you."

    show expression "images/backgrounds/ch1/bg_ch1_town_fight6a.webp" as protester onlayer master zorder 7:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

    with fastest_dissolve

    "It's easily intercepted."

    show expression "images/effects/green_smack.webp" as smack onlayer effects:
        anchor (0.5, 0.5) pos (0.4, 0.4)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    show expression "images/backgrounds/ch1/bg_ch1_town_fight6b.webp" as punch onlayer master zorder 7:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

    with small_screenshake

    "His wrist shatters as you disarm him."

    show expression "images/effects/bone_crack.webp" as bone_crack onlayer effects:
        anchor (0.5, 0.5) pos (0.3, 0.4)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    show expression "images/backgrounds/ch1/bg_ch1_town_fight7.webp" as protester onlayer master zorder 7:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

    hide punch onlayer master

    with small_screenshake

    pause 0.5

    show expression "images/backgrounds/ch1/bg_ch1_town_fight8a.webp" as protester onlayer master zorder 7:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

    show expression "images/backgrounds/ch1/bg_ch1_town_fight8b.webp" as knife onlayer master zorder 7:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

        ease 2.0 yoffset 1000

    with big_screenshake

    ch_protester "AAAAAH!"
    "He screams in pain, as you displace his broken wrist even further, the knife falling from his grasp."

    show expression "images/backgrounds/ch1/bg_ch1_town_fight9a.webp" as protester onlayer master zorder 7:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

    with fastest_dissolve

    pause 0.5

    show expression "images/effects/pow.webp" as pow onlayer effects:
        anchor (0.5, 0.5) pos (0.6, 0.55)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    show expression "images/backgrounds/ch1/bg_ch1_town_fight9b.webp" as punch onlayer master zorder 7:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

    show expression "images/backgrounds/ch1/bg_ch1_town_fight9c.webp" as spit onlayer master zorder 7:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

    with small_screenshake

    "A light punch, and you feel another jaw break under your knuckles."

    $ fade_to_black(0.4)

    hide protester onlayer master
    hide punch onlayer master
    hide spit onlayer master

    $ x = clamp(renpy.random.random(), 0.3, 0.7)
    $ y = clamp(renpy.random.random(), 0.3, 0.7)

    show expression "images/effects/green_smack.webp" as smack onlayer effects:
        anchor (0.5, 0.5) pos (x, y)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    with small_screenshake

    "You feel a sense of satisfaction as some of the attackers run. . ."

    $ x = clamp(renpy.random.random(), 0.3, 0.7)
    $ y = clamp(renpy.random.random(), 0.3, 0.7)

    show expression "images/effects/crack.webp" as crack onlayer effects:
        anchor (0.5, 0.5) pos (x, y)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    with small_screenshake

    "But many still try to overwhelm you, even now."

    $ x = clamp(renpy.random.random(), 0.3, 0.7)
    $ y = clamp(renpy.random.random(), 0.3, 0.7)

    show expression "images/effects/pow.webp" as pow onlayer effects:
        anchor (0.5, 0.5) pos (x, y)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    with big_screenshake

    "Why won't they just give up. . ."

    $ x = clamp(renpy.random.random(), 0.3, 0.7)
    $ y = clamp(renpy.random.random(), 0.3, 0.7)

    show expression "images/effects/bone_crack.webp" as bone_crack onlayer effects:
        anchor (0.5, 0.5) pos (x, y)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    with big_screenshake

    return

label ch1_mutant_hate_path_1A:
    "These pricks are trying to kill you, for no goddamn reason."
    "*SHICK*"
    "You rip the knife out and feel blood trickle down your side."
    "It's time to show them why they should be scared of mutants."
    "You still can't control your absorption power, it's either fully on or off. . ."
    "But any compunctions you had about using it, vanished when that knife tore into you."

    call ch1_mutant_hate_path_1 from _call_ch1_mutant_hate_path_1

    ". . ." with small_screenshake
    ". . . . ." with small_screenshake

    $ x = clamp(renpy.random.random(), 0.3, 0.7)
    $ y = clamp(renpy.random.random(), 0.3, 0.7)

    show expression "images/effects/green_smack.webp" as smack onlayer effects:
        anchor (0.5, 0.5) pos (x, y)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    show expression "images/backgrounds/ch1/bg_ch1_town_mob4.webp" as mob onlayer master zorder 4:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

    $ fade_in_from_black(0.4)

    "The last attacker collapses at your feet."
    ch_Player "*huff* *huff* *huff*"
    "As you look at all the people you just fought, laying battered on the ground, you can't help but feel horrified by what just happened."
    "Horrified by your own reaction. . . did you feel satisfaction from hurting people?"

    return

label ch1_mutant_hate_path_1B:
    "These people want to actually kill you!"
    "*SHICK*"
    "Pulling the knife out with shaky hands, you can feel blood trickle down your side."
    "You still can't control your absorption power, it's either fully on or off. . ."
    "But fear has overcome any reservations you had about using it."

    call ch1_mutant_hate_path_1 from _call_ch1_mutant_hate_path_1_1

    ch_Player "Please, just stop!"
    ". . ." with small_screenshake
    ". . . . ." with small_screenshake

    $ x = clamp(renpy.random.random(), 0.3, 0.7)
    $ y = clamp(renpy.random.random(), 0.3, 0.7)

    show expression "images/effects/green_smack.webp" as smack onlayer effects:
        anchor (0.5, 0.5) pos (x, y)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    show expression "images/backgrounds/ch1/bg_ch1_town_mob4.webp" as mob onlayer master zorder 4:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

    $ fade_in_from_black(0.4)

    "The last attacker collapses at your feet."
    ch_Player "*huff* *huff* *huff*"
    "As you look at all the people you just fought, laying battered on the ground, you can't help but feel horrified by what just happened."
    "Horrified, but thankful you managed to survive. . ."

    return

label ch1_mutant_hate_path_1C:
    "These people want to kill you."
    "You will {i}not{/i} let them."
    "*SHICK*"
    "Pulling the knife out with a steady hand, you ignore the blood trickling down your side - it won't matter in a moment."
    "You still can't control your absorption power, it's either fully on or off. . ."
    "But their barbarism has forced your hand."

    call ch1_mutant_hate_path_1 from _call_ch1_mutant_hate_path_1_2

    ch_Player "Have you not had enough?!"
    ". . ." with small_screenshake
    ". . . . ." with small_screenshake

    $ x = clamp(renpy.random.random(), 0.3, 0.7)
    $ y = clamp(renpy.random.random(), 0.3, 0.7)

    show expression "images/effects/green_smack.webp" as smack onlayer effects:
        anchor (0.5, 0.5) pos (x, y)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    show expression "images/backgrounds/ch1/bg_ch1_town_mob4.webp" as mob onlayer master zorder 4:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

    $ fade_in_from_black(0.4)

    "The last attacker collapses at your feet."
    ch_Player "*huff* *huff* *huff*"
    "As you look at all the people you just fought, laying battered on the ground, you can't help but feel horrified by what just happened."
    "Horrified and saddened by how far they forced you to go. . ."

    return