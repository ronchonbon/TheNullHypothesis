define ch_cashier = Character("Cashier")
define ch_mutant = Character("???")

init -1:
    
    default MallSalesperson = NPCClass("mall")

init python:

    def ch1_season_two_main_Quest():
        name = "Chapter I: Winter"

        string = "ch1_season_two_main_Quest"

        Quest_type = "main"

        chapter = 1

        description = "Explore your new home and get to know its students"

        objectives = {
            "Increase your level": ["Player.level", 3],

            "Complete [Rogue.name]'s Winter Quest": ["QuestPool.Quests['Rogue_ch1_season_two_Quest'].completed", None],
            "Complete [Laura.name]'s Winter Quest": ["QuestPool.Quests['Laura_ch1_season_two_Quest'].completed", None],
            "Complete [Jean.name]'s Winter Quest": ["QuestPool.Quests['Jean_ch1_season_two_Quest'].completed", None],

            "Gain Trust across all characters": ["Rogue.trust + Laura.trust + Jean.trust", 750]}

        optional_objectives = {}

        rewards = {
            "unlock": ["love", "trust", "actions", "shop"]}
            
        criteria = [
            "chapter == 1 and season == 2"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)

init python:

    def ch1_season_two_complete():
        label = "ch1_season_two_complete"

        conditions = [
            "QuestPool.Quests['ch1_season_two_main_Quest'].completed"]

        automatic = True

        return EventClass(label, conditions, automatic = automatic)

label ch1_season_two_complete:
    "You have met all requirements to progress the main story. Check your journal for more information."

    $ season_completed = True

    return

init python:

    def ch1_season_two_progress():
        label = "ch1_season_two_progress"

        conditions = [
            "EventScheduler.Events['ch1_season_two_complete'].completed",
            "not EventScheduler.Events['ch1_season_two_progress'].completed or weekday > 4",
            "not EventScheduler.Events['ch1_Sentinel_attack'].completed",
            "not Present"]

        waking = True

        priority = 99
        repeatable = True

        return EventClass(label, conditions, waking = waking, priority = priority, repeatable = repeatable)

label ch1_season_two_progress:
    $ ongoing_Event = True

    if not Player.History.check("received_Winter_Super_Sale_text"):
        "You wake up and get ready for the day as usual."

        call receive_text(MallSalesperson, "Winter Super Sale*!\n\nFind special offers in a mall near you!\n\nUp to 50%** off at all your favorite clothing and accessory shops!\n\n*{size=-5}Weekend mornings only{/size}\n\n**{size=-5}One purchase per customer{/size}") from _call_receive_text_653
        call open_texts(MallSalesperson) from _call_open_texts_10

        pause

        $ current_phone_screen = "text_choice"

        call open_texts(Kurt) from _call_open_texts_11
        call send_text(Kurt, "hey, I just got a weird text") from _call_send_text_49
        call send_text(Kurt, "says there's a sale going on in the mall") from _call_send_text_50
        call receive_text(Kurt, "Oh, ja") from _call_receive_text_654
        call receive_text(Kurt, "Happens around zis time of year") from _call_receive_text_655
        call receive_text(Kurt, "Not sure how zey get our numbers, but is legit") from _call_receive_text_656
        call send_text(Kurt, "cool, thanks") from _call_send_text_51
        call receive_text(Kurt, "You going?") from _call_receive_text_657
        call receive_text(Kurt, "I would go too, but busy") from _call_receive_text_658
        call receive_text(Kurt, "Sorry Bruder") from _call_receive_text_659

        pause

        $ current_phone_screen = "text_choice"

        call open_texts(MallSalesperson) from _call_open_texts_12

        if weekday <= 4:
            "Seems like you have to wait until the weekend to take advantage of the sale."

        $ Player.History.update("received_Winter_Super_Sale_text")

    if weekday > 4:
        $ current_phone_screen = "text_choice"

        call open_texts(MallSalesperson) from _call_open_texts_38

        $ choice_disabled = False

        menu:
            "Progress the main story" if Player.cash >= 40:
                hide screen phone_screen

                $ EventScheduler.Events["ch1_Sentinel_attack"].start()
            "Progress the main story (locked)" if Player.cash < 40:
                pass
            "Postpone story progress":
                pass

    pause 1.0

    hide screen phone_screen

    $ ongoing_Event = False

    return

init python:

    def ch1_Sentinel_attack():
        label = "ch1_Sentinel_attack"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label ch1_Sentinel_attack:
    $ ongoing_Event = True

    $ weather = None

    $ snow_left = 0

    play music "sounds/music/Disconnect.ogg" fadeout 1.0

    "You grab your wallet and prepare to head to the mall."

    call open_texts(Rogue) from _call_open_texts_13
    call send_text(Rogue, "hey, I'm going to the mall") from _call_send_text_52
    call send_text(Rogue, "wanna come?") from _call_send_text_53
    call receive_text(Rogue, "Wish I could :((") from _call_receive_text_660
    call receive_text(Rogue, "Busy this mornin") from _call_receive_text_661

    pause

    $ current_phone_screen = "text_choice"

    call open_texts(Jean) from _call_open_texts_14
    call send_text(Jean, "hey, I'm going to the mall") from _call_send_text_54
    call send_text(Jean, "wanna come?") from _call_send_text_55
    call receive_text(Jean, "UGH") from _call_receive_text_662
    call receive_text(Jean, "YES, I wanna") from _call_receive_text_663
    call receive_text(Jean, "But I really can't right now </3") from _call_receive_text_664

    pause

    $ current_phone_screen = "text_choice"

    call open_texts(Laura) from _call_open_texts_15
    call send_text(Laura, "hey, I'm going to the mall") from _call_send_text_56
    call send_text(Laura, "wanna come?") from _call_send_text_57
    call receive_text(Laura, "Yes") from _call_receive_text_665
    call send_text(Laura, "you do???") from _call_send_text_58
    call receive_text(Laura, "But I cannot") from _call_receive_text_666
    call receive_text(Laura, "Training") from _call_receive_text_667
    call send_text(Laura, "dammit") from _call_send_text_59

    pause

    hide screen phone_screen

    "Apparently you're destined to go alone. . ."
    "Resigned to your fate, you head out."

    call remove_Characters(location = "bg_hallway") from _call_remove_Characters_219
    call set_the_scene(location = "bg_hallway") from _call_set_the_scene_236

    "You notice more people than usual bustling about today."

    call remove_Characters(location = "bg_campus") from _call_remove_Characters_220
    call set_the_scene(location = "bg_campus") from _call_set_the_scene_237

    "As you exit the mansion, you realize there are a lot of other students also heading in the mall's direction."
    "They probably got a text about the sale as well."

    $ fade_to_black(0.4)

    show expression "images/backgrounds/ch1/bg_ch1_mall_phase1.webp" as mall_background onlayer master zorder 4:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

    show top_bar onlayer master zorder 5:
        transform_anchor True

        align (0.5, 0.5)

    $ fade_in_from_black(0.4)

    "There are a lot more people around than usual."
    "Seems like everyone had the same idea today, and you recognize several of your classmates walking around as well."
    "You pick up the pace so you don't miss out on any deals."

    $ nothing_bought = True
    $ already_visited = False

    while nothing_bought:
        menu:
            "'Mutant Couture'":
                if not already_visited:
                    "You rush over to Mutant Couture."

                    ch_cashier "Welcome to Mutant Couture! We're having a 50\%-off sale on all items!"
                    ch_Player "Sweet." 

                call screen shop_screen("clothing", discount = True, restricted = False)
            "'Bear With Me'":
                if not already_visited:
                    "You rush over to Bear With Me."

                    ch_cashier "Welcome to Bear With Me! We're having a 50\%-off sale on all items!"
                    ch_Player "Sweet." 

                call screen shop_screen("gift", discount = True, restricted = False)
            "'X-Treme Intimates'":
                if not already_visited:
                    "You rush over to X-Treme Intimates."

                    ch_cashier "Welcome to X-Treme Intimates! We're having a 50\%-off sale on all items!"
                    ch_Player "Sweet." 

                call screen shop_screen("lingerie", discount = True, restricted = False)
            "'The Moaning of Life'":
                if not already_visited:
                    "You rush over to The Moaning of Life."

                    ch_cashier "Welcome to The Moaning of Life! We're having a 50\%-off sale on all items!"
                    ch_Player "Sweet." 

                call screen shop_screen("sex", discount = True, restricted = False)

        if _return:
            $ nothing_bought = False
        else:
            "You should probably buy something before the store gets mobbed."

            $ already_visited = True

    $ _skipping = False

    ch_cashier "Thank you for the purchase!"

    play music "sounds/cinematic/Sentinels.ogg" fadeout 0.25
    show screen disable_click(1.0)

    ch_cashier "Is there anything else I can help you with to. . .{w= 1.5}{nw}"

    show expression "images/effects/crash.webp" as crash onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    with big_screenshake

    show expression "images/backgrounds/ch1/bg_ch1_mall_phase2.webp" as mall_background onlayer master zorder 4:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

    show expression "images/backgrounds/ch1/bg_ch1_mall_phase2_Sentinel.webp" as Sentinel onlayer master zorder 6:
        subpixel True
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

        yoffset -int(0.025*config.screen_height)
        ease 15.0 yoffset 0

    show expression "images/backgrounds/ch1/bg_ch1_mall_phase2_flames1.webp" as flames1 onlayer master zorder 7:
        subpixel True
        transform_anchor True

        anchor (0.147, 0.435) pos (0.147, 0.435)
        zoom cinematic_adjustment

        parallel:
            yoffset -int(0.025*config.screen_height)
            ease 15.0 yoffset 0
        parallel:
            choice:
                ease 0.1 xzoom cinematic_adjustment*1.01 yzoom cinematic_adjustment*1.01
            choice:
                ease 0.1 xzoom cinematic_adjustment*1.01 yzoom cinematic_adjustment*1.0
            choice:
                ease 0.1 xzoom cinematic_adjustment*1.01 yzoom cinematic_adjustment*0.99
            choice:
                ease 0.1 xzoom cinematic_adjustment*1.0 yzoom cinematic_adjustment*1.0
            choice:
                ease 0.1 xzoom cinematic_adjustment*0.99 yzoom cinematic_adjustment*0.99
            choice:
                ease 0.1 xzoom cinematic_adjustment*0.99 yzoom cinematic_adjustment*0.99
            choice:
                ease 0.1 xzoom cinematic_adjustment*1.0 yzoom cinematic_adjustment*1.01
            choice:
                ease 0.1 xzoom cinematic_adjustment*1.01 yzoom cinematic_adjustment*1.01

            repeat

    show expression "images/backgrounds/ch1/bg_ch1_mall_phase2_flames2.webp" as flames2 onlayer master zorder 7:
        subpixel True
        transform_anchor True

        anchor (0.380, 0.438) pos (0.380, 0.438)
        zoom cinematic_adjustment

        parallel:
            yoffset -int(0.025*config.screen_height)
            ease 15.0 yoffset 0
        parallel:
            choice:
                ease 0.1 xzoom cinematic_adjustment*1.01 yzoom cinematic_adjustment*1.01
            choice:
                ease 0.1 xzoom cinematic_adjustment*1.01 yzoom cinematic_adjustment*1.0
            choice:
                ease 0.1 xzoom cinematic_adjustment*1.01 yzoom cinematic_adjustment*0.99
            choice:
                ease 0.1 xzoom cinematic_adjustment*1.0 yzoom cinematic_adjustment*1.0
            choice:
                ease 0.1 xzoom cinematic_adjustment*0.99 yzoom cinematic_adjustment*0.99
            choice:
                ease 0.1 xzoom cinematic_adjustment*0.99 yzoom cinematic_adjustment*0.99
            choice:
                ease 0.1 xzoom cinematic_adjustment*1.0 yzoom cinematic_adjustment*1.01
            choice:
                ease 0.1 xzoom cinematic_adjustment*1.01 yzoom cinematic_adjustment*1.01

            repeat

    show expression "images/backgrounds/ch1/bg_ch1_mall_phase2_foreground.webp" as smoke onlayer master zorder 8:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

    with faster_dissolve

    $ Sentinel.name = "???"
    $ Sentinel.give_trait("electronic")
    
    ch_Player "Holy shi-"
    ch_Sentinel "Human citizens, do not be alarmed."

    $ Sentinel.name = "Sentinel"

    ch_Sentinel "We Sentinels are here to serve and protect." 
    "It's like something out of a comic book. 20-foot-tall giant robots flying down through the roof. . ."
    ch_Sentinel "Commencing mutant identification and neutralization protocol."
    ch_Sentinel "X-Gene carriers detected."
    ch_Sentinel "Targets identified. . ."
    ch_Sentinel "Mutants, surrender or die."
    "The Sentinels hover in mid-air, ominously, as every mutant in the room is too shocked to move."
    "The civilians, on the other hand, are all running away like their lives depend on it."
    "Before you can do anything yourself, the choice of whether to run or fight is taken out of your hands." 
    ch_mutant "WE'RE NOT GOING ANYWHERE YOU ROBOT FUCKS!"
    ch_mutant "I'LL HOLD THEM OFF, EVERYBODY RUN!"

    show solid_black onlayer cinematic

    show expression "images/effects/crash.webp" as crash onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    "The man closest to the Sentinels leaps into the air, poised to attack. . ."

    show expression "images/effects/crash.webp" as crash onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    hide Sentinel onlayer master
    hide flames1 onlayer master
    hide flames2 onlayer master
    hide smoke onlayer master
    hide solid_black onlayer cinematic

    show expression "images/backgrounds/ch1/bg_ch1_mall_phase3.webp" as mall_background onlayer master zorder 4:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

    with small_screenshake

    ". . . and is immediately snatched out of the air and slammed into the ground."
    "You watch on, horrified, as more of your fellow students refuse to go quietly and attack in kind."
    "The Sentinels retaliate without mercy."

    show expression "images/effects/bzilll.webp" as bzilll onlayer effects:
        anchor (0.5, 0.5) pos (0.125, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.5 alpha 1.0
        ease 1.0 alpha 0.0

    show expression "images/backgrounds/ch1/bg_ch1_mall_phase3_laser3.webp" as laser3 onlayer master zorder 6:
        subpixel True
        transform_anchor True

        anchor (0.050, 0.397) pos (0.050, 0.397)
        zoom cinematic_adjustment

        block:
            choice:
                ease 5.0 xzoom 1.5*cinematic_adjustment rotate -0.5
            choice:
                ease 5.0 xzoom 1.5*cinematic_adjustment rotate 0.5

            repeat

    with small_screenshake

    "They clearly have a way of determining who is a mutant and who is not."
    "Some mutants fight, others flee, and there are already a few lying motionless on the ground. . ."

    show expression "images/effects/bzilll.webp" as bzilll onlayer effects:
        anchor (0.5, 0.5) pos (0.55, 0.3)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.5 alpha 1.0
        ease 1.0 alpha 0.0

    show expression "images/backgrounds/ch1/bg_ch1_mall_phase3_laser2.webp" as laser2 onlayer master zorder 6:
        subpixel True
        transform_anchor True

        anchor (0.446, 0.254) pos (0.446, 0.254)
        zoom cinematic_adjustment

        block:
            choice:
                ease 7.5 xzoom 0.9*cinematic_adjustment rotate -1
            choice:
                ease 7.5 xzoom 0.95*cinematic_adjustment rotate -0.5
            choice:
                ease 7.5 xzoom 1.0*cinematic_adjustment rotate -0.1

            repeat

    hide laser3 onlayer master

    with small_screenshake

    "The Sentinels are overpowering your fellow mutants."
    "A sense of dread only deepens as you watch one of the Sentinels copy a mutant's ability and use it against them. . ."
    ". . . kind of like [Rogue.name]'s power."

    show expression "images/effects/bzilll.webp" as bzilll onlayer effects:
        anchor (0.5, 0.5) pos (0.6, 0.45)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.5 alpha 1.0
        ease 1.0 alpha 0.0

    show expression "images/backgrounds/ch1/bg_ch1_mall_phase3_laser1.webp" as laser1 onlayer master zorder 6:
        subpixel True
        transform_anchor True

        anchor (0.503, 0.533) pos (0.503, 0.533)
        zoom cinematic_adjustment

        block:
            choice:
                ease 7.5 xzoom 1.1*cinematic_adjustment rotate -0.5
            choice:
                ease 7.5 xzoom 1.1*cinematic_adjustment rotate 0.5 

            repeat

    hide laser2 onlayer master

    with small_screenshake

    ch_mutant "{i}AAAAH! HEEEELP!{/i}"
    "You hear a girl scream at the top of her lungs."
    "The cry for help shakes you out of your stupor and sends you over the edge."

    menu:
        extend ""
        "Help get the the girl to safety (reluctant)":
            call ch1_Sentinel_attack_path_1A from _call_ch1_Sentinel_attack_path_1A

            $ Player.History.update("Reluctant")
            $ Player.History.update("ch1_Sentinel_attack_path_1A")
        "Try to distract the Sentinels (determined)":
            call ch1_Sentinel_attack_path_1B from _call_ch1_Sentinel_attack_path_1B

            $ Player.History.update("Determined")
            $ Player.History.update("ch1_Sentinel_attack_path_1B")
        "Attack the Sentinels (bitter)":
            call ch1_Sentinel_attack_path_1C from _call_ch1_Sentinel_attack_path_1C

            $ Player.History.update("Bitter")
            $ Player.History.update("ch1_Sentinel_attack_path_1C")

    $ fade_to_black(0.4)

    show expression "images/effects/bzilll.webp" as bzilll onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    hide laser1 onlayer master
    hide laser2 onlayer master
    hide laser3 onlayer master

    with small_screenshake

    "Helping the girl to her feet, you watch as the Sentinels incapacitate one mutant after another."
    ch_Player "Quick, get the hell out of here!" 
    "She's shaky on her feet, face pale, but she manages to start running away."
    "You're about to turn and look for another person to help. . ."

    show expression "images/backgrounds/ch1/bg_ch1_mall_phase4.webp" as mall_background onlayer master zorder 4:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

    show expression "images/backgrounds/ch1/bg_ch1_mall_phase4_Sentinel.webp" as Sentinel onlayer master zorder 6:
        transform_anchor True

        align (0.5, 0.5)
        zoom cinematic_adjustment

    $ fade_in_from_black(1.5)

    "Getting so close to the Sentinel seems to have gotten its attention. . ."
    "It looms over you, poised to strike."

    "They were intimidating enough when one wasn't standing over you, staring straight into your eyes."

    ch_Sentinel "Civilian, evacua-"

    show expression "images/effects/click.webp" as click onlayer effects:
        anchor (0.5, 0.5) pos (0.35, 0.1)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.25 alpha 1.0
        ease 1.0 alpha 0.0

    "The Sentinel stops mid-sentence, as its eyes scan you once again."
    ch_Sentinel "Commencing identification protocol. . ."
    ch_Sentinel "Inconclusive."

    show expression "images/effects/click.webp" as click onlayer effects:
        anchor (0.5, 0.5) pos (0.45, 0.25)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.25 alpha 1.0
        ease 1.0 alpha 0.0

    ch_Sentinel "Commencing identification protocol. . ."
    ch_Sentinel "Inconclu-"
    "The robot stutters and cocks its head, your heart starts beating even faster."

    show expression "images/effects/click.webp" as click onlayer effects:
        anchor (0.5, 0.5) pos (0.55, 0.1)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.25 alpha 1.0
        ease 1.0 alpha 0.0

    ch_Sentinel "Unknown mutant identified."
    ch_Sentinel "Mutant, what is your power?"
    ch_Sentinel "If you do not resist, you will not be destroyed."

    menu:
        extend ""
        "I'm not telling you shit. (bitter)":
            if Player.History.check("ch1_Sentinel_attack_path_1A"):
                ch_Sentinel "This response is incongruous with your previous behavior. . ." 
                ch_Sentinel "Reasoning with you in such a tumultuous emotional state is deemed futile." 
            elif Player.History.check("ch1_Sentinel_attack_path_1B"):
                ch_Sentinel "Your determination has been noted. . ." 
                ch_Sentinel "Reasoning with you is deemed futile."
            elif Player.History.check("ch1_Sentinel_attack_path_1C"):
                ch_Sentinel "This response is congruent with your previous aggressive behavior. . ." 
                ch_Sentinel "Reasoning with you is deemed futile. "

            $ Player.History.update("Bitter")
        "Why are you doing this? We're just college students! (reluctant)":
            if Player.History.check("ch1_Sentinel_attack_path_1A"):
                ch_Sentinel "Our programming is specific and binding. . ." 
                ch_Sentinel "You are granted another chance to comply."
            elif Player.History.check("ch1_Sentinel_attack_path_1B"):
                ch_Sentinel "Our programming is specific and binding. . ." 
                ch_Sentinel "You are granted another chance to comply."
            elif Player.History.check("ch1_Sentinel_attack_path_1C"):
                ch_Sentinel "Our programming is specific and binding. . ." 
                ch_Sentinel "This response is incongruous with your previous behavior. . ." 
                ch_Sentinel "Reasoning with you in such a tumultuous emotional state is deemed futile."

            $ Player.History.update("Reluctant")
        "If you tell your friends to stop, maybe I'll talk. (determined)":
            if Player.History.check("ch1_Sentinel_attack_path_1A"):
                ch_Sentinel "These terms are not acceptable. . ." 
                ch_Sentinel "You are granted another chance to comply."
            elif Player.History.check("ch1_Sentinel_attack_path_1B"):
                ch_Sentinel "These terms are not acceptable." 
                ch_Sentinel "Your determination has been noted, reasoning with you is deemed futile."
            elif Player.History.check("ch1_Sentinel_attack_path_1C"):
                ch_Sentinel "These terms are not acceptable." 
                ch_Sentinel "Your previous aggressive behavior is noted, reasoning with you is deemed futile."

            $ Player.History.update("Determined")

    "You try thinking of a way out, but with two other Sentinels nearby handily defeating the other students, despair creeps in."
    ch_Sentinel "Your lack of compliance is noted, destruction imminent."
    "You get into a defensive stance, ready to dodge whatever attack comes your way."
    "As you prepare yourself, you can't help but think. . ."
    "If only you weren't so weak. . ."
    "If only you could do more than just wait to die. . ."
    "Even just the ability to borrow someone else's power, like [Rogue.name]. . ."
    ch_Player "What I wouldn't give to have some real power. . ."

    with big_screenshake

    $ Player.mutant_abilities.append("absorption")
    $ Player.power = 50

    "As soon as you speak, you're racked by a wave of nausea, and a paralyzing pain shoots throughout your body."

    $ _skipping = False

    "Perfect timing, as now you're unable to dodge the Sentinel's laser."

    show expression "images/backgrounds/ch1/bg_ch1_mall_phase4_laser.webp" as laser onlayer master zorder 6:
        subpixel True
        transform_anchor True

        anchor (0.608, 0.473) pos (0.608, 0.473)
        zoom cinematic_adjustment

        alpha 0.0
        ease 5.0 alpha 1.0

    show expression "images/effects/bzzz.webp" as bzzz onlayer effects:
        anchor (0.5, 0.5) pos (0.65, 0.65)

        zoom 0.25
        alpha 0.0
        ease 5.0 zoom 0.5 alpha 1.0
        ease 1.0 alpha 0.0

    show screen disable_click(5.0)

    "You hear the laser charge and manage to at least put your arms up while waiting for the beam to connect. . .{w=5}{nw}"
    "Is this how you die, to some fucking killer robots? Without even getting to know why. . ."

    show expression "images/effects/bzilll.webp" as bzilll onlayer effects:
        anchor (0.5, 0.5) pos (0.65, 0.55)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    show solid_black onlayer cinematic

    with big_screenshake

    show expression "images/effects/bone_crack.webp" as bone_crack onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    $ fade_to_black(0.4)

    $ Player.power = 0

    "The last thing you hear is the sound of searing flesh, and all the bones in your right arm breaking. . ."
    
    play music "sounds/music/Almost an Ending.ogg" fadeout 5.0

    "It immediately knocks you unconscious."
    ". . ."
    "There are no dreams."
    "You cannot see, nor hear anything."
    "This feeling of nothingness lasts forever. . ."
    ". . . until."

    show expression "images/effects/crash.webp" as crash onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    with big_screenshake

    $ Piotr.name = "???"
    $ Logan.name = "???"
    $ Laura.temp = Laura.name
    $ Laura.name = "???"
    $ Cecilia.name = "???"
    $ Jean.temp = Jean.name
    $ Jean.name = "???"
    $ Rogue.temp = Rogue.name
    $ Rogue.name = "???"

    ch_Piotr "Comrade, over here!"
    ". . ."
    ch_Piotr "It looks like he is still breathing."
    ch_Piotr "Bozhe moi!"
    ch_Logan "Careful bub, make sure nobody but [Laura.public_name] 'n I get near 'em."

    $ Piotr.name = "Colossus"
    $ Logan.name = "Logan"

    "You feel weightless."
    ch_Laura "{i}Grrrrrrrrr{/i}. . . if you're not careful, I will kill you."
    "That last voice sounded like [Laura.temp]. . ."
    ". . ."
    "Another eternity passes. . ."

    call knock_on_door(times = 2) from _call_knock_on_door_27

    ch_Cecilia "[Laura.public_name], put some clothes on, we're coming in to evaluate him. . ."
    ". . . was that the doctor?"
    ch_Laura "One minute."

    if Jean.love >= 125:
        ch_Jean "How come she gets to cuddle up with him. . . like that." 
        ". . . [Jean.name]?"

    if Rogue.love >= 125:
        ch_Rogue "Ah would be willin' to. . . {size=-5}try it as well{/size}. . ." 
        ". . . [Rogue.name]?"

    if Jean.love >= 125 or Rogue.love >= 125:
        ch_Cecilia "{i}Ahem{/i}. . . you know exactly why [Laura.public_name] can be the only one." 

    ". . ."
    "More time passes."
    ch_Cecilia "[Laura.public_name], you have to recover at some point!"
    ch_Laura "{i}Just{/i}. . . {i}a little while{/i}. . . {i}longer{/i}. . ."
    ". . ."
    ". . . . . ."

    hide mall_background onlayer master
    hide top_bar onlayer master
    hide Sentinel onlayer master
    hide laser onlayer master
    hide solid_black onlayer cinematic

    $ counter = 0

    while counter < 46:
        call start_new_day(fast = True) from _call_start_new_day_4

        python:
            for C in all_Companions:
                C.timed_text_options = {}

        $ counter += 1

    $ season = 3

    $ season_day = 0

    $ weather = None

    $ snow_left = 0

    python:
        for C in all_Characters:
            C.History.manually_reset("event")
            C.History.manually_reset("season")

    $ Player.History.manually_reset("event")
    $ Player.History.manually_reset("season")

    $ time_index = 1
    
    $ lighting = "day"

    $ infirmary_in_bed = True
        
    $ Player.power = 75

    camera:
        blur 15

    call remove_Characters(location = "bg_infirmary") from _call_remove_Characters_221
    call set_the_scene(location = "bg_infirmary") from _call_set_the_scene_238

    "Your eyes slowly open, trying to adjust to the light."

    camera:
        ease 2.0 blur 0

    "The room is empty, and you feel. . ."
    "Hungry?"
    "Not hungry like you skipped a meal."
    "But a deep, primal hunger, permeating throughout every cell in your body."
    "You look down at yourself, lifting the blankets. . ."
    "You're naked, which isn't too surprising, but what is surprising is that your body doesn't seem to have wasted away at all."
    "All the muscle mass and tone is still there."
    "In fact, you feel surprisingly good. Better than ever."
    "Maybe you weren't actually asleep for that long?"

    $ Cecilia.name = "Dr. Reyes"

    ch_Cecilia "You're awake?!"

    show expression "images/backgrounds/base/bg_infirmary_doctor.webp" as Cecilia onlayer master zorder 0:
        transform_anchor True

        align (0.5, 0.5)
        xzoom -cinematic_adjustment yzoom cinematic_adjustment

    with dissolve

    ch_Player "I. . . guess so?"
    ch_Player "How long has it been. . ."
    ch_Player ". . . and why are you standing so far away?"
    ch_Cecilia "It's been six weeks since the incident at the mall."
    ch_Player "What the hell?!"
    ch_Player "Six weeks?!"
    ch_Cecilia "And since then, you've been. . . dangerous to be around."
    ch_Player "Dangerous? What are you talking about?"
    ch_Cecilia "Shortly after you, and many of the students at the mall were incapacitated. . . or killed. . ."
    ch_Cecilia "The X-Men arrived and managed to drive the Sentinels away."
    ch_Cecilia "When you were found, it became apparent that anyone who got within a few feet of you had all their strength and stamina rapidly depleted."
    ch_Player "Holy shit. . . did I hurt anyone?!"
    ch_Cecilia "No, don't worry."
    ch_Cecilia "It wasn't so rapid that they weren't able to get away."
    ch_Cecilia "Logan and [Laura.public_name] were able to carry you back to the Institute, thanks to their regenerative ability."
    ch_Cecilia "During that process, we noticed your condition visibly improve as you seemed to feed off of their strength."
    ch_Cecilia "When [Laura.public_name] realized this fact, she took it upon herself to hasten your recovery for the past 6 weeks."
    ch_Player "Holy shit. . ."
    ch_Cecilia "It seems to have been effective, considering your current state."
    "She looks you up and down."
    ch_Cecilia "[Laura.public_name] is currently still recovering from the most recent 'session'."

    call change_Outfit(Jean, Jean.Wardrobe.Outfits["Casual 1"], instant = True) from _call_change_Outfit_31
    call show_Character(Jean, x = stage_far_far_right) from _call_show_Character_5

    $ Jean.name = Jean.temp
    $ Jean.change_face("surprised3")

    $ temp = Jean.Player_petname.capitalize()

    ch_Jean "[temp], you're awake?!"
    ch_Cecilia "I'll leave you two to catch up."

    hide Cecilia onlayer master with dissolve

    "[Jean.name]'s about to run over. . ."
    "You try to turn off your power, but it feels different than before and won't listen to you."

    $ Jean.change_face("perplexed")

    ch_Player "Wait!" 

    $ Jean.change_face("worried2")

    ch_Jean "Can't you turn it off now that you're awake?"

    $ Jean.change_face("worried1")

    ch_Jean "I need to hug you."
    ch_Player "I'm trying. . ."

    $ Jean.change_face("angry1")

    ch_Jean "Then let's give you a reason to try harder."

    call show_Character(Jean, x = stage_far_right, sprite_zoom = 1.4*Jean_standing_zoom) from _call_show_Character_6

    "Without any hesitation, [Jean.name] walks right up to you and grabs your hand."

    $ Jean.change_face("surprised2")

    ch_Player "What are you doing?!"

    $ Jean.change_face("worried2")

    ch_Jean "I know you can do it."
    ch_Jean "You just need a little help from your big sis'." 
    ch_Player "My 'big sis''?"

    $ Jean.change_face("worried1", eyes = "closed")

    call Jean_activate_psychic from _call_Jean_activate_psychic_33

    ch_Jean "First, let me try calming you down with my power." 

    $ Jean.change_face("angry1", eyes = "closed")

    "You somehow feel a presence press itself against your mind."

    $ Jean.change_face("worried3")

    call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_33

    "As soon as it does, you see [Jean.name] physically recoil, and the presence disappears."

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Jean "Well that didn't work. . ."

    $ Jean.change_face("angry1")

    "You try to push her away, but she squeezes your hand tightly."
    ch_Jean "[Player.first_name], I know you can do this." 

    $ Jean.change_face("worried1", mouth = "smirk")

    "You hear the confidence in her voice, but you can feel as her grip weakens, and her face starts turning pale."
    "Your mind is a mess of uncontrollable feelings."
    "Worry, helplessness, desperation. . ."
    "{size=+20}Fear.{/size}"

    $ fade_to_black(0.4)

    "You close your eyes."
    "Just like during training with [Jean.name], you struggle against your instincts."
    ". . ."
    "Her grip on your hand weakens even further."
    "{size=+20}Anger.{/size}"
    "Enough."
    "You impose the full force of your {i}will{/i} upon the power inside you."
    ". . ."

    show expression "images/effects/zing.webp" as zing onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    "Your will is indomitable, and the power finally concedes."

    $ Player.power = 0
    
    $ fade_in_from_black(0.4)

    $ Jean.change_face("pleased2")

    ch_Jean "You did it!" 

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Player "Yeah. . ."
    ch_Player "That was surprisingly exhausting."
    "Her grip on your hand reaffirms itself."

    $ Jean.change_face("confused1", mouth = "smirk")

    ch_Jean "You cut it a bit close there, little. . . [Jean.Player_petname]." 

    $ Jean.change_face("worried1", eyes = "right")

    menu:
        extend ""
        "Encourage the sib dynamic (encourage_quirk)":
            ch_Player "You called yourself my 'big sis''. . ." 
            
            $ Jean.change_face("surprised2") 
            
            ch_Player "Can I call you that from now on?" 
            
            $ Jean.change_face("pleased2") 
            
            ch_Jean "You should do that." 
            
            $ Jean.change_face("worried1", mouth = "smirk", blush = 1) 
            
            ch_Jean "Because I really like being your 'big sis''."

            $ Jean.petname = "big sis'"

            $ Jean.History.update("quirk_encouraged")
        "Discourage the sib dynamic (discourage_quirk)":
            ch_Player "You called yourself my 'big sis''. . ." 
            
            $ Jean.change_face("worried2") 
            
            ch_Player "But I like using your name." 
            
            $ Jean.change_face("worried1", mouth = "smirk") 
            
            ch_Jean "Then I guess I'll just use your name too, [Player.first_name]."

            $ Jean.Player_petname = Player.first_name
            $ Jean.petname = Jean.name

            $ Jean.History.update("quirk_discouraged")

    $ Jean.change_face("worried1")

    ch_Jean ". . ."

    $ Jean.change_face("worried1", eyes = "right")

    ch_Jean "I don't like seeing you get hurt."

    $ Jean.change_face("confused1", eyes = "squint")

    ch_Jean "Hmmm. . ."

    $ Jean.change_face("neutral")

    ch_Player "What?"
    ch_Jean "Oh, nothing."
    ch_Jean "Just thinking about how much time I can afford away from studying."

    $ Jean.change_face("confused1", mouth = "smirk")

    ch_Player "For?"
    ch_Jean "To smother you with training and stuff, duh." 

    $ Jean.change_face("smirk2")

    ch_Jean "Alright, I'm gonna go let people know you're awake."
    ch_Player "Thanks. . . for everything." 

    $ Jean.change_face("happy")

    call remove_Characters(Jean) from _call_remove_Characters_222

    "After a few minutes."

    call knock_on_door(times = 2) from _call_knock_on_door_28

    $ Rogue.name = Rogue.temp
    $ temp = Rogue.Player_petname.capitalize()

    ch_Rogue "[temp]? Can ah come in?"
    ch_Player "[Rogue.name]? Absolutely."

    call change_Outfit(Rogue, Rogue.Wardrobe.Outfits["Casual 1"], instant = True) from _call_change_Outfit_32
    call show_Character(Rogue, x = stage_far_far_right) from _call_show_Character_7

    $ Rogue.change_face("worried1")

    ch_Rogue "Can ah. . . come close?"
    ch_Player "Yeah, don't worry. I have my power under control now." 

    $ Rogue.change_face("worried2")

    call show_Character(Rogue, x = stage_far_right, sprite_zoom = 1.4*Rogue_standing_zoom) from _call_show_Character_8

    $ Rogue.change_face("worried1", eyes = "right")

    "She moves closer, but still refrains from touching you."
    ch_Player "What's wrong?"

    $ Rogue.change_face("worried2")

    ch_Rogue "Is yer. . . nullification off as well?"
    ch_Player "I don't. . . huh. . ."

    $ Rogue.change_face("worried1")

    $ fade_to_black(0.4)

    "Instead of responding, you close your eyes feel the power inside you."
    "Except now. . . it's powers, plural. . ."
    "There is this new one, the one which you were just able to restrain."
    "Alongside it, you feel what seems to be your nullification, which does not seem to be similarly restrained."

    $ fade_in_from_black(0.4)

    $ Rogue.change_face("worried2")

    ch_Rogue "Are ya alright?"
    ch_Player "I am."
    ch_Player "And, it's weird, but even after turning off my new power, the nullification still seems to be active."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "Ah still don't think ah should. . ."
    ch_Player "It'll be okay."
    ch_Player "I promise."

    $ Rogue.change_face("worried1")

    ch_Rogue "Alright."

    $ Rogue.change_face("worried1", eyes = "down")

    "She slowly reaches out and takes your hand."

    $ Rogue.change_face("worried2")

    pause 1.0

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Player "See?" 

    $ Rogue.change_face("worried1")

    ch_Rogue "How are ya doin'?"

    $ Rogue.change_face("confused1")

    ch_Player "I'm actually doing really well."
    ch_Player "Whatever happened to me back there. . . it seems like it transformed part of my ability into something kinda similar to yours." 

    $ Rogue.change_face("perplexed")

    ch_Rogue "You're kiddin'?!"

    $ Rogue.change_face("worried1")

    ch_Player "I'm not, and it looks like it's a big reason why I recovered so well." 

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Player "So, I guess I kinda have you to thank." 
    ch_Rogue "Ah'm glad." 
    "Her grip tightens around yours."

    $ Rogue.change_face("worried1", eyes = "down")

    ch_Player "What's wrong?"
    ch_Rogue "Ah just really hate seein' you get hurt. . ."

    menu:
        extend ""
        "You trust me, right? (encourage_quirk)":
            call change_Character_stat(Rogue, "trust", medium_stat) from _call_change_Character_stat_483

            $ Rogue.change_face("worried2")

            pause 1.0

            $ Rogue.change_face("worried1") 
            
            ch_Rogue "Of course ah do." 
            ch_Player "And you'll always be there for me if something does happen?" 
            
            $ Rogue.change_face("worried1", mouth = "smirk", blush = 1) 
            
            ch_Rogue "Ain't no way ah'd be anywhere else." 
            ch_Player "Then there's nothing to worry about." 
            ch_Player "You'll always be at my side." 
            
            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

            $ Rogue.History.update("quirk_encouraged")
        "Hurt? Nothing hurts now that you're here. (discourage_quirk)":
            call change_Character_stat(Rogue, "love", medium_stat) from _call_change_Character_stat_484

            $ Rogue.change_face("surprised2")

            pause 1.0

            $ Rogue.change_face("sly") 
            
            ch_Rogue "Heh, real smooth, [Rogue.Player_petname]." 
            
            $ Rogue.change_face("smirk2") 
            
            ch_Player "But seriously, you're always worried about me." 
            ch_Player "I really appreciate it." 
            
            $ Rogue.change_face("worried1", mouth = "smirk") 
            
            ch_Rogue "Of course." 
            ch_Rogue "Ah just hope next time ah can actually help ya not get injured in the first place. . ."

            $ Rogue.History.update("quirk_discouraged")

    $ Rogue.change_face("smirk2")

    ch_Rogue "Alright, ah can't keep ya all to myself."
    ch_Rogue "I'm sure [Laura.public_name] would appreciate knowin' yer awake."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    pause 1.0

    $ Rogue.change_face("worried1", mouth = "lipbite", eyes = "right", blush = 1)

    $ temp = Rogue.Player_petname.capitalize()

    ch_Rogue "[temp]. . . should I go now? So ah can go tell her?"
    "Did she just ask for permission?"

    menu:
        extend ""
        "Encourage this behavior (encourage_quirk)":
            call change_Character_stat(Rogue, "love", small_stat) from _call_change_Character_stat_485

            ch_Player "Heh, you don't have to be so formal about it." 
            
            $ Rogue.change_face("worried2", mouth = "lipbite", blush = 2) 
            
            ch_Player "Yes, you can go." 
            
            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

            ch_Rogue "Thanks. . ."

            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Rogue "Ah'll be less formal. . . next time."

            $ Rogue.change_face("worried2", blush = 1)

            ch_Player "Wait, do you think she's had enough time to recover?" 

            $ Rogue.change_face("worried1")

            ch_Player "It might be a good idea to just let her rest."
            ch_Rogue "Ah. . . well she's been restin' for 'bout an hour."
            ch_Rogue "Ah don't know if it's my place. . ."
            ch_Rogue "But you know she'll get real angry if she knew you waited on her. . ." 

            $ Rogue.change_face("worried1", mouth = "smirk")

            ch_Player "Good point." 

            $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

            ch_Player "Alright, I'll see you later then." 

            $ Rogue.History.update("quirk_encouraged")
        "Discourage this behavior (discourage_quirk)":
            call change_Character_stat(Rogue, "trust", small_stat) from _call_change_Character_stat_486

            $ Rogue.change_face("worried2", blush = 1) 

            $ temp = Rogue.petname.capitalize()
            
            ch_Player "[temp], you don't have to ask for permission. . ." 
            
            $ Rogue.change_face("worried1", eyes = "right", blush = 1)

            pause 1.0

            $ Rogue.change_face("worried1", mouth = "smirk")

            ch_Rogue "Alright. . . Ah'll head out then."
            ch_Player "Do you think she's had enough time to recover?"
            ch_Player "Maybe you should just let her rest. . ." 

            $ Rogue.change_face("confused1", mouth = "smirk")

            ch_Rogue "It's been 'bout an hour, and you know she'd just get real mad if she knew you waited on her. . ." 

            $ Rogue.change_face("smirk2")

            ch_Player "You're definitely right about that." 
            ch_Player "Alright, I'll see you later."
            
            $ Rogue.History.update("quirk_discouraged")

    call remove_Characters(Rogue) from _call_remove_Characters_223

    "You wait around for a few minutes, until you hear yelling outside."

    ch_Laura ". . . BEEN AWAKE FOR HOW LONG?!"

    show expression "images/effects/crash.webp" as crash onlayer effects:
        anchor (0.5, 0.5) pos (0.75, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    $ Laura.name = Laura.temp

    "The door is violently swung open, and a fuming [Laura.name] appears."

    # call change_Outfit(Laura, Laura.Wardrobe.Outfits["Casual 1"], instant = True)
    call try_on(Laura, Laura.Wardrobe.Clothes["messy hair"]) from _call_try_on_3

    call show_Character(Laura, x = stage_far_right, sprite_zoom = 1.4*Laura_standing_zoom) from _call_show_Character_9

    $ Laura.change_face("furious")

    "Despite the anger, she looks more haggard than you've ever seen her before."
    ch_Player "Are you o-"

    $ Laura.change_face("angry1", eyes = "closed")

    "She doesn't stop and pulls you right into a bear hug."
    "Her grip is weaker than usual, but she still manages to squeeze all the air out of your lungs."
    ch_Player "{i}Can't{/i}. . . {i}breathe{/i}. . ."
    ch_Laura "Tough."

    $ Laura.change_face("furious")

    "She holds you in the hug for an entire minute before she's satisfied."

    $ Laura.change_face("worried2", blush = 1)

    pause 1.0

    $ Laura.change_face("worried1", eyes = "right", blush = 1)

    ch_Player "I heard what you did for me. . ."
    ch_Laura "What exactly did they tell you?"

    $ Laura.change_face("suspicious2", blush = 1)

    ch_Player "Just that you basically let me siphon off your strength and stamina for the past six weeks so I could heal faster. . ." 

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Player ". . . I also heard something about you needing to put your clothes on."
    ch_Player "What was that about?" 

    $ Laura.change_face("furious", blush = 2)

    ch_Laura "It just seemed. . . the more skin contact we had. . ."

    $ Laura.change_face("angry1", eyes = "right", blush = 3)

    ch_Laura "The more rapidly you would heal. . ."

    $ Laura.change_face("suspicious2", blush = 1)

    ch_Player "So you. . . basically cuddled up next to me. . . with both of us naked." 
    ch_Laura "Yes. . ."

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura "I respected your modesty, and nobody actually saw us like that but the doctor. . ." 

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura "{size=-5}Plus [Rogue.name] and [Jean.name]{/size}." 

    $ Laura.change_face("angry1", blush = 1) 

    ch_Player "{i}Ahem{/i}. . . well, regardless of the method." 

    $ Laura.change_face("worried2")

    pause 1.0

    $ Laura.change_face("angry1", eyes = "right", blush = 1)  

    ch_Player "I don't know what else to say but thank you." 
    ch_Laura "Shut up. . ."

    $ Laura.change_face("angry1", eyes = "right", blush = 2)

    ch_Laura ". . . {size=-5}you're welcome{/size}."

    $ Laura.change_face("suspicious2")

    ch_Laura "But you are losing freedom privileges."
    ch_Player "I'm losing what?"

    $ Laura.change_face("angry1")

    ch_Laura "You keep getting injured, so you obviously can't take care of yourself." 

    $ Laura.change_face("angry2")

    ch_Laura "Until that changes, you do what I say, when I say it." 

    $ Laura.change_face("furious")

    ch_Laura "No complaining."

    menu:
        extend ""
        "Encourage her protectiveness (encourage_quirk)":
            $ Laura.change_face("angry2") 
            
            ch_Player "It does make me feel better. . . whenever you're there to back me up." 
            ch_Player "It's not usually how friendships work. . ." 
            ch_Player "But I like the idea of you telling me what to do. . ." 
            
            $ Laura.change_face("sly", blush = 1)
            
            ch_Laura "I also. . . like the feeling it gives me. . ."

            $ Laura.History.update("quirk_encouraged")
        "Discourage her protectiveness (discourage_quirk)":
            $ Laura.change_face("confused1") 
            
            ch_Player "[Laura.name], you can't just take charge of someone's life like that." 
            ch_Player "You can strongly encourage someone to be more careful or help them prepare for the worst." 
            
            $ Laura.change_face("angry2") 
            
            ch_Player "That's how friends usually do it. . ." 
            ch_Laura "Very well. . . then you will be {i}strongly{/i} encouraged."
            
            $ Laura.History.update("quirk_discouraged")

    $ Laura.change_face("neutral")

    ch_Laura "From now on, you can also expect the intensity of your training to drastically increase."

    $ Laura.change_face("angry1")

    ch_Player "Wait no, I. . ." 

    if Laura.History.check("quirk_encouraged") >= Laura.History.check("quirk_discouraged"):
        "She interrupts you."

        $ Laura.change_face("furious", blush = 1)

        ch_Laura "{i}Grrrrrrrrr{/i}. . . what did I just say?"

        $ Laura.change_face("angry2", blush = 2)

        ch_Player "Never mind. . . if you think it's necessary. . ."
        "She just stares at you intensely."
        ". . ."
    else:
        $ Laura.change_face("furious")

        ch_Laura "I am {i}strongly{/i} encouraging you to listen to me." 

        $ Laura.change_face("angry1")

        ch_Player "Okay okay, fine." 
        ch_Player "If you think it's that important. . ."
        ch_Laura "I {i}know{/i} it is." 

    call receive_text(Charles, "I am very glad to hear that you have awakened.") from _call_receive_text_668

    $ Laura.change_face("confused1")

    call open_texts(Charles) from _call_open_texts_16
    call receive_text(Charles, "Whenever you get a chance, please come to my study.") from _call_receive_text_669

    pause

    call send_text(Charles, "thanks [Charles.name]") from _call_send_text_60
    call send_text(Charles, "I'll be there soon") from _call_send_text_61

    pause 2.0

    hide screen phone_screen

    ch_Player "Sorry, [Laura.name]. [Charles.name] wants to talk." 

    $ Laura.change_face("angry1")

    ch_Player "You should really go recover some more." 

    $ Laura.change_face("angry1", eyes = "right")

    ch_Laura "No. . ."
    ch_Player "Please?"

    $ Laura.change_face("worried1", eyes = "right")

    ch_Player "How can you expect to fully protect me if you're in a weakened state?"

    $ Laura.change_face("angry1")

    ch_Laura ". . . Fine. I won't need long."
    ch_Player "Thank you."

    $ Laura.change_face("surprised2", blush = 1)

    "You're about to get up from the bed. . ."
    ch_Laura "You. . . have no clothes. . ."

    $ Laura.change_face("confused1", eyes = "squint", blush = 1)

    ch_Player "Oh shit! Sorry. . ." 
    ch_Laura "It's fine. . . bye."

    call remove_Characters(Laura) from _call_remove_Characters_262

    "You find your clothes folded neatly at the foot of the bed."

    $ infirmary_in_bed = False

    "You get up and get dressed." 

    $ fade_to_black(0.4)

    call send_Characters(Charles, location = "bg_study") from _call_send_Characters_175
    call remove_everyone_but(Charles, location = "bg_study") from _call_remove_everyone_but_5
    call set_the_scene(location = "bg_study") from _call_set_the_scene_239

    $ Charles.change_face("happy")

    ch_Charles "[Player.first_name]! I am very glad to see you in good condition."

    $ Charles.change_face("sad")

    ch_Charles "We were all quite worried."
    ch_Player "Well thankfully It doesn't seem like I was left with any physical scars." 

    $ Charles.change_face("neutral")

    ch_Player "Just mental ones I guess. . ."
    ch_Charles "Such is the way of things, unfortunately."

    $ Charles.change_face("confused1")

    ch_Charles "Your physical recovery was quite surprising, for the second time, no less."
    ch_Charles "No doubt thanks to this new 'evolution' of your power."
    ch_Player "Yeah, what the hell is up with that?"
    ch_Player "Why do things keep changing?"

    $ Charles.change_face("neutral")

    ch_Charles "I have been discussing this at length with Forge and Beast."
    ch_Charles "There are several possible explanations, but most of them are only theoretical phenomena."
    ch_Charles "The most likely explanation is simply the fact that you are quite new to your powers and have not yet been able to explore all of its capabilities."

    $ Charles.change_face("sad")

    ch_Charles "Whether or not severe duress is required for all your capabilities to be revealed, remains to be seen."

    if Player.History.check("ch1_Sentinel_attack_path_1A"):
        ch_Charles "Unfortunately, you are no stranger to duress by now. . ."
        ch_Charles "I was informed about your actions during the attack from other students who were present."
        ch_Charles "Your efforts to get your fellow mutants out of harm's way is commendable."
        ch_Charles "I just wish you had not been. . . punished for such bravery. . ."
    elif Player.History.check("ch1_Sentinel_attack_path_1B"):
        ch_Charles "I have heard, from other students that were present, about your actions in the mall during the attack."
        ch_Charles "Your efforts to delay and distract the Sentinels are certainly commendable."
        ch_Charles "I just wish you had not been. . . punished for such bravery. . ."
    elif Player.History.check("ch1_Sentinel_attack_path_1C"):
        ch_Charles "There has been a lot of talk concerning your actions in the mall during the attack."

        $ Charles.change_face("confused1")

        ch_Charles "You mustn't let your anger fuel your actions." 
        ch_Charles "I know too well what can happen to someone when. . . they let anger and hatred control them."

    $ Charles.change_face("neutral")

    ch_Charles "These 'Sentinels' will not be the last foe you may have to face."
    ch_Player "Who even are the 'Sentinels', and why the hell would they attack a bunch of college students?!"

    $ Charles.change_face("sad")

    ch_Charles "They are a weapon humanity has developed, in their campaign against mutant-kind."
    ch_Charles "Developed. . . by our own government, no less."

    $ Charles.change_face("confused1")

    ch_Charles "But to use them in such an underhanded and public manner. . ."
    ch_Charles "I fear we are reaching a tipping point, as tensions will only continue to rise."
    ch_Player "They're getting desperate. . ."

    $ Charles.change_face("sad")

    menu:
        extend ""
        "I have to be prepared, because a 'next time' seems all but inevitable. (determined)":
            if Player.History.check("ch1_Sentinel_attack_path_1B"):
                ch_Charles "Let this determination fuel you, [Player.first_name]. Preparedness may be what saves us all."
            else:
                ch_Charles "These are trying times. Do not let your resolve to be better than before waver."

            $ Player.History.update("Determined")
        "I don't know if I can handle all this. . . how many more times am I going to get attacked?! (reluctant)":
            if Player.History.check("ch1_Sentinel_attack_path_1A"):
                ch_Charles "Do not worry, [Player.first_name]. You will not have to handle it alone."
            else:
                ch_Charles "These are trying times. Do not let your resolve to be better than before waver." 

            $ Player.History.update("Reluctant")
        "I'm sorry, [Charles.name], but they will get what's coming to them. . . I won't be such a pushover next time. (bitter)":
            if Player.History.check("ch1_Sentinel_attack_path_1C"):
                ch_Charles "Please, [Player.first_name]. We must be better than them."
            else:
                ch_Charles "These are trying times. Do not let your resolve to be better than before waver." 

            $ Player.History.update("Bitter")

    $ Charles.change_face("neutral")

    ch_Player "I guess there's not much else we can do right now. . .  other than be prepared."
    ch_Charles "Keep your friends and allies close, [Player.first_name]. We may all need each other in the coming days."
    ch_Player "I will, thanks."

    $ Charles.change_face("confused1")

    ch_Player "By the way, the X-Men, are they still around?"

    $ Charles.change_face("neutral")

    ch_Charles "I'm afraid not."
    ch_Charles "They departed several weeks ago."

    $ Charles.change_face("happy")

    ch_Charles "However, Ororo visited your bedside many times, before she was forced to leave."
    ch_Charles "Piotr as well."
    ch_Charles "We all care about you very much."
    ch_Player "Thanks for letting me know. . ."

    $ fade_to_black(0.4)

    call set_the_scene(location = Player.home) from _call_set_the_scene_240

    "You notice several weeks of notifications have accumulated on your phone."
    "You casually scroll through them, but an account balance update catches your eye."
    ch_Player "Wait. . . that can't be right."

    call open_texts(Charles) from _call_open_texts_17
    call send_text(Charles, "uh. . . did my money account glitch?") from _call_send_text_62
    call send_text(Charles, f"why do I have a balance of ${Player.cash}?") from _call_send_text_63

    pause 2.0

    call receive_text(Charles, f"Surely you did not expect us to ding your stipend simply for being in a coma, {Player.first_name}.") from _call_receive_text_670
    call receive_text(Charles, "Do not overly concern yourself.") from _call_receive_text_671
    call receive_text(Charles, "You have been through enough to justify a modest reward.") from _call_receive_text_672

    pause 1.0

    call send_text(Charles, f"wow. . . huh. thanks, {Charles.name}") from _call_send_text_64

    pause

    hide screen phone_screen

    call refresh_season_content from _call_refresh_season_content_2

    $ Player.date_planned = {}
    $ Player.schedule = {}

    python:
        for C in all_Companions:
            C.wants_alone_time = 0
            C.schedule = {}

    pause 2.0

    $ unlocked_Characters.append(Sentinel)

    $ clock = 0

    $ season_completed = False

    $ ongoing_Event = False

    return

label ch1_Sentinel_attack_path_1A:
    show expression "images/effects/bzilll.webp" as bzilll onlayer effects:
        anchor (0.5, 0.5) pos (0.125, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.5 alpha 1.0
        ease 1.0 alpha 0.0

    show expression "images/backgrounds/ch1/bg_ch1_mall_phase3_laser3.webp" as laser3 onlayer master zorder 6:
        subpixel True
        transform_anchor True

        anchor (0.050, 0.397) pos (0.050, 0.397)
        zoom cinematic_adjustment

        block:
            choice:
                ease 5.0 xzoom 1.5*cinematic_adjustment rotate -0.5
            choice:
                ease 5.0 xzoom 1.5*cinematic_adjustment rotate 0.5

            repeat

    hide laser1 onlayer master

    with small_screenshake

    "You see a woman on the ground. . ."

    show comic_cutout1 onlayer master zorder 99:
        anchor (0.5, 0.5) pos (0.7, 0.7) xysize (600, 500)
    
    show expression "images/backgrounds/ch1/bg_ch1_mall_phase3.webp" as mall_background onlayer comic_cutout1 zorder 0:
        transform_anchor True

        anchor (0.5, 0.5) pos (-0.9, -0.95)
        zoom 2.0*cinematic_adjustment

    "Your heart races as you remember what happened to [Rogue.name] in the fall."
    "You rush over to try and at least help the poor girl."

    hide comic_cutout1 onlayer master
    hide mall_background onlayer comic_cutout1

    "Without thinking, you dash right between the Sentinel's legs to get to her."
    "You graze the Sentinel on the way by and, just as you thought, your power has no effect."

    return

label ch1_Sentinel_attack_path_1B:
    show expression "images/effects/bzilll.webp" as bzilll onlayer effects:
        anchor (0.5, 0.5) pos (0.125, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.5 alpha 1.0
        ease 1.0 alpha 0.0

    show expression "images/backgrounds/ch1/bg_ch1_mall_phase3_laser3.webp" as laser3 onlayer master zorder 6:
        subpixel True
        transform_anchor True

        anchor (0.050, 0.397) pos (0.050, 0.397)
        zoom cinematic_adjustment

        block:
            choice:
                ease 5.0 xzoom 1.5*cinematic_adjustment rotate -0.5
            choice:
                ease 5.0 xzoom 1.5*cinematic_adjustment rotate 0.5

            repeat

    hide laser1 onlayer master

    with small_screenshake

    "You rush over to the nearest sentinel to try and take some attention off the fleeing students."

    show expression "images/effects/bzilll.webp" as bzilll onlayer effects:
        anchor (0.5, 0.5) pos (0.55, 0.3)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.5 alpha 1.0
        ease 1.0 alpha 0.0

    show expression "images/backgrounds/ch1/bg_ch1_mall_phase3_laser2.webp" as laser2 onlayer master zorder 6:
        subpixel True
        transform_anchor True

        anchor (0.446, 0.254) pos (0.446, 0.254)
        zoom cinematic_adjustment

        block:
            choice:
                ease 7.5 xzoom 0.9*cinematic_adjustment rotate -1
            choice:
                ease 7.5 xzoom 0.95*cinematic_adjustment rotate -0.5
            choice:
                ease 7.5 xzoom 1.0*cinematic_adjustment rotate -0.1

            repeat

    hide laser3 onlayer master

    with small_screenshake

    "As soon as you arrive, you watch helplessly as someone behind you gets turned into a crater."
    "Your resolve is fraying, but you don't flee."
    "Lacking any real offensive ability, you pick up a chunk of rubble and throw it as hard as you can."
    ch_Player "OVER HERE MOTHERFUCKER!"

    show expression "images/effects/clang.webp" as clang onlayer effects:
        anchor (0.5, 0.5) pos (0.3, 0.45)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    "The chunk of concrete shatters as it hits the Sentinel square in the jaw."
    "Apparently you're not enough of a threat to even register, and it barely flinches."

    show expression "images/effects/bzilll.webp" as bzilll onlayer effects:
        anchor (0.5, 0.5) pos (0.6, 0.45)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.5 alpha 1.0
        ease 1.0 alpha 0.0

    show expression "images/backgrounds/ch1/bg_ch1_mall_phase3_laser1.webp" as laser1 onlayer master zorder 6:
        subpixel True
        transform_anchor True

        anchor (0.503, 0.533) pos (0.503, 0.533)
        zoom cinematic_adjustment

        block:
            choice:
                ease 7.5 xzoom 1.1*cinematic_adjustment rotate -0.5
            choice:
                ease 7.5 xzoom 1.1*cinematic_adjustment rotate 0.5 

            repeat

    hide laser2 onlayer master

    with small_screenshake

    "You look around for something else to throw, when you spot a girl, the one who screamed, struggling to get up. . ."

    show comic_cutout1 onlayer master zorder 99:
        anchor (0.5, 0.5) pos (0.7, 0.7) xysize (600, 500)
    
    show expression "images/backgrounds/ch1/bg_ch1_mall_phase3.webp" as mall_background onlayer comic_cutout1 zorder 0:
        transform_anchor True

        anchor (0.5, 0.5) pos (-0.9, -0.95)
        zoom 2.0*cinematic_adjustment

    "Your heart starts racing, as you remember what happened to [Rogue.name] in the first semester."
    "You rush over to try and at least help the poor girl."

    hide comic_cutout1 onlayer master
    hide mall_background onlayer comic_cutout1

    "You graze the Sentinel on the way by and, just as you thought, your power has no effect."
    "You just keep running."

    return

label ch1_Sentinel_attack_path_1C:
    show expression "images/effects/bzilll.webp" as bzilll onlayer effects:
        anchor (0.5, 0.5) pos (0.125, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.5 alpha 1.0
        ease 1.0 alpha 0.0

    show expression "images/backgrounds/ch1/bg_ch1_mall_phase3_laser3.webp" as laser3 onlayer master zorder 6:
        subpixel True
        transform_anchor True

        anchor (0.050, 0.397) pos (0.050, 0.397)
        zoom cinematic_adjustment

        block:
            choice:
                ease 5.0 xzoom 1.5*cinematic_adjustment rotate -0.5
            choice:
                ease 5.0 xzoom 1.5*cinematic_adjustment rotate 0.5

            repeat

    hide laser1 onlayer master

    with small_screenshake

    "Seeing one fellow student after another get injured and maimed causes your blood to boil."
    "With little regard for your own safety, you sprint full tilt at the Sentinels."

    show expression "images/effects/bzilll.webp" as bzilll onlayer effects:
        anchor (0.5, 0.5) pos (0.55, 0.3)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.5 alpha 1.0
        ease 1.0 alpha 0.0

    show expression "images/backgrounds/ch1/bg_ch1_mall_phase3_laser2.webp" as laser2 onlayer master zorder 6:
        subpixel True
        transform_anchor True

        anchor (0.446, 0.254) pos (0.446, 0.254)
        zoom cinematic_adjustment

        block:
            choice:
                ease 7.5 xzoom 0.9*cinematic_adjustment rotate -1
            choice:
                ease 7.5 xzoom 0.95*cinematic_adjustment rotate -0.5
            choice:
                ease 7.5 xzoom 1.0*cinematic_adjustment rotate -0.1

            repeat

    hide laser3 onlayer master

    with small_screenshake

    "They're still distracted by the other mutants, and you run right up to one's leg."
    "You punch it with all your might. . ."

    show expression "images/effects/bone_crack.webp" as bone_crack onlayer effects:
        anchor (0.5, 0.5) pos (0.4, 0.7)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    "A bone in your hand breaks, and your nullification has no effect either."
    "Still fueled by anger, you pick up a piece of rebar with concrete still attached and start wailing on the Sentinel."

    show expression "images/effects/clang.webp" as clang onlayer effects:
        anchor (0.5, 0.5) pos (0.4, 0.7)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    "That doesn't do anything either, and the rebar just bends."
    "The Sentinel just ignores you."

    show expression "images/effects/bzilll.webp" as bzilll onlayer effects:
        anchor (0.5, 0.5) pos (0.6, 0.45)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.5 alpha 1.0
        ease 1.0 alpha 0.0

    show expression "images/backgrounds/ch1/bg_ch1_mall_phase3_laser1.webp" as laser1 onlayer master zorder 6:
        subpixel True
        transform_anchor True

        anchor (0.503, 0.533) pos (0.503, 0.533)
        zoom cinematic_adjustment

        block:
            choice:
                ease 7.5 xzoom 1.1*cinematic_adjustment rotate -0.5
            choice:
                ease 7.5 xzoom 1.1*cinematic_adjustment rotate 0.5 

            repeat

    hide laser2 onlayer master

    with small_screenshake

    "You look around for something else to use as a weapon, when you spot a girl, the one who screamed, struggling to get up. . ."

    show comic_cutout1 onlayer master zorder 99:
        anchor (0.5, 0.5) pos (0.7, 0.7) xysize (600, 500)
    
    show expression "images/backgrounds/ch1/bg_ch1_mall_phase3.webp" as mall_background onlayer comic_cutout1 zorder 0:
        transform_anchor True

        anchor (0.5, 0.5) pos (-0.9, -0.95)
        zoom 2.0*cinematic_adjustment

    "Your heart starts racing, as you remember what happened to [Rogue.name] in the first semester."
    "You rush over to try and at least help the poor girl."

    hide comic_cutout1 onlayer master
    hide mall_background onlayer comic_cutout1

    return