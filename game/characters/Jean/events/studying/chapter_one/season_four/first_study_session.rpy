init python:

    def Jean_chapter_one_season_four_first_study_session():
        label = "Jean_chapter_one_season_four_first_study_session"

        conditions = [
            "chapter == 1 and season == 4",

            "not Jean.History.check('studied_with_Player', tracker = 'season')",
            
            "Player.behavior == 'studying' and Jean in Player.behavior_Partners and Jean.behavior == 'studying'"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Jean_chapter_one_season_four_first_study_session:
    $ ongoing_Event = True
    
    $ Jean.change_face("worried1", mouth = "smirk")

    pause 1.0

    $ Jean.change_face("worried1", eyes = "right")

    ch_Jean ". . ."
    ch_Player "What's wrong?"

    $ Jean.change_face("worried2")

    ch_Jean "Nothing's wrong!"

    $ Jean.change_face("worried1", eyes = "right")

    ch_Jean "It's just. . ."

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Jean "No. . ."
    ch_Jean "Nothing."
    ch_Jean "Let's just start studying."
    ch_Jean "Come help me with this stuff."
    ch_Player "Alright. . ."

    $ Jean.change_face("worried1", eyes = "down")

    "As you both set up the study guides and textbooks, you notice something odd."
    "Much unlike her normal self during these study sessions, she seems quite distracted and also doesn't seem to care much at all about how things are organized."

    $ Jean.change_face("smirk1", eyes = "right")

    ch_Player "Are y-"

    $ Jean.change_face("worried2")

    pause 1.0

    $ Jean.change_face("smirk2")

    "She interrupts you, and her entire demeanor changes on a dime."

    $ Jean.change_face("happy")

    ch_Jean "Cool! Thanks for the help."
    ch_Jean "That's good enough, [Jean.Player_petname]."
    $ Jean.change_face("smirk2")

    ch_Jean "We can get started."
    "[Jean.name] doesn't give you another chance to speak, as she pushes you down onto the bed."

    $ Jean.change_face("worried1", eyes = "down")

    "Usually, such disorganization would bother her a lot, but not today apparently. . ."

    $ Jean.change_face("smirk2", eyes = "down")

    "At least, not that she clearly shows." 
    "Once the session starts in earnest, something is clearly distracting her, as she struggles to remain focused on helping you."

    $ Jean.change_face("angry1", eyes = "right")

    "During one particular moment, when she zones out again. . ."

    $ temp = Jean.petname.capitalize()

    menu:
        extend ""
        "You zoned out again. . . tell me what's bothering you so much. Are you really okay?":
            $ Jean.change_face("confused2")

            ch_Jean "I. . . am {i}really{/i} not okay. . ." 
            
            call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_117 
            call change_Companion_stat(Jean, "trust", 0) from _call_change_Companion_stat_118
        "[temp]? Is everything really okay? You're getting distracted again. . .":
            $ Jean.change_face("worried2")

            ch_Jean "No, [Jean.Player_petname], I am {i}really{/i} not okay." 
            
            call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_119
        "Really? What the hell's gotten into you? At this rate, studying with [Laura.name] would be more productive. . .":
            $ Jean.change_face("appalled1")

            ch_Jean "Oh please, like studying with that feral animal would be productive at all. . ." 
            
            $ Jean.change_face("worried1", eyes = "right") 
            
            ch_Jean "Sorry. . . that was mean. . ." 
            
            call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_120 
            call change_Companion_stat(Jean, "trust", 0) from _call_change_Companion_stat_121

    $ Jean.change_face("appalled2")

    pause 1.0

    $ Jean.change_face("furious", eyes = "right")

    ch_Jean "UGH!"
    ch_Jean "I just can't do this anymore."
    
    $ Jean.change_face("worried3")

    if Jean in Partners:
        ch_Jean "I don't mean our relationship!"
    else:
        ch_Jean "I don't mean our friendship!"

    $ Jean.change_face("worried1", eyes = "down")

    ch_Jean "I mean. . . {i}this{/i}."
    "She gestures to the mess of papers and books all over her bed."

    $ Jean.change_face("worried1")

    ch_Player "We can take a break from studying if you want."

    $ Jean.change_face("worried2")

    ch_Jean "Ugh, I mean in general, [Player.first_name]."
    
    if Player.scholarship == "academic":
        ch_Jean "C'mon, you probably know how I feel." 
        
        $ Jean.change_face("worried1") 
        
        ch_Jean "You had super good grades in college before all this." 
        ch_Jean "Probably spent a ton of time studying instead of doing fun stuff."
    else:
        ch_Jean "I know you might not know exactly how I feel. . . but you still did pretty well in college. . ." 
        
        $ Jean.change_face("worried1") 
        
        ch_Jean "What the professors expect from us here at the Institute, you have to know how much studying it takes to do well."

    $ temp = Jean.Player_petname.capitalize()

    ch_Jean "[temp], I don't think you understand just how much of my life I've wasted staring at these goddamn books."

    $ Jean.change_face("angry1", eyes = "right")

    ch_Jean "So focused on getting perfect grades, instead of having fun or taking care of myself."

    $ Jean.change_face("worried3")

    ch_Jean "I mean for god's sake, you're one of my best friends, and you've only been here for a few months."

    $ Jean.change_face("sad", eyes = "right")

    ch_Jean "How sad is that."

    $ Jean.change_face("worried1")

    ch_Jean "And now, I'm just a couple months away from graduating. . ."
    ch_Jean "It's not like I'm going anywhere, I'll probably just be another professor here, staying with the X-Men."

    $ Jean.change_face("worried1", eyes = "right")

    ch_Jean "What did it even matter. . . being 'top of my class'?"

    $ Jean.change_face("angry1", eyes = "right")

    ch_Jean "Who actually gives a shit."
    ch_Jean ". . . such a waste of time."

    menu:
        extend ""
        "[Jean.name], you can't think about it that way.":
            $ Jean.change_face("worried3")

            ch_Jean "What other way is there to think about it?" 
            
            $ Jean.change_face("angry1", eyes = "right") 
            
            ch_Jean "It doesn't matter in the end." 
            
            call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_122 
            call change_Companion_stat(Jean, "trust", 0) from _call_change_Companion_stat_123
        "I. . . give a shit. And you can't think like that.":
            $ Jean.change_face("worried3")

            ch_Jean "How can I not?!" 
            
            $ Jean.change_face("angry1", eyes = "right") 
            
            ch_Jean "Even deep down, I know you think it's probably a waste." 
            
            call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_124
        "Oh please, stop lying to yourself.":
            $ Jean.change_face("appalled1")

            ch_Jean "What the hell?" 
            
            call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_125 
            call change_Companion_stat(Jean, "trust", 0) from _call_change_Companion_stat_126

    $ Jean.change_face("confused2")

    ch_Player "You know just as well as I how much of a shit you give."

    $ Jean.change_face("worried2")

    ch_Player "And just think about how much of an impact you've had on someone like me by giving a shit."

    $ Jean.change_face("worried1", eyes = "down")

    ch_Player "You've been unimaginably helpful, both acclimating me to the classes here, but also helping me get used to all this mutant stuff as well."

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Player "I know how much you care about helping me."
    ch_Player "And it's not like you're graduating tomorrow." 
    ch_Player "There's still plenty of semester left to make up for lost time."

    $ Jean.change_face("worried1")

    ch_Jean "But what's the best way to do that?"
    ch_Jean "Did. . . you have something in mind?"
    ch_Player "This isn't really something you meticulously plan and prepare for."

    $ Jean.change_face("worried2")

    ch_Player "Why not, for once in your life, stop caring so much and focus on relaxing."

    $ Jean.change_face("confused1")

    ch_Jean "Well, since you seem to be an expert all of a sudden, you'll just have to take responsibility."

    if Jean.History.check("quirk_encouraged") >= Jean.History.check("quirk_discouraged"):
        ch_Jean "I think it's time for my little bro' to take care of his big sis'."

    ch_Player "For starters. . ."

    $ Jean.change_face("surprised2")

    "You haphazardly shove all the papers and books off of the bed."

    $ Jean.change_face("confused1")

    "Then, you get up and go to find her music player."
    "She just sits on the bed, looking bewildered."
    "You put on some chill tunes and lay down next to her on the bed."
    ch_Player "So, did I pick the right song?"

    $ Jean.change_face("confused1", mouth = "smirk")

    ch_Jean "Oh hell yes." 

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Jean "This band is my favorite. . . when I do get to listen to them. . ."

    $ fade_to_black(1.5)

    "[Jean.name] lays back down on the bed, and the both of you stare up at the ceiling." 
    "She goes on and on about the music - how she has a hard time focusing when it's playing, so she doesn't listen to it much."
    "The conversation continues as you both share much about yourselves, the topics meandering around whatever is on your minds."
    "Instead of a hardcore study session like planned, you both let the hours leisurely pass by, just enjoying each other's company."

    $ fade_in_from_black(1.5)

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Jean "I haven't {i}wasted{/i} that much time in a long while. . ."
    ch_Player "Feels good, right?"

    $ Jean.change_face("smirk2")

    ch_Jean "Yeah, [Jean.Player_petname], it does."
    ch_Jean "Let's do it again sometime soon."

    $ ongoing_Event = False

    return