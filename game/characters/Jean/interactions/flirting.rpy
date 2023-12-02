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
        "j": "Thanks for offering to tutor me. Studying with a genius is a huge help.",
        "k": "You always smell so good.",
        "l": "Your hair is stunning, such a vibrant red.",
        "n": "Your smile really brightens my day.",
        "o": "I've seen you training without your powers, and you still look amazing."}

    if Jean.quirk:
        $ lines.update({"i": "I couldn't be luckier. . . you take great care of me."})

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
            call expression f"Jean_flirt_a{indices[0]}" from _call_expression_6
        "[second_compliment]":
            call expression f"Jean_flirt_a{indices[1]}" from _call_expression_7
        "[third_compliment]":
            call expression f"Jean_flirt_a{indices[2]}" from _call_expression_8
        "Back":
            return

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

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_223 
    elif dice_roll == 2:
        $ Jean.change_face("pleased2")

        pause 1.0

        $ Jean.change_face("sly", blush = 1) 

        ch_Jean "We definitely have to hang out and listen to music together at some point."

        $ Jean.change_face("smirk2", blush = 1)

        ch_Jean "I'll show you my favorites."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_224 
    elif dice_roll == 3:
        $ Jean.change_face("pleased2", blush = 1)

        ch_Jean "You think so?" 

        $ Jean.change_face("smirk1", eyes = "right", blush = 1) 

        ch_Jean "I mean, of course I do. . ." 

        $ Jean.change_face("smirk2", blush = 1)

        ch_Jean "We should totally listen together at some point."
        ch_Jean "I know you're a big music guy, wouldn't mind hearing what kinda stuff you like." 

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_225

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

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_226
    elif dice_roll == 2:
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("pleased2", blush = 1) 

        ch_Jean "Aw, thanks. . ." 

        $ Jean.change_face("smirk2", eyes = "right")

        ch_Jean "You look pretty great yourself. . ."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_227
    elif dice_roll == 3:
        $ Jean.change_face("sexy", eyes = "down")

        pause 1.0

        $ Jean.change_face("sly", blush = 1) 

        ch_Jean "Yeah, I do."
        ch_Jean "You look particularly good right now too. . ." 

        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_228
        call change_Companion_stat(Jean, "desire", 0) from _call_change_Companion_stat_229

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

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_230
    elif dice_roll == 2:
        $ Jean.change_face("pleased2", blush = 1)

        ch_Jean "Right?!" 

        $ Jean.change_face("smirk2", eyes = "down") 

        ch_Jean "Glad you agree." 

        $ Jean.change_face("smirk2")

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_231
    elif dice_roll == 3:
        $ Jean.change_face("confused1", mouth = "smirk", blush = 1) 

        ch_Jean "You're just saying that because you picked this one out." 

        $ Jean.change_face("smirk2", eyes = "down", blush = 1)

        ch_Jean "I mean. . . you're not wrong, though." 

        $ Jean.change_face("smirk2", blush = 1)

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_232
    elif dice_roll == 4:
        $ Jean.change_face("pleased1", blush = 1) 

        ch_Jean "Well, you're lucky I let you talk me into wearing it." 

        $ Jean.change_face("smirk2", mouth = "lipbite", eyes = "down", blush = 1) 

        ch_Jean "It does work. . ." 

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "And of course, I can rock just about anything." 

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_233

    return

label Jean_flirt_ad:
    $ start = 1
    $ finish = 1

    if not approval_check(Jean, threshold = [150, 125]):
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

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_234
    elif dice_roll == 2:
        $ Jean.change_face("sly", blush = 1) 

        ch_Jean "Yeah?" 

        $ Jean.change_face("sexy", eyes = "down", blush = 1)

        ch_Jean "I know you're obsessed with them. . ." 

        $ Jean.change_face("sexy", blush = 1)

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_235
        call change_Companion_stat(Jean, "desire", 0) from _call_change_Companion_stat_236
    elif dice_roll == 3:
        $ Jean.change_face("appalled2")

        pause 1.0

        $ Jean.change_face("angry1") 

        ch_Jean "Stop staring at my chest, jerk." 

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_237
        call change_Companion_stat(Jean, "trust", 0) from _call_change_Companion_stat_238
    elif dice_roll == 4:
        $ Jean.change_face("perplexed")

        pause 1.0

        $ Jean.change_face("appalled1") 

        ch_Jean "What the hell is wrong with you?!" 

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_239
        call change_Companion_stat(Jean, "trust", 0) from _call_change_Companion_stat_240

    return

label Jean_flirt_ae:
    $ start = 1
    $ finish = 1

    if not approval_check(Jean, threshold = [150, 125]):
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

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1187
        call change_Companion_stat(Jean, "desire", 0) from _call_change_Companion_stat_1188
    elif dice_roll == 2:
        $ Jean.change_face("sly", blush = 1) 

        ch_Jean "You like it?"

        $ Jean.change_face("sexy", blush = 1) 

        ch_Jean "I like yours too. . ."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1189
        call change_Companion_stat(Jean, "desire", 0) from _call_change_Companion_stat_1190
    elif dice_roll == 3:
        $ Jean.change_face("confused1")

        ch_Jean "Really?"

        $ Jean.change_face("angry1", eyes = "down") 

        ch_Jean "Why would you say something like that?"

        $ Jean.change_face("angry1")

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1191
        call change_Companion_stat(Jean, "trust", 0) from _call_change_Companion_stat_1192
    elif dice_roll == 4:
        $ Jean.change_face("perplexed") 

        ch_Jean "The fuck?"

        $ Jean.change_face("appalled1")

        ch_Jean "Stop staring at my ass, or else."

        $ Jean.change_face("angry1")

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1193
        call change_Companion_stat(Jean, "trust", 0) from _call_change_Companion_stat_1194

    return

label Jean_flirt_af:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Jean.change_face("surprised2")

        pause 0.5

        $ Jean.change_face("smirk2", blush = 1) 

        ch_Jean "That's. . ."

        $ Jean.change_face("smirk2", blush = 2)

        ch_Jean "Really sweet. . ."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1195 
    elif dice_roll == 2:
        $ Jean.change_face("pleased2")

        pause 0.5

        $ Jean.change_face("smirk2", blush = 1) 

        ch_Jean "Well, good."
        ch_Jean "You're the one I actually want to mesmerize. . ."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1196

    return

label Jean_flirt_ag:
    $ start = 1
    $ finish = 1

    if not approval_check(Jean, threshold = [175, 150]):
        $ start = 3
        $ finish = 4
    elif Player.scholarship == "athletic":
        $ finish = 2

    $ dice_roll = renpy.random.randint(start, finish)

    if dice_roll == 1:
        $ Jean.change_face("confused3")

        pause 0.5

        $ Jean.change_face("appalled2", blush = 1) 

        ch_Jean "I'm not {i}that{/i} slender."

        $ Jean.change_face("worried1", eyes = "left", blush = 1) 

        ch_Jean "But. . . you think I look good now?"

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1197
    elif dice_roll == 2:
        $ Jean.change_face("surprised2")

        pause 0.5

        $ Jean.change_face("pleased2", blush = 1) 

        ch_Jean "Maybe a bit more than other people. . ."

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "You like the way I look?"

        $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1)

        pause 0.5

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "You're the one who looks like they work out a lot. . ."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1198
    elif dice_roll == 3:
        $ Jean.change_face("perplexed") 

        ch_Jean "I don't work out {i}that{/i} much. . ."

        $ Jean.change_face("appalled1")

        ch_Jean "Maybe that's not something you should be worrying about."

        $ Jean.change_face("angry1")

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1199
        call change_Companion_stat(Jean, "trust", 0) from _call_change_Companion_stat_1200
    elif dice_roll == 4:
        $ Jean.change_face("appalled2") 

        ch_Jean "Stop worrying so much about my figure."

        $ Jean.change_face("angry1")

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1201
        call change_Companion_stat(Jean, "trust", 0) from _call_change_Companion_stat_1202

    return

label Jean_flirt_ah:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Jean.change_face("pleased2", blush = 1) 

        ch_Jean "That's. . ."

        $ Jean.change_face("smirk2") 

        ch_Jean "I mean, I am pretty dreamy. . ."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1203
    elif dice_roll == 2:
        $ Jean.change_face("surprised2")

        pause 0.5

        $ Jean.change_face("sly", blush = 1) 

        ch_Jean "Better not have been anything weird."

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "I'll let it slide. . ."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1204

    return

label Jean_flirt_ai:
    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        $ Jean.change_face("pleased2")

        pause 0.5

        $ Jean.change_face("smirk2", blush = 1) 

        ch_Jean "You are the luckiest, [Jean.Player_petname]. . ."
        ch_Jean "And I couldn't ask for a better little brother."

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1205
        call change_Companion_stat(Jean, "desire", 0) from _call_change_Companion_stat_1206
    elif dice_roll == 2:
        $ Jean.change_face("sly")

        pause 0.5

        $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 

        ch_Jean "You're only saying that because of. . ."

        $ Jean.change_face("sly", eyes = "down", mouth = "lipbite", blush = 1) 

        ch_Jean "How good I make you feel."

        $ Jean.change_face("sly", blush = 1)

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1207
        call change_Companion_stat(Jean, "desire", 0) from _call_change_Companion_stat_1208
    elif dice_roll == 3:
        $ Jean.change_face("pleased2")

        pause 0.5

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "Of course you think that."

        $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1)  

        ch_Jean "I spoil my little bro'. . ."

        $ Jean.change_face("sexy", blush = 1)

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1209
        call change_Companion_stat(Jean, "desire", 0) from _call_change_Companion_stat_1210
    elif dice_roll == 4:
        $ Jean.change_face("pleased2")

        pause 0.5

        $ Jean.change_face("sexy", blush = 1) 

        ch_Jean "Well, when you're such a good little brother. . ."

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 

        ch_Jean "I can't help but spoil you."

        $ Jean.change_face("sexy", eyes = "down", blush = 2)

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1211
        call change_Companion_stat(Jean, "desire", 0) from _call_change_Companion_stat_1212

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

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1213 
    elif dice_roll == 2:
        $ Jean.change_face("pleased2")

        pause 0.5

        $ Jean.change_face("happy", blush = 1) 

        ch_Jean "You're welcome!"

        $ Jean.change_face("smirk2", blush = 1) 

        ch_Jean "Plus, I would be tutoring you whether you like it or not."
        ch_Jean "It's for your own good."

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "And I like spending time with you. . ."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1214 
    elif dice_roll == 3:
        $ Jean.change_face("surprised2")

        pause 0.5

        $ Jean.change_face("worried1", blush = 1) 

        ch_Jean "You think I'm a genius?"

        $ Jean.change_face("smirk2", eyes = "left", blush = 1) 

        ch_Jean "I mean. . . I am amazingly brilliant."

        $ Jean.change_face("smirk2", blush = 1)

        ch_Jean "But you're even smar. . ."

        $ Jean.change_face("smirk2", eyes = "right", mouth = "lipbite", blush = 1) 

        ch_Jean "{i}Nearly{/i} as smart as I am. . ."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1215

    return

label Jean_flirt_ak:
    if not approval_check(Jean, threshold = [150, 125]):
        $ dice_roll = renpy.random.randint(3, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Jean.change_face("surprised2")

        $ Jean.change_face("confused1", mouth = "smirk", blush = 1) 

        ch_Jean "I have been trying this new perfume. . ." 

        $ Jean.change_face("smirk2")

        ch_Jean "Glad you like it."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_241
    elif dice_roll == 2:
        $ Jean.change_face("pleased2", blush = 1) 

        ch_Jean "I know, this new conditioner smells great, right?!" 

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "I like the way you smell too. . ."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_242
    elif dice_roll == 3:
        $ Jean.change_face("perplexed") 

        ch_Jean "What the heck. . ." 

        $ Jean.change_face("confused1")

        ch_Jean "Maybe stop standing so close."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_243
        call change_Companion_stat(Jean, "trust", 0) from _call_change_Companion_stat_244

    return

label Jean_flirt_al:
    $ Jean.change_face("surprised2") 

    pause 0.5

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Jean "You think so?"

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

    ch_Jean "That's really sweet. . ."

    call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1216 

    return

label Jean_flirt_am:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("pleased2") 

        pause 0.5

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "What can I say. . ."
        ch_Jean "I'm the whole package."

        $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1)

        pause 0.5

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "You're pretty impressive yourself."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1217
    elif dice_roll == 2:
        $ Jean.change_face("surprised2")

        pause 0.5

        $ Jean.change_face("smirk2", blush = 1) 

        ch_Jean "My powers are awesome. . ."

        $ Jean.change_face("worried1", blush = 2) 

        ch_Jean "If only they cooperated."
        ch_Jean "I do really appreciate your help with that, by the way."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1218
    elif dice_roll == 3:
        $ Jean.change_face("sly", blush = 1) 

        ch_Jean "You're impressive too, ya'know."

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "I've seen you training without me."
        ch_Jean "You pick things up super quick. . ."

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 2)

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1219

    return

label Jean_flirt_an:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("happy")

        pause 0.5

        $ Jean.change_face("smirk2", blush = 1) 

        ch_Jean "I'm glad you like it. . ."

        $ Jean.change_face("smirk2", eyes = "left", blush = 1) 

        ch_Jean "Can't help but smile around you."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1220
    elif dice_roll == 2:
        $ Jean.change_face("pleased2")

        pause 0.5

        $ Jean.change_face("smirk2", blush = 1)

        ch_Jean "I guess I'll have to do it more often, then. . ."

        $ Jean.change_face("sly", blush = 1) 

        ch_Jean "As long as you smile for me too."

        $ Jean.change_face("smirk2", blush = 2) 

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1221
    elif dice_roll == 3:
        $ Jean.change_face("surprised2")

        pause 0.5

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "Wow, uhm. . ."

        $ Jean.change_face("smirk2", eyes = "right", mouth = "lipbite", blush = 2) 

        ch_Jean "I'm glad."

        $ Jean.change_face("smirk2", blush = 1) 

        ch_Jean "You're lucky I can't help it around you."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1222

    return

label Jean_flirt_ao:
    if Player.scholarship == "athletic":
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Jean.change_face("surprised2")

        pause 0.5

        $ Jean.change_face("confused1", blush = 1)

        ch_Jean "You were watching me?"

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "I do look amazing, don't I. . ."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1223
        call change_Companion_stat(Jean, "trust", 0) from _call_change_Companion_stat_1224
    elif dice_roll == 2:
        $ Jean.change_face("pleased2")

        pause 0.5

        $ Jean.change_face("smirk2", blush = 1) 

        ch_Jean "Thanks, [Jean.Player_petname]. . ."
        ch_Jean "But seriously, look who's talking."

        $ Jean.change_face("smirk2", eyes = "down", blush = 1)

        pause 0.5

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "I can barely keep my eyes off of you whenever you're training. . ."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1225
        call change_Companion_stat(Jean, "trust", 0) from _call_change_Companion_stat_1226

    return

label Jean_flirt_ap:
    $ Jean.change_face("surprised2")

    pause 0.5

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

    call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1227
    call change_Companion_stat(Jean, "trust", 0) from _call_change_Companion_stat_1228

    return

label Jean_flirt_aq:
    $ Jean.change_face("pleased2")

    pause 0.5

    $ Jean.change_face("smirk2", blush = 1) 

    ch_Jean "Aw. . . thanks, [Jean.Player_petname]."

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "I'm glad you appreciate how hard I try."

    $ Jean.change_face("worried1", blush = 1) 

    ch_Jean "I wish I had more time to spend on my appearance."
    ch_Jean "But I barely have any free time. . ."

    call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1229
    call change_Companion_stat(Jean, "trust", 0) from _call_change_Companion_stat_1230

    return

label Jean_flirt_ar:
    $ Jean.change_face("pleased2")

    pause 0.5

    $ Jean.change_face("smirk1", blush = 1) 

    ch_Jean "Well. . . I'm not gonna dispute that. . ."

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "But. . . I mean, it's not like I'm all that much smarter than you."

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 

    ch_Jean "And I do have to try pretty hard."
    ch_Jean "Unlike you, where everything comes so easily."

    call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1231
    call change_Companion_stat(Jean, "trust", 0) from _call_change_Companion_stat_1232

    return

label Jean_flirt_b:
    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        ch_Player "If I had a dollar for every IQ point you have, I'd be a millionaire."

        $ Jean.change_face("confused1", mouth = "smirk") 

        ch_Jean "A pickup line, really?"

        $ Jean.change_face("smirk2")

        ch_Jean "At least it wasn't about my ass or something. . ."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1233
    elif dice_roll == 2:
        ch_Player "Math isn't my best subject, but even I know you're a perfect 10."

        $ Jean.change_face("perplexed") 

        pause 0.5

        $ Jean.change_face("confused1")

        ch_Jean "Well, you're not wrong. . . but seriously?"

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1234
    elif dice_roll == 3:
        ch_Player "By the way, are you a model?"

        $ Jean.change_face("confused1", mouth = "smirk") 

        ch_Jean "No. . ."
        ch_Player "Oh, when did you quit?"

        $ Jean.change_face("pleased2", blush = 1)

        pause 1.0

        $ Jean.change_face("confused1", mouth = "smirk")

        ch_Jean "Heh, at least it was funny."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1235
    elif dice_roll == 4:
        ch_Player "You don't happen to have a protractor on you, do you?"

        $ Jean.change_face("confused1") 

        ch_Jean "I don't, sorry."
        ch_Player "It's fine, I don't need one to know you're acute-y."

        $ Jean.change_face("pleased1")

        pause 0.5

        $ Jean.change_face("confused1", mouth = "smirk")

        ch_Jean "Ugh, really?"
        ch_Jean "That was so bad I actually kinda liked it. . ."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1236

    return

label Jean_flirt_c:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Jean.change_face("pleased2", blush = 1)

        pause 0.5

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "Oh, hey. . ."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1237 
    elif dice_roll == 2:
        $ Jean.change_face("confused1", mouth = "smirk", blush = 1) 

        ch_Jean ". . . Need something?"
        ch_Player "No, sorry. Just got lost in your eyes there for a second. . ."

        $ Jean.change_face("pleased2", blush = 1) 

        pause 0.5

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "Oh. . ."

        $ Jean.change_face("smirk2", mouth = "lipbite", eyes= "left", blush = 1)

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1238

    return

label Jean_flirt_d:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        ch_Jean "Yes!"

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "Heh, I mean. . . sure."
        "You gently grasp her hand."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1239
    elif dice_roll == 2:
        ch_Jean "Of course we can."

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        "She reaches out and takes your hand, interlacing her fingers with yours."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1240
    elif dice_roll == 3:
        ch_Jean "C'mere. . ."

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        "She takes your hand and gives it a light squeeze."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1241

    return

label Jean_flirt_ea:
    "She gives you a quick peck."
    ch_Jean "Ask for a real kiss next time."

    $ Jean.change_face("smirk2", mouth = "lipbite")

    call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1242

    return

label Jean_flirt_eb:
    if Player.location in public_locations and approval_check(Jean, threshold = [100, 50]):
        $ Jean.change_face("smirk2", eyes = "left", mouth = "lipbite", blush = 1) 

        ch_Jean "Screw it. . ." 

        $ Jean.change_face("kiss1", blush = 1) 

        "She pulls you into a brief kiss before pulling away." 

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Jean "You can bet there will be more later. . ." 

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1243
    elif Player.location in public_locations:
        $ Jean.change_face("worried1", eyes = "left", mouth = "lipbite", blush = 1) 

        ch_Jean "I really wanna. . ." 
        ch_Jean "Later, when there aren't so many people around." 

        $ Jean.change_face("worried1", blush = 1)
    elif Jean.quirk:
        $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 

        ch_Jean "Want a kiss from your big sister?"

        $ Jean.change_face("sly", brows = "cocked", mouth = "lipbite", blush = 1)

        ch_Jean "Well, what do you say?"
        ch_Player "Please. . ."

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 2)

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1244
        call change_Companion_stat(Jean, "desire", 0) from _call_change_Companion_stat_1245

        $ Jean.change_face("kiss2", blush = 2)  

        "After a quick kiss, she pulls away." 

        $ Jean.change_face("sexy", blush = 2)
    else:
        $ Jean.change_face("pleased2", mouth = "lipbite", blush = 1) 

        ch_Jean "Want a kiss, huh?"

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1246 

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

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1249
    elif Player.location in public_locations:
        $ Jean.change_face("confused1", eyes = "left") 

        pause 0.5

        $ Jean.change_face("smirk2") 

        ch_Jean "Fine. . ." 
        ch_Jean "But only a quick one."

        $ Jean.change_face("worried1")

        ch_Jean "PDA isn't really my kinda thing. . ."
        $ Jean.change_face("worried1", eyes = "closed")

        "She pulls you into a hug, giving you a quick squeeze before letting go."

        $ Jean.change_face("smirk2")

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1250
    elif approval_check(Jean, threshold = [50, 25]):
        $ Jean.change_face("pleased2", blush = 1) 

        ch_Jean "I love hugging you." 

        $ Jean.change_face("smirk2", eyes = "closed", blush = 1) 

        "Without another word, she pulls you into her arms." 
        "She squeezes you tightly, and holds the embrace for a long moment." 

        $ Jean.change_face("smirk2", blush = 1)

        ch_Jean "Could you. . . hug me more often?" 

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1251
    else:
        $ Jean.change_face("pleased2")

        pause 0.5

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "Yeah. . ."
        ch_Jean "C'mere."

        $ Jean.change_face("smirk2", eyes = "closed", blush = 1) 

        "She wraps her arms around you and squeezes gently." 

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "That was nice. . ." 

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1252

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

    call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1253

    return

label Jean_flirt_h:
    if approval_check(Jean, threshold = [175, 150]):
        $ Jean.change_face("pleased2", blush = 1)

        pause 0.5

        $ Jean.change_face("smirk2", eyes = "closed", mouth = "lipbite", blush = 1) 

        "You run your hand through [Jean.name]'s hair."
        "She leans into it, and holds your hand against her head for a moment." 

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "I like when you do that." 

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1254
    else:
        $ Jean.change_face("surprised2", blush = 1) 

        "You run your hand through [Jean.name]'s hair, causing her to shudder slightly." 

        $ Jean.change_face("worried1", eyes = "closed", blush = 1)

        "She shudders slightly."

        $ Jean.change_face("worried1", blush = 1)

        ch_Jean "That was. . . interesting"

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1255

    return

label Jean_flirt_i:
    if Player.location in public_locations and approval_check(Jean, threshold = [125, 125]):
        $ Jean.change_face("pleased1")

        pause 0.5

        $ Jean.change_face("smirk2", blush = 1) 

        "You wrap your arm around [Jean.name] and she turns to hug you." 

        $ Jean.change_face("smirk2", eyes = "closed", blush = 1) 

        ch_Jean "If you wanted a hug, you should've just said so. . ." 
        "After a moment, she pulls away." 

        $ Jean.change_face("smirk2", blush = 1)

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1256
    elif Player.location in public_locations:
        $ Jean.change_face("perplexed")

        pause 0.5

        $ Jean.change_face("confused2", eyes = "right")

        pause 0.5

        $ Jean.change_face("confused1", blush = 1) 

        "As you wrap your arm around [Jean.name], she stiffens, and pulls away." 

        $ Jean.change_face("worried1", blush = 1) 

        ch_Jean "Sorry. . . I just. . ." 
        ch_Jean "I don't mind, if it's you. . . but not around here." 
    elif approval_check(Jean, threshold = [125, 125]):
        $ Jean.change_face("pleased1", blush = 1) 

        pause 0.5

        $ Jean.change_face("kiss1", blush = 1)

        "As you wrap an arm around [Jean.name], she turns and kisses you." 

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1257

        $ Jean.change_face("kiss2", blush = 2)
    else:
        $ Jean.change_face("surprised2")

        pause 0.5

        $ Jean.change_face("pleased1", blush = 1) 

        "As you wrap your arm around [Jean.name], she leans her head on your shoulder." 

        $ Jean.change_face("smirk2", eyes = "closed", blush = 1)

        ch_Jean "You're pretty comfy."
        "After a moment, she pulls away." 

        $ Jean.change_face("smirk2", blush = 1)

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1261

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

        pause 0.5

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

        call change_Companion_stat(Jean, "desire", 0) from _call_change_Companion_stat_1262

        $ Jean.change_face("sexy", blush = 1) 

        ch_Jean "Satisfied?" 

        $ Jean.change_face("sexy", eyes = "down", blush = 2) 

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1263
    elif Player.location in public_locations:
        $ Jean.change_face("perplexed")

        pause 0.5

        $ Jean.change_face("confused1")

        ch_Jean "Seriously?"
        ch_Jean "Why would I let you do that here of all places?"

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1264
    elif Jean.quirk:
        $ Jean.change_face("perplexed")

        pause 0.5

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

        call change_Companion_stat(Jean, "desire", 0) from _call_change_Companion_stat_1265

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

        pause 0.5

        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        call change_Companion_stat(Jean, "desire", 0) from _call_change_Companion_stat_1266

        ch_Jean "I enjoyed that. . ."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1267
    else:
        $ Jean.change_face("worried2")

        pause 0.5

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

        call change_Companion_stat(Jean, "desire", 0) from _call_change_Companion_stat_1268

        $ Jean.change_face("surprised2", mouth = "lipbite", blush = 2) 

        pause 0.5

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "That was pretty hard. . ." 

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1269

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

    call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1270
    call change_Companion_stat(Jean, "desire", 0) from _call_change_Companion_stat_1271

    $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 

    ch_Jean "That better turn into a real kiss later. . ."

    return

label Jean_flirt_ob:
    "As you walk up to her, she seems to realize your intentions." 
    "Before you can do anything, she grabs you, and pulls you into a deep kiss."

    $ Jean.change_face("kiss2", blush = 1) 

    call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1272
    call change_Companion_stat(Jean, "desire", 0) from _call_change_Companion_stat_1273

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

    call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1274
    call change_Companion_stat(Jean, "desire", 0) from _call_change_Companion_stat_1275 

    pause 0.5

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Jean "Really think so?"
    ch_Player "I do, you're the best." 

    $ Jean.change_face("worried1", blush = 1) 

    ch_Jean "I try my best to take good care of you. . ." 

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "You're a great little brother too."

    call change_Companion_stat(Jean, "desire", 0) from _call_change_Companion_stat_1276 

    return

label Jean_flirt_qb:
    $ Jean.change_face("pleased2", blush = 1) 

    call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1277
    call change_Companion_stat(Jean, "desire", 0) from _call_change_Companion_stat_1278

    pause 0.5

    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Jean "I know you're obsessed with your big sister."
    ch_Jean "You really are the luckiest." 

    $ Jean.change_face("sexy", eyes = "down", blush = 1) 

    ch_Jean "Plus, you're only saying that because I make sure to take good care of you. . ." 

    $ Jean.change_face("sexy", blush = 1) 

    ch_Jean "Doesn't mean I don't like being flattered. . ."

    call change_Companion_stat(Jean, "desire", 0) from _call_change_Companion_stat_1279

    return

label Jean_flirt_qc:
    $ Jean.change_face("confused2", mouth = "smirk", blush = 1) 

    call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1280
    call change_Companion_stat(Jean, "desire", 0) from _call_change_Companion_stat_1281

    pause 0.5

    $ Jean.change_face("sly", blush = 1)

    ch_Jean "Trying to earn brownie points, [Jean.Player_petname]?" 
    ch_Jean "Think that'll get me to stop teasing you?"

    $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 

    ch_Jean "I know you like the teasing." 

    $ Jean.change_face("sexy", eyes = "down", blush = 1) 

    ch_Jean "I can always tell." 

    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Jean "But, that doesn't mean you should stop expressing your thanks. . ."

    call change_Companion_stat(Jean, "desire", 0) from _call_change_Companion_stat_1282

    return

label Jean_flirt_r:
    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        $ Jean.change_face("happy", blush = 1)

        ch_Player "Just wanted to say that I love you."

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "Aw, I love you too!"

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1283
        call change_Companion_stat(Jean, "trust", 0) from _call_change_Companion_stat_1284
    elif dice_roll == 2:
        $ Jean.change_face("worried1", blush = 1)

        ch_Player "I love you, by the way."
        ch_Jean "You do. . . ?"

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "I mean of course you do."
        ch_Jean "I love you too, [Jean.Player_petname]."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1285
        call change_Companion_stat(Jean, "trust", 0) from _call_change_Companion_stat_1286
    elif dice_roll == 3:
        $ Jean.change_face("happy", blush = 1)

        ch_Player "Hey, I love you."

        $ Jean.change_face("kiss2", blush = 1)

        "She doesn't respond, just pulling you into a kiss."

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "I know, I love you too, [Jean.Player_petname]."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1287
        call change_Companion_stat(Jean, "trust", 0) from _call_change_Companion_stat_1288
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

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1289
        call change_Companion_stat(Jean, "trust", 0) from _call_change_Companion_stat_1290

    return