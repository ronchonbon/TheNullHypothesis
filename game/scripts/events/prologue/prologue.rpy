define ch_reporter = Character("Reporter")
define ch_Samson = Character("Dr. Samson")

label prologue:
    $ check_predicted_images()

    show filter onlayer filters:
        alpha 0.5

    show expression "images/backgrounds/ch0/bg_ch0_Earth.webp" as bg_ch0 zorder 0:
        subpixel True
        transform_anchor True

        align (0.5, 0.5)
        zoom 0.5
        alpha 0.0

        parallel:
            ease 2.0 alpha 1.0
        parallel:
            ease 30.0 zoom 0.7

    $ renpy.pause(1.6, hard = True)

    show background zorder 0
    show midground zorder 2
    show foreground zorder 4
    show cover1 zorder 97
    show cover2 zorder 98
    show bottom_bar zorder 99

    $ renpy.pause(0.8, hard = True)

    $ _skipping = True

    "The world's population of mutants - individuals born with the X-Gene, which can give rise to superhuman abilities - grows everyday."
    "Tensions between mutants and non-mutants are at an all-time high."
    "A team of mutant heroes known as the X-Men fight against threats to the tenuous peace between human and mutantkind."

    show expression "images/backgrounds/ch0/bg_ch0_lecture_closed.webp" as bg_ch0:
        subpixel True
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    "As a young college student, however, a geopolitical inter-species power struggle is a little outside your worldview."

    $ Amahl.name = "Prof. Farouk"

    ch_Amahl "Good morning, class."
    ch_Amahl "I do hope you have all been keeping up with the assigned readings: we will start things off today with a pop quiz!"
    "A chorus of groans echoes through the lecture hall - apparently many of your fellow classmates have in fact not been keeping up with the assigned readings."
    ch_Amahl "Yes, yes, enough whining. Pass the papers to the back row, quickly now."
    "A quiz eventually makes its way back to you. . ."

    call screen test_screen()

    if not first_name:
        $ first_name = "John"

    if not last_name:
        $ last_name = "Doe"

    $ first_name = first_name.strip()
    $ last_name = last_name.strip()

    $ Player.first_name = first_name
    $ Player.last_name = last_name
    $ Player.full_name = f"{first_name} {last_name}"

    $ save_name = Player.full_name + "\nPrologue"

    $ Jean.Player_petname = Player.first_name
    $ Laura.Player_petname = Player.first_name
    $ Ororo.Player_petname = Player.first_name

    "After answering all the questions, you pass the paper back to the front of the lecture hall. That wasn't too difficult. . . right?"

    $ black_screen = True

    show black_screen onlayer effects

    $ fade_to_black(0.4)

    "Apparently [Amahl.name] did not choose mercy today: the lecture is just as dry and painful as usual."
    "After listening to him enjoy his own voice for a while, you decide to distract yourself by watching the news."

    show expression "images/backgrounds/ch0/bg_ch0_lecture_blurred.webp" as bg_ch0:
        subpixel True
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    $ fade_in_from_black(0.4)
        
    ch_reporter "We're now speaking with our guest and renowned psychiatrist, Dr. Samson."
    ch_reporter "It's a pleasure to have you with us today."
    ch_Samson "Thank you for inviting me."
    ch_reporter "What do you make of the recent wave of violent crime baffling law enforcement nationwide?{p}The only common thread appears to be amnesia and disorientation by the perpetrators, who claim to remember nothing upon arrest."
    ch_Player "Jesus, more attacks?"
    ch_Player "There can't be anything worse than being brainwashed like that."
    ch_Player "I'd give anything to not be affected by that kind of danger. . ."

    $ Player.power = 50

    "You feel a sharp pain radiate throughout your body, followed by a sudden bout of nausea. " with small_screenshake
    ch_Player "What the fuck???"

    show expression "images/backgrounds/ch0/bg_ch0_lecture.webp" as bg_ch0:
        subpixel True
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment
        blur 0

    ch_Amahl "Mr. [Player.last_name]!" with small_screenshake
    "You snap back to reality, sweat trickling down your back from the discomfort."
    ch_Amahl "Have you ever considered that, if you spent less time on your computer in class and more time paying attention, you might not have failed our last midterm exam?"
    ch_Amahl "Do you have no respect for my lecture, Mr. [Player.last_name], no discipline?"
    "Your face flushes as you feel an entire lecture hall of students turn your way."

    menu:
        extend ""
        "Sorry, [Amahl.name]. You know this class is the reason I wake up every morning.":
            call prologue_1A from _call_prologue_1A
        "Look, Professor, I think that breakfast burrito I ate is starting to fight back. May I please be excused?":
            call prologue_1B from _call_prologue_1B
        "Are you being an asshole on purpose or are you just that conceited? I'm just going to excuse myself. . .":
            call prologue_1C from _call_prologue_1C

    "For the briefest moment, a terrifying look of malice flashes across [Amahl.name]'s face. . .{w} quickly replaced by mild irritation."
    ch_Amahl "I've had enough of your insolence, Mr. [Player.last_name]. You may be excused, but we will have a {i}talk{/i} during my office hours."
    "Shit, now you've done it. . ."

    $ Player.power = 0

    $ fade_to_black(0.4)

    pause 2.0

    show expression "images/backgrounds/ch0/bg_ch0_stall_open.webp" as bg_ch0:
        subpixel True
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    "Some time later. . ."

    $ fade_in_from_black(0.4)

    "You go to the bathroom to wash your face and take a look at yourself in the mirror."

    call screen Player_customization_screen(scholarship = True)

    $ Player.power = 50

    $ Player.check_if_mutation_is_visible()
            
    if Player.visible_mutation:
        if Player.skin_color in ["blue", "green", "red"]:
            "As you look on, your skin begins to ripple and. . . change color. . ."
        
        if Player.ears in ["elf", "fin"]:
            "You feel like the cartilage in your ears is flexing and. . . rearranging. . ."

        ch_Player "What the fuck?!"
        ch_Player "Pull it together, [Player.first_name], you're seeing things. . ."
    else:
        ch_Player "What the hell is going on. . ."

    show expression "images/backgrounds/ch0/bg_ch0_stall_open.webp" as bg_ch0:
        subpixel True
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

        block:
            ease 1.5 blur 15
            ease 1.5 blur 0
            repeat

    "You feel like you're about to throw up."

    show expression "images/backgrounds/ch0/bg_ch0_stall_closed.webp" as bg_ch0:
        subpixel True
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

        block:
            ease 1.5 blur 15
            ease 1.5 blur 0
            repeat

    "You stumble into a bathroom stall, lock the door, and crouch over the toilet seat."
    ch_Player "Fuck, what's happening. . ."
    "Your mounting anxiety gives way to a sense of dread."
    "The hairs on your arms and the back of your neck rise up. You begin shivering uncontrollably."

    show expression "images/backgrounds/ch0/bg_ch0_stall_closed.webp" as bg_ch0:
        subpixel True
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment
        blur 0

    $ Player.power = 0

    "Your attention suddenly shifts to the sound of the bathroom door slamming shut." with small_screenshake

    play music "sounds/cinematic/Shadow King.ogg" fadeout 0.5 fadein 0.5
    
    $ Amahl.name = "???"

    if flashing_lights:
        $ i = 10

        while i > 0:
            if i % 2 == 0:
                show expression "images/backgrounds/ch0/bg_ch0_stall_dark_closed.webp" as bg_ch0_overlay:
                    subpixel True
                    transform_anchor True

                    align (0.5, 0.5)
                    zoom background_adjustment
            else:
                hide bg_ch0_overlay 

            pause 0.02

            $ i -= 1

    show expression "images/backgrounds/ch0/bg_ch0_stall_dark_closed.webp" as bg_ch0:
        subpixel True
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    $ Amahl.telepathic = True

    if flashing_lights:
        ch_Amahl "Mr. [Player.last_name]." with rumble
    else:
        ch_Amahl "Mr. [Player.last_name]."

    "The deep, inhuman voice is like something from your nightmares."
    "You cover your ears in a primal reaction."
    
    if flashing_lights:
        ch_Amahl "I know you are in there." with rumble
    else:
        ch_Amahl "I know you are in there."

    "You realize the voice is coming from inside your head."
    "Panic fills your lungs. Something inside you knows it's already too late to call for help."

    show expression "images/backgrounds/ch0/bg_ch0_stall_dark_open.webp" as bg_ch0:
        subpixel True
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    "The stall door unlocks itself and begins to open."
    "You kick out wildly, trying to shut the door."
    
    if flashing_lights:
        ch_Amahl "Do not resist. Sleep." with rumble
    else:
        ch_Amahl "Do not resist. Sleep."

    "The command causes you to collapse to the floor."
    "An immense weight presses down on you."
    "You are an insect being crushed under a boot."

    $ Amahl.telepathic = False

    pause 2.0

    play music "sounds/music/Almost an Ending.ogg" fadeout 0.5 fadein 0.5

    if flashing_lights:
        $ i = 10

        while i > 0:
            if i % 2 == 0:
                show expression "images/backgrounds/ch0/bg_ch0_stall_open.webp" as bg_ch0_overlay:
                    subpixel True
                    transform_anchor True

                    align (0.5, 0.5)
                    zoom background_adjustment
            else:
                hide bg_ch0_overlay 

            pause 0.02

            $ i -= 1

    show expression "images/backgrounds/ch0/bg_ch0_stall_open.webp" as bg_ch0:
        subpixel True
        transform_anchor True

        align (0.5, 0.5)
        zoom background_adjustment

    "Suddenly, the weight lifts off you."
    "The stall door swings lazily on its hinges."
    
    $ fade_to_black(0.4)
    
    "Gasping for air, you drift in and out of consciousness. You hear a new voice."
    "A human voice."

    $ Charles.name = "???"
    $ Charles.telepathic = True

    ch_Charles "It is alright, [Player.first_name]. . . You are safe. . . You are among friends now. . ."

    $ Charles.telepathic = False

    hide new_game_background 
    hide new_game_comic 
    hide bg_ch0 
    hide bg_ch0_overlay

    $ renpy.pause(2.0, hard = True)

    jump day_one_intro

label prologue_1A:
    "You succeed in making some of your classmates chuckle."
    ch_Amahl "I am honored by your enthusiasm, Mr. [Player.last_name]."
    ch_Amahl "Perhaps you would care to prove your fervor and enlighten us with your insights on today's subject?"

    menu:
        extend ""
        "Let's see. . . Jung's Shadow, encompasses not only our darkest, most reprehensible tendencies, but also our strongest creative desires. For example, your driving urge to be a raging asshole. Now if you'll excuse me, I have to go throw up.":
            pass

    return

label prologue_1B:
    ch_Amahl "I don't care for your silly excuses, Mr. [Player.last_name]. If you leave so early in the lecture I'll have no choice but to mark you as absent."
    ch_Amahl "At any rate, your lack of respect and plummeting academic performance does you more disservice than it does me."
    ch_Amahl "Whether you succeed or fail, your tuition still funds my penthouse in Cairo."

    menu:
        extend ""
        "'So early'?! There's only like 15 minutes left! It's a wonder how you managed to become a psych professor when you aren't even capable of empathy. . . {size=-10}asshole{/size}.":
            pass

    return

label prologue_1C:
    "You succeed in making some of your classmates chuckle."
    ch_Amahl "If you dislike my class that much, you are free to attend whatever matters interest you more."
    ch_Amahl "What you are not entitled to do, Mr. [Player.last_name], is waste my time."

    menu:
        extend ""
        "You've gotta be doing it on purpose. Anyways, see you next week, Professor. . . {size=-10}dickhead{/size}.":
            pass

    return