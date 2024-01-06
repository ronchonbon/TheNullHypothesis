label Jean_flirt_a:
    $ lines = {
        "a": "What kind of music are you into? I'm sure you have great taste.",
        "b": "You look drop-dead gorgeous today. . . as always, I mean.",
        "c": "Your outfit looks really cute today.",
        "d": "That top makes your tits look amazing.",
        "e": "I can't stop looking at your ass. . . It's just so. . . perfect.",
        "f": "Your green eyes are so vibrant. . . mesmerizing.",
        "g": "Do you work out a lot? You're super slender. . . in a good way.",
        "h": "I had a dream about you. . . It was nice.",
        "k": "You always smell so good.",
        "l": "Your hair is stunning, such a vibrant red.",
        "n": "Your smile really brightens my day.",
        "o": "I've seen you training without your powers, and you still look amazing."}

    if Jean.check_traits("quirk"):
        $ lines.update({"i": "I couldn't be luckier. . . you take great care of me."})

    if Jean.History.check("studied_with_Player"):
        $ lines.update({"j": "Thanks for offering to tutor me. Studying with a genius is a huge help."})

    if Jean.History.check("trained_with_Player"):
        $ lines.update({"m": "Your powers are super impressive, not to mention you look awesome while you use them."})

    if Player.scholarship == "athletic":
        $ lines.update({"p": "You're in amazing shape by the way. . . it's super impressive, when your power isn't even physically based. . . (athletic)"})
    elif Player.scholarship == "academic":
        $ lines.update({"r": "I thought I was smart, but you must be a genius. . . (academic)"})
    elif Player.scholarship == "artistic":
        $ lines.update({"q": "I really love how fashionable you are. You always look fantastic. (artistic)"})

    $ indices = list(lines.keys())

    $ renpy.random.shuffle(indices)

    $ first_compliment = lines[indices[0]]
    $ second_compliment = lines[indices[1]]
    $ third_compliment = lines[indices[2]]

    menu:
        "[first_compliment]":
            $ flirting_type = "a" + indices[0]
        "[second_compliment]":
            $ flirting_type = "a" + indices[1]
        "[third_compliment]":
            $ flirting_type = "a" + indices[2]
        "Back":
            return

    if approval_check(Jean, threshold = f"flirting_{flirting_type}"):
        call change_Character_stat(Jean, "love", Jean_flirting_bonuses[flirting_type][0]) from _call_change_Character_stat_593
        call change_Character_stat(Jean, "trust", Jean_flirting_bonuses[flirting_type][1]) from _call_change_Character_stat_594
    else:
        call change_Character_stat(Jean, "love", Jean_flirting_penalties[flirting_type][0]) from _call_change_Character_stat_595
        call change_Character_stat(Jean, "trust", Jean_flirting_penalties[flirting_type][1]) from _call_change_Character_stat_598

    call expression f"Jean_flirt_{flirting_type}" from _call_expression_6

    return

label Jean_flirt_aa:
    if Player.scholarship == "artistic":
        $ dice_roll = renpy.random.randint(1, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Jean.change_face("pleased1", blush = 1)

        ch_Jean "That's sweet, and you're right, of course."

        $ Jean.change_face("smirk2")
        
        ch_Jean "If I get a chance, I'll make you a playlist."
    elif dice_roll == 2:
        $ Jean.change_face("pleased2")

        pause 1.0

        $ Jean.change_face("sly", blush = 1) 

        ch_Jean "We definitely have to hang out and listen to music together at some point."

        $ Jean.change_face("smirk2", blush = 1)

        ch_Jean "I'll show you my favorites."
    elif dice_roll == 3:
        $ Jean.change_face("pleased2", blush = 1)

        ch_Jean "You think so?" 

        $ Jean.change_face("smirk1", eyes = "right", blush = 1) 

        ch_Jean "I mean, of course I do. . ." 

        $ Jean.change_face("smirk2", blush = 1)

        ch_Jean "We should totally listen together at some point."
        ch_Jean "I know you're a big music guy, wouldn't mind hearing what kinda stuff you like." 

    return

label Jean_flirt_ab:
    if Jean.status["horny"] or Jean.status["nympho"]:
        $ dice_roll = renpy.random.randint(1, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Jean.change_face("pleased2", blush = 1)

        pause 1.0

        $ Jean.change_face("sly", blush = 1) 

        ch_Jean "Damn right I do." 

        $ Jean.change_face("smirk2") 

        ch_Jean "I'll forgive the little slip up. . ."
    elif dice_roll == 2:
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("pleased2", blush = 1) 

        ch_Jean "Aw, thanks. . ." 

        $ Jean.change_face("smirk2", eyes = "right")

        ch_Jean "You look pretty great yourself. . ."
    elif dice_roll == 3:
        $ Jean.change_face("sexy", eyes = "down")

        pause 1.0

        $ Jean.change_face("sly", blush = 1) 

        ch_Jean "Yeah, I do."
        ch_Jean "You look particularly good right now too. . ." 

        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    return

label Jean_flirt_ac:
    if Jean.Outfit.Outfit_type == "custom":
        $ dice_roll = renpy.random.randint(1, 4)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Jean.change_face("pleased1", blush = 1)

        ch_Jean "Thanks, [Jean.Player_petname]!" 

        $ Jean.change_face("smirk2", eyes = "down", blush = 1) 

        ch_Jean "It is super cute. . . I look great." 

        $ Jean.change_face("smirk2", blush = 1)
    elif dice_roll == 2:
        $ Jean.change_face("pleased2", blush = 1)

        ch_Jean "Right?!" 

        $ Jean.change_face("smirk2", eyes = "down") 

        ch_Jean "Glad you agree." 

        $ Jean.change_face("smirk2")
    elif dice_roll == 3:
        $ Jean.change_face("confused1", mouth = "smirk", blush = 1) 

        ch_Jean "You're just saying that because you picked this one out." 

        $ Jean.change_face("smirk2", eyes = "down", blush = 1)

        ch_Jean "I mean. . . you're not wrong, though." 

        $ Jean.change_face("smirk2", blush = 1)
    elif dice_roll == 4:
        $ Jean.change_face("pleased1", blush = 1) 

        ch_Jean "Well, you're lucky I let you talk me into wearing it." 

        $ Jean.change_face("smirk2", mouth = "lipbite", eyes = "down", blush = 1) 

        ch_Jean "It does work. . ." 

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "And of course, I can rock just about anything." 

    return

label Jean_flirt_ad:
    $ start = 1
    $ finish = 1

    if not approval_check(Jean, threshold = Jean_thresholds["flirting_ad"]):
        $ start = 3
        $ finish = 4
    
    if Jean.status["horny"] or Jean.status["nympho"]:
        $ finish = 2

    $ dice_roll = renpy.random.randint(start, finish)

    if dice_roll == 1:
        $ Jean.change_face("worried3", blush = 1) 

        ch_Jean "Really?" 

        $ Jean.change_face("worried1", eyes = "down", blush = 1)

        ch_Jean "You think they're. . . big enough?" 

        $ Jean.change_face("worried1", blush = 1)
    elif dice_roll == 2:
        $ Jean.change_face("sly", blush = 1) 

        ch_Jean "Yeah?" 

        $ Jean.change_face("sexy", eyes = "down", blush = 1)

        ch_Jean "I know you're obsessed with them. . ." 

        $ Jean.change_face("sexy", blush = 1)
    elif dice_roll == 3:
        $ Jean.change_face("appalled2")

        pause 1.0

        $ Jean.change_face("angry1") 

        ch_Jean "Stop staring at my chest, jerk." 
    elif dice_roll == 4:
        $ Jean.change_face("perplexed")

        pause 1.0

        $ Jean.change_face("appalled1") 

        ch_Jean "What the hell is wrong with you?!" 

    return

label Jean_flirt_ae:
    $ start = 1
    $ finish = 1

    if not approval_check(Jean, threshold = Jean_thresholds["flirting_ae"]):
        $ start = 3
        $ finish = 4
    elif Jean.status["horny"] or Jean.status["nympho"]:
        $ finish = 2

    $ dice_roll = renpy.random.randint(start, finish)

    if dice_roll == 1:
        $ Jean.change_face("pleased2", blush = 1) 

        ch_Jean "Well. . ."

        $ Jean.change_face("pleased1", eyes = "down", blush = 1) 

        ch_Jean "It is pretty perfect. . ."

        $ Jean.change_face("smirk2", blush = 1)
    elif dice_roll == 2:
        $ Jean.change_face("sly", blush = 1) 

        ch_Jean "You like it?"

        $ Jean.change_face("sexy", blush = 1) 

        ch_Jean "I like yours too. . ."
    elif dice_roll == 3:
        $ Jean.change_face("confused1")

        ch_Jean "Really?"

        $ Jean.change_face("angry1", eyes = "down") 

        ch_Jean "Why would you say something like that?"

        $ Jean.change_face("angry1")
    elif dice_roll == 4:
        $ Jean.change_face("perplexed") 

        ch_Jean "The fuck?"

        $ Jean.change_face("appalled1")

        ch_Jean "Stop staring at my ass, or else."

        $ Jean.change_face("angry1")

    return

label Jean_flirt_af:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("smirk2", blush = 1) 

        ch_Jean "That's. . ."

        $ Jean.change_face("smirk2", blush = 2)

        ch_Jean "Really sweet. . ."
    elif dice_roll == 2:
        $ Jean.change_face("pleased2")

        pause 1.0

        $ Jean.change_face("smirk2", blush = 1) 

        ch_Jean "Well, good."
        ch_Jean "You're the one I actually want to mesmerize. . ."

    return

label Jean_flirt_ag:
    $ start = 1
    $ finish = 1

    if not approval_check(Jean, threshold = Jean_thresholds["flirting_ag"]):
        $ start = 3
        $ finish = 4
    elif Player.scholarship == "athletic":
        $ finish = 2

    $ dice_roll = renpy.random.randint(start, finish)

    if dice_roll == 1:
        $ Jean.change_face("confused3")

        pause 1.0

        $ Jean.change_face("appalled2", blush = 1) 

        ch_Jean "I'm not {i}that{/i} slender."

        $ Jean.change_face("worried1", eyes = "left", blush = 1) 

        ch_Jean "But. . . you think I look good now?"
    elif dice_roll == 2:
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("pleased2", blush = 1) 

        ch_Jean "Maybe a bit more than other people. . ."

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "You like the way I look?"

        $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1)

        pause 1.0

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "You're the one who looks like they work out a lot. . ."
    elif dice_roll == 3:
        $ Jean.change_face("perplexed") 

        ch_Jean "I don't work out {i}that{/i} much. . ."

        $ Jean.change_face("appalled1")

        ch_Jean "Maybe that's not something you should be worrying about."

        $ Jean.change_face("angry1")
    elif dice_roll == 4:
        $ Jean.change_face("appalled2") 

        ch_Jean "Stop worrying so much about my figure."

        $ Jean.change_face("angry1")

    return

label Jean_flirt_ah:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Jean.change_face("pleased2", blush = 1) 

        ch_Jean "That's. . ."

        $ Jean.change_face("smirk2") 

        ch_Jean "I mean, I am pretty dreamy. . ."
    elif dice_roll == 2:
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("sly", blush = 1) 

        ch_Jean "Better not have been anything weird."

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "I'll let it slide. . ."

    return

label Jean_flirt_ai:
    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        $ Jean.change_face("pleased2")

        pause 1.0

        $ Jean.change_face("smirk2", blush = 1) 

        ch_Jean "You are the luckiest, [Jean.Player_petname]. . ."
        ch_Jean "And I couldn't ask for a better little brother."

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)
    elif dice_roll == 2:
        $ Jean.change_face("sly")

        pause 1.0

        $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 

        ch_Jean "You're only saying that because of. . ."

        $ Jean.change_face("sly", eyes = "down", mouth = "lipbite", blush = 1) 

        ch_Jean "How good I make you feel."

        $ Jean.change_face("sly", blush = 1)
    elif dice_roll == 3:
        $ Jean.change_face("pleased2")

        pause 1.0

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "Of course you think that."

        $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1)  

        ch_Jean "I spoil my little bro'. . ."

        $ Jean.change_face("sexy", blush = 1)
    elif dice_roll == 4:
        $ Jean.change_face("pleased2")

        pause 1.0

        $ Jean.change_face("sexy", blush = 1) 

        ch_Jean "Well, when you're such a good little brother. . ."

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 

        ch_Jean "I can't help but spoil you."

        $ Jean.change_face("sexy", eyes = "down", blush = 2)

    return

label Jean_flirt_aj:
    if Player.scholarship == "academic":
        $ dice_roll = renpy.random.randint(1, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Jean.change_face("pleased2", blush = 1) 

        ch_Jean "Well. . . I do try. . ."

        $ Jean.change_face("smirk2", blush = 1) 

        ch_Jean "And tutoring you is a ton of fun."

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "You really are the luckiest."
    elif dice_roll == 2:
        $ Jean.change_face("pleased2")

        pause 1.0

        $ Jean.change_face("happy", blush = 1) 

        ch_Jean "You're welcome!"

        $ Jean.change_face("smirk2", blush = 1) 

        ch_Jean "Plus, I would be tutoring you whether you like it or not."
        ch_Jean "It's for your own good."

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "And I like spending time with you. . ."
    elif dice_roll == 3:
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("worried1", blush = 1) 

        ch_Jean "You think I'm a genius?"

        $ Jean.change_face("smirk2", eyes = "left", blush = 1) 

        ch_Jean "I mean. . . I am amazingly brilliant."

        $ Jean.change_face("smirk2", blush = 1)

        ch_Jean "But you're even smar. . ."

        $ Jean.change_face("smirk2", eyes = "right", mouth = "lipbite", blush = 1) 

        ch_Jean "{i}Nearly{/i} as smart as I am. . ."

    return

label Jean_flirt_ak:
    if not approval_check(Jean, threshold = Jean_thresholds["flirting_ak"]):
        $ dice_roll = renpy.random.randint(3, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Jean.change_face("surprised2")

        $ Jean.change_face("confused1", mouth = "smirk", blush = 1) 

        ch_Jean "I have been trying this new perfume. . ." 

        $ Jean.change_face("smirk2")

        ch_Jean "Glad you like it."
    elif dice_roll == 2:
        $ Jean.change_face("pleased2", blush = 1) 

        ch_Jean "I know, this new conditioner smells great, right?!" 

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "I like the way you smell too. . ."
    elif dice_roll == 3:
        $ Jean.change_face("perplexed") 

        ch_Jean "What the heck. . ." 

        $ Jean.change_face("confused1")

        ch_Jean "Maybe stop standing so close."

    return

label Jean_flirt_al:
    $ Jean.change_face("surprised2") 

    pause 1.0

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Jean "You think so?"

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

    ch_Jean "That's really sweet. . ."

    return

label Jean_flirt_am:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("pleased2") 

        pause 1.0

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "What can I say. . ."
        ch_Jean "I'm the whole package."

        $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1)

        pause 1.0

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "You're pretty impressive yourself."
    elif dice_roll == 2:
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("smirk2", blush = 1) 

        ch_Jean "My powers are awesome. . ."

        $ Jean.change_face("worried1", blush = 2) 

        ch_Jean "If only they cooperated."
        ch_Jean "I do really appreciate your help with that, by the way."
    elif dice_roll == 3:
        $ Jean.change_face("sly", blush = 1) 

        ch_Jean "You're impressive too, ya'know."

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "I've seen you training without me."
        ch_Jean "You pick things up super quick. . ."

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 2)

    return

label Jean_flirt_an:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("happy")

        pause 1.0

        $ Jean.change_face("smirk2", blush = 1) 

        ch_Jean "I'm glad you like it. . ."

        $ Jean.change_face("smirk2", eyes = "left", blush = 1) 

        ch_Jean "Can't help but smile around you."
    elif dice_roll == 2:
        $ Jean.change_face("pleased2")

        pause 1.0

        $ Jean.change_face("smirk2", blush = 1)

        ch_Jean "I guess I'll have to do it more often, then. . ."

        $ Jean.change_face("sly", blush = 1) 

        ch_Jean "As long as you smile for me too."

        $ Jean.change_face("smirk2", blush = 2)
    elif dice_roll == 3:
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "Wow, uhm. . ."

        $ Jean.change_face("smirk2", eyes = "right", mouth = "lipbite", blush = 2) 

        ch_Jean "I'm glad."

        $ Jean.change_face("smirk2", blush = 1) 

        ch_Jean "You're lucky I can't help it around you."

    return

label Jean_flirt_ao:
    if Player.scholarship == "athletic":
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("confused1", blush = 1)

        ch_Jean "You were watching me?"

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "I do look amazing, don't I. . ."
    elif dice_roll == 2:
        $ Jean.change_face("pleased2")

        pause 1.0

        $ Jean.change_face("smirk2", blush = 1) 

        ch_Jean "Thanks, [Jean.Player_petname]. . ."
        ch_Jean "But seriously, look who's talking."

        $ Jean.change_face("smirk2", eyes = "down", blush = 1)

        pause 1.0

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "I can barely keep my eyes off of you whenever you're training. . ."

    return

label Jean_flirt_ap:
    $ Jean.change_face("surprised2")

    pause 1.0

    $ Jean.change_face("worried1", blush = 1) 

    ch_Jean "You really think so?"

    $ Jean.change_face("worried1", eyes = "left", blush = 1)

    ch_Jean "I've always been worried about getting complacent and just letting my powers carry me. . ."
    ch_Jean "Been trying super hard to not let that happen."

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)
    
    ch_Jean "Thanks for noticing."

    $ Jean.change_face("smirk2", mouth = "lipbite", eyes = "down", blush = 1) 

    ch_Jean "Plus. . . you look like you know a thing or two about being in amazing shape. . ."

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    return

label Jean_flirt_aq:
    $ Jean.change_face("pleased2")

    pause 1.0

    $ Jean.change_face("smirk2", blush = 1) 

    ch_Jean "Aw. . . thanks, [Jean.Player_petname]."

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "I'm glad you appreciate how hard I try."

    $ Jean.change_face("worried1", blush = 1) 

    ch_Jean "I wish I had more time to spend on my appearance."
    ch_Jean "But I barely have any free time. . ."

    return

label Jean_flirt_ar:
    $ Jean.change_face("pleased2")

    pause 1.0

    $ Jean.change_face("smirk1", blush = 1) 

    ch_Jean "Well. . . I'm not gonna dispute that. . ."

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "But. . . I mean, it's not like I'm all that much smarter than you."

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 

    ch_Jean "And I do have to try pretty hard."
    ch_Jean "Unlike you, where everything comes so easily."

    return

label Jean_flirt_b:
    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        ch_Player "If I had a dollar for every IQ point you have, I'd be a millionaire."

        $ Jean.change_face("confused1", mouth = "smirk") 

        ch_Jean "A pickup line, really?"

        $ Jean.change_face("smirk2")

        ch_Jean "At least it wasn't about my ass or something. . ."
    elif dice_roll == 2:
        ch_Player "Math isn't my best subject, but even I know you're a perfect 10."

        $ Jean.change_face("perplexed") 

        pause 1.0

        $ Jean.change_face("confused1")

        ch_Jean "Well, you're not wrong. . . but seriously?"
    elif dice_roll == 3:
        ch_Player "By the way, are you a model?"

        $ Jean.change_face("confused1", mouth = "smirk") 

        ch_Jean "No. . ."
        ch_Player "Oh, when did you quit?"

        $ Jean.change_face("pleased2", blush = 1)

        pause 1.0

        $ Jean.change_face("confused1", mouth = "smirk")

        ch_Jean "Heh, at least it was funny."
    elif dice_roll == 4:
        ch_Player "You don't happen to have a protractor on you, do you?"

        $ Jean.change_face("confused1") 

        ch_Jean "I don't, sorry."
        ch_Player "It's fine, I don't need one to know you're acute-y."

        $ Jean.change_face("pleased1")

        pause 1.0

        $ Jean.change_face("confused1", mouth = "smirk")

        ch_Jean "Ugh, really?"
        ch_Jean "That was so bad I actually kinda liked it. . ."

    return

label Jean_flirt_c:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Jean.change_face("pleased2", blush = 1)

        pause 1.0

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "Oh, hey. . ."
    elif dice_roll == 2:
        $ Jean.change_face("confused1", mouth = "smirk", blush = 1) 

        ch_Jean ". . . Need something?"
        ch_Player "No, sorry. Just got lost in your eyes there for a second. . ."

        $ Jean.change_face("pleased2", blush = 1) 

        pause 1.0

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "Oh. . ."

        $ Jean.change_face("smirk2", mouth = "lipbite", eyes= "left", blush = 1)

    return

label Jean_flirt_d:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        ch_Jean "Yes!"

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "Heh, I mean. . . sure."
        "You gently grasp her hand."
    elif dice_roll == 2:
        ch_Jean "Of course we can."

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        "She reaches out and takes your hand, interlacing her fingers with yours."
    elif dice_roll == 3:
        ch_Jean "C'mere. . ."

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        "She takes your hand and gives it a light squeeze."

    return

label Jean_flirt_ea:
    "She gives you a quick peck."
    ch_Jean "Ask for a real kiss next time."

    $ Jean.change_face("smirk2", mouth = "lipbite")

    return

label Jean_flirt_eb:
    if Player.location in public_locations and approval_check(Jean, threshold = [100, 50]):
        $ Jean.change_face("smirk2", eyes = "left", mouth = "lipbite", blush = 1) 

        ch_Jean "Screw it. . ." 

        $ Jean.change_face("kiss1", blush = 1) 

        "She pulls you into a brief kiss before pulling away." 

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "You can bet there will be more later. . ."
    elif Player.location in public_locations:
        $ Jean.change_face("worried1", eyes = "left", mouth = "lipbite", blush = 1) 

        ch_Jean "I really wanna. . ." 
        ch_Jean "Later, when there aren't so many people around." 

        $ Jean.change_face("worried1", blush = 1)
    elif Jean.check_traits("quirk"):
        $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 

        ch_Jean "Want a kiss from your big sister?"

        $ Jean.change_face("sly", brows = "cocked", mouth = "lipbite", blush = 1)

        ch_Jean "Well, what do you say?"
        ch_Player "Please. . ."

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 2)

        pause 1.0

        $ Jean.change_face("kiss2", blush = 2)  

        "After a quick kiss, she pulls away." 

        $ Jean.change_face("sexy", blush = 2)
    else:
        $ Jean.change_face("pleased2", mouth = "lipbite", blush = 1) 

        ch_Jean "Want a kiss, huh?"

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "You really are the luckiest."

        $ Jean.change_face("kiss2", blush = 1) 

        "She pulls you in tight and presses her lips against yours."

    return

label Jean_flirt_f:
    if Player.location in public_locations and approval_check(Jean, threshold = [50, 25]):
        $ Jean.change_face("pleased1") 

        ch_Jean "A hug? Sure!" 

        $ Jean.change_face("smirk2", eyes = "closed") 

        "She pulls you into her arms, and holds you for a brief moment." 

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "You give good hugs."
    elif Player.location in public_locations:
        $ Jean.change_face("confused1", eyes = "left") 

        pause 1.0

        $ Jean.change_face("smirk2") 

        ch_Jean "Fine. . ." 
        ch_Jean "But only a quick one."

        $ Jean.change_face("worried1")

        ch_Jean "PDA isn't really my kinda thing. . ."
        $ Jean.change_face("worried1", eyes = "closed")

        "She pulls you into a hug, giving you a quick squeeze before letting go."

        $ Jean.change_face("smirk2")
    elif approval_check(Jean, threshold = [50, 25]):
        $ Jean.change_face("pleased2", blush = 1) 

        ch_Jean "I love hugging you." 

        $ Jean.change_face("smirk2", eyes = "closed", blush = 1) 

        "Without another word, she pulls you into her arms." 
        "She squeezes you tightly, and holds the embrace for a long moment." 

        $ Jean.change_face("smirk2", blush = 1)

        ch_Jean "Could you. . . hug me more often?" 
    else:
        $ Jean.change_face("pleased2")

        pause 1.0

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "Yeah. . ."
        ch_Jean "C'mere."

        $ Jean.change_face("smirk2", eyes = "closed", blush = 1) 

        "She wraps her arms around you and squeezes gently." 

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "That was nice. . ."

    return

label Jean_flirt_g:
    $ Jean.change_face("confused1", mouth = "smirk") 

    ch_Jean "As if you have to ask."

    $ Jean.change_face("smirk2")

    ch_Jean "You gonna start?"

    $ Jean.change_face("smirk2", eyes = "closed") 

    "You get right to work, and she leans back into your hands, shuddering." 

    $ Jean.change_face("smirk2", blush = 1) 

    ch_Jean "You're pretty good at that."

    return

label Jean_flirt_h:
    if approval_check(Jean, threshold = [175, 150]):
        $ Jean.change_face("pleased2", blush = 1)

        pause 1.0

        $ Jean.change_face("smirk2", eyes = "closed", mouth = "lipbite", blush = 1) 

        "You run your hand through [Jean.name]'s hair."
        "She leans into it, and holds your hand against her head for a moment." 

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "I like when you do that." 
    else:
        $ Jean.change_face("surprised2", blush = 1) 

        "You run your hand through [Jean.name]'s hair, causing her to shudder slightly." 

        $ Jean.change_face("worried1", eyes = "closed", blush = 1)

        "She shudders slightly."

        $ Jean.change_face("worried1", blush = 1)

        ch_Jean "That was. . . interesting"

    return

label Jean_flirt_i:
    if Player.location in public_locations and approval_check(Jean, threshold = [125, 125]):
        $ Jean.change_face("pleased1")

        pause 1.0

        $ Jean.change_face("smirk2", blush = 1) 

        "You wrap your arm around [Jean.name] and she turns to hug you." 

        $ Jean.change_face("smirk2", eyes = "closed", blush = 1) 

        ch_Jean "If you wanted a hug, you should've just said so. . ." 
        "After a moment, she pulls away." 

        $ Jean.change_face("smirk2", blush = 1)
    elif Player.location in public_locations:
        $ Jean.change_face("perplexed")

        pause 1.0

        $ Jean.change_face("confused2", eyes = "right")

        pause 1.0

        $ Jean.change_face("confused1", blush = 1) 

        "As you wrap your arm around [Jean.name], she stiffens, and pulls away." 

        $ Jean.change_face("worried1", blush = 1) 

        ch_Jean "Sorry. . . I just. . ." 
        ch_Jean "I don't mind, if it's you. . . but not around here." 
    elif approval_check(Jean, threshold = [125, 125]):
        $ Jean.change_face("pleased1", blush = 1) 

        pause 1.0

        $ Jean.change_face("kiss1", blush = 1)

        "As you wrap an arm around [Jean.name], she turns and kisses you." 

        $ Jean.change_face("kiss2", blush = 2)
    else:
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("pleased1", blush = 1) 

        "As you wrap your arm around [Jean.name], she leans her head on your shoulder." 

        $ Jean.change_face("smirk2", eyes = "closed", blush = 1)

        ch_Jean "You're pretty comfy."
        "After a moment, she pulls away." 

        $ Jean.change_face("smirk2", blush = 1)

    return

label Jean_flirt_ja:

    return

label Jean_flirt_jb:

    return

label Jean_flirt_jc:

    return

label Jean_flirt_jd:

    return

label Jean_flirt_ka:

    return

label Jean_flirt_kb:

    return

label Jean_flirt_l:
    if Player.location in public_locations and approval_check(Jean, threshold = [350, 325]):
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "Fine. . . but not too hard. . ."

        show expression "images/effects/smack.webp" as smack onlayer effects:
            anchor (0.5, 0.5) pos (Jean.sprite_position[0], 0.7)

            zoom 0.0
            alpha 0.0
            ease 0.1 zoom 1.0 alpha 1.0
            ease 1.0 alpha 0.0

        with small_screenshake
        
        "You give her ass a relatively light smack, and she lets out a small gasp." 

        $ Jean.change_face("sexy", blush = 1) 

        ch_Jean "Satisfied?" 

        $ Jean.change_face("sexy", eyes = "down", blush = 2) 
    elif Player.location in public_locations:
        $ Jean.change_face("perplexed")

        pause 1.0

        $ Jean.change_face("confused1")

        ch_Jean "Seriously?"
        ch_Jean "Why would I let you do that here of all places?"
    elif Jean.check_traits("quirk"):
        $ Jean.change_face("perplexed")

        pause 1.0

        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Jean "Hmmm. . ."

        show expression "images/effects/smack.webp" as smack onlayer effects:
            anchor (0.5, 0.5) pos (0.5, 0.7)

            zoom 0.0
            alpha 0.0
            ease 0.1 zoom 1.0 alpha 1.0
            ease 1.0 alpha 0.0

        with small_screenshake
        
        "Without saying anything, she gives your ass a smack, leaving a light stinging sensation." 

        $ Jean.change_face("sexy", blush = 1) 

        ch_Jean "Naughty little brothers get spanked."
        ch_Jean "But I guess I'll let you do it back to me. . ."

        show expression "images/effects/smack.webp" as smack onlayer effects:
            anchor (0.5, 0.5) pos (Jean.sprite_position[0], 0.7)

            zoom 0.0
            alpha 0.0
            ease 0.1 zoom 1.0 alpha 1.0
            ease 1.0 alpha 0.0

        with small_screenshake
        
        "In retaliation, you smack her ass a bit harder than normal."
        "It takes her off guard, and she can't help but let out a small cry."

        $ Jean.change_face("surprised2", mouth = "lipbite", blush = 2) 

        pause 1.0

        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Jean "I enjoyed that. . ."
    else:
        $ Jean.change_face("worried2")

        pause 1.0

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "That's pretty naughty, [Jean.Player_petname]."

        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Jean "Okay, but not hard."

        show expression "images/effects/smack.webp" as smack onlayer effects:
            anchor (0.5, 0.5) pos (Jean.sprite_position[0], 0.7)

            zoom 0.0
            alpha 0.0
            ease 0.1 zoom 1.0 alpha 1.0
            ease 1.0 alpha 0.0

        with small_screenshake
        
        "You give her ass a proper smack, and she shudders slightly from the impact."

        $ Jean.change_face("surprised2", mouth = "lipbite", blush = 2) 

        pause 1.0

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "That was pretty hard. . ."

    return

label Jean_flirt_ma:

    return

label Jean_flirt_mb:

    return

label Jean_flirt_mc:

    return

label Jean_flirt_na:

    return

label Jean_flirt_nb:

    return

label Jean_flirt_nc:

    return

label Jean_flirt_oa:
    "You walk up to her, and give her a quick kiss on the cheek." 

    $ Jean.change_face("pleased2")

    $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 

    ch_Jean "That better turn into a real kiss later. . ."

    return

label Jean_flirt_ob:
    "As you walk up to her, she seems to realize your intentions." 
    "Before you can do anything, she grabs you, and pulls you into a deep kiss."

    $ Jean.change_face("kiss2", blush = 1)

    "She holds you tightly against herself for another moment, before letting go." 

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

    ch_Jean "Beat you to it. . ." 

    $ Jean.change_face("smirk2", blush = 1) 

    return

label Jean_flirt_pa:

    return

label Jean_flirt_pb:

    return

label Jean_flirt_pc:

    return

label Jean_flirt_pd:

    return

label Jean_flirt_qa:
    $ Jean.change_face("pleased2", blush = 1)

    pause 1.0

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Jean "Really think so?"
    ch_Player "I do, you're the best." 

    $ Jean.change_face("worried1", blush = 1) 

    ch_Jean "I try my best to take good care of you. . ." 

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "You're a great little brother too."

    return

label Jean_flirt_qb:
    $ Jean.change_face("pleased2", blush = 1)

    pause 1.0

    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Jean "I know you're obsessed with your big sister."
    ch_Jean "You really are the luckiest." 

    $ Jean.change_face("sexy", eyes = "down", blush = 1) 

    ch_Jean "Plus, you're only saying that because I make sure to take good care of you. . ." 

    $ Jean.change_face("sexy", blush = 1) 

    ch_Jean "Doesn't mean I don't like being flattered. . ."

    return

label Jean_flirt_qc:
    $ Jean.change_face("confused2", mouth = "smirk", blush = 1)

    pause 1.0

    $ Jean.change_face("sly", blush = 1)

    ch_Jean "Trying to earn brownie points, [Jean.Player_petname]?" 
    ch_Jean "Think that'll get me to stop teasing you?"

    $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 

    ch_Jean "I know you like the teasing." 

    $ Jean.change_face("sexy", eyes = "down", blush = 1) 

    ch_Jean "I can always tell." 

    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Jean "But, that doesn't mean you should stop expressing your thanks. . ."

    return

label Jean_flirt_r:
    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        $ Jean.change_face("happy", blush = 1)

        ch_Player "Just wanted to say that I love you."

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "Aw, I love you too!"
    elif dice_roll == 2:
        $ Jean.change_face("worried1", blush = 1)

        ch_Player "I love you, by the way."
        ch_Jean "You do. . . ?"

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "I mean of course you do."
        ch_Jean "I love you too, [Jean.Player_petname]."
    elif dice_roll == 3:
        $ Jean.change_face("happy", blush = 1)

        ch_Player "Hey, I love you."

        $ Jean.change_face("kiss2", blush = 1)

        "She doesn't respond, just pulling you into a kiss."

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "I know, I love you too, [Jean.Player_petname]."
    elif dice_roll == 4:
        $ Jean.change_face("sly", blush = 1)

        ch_Player "I lov-"
        "[Jean.name] puts a finger over your mouth, stopping you."
        ch_Jean "I get to say it first."

        $ Jean.change_face("worried1", blush = 1)

        ch_Jean "I love you. . ."
        ch_Jean "You love me too, right?"

        $ Jean.change_face("smirk2", blush = 1)

        ch_Player "I do."
        ch_Jean "Good."

    return