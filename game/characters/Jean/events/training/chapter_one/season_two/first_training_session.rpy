init python:

    def Jean_chapter_one_season_two_first_training_session():
        label = "Jean_chapter_one_season_two_first_training_session"

        conditions = [
            "chapter == 1 and season == 2",

            "not Jean.History.check('trained_with_Player', tracker = 'season')",
            
            "Player.behavior == 'training' and Jean in Player.behavior_Partners and Jean.behavior == 'training'"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Jean_chapter_one_season_two_first_training_session:
    $ ongoing_Event = True
    
    $ Jean.change_face("worried1")
    
    ch_Player "You okay?"

    $ Jean.change_face("angry1")

    ch_Jean "I'm not the one who almost died."

    $ Jean.change_face("worried1")

    ch_Jean "I was just worried about you. . ."
    ch_Jean "Are {i}you{/i} okay?"

    menu:
        extend ""
        "I am, really. I appreciate your concern.":
            $ Jean.change_face("confused1", mouth = "smirk")

            ch_Jean "How could I not be concerned?" 
            
            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_198
            call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_199
        "Not really. . . but thanks for caring.":
            $ Jean.change_face("worried2")

            ch_Jean "Of course I care!" 
            
            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_200
        "I'm not dead so, yeah. . . mostly just pissed that I was so useless.":
            $ Jean.change_face("angry1")

            ch_Jean "You weren't useless!" 
            
            call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_201

    $ Jean.change_face("worried1")

    ch_Jean "What about your injuries?"
    ch_Jean "I thought they were pretty bad?"
    ch_Player "Physically, I feel better than ever."

    $ Jean.change_face("confused1")

    ch_Player "Xavier seems to think I have a 'robust constitution' as a by-product of my power or something."
    ch_Player "So, now I heal pretty fast."
    ch_Jean "Hmm. . ."
    ch_Jean "I guess you're in a similar situation as I was."
    ch_Player "How do you mean?"

    $ Jean.change_face("smirk1")

    ch_Jean "Well, at first, I thought my powers were only telepathic."
    ch_Jean "It wasn't until later that I figured out I also had telekinesis."
    ch_Jean "That's probably what's going on with you."

    $ Jean.change_face("smirk2")

    ch_Jean "Who knows what else you might be capable of, with my help." 
    ch_Jean "Okay, that's enough chit-chat."

    $ Jean.change_face("happy")

    ch_Jean "Time to hit you with tennis balls and see if anything's changed."

    call Jean_activate_psychic from _call_Jean_activate_psychic_27

    ch_Player "Wai-"

    $ fade_to_black(0.4)

    "Just as she promised, tennis balls come flying at you from every angle."
    "You try your hardest to shut the nullification down, despite the pain you'll likely feel by letting the balls hit you."
    "Your awareness of the ability inside you has increased, but your control is only marginally better."
    "Imposing your will on it feels like trying to keep hold of a wet bar of soap."
    "Just as you're about to get a grip, it slips through your fingers."

    $ fade_in_from_black(0.4)

    call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_27

    $ Jean.change_face("confused1")

    ch_Jean "Any easier today?"
    ch_Player "Actually yeah, a bit."
    ch_Player "It's like I'm more aware of the power, but still have a hard time getting hold of it."

    $ Jean.change_face("smirk2")

    ch_Jean "That's great!"
    ch_Jean "You're getting there."
    ch_Player "Gives me a bit of a headache, though. . ."

    $ Jean.change_face("worried1")

    ch_Jean "Aw, poor [Jean.Player_petname]."
    ch_Jean "Let's try something else."

    $ Jean.change_face("sly", blush = 1) 

    ch_Jean "We don't want you to hurt yourself."

    $ fade_to_black(0.4)

    "Apparently she isn't worried about hurting you herself, however."
    "You spend the next little while sparring with [Jean.name]."
    "She's surprised by your ability, and it seems like the training with [Laura.name] has paid off. . ."
    "Wait, was she always this slow?"

    $ fade_in_from_black(0.4)

    $ Jean.change_face("confused1", eyes = "squint")

    ch_Jean "Since when were you this strong. . . and fast?"

    if Laura.History.check("trained_with_Player") >= 5:
        ch_Jean "Sure your techniques and stuff are a lot better. . ."
    else:
        ch_Jean "Your technique still isn't even that great. . ."

    if Laura.History.check("trained_with_Player", tracker = "season"):
        ch_Player "Ever since this 'robust constitution' thing I guess. . . [Laura.name] tested me and it's like I'm on another level."
    else:
        ch_Player "I dunno. . . maybe it has to do with this new 'robust constitution' thing. . ."

    $ Jean.change_face("suspicious1")

    ch_Jean "Well, whatever it is. . ."

    $ Jean.change_face("smirk1")

    ch_Jean "Maybe now I won't have to worry about you so much."
    ch_Jean "It's impressive. . ."

    $ Jean.change_face("sly")

    ch_Jean "But still not as impressive as this. . ."

    call Jean_activate_psychic from _call_Jean_activate_psychic_28

    $ fade_to_black(0.4)

    "She proceeds to flaunt her powers, not holding back, seemingly in an attempt to one up you."
    "As if you needed reminding who the real powerhouse was. . ."
    "Despite the bravado, she still seems to struggle quite a bit with maintaining control."
    "At least you don't have to step in by the end."

    $ fade_in_from_black(0.4)

    call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_28

    $ Jean.change_face("angry1", eyes = "right")

    ch_Player "Why are you angry?"
    ch_Player "That was great!"
    ch_Player "You didn't even need my help."

    $ Jean.change_face("angry1")

    ch_Jean "Ugh!"
    ch_Jean "Because you're making leaps and bounds, while I'm over here barely crawling."

    $ Jean.change_face("worried1", eyes = "right")

    $ temp = Jean.petname.capitalize()

    menu:
        extend ""
        "[temp], I've just been stumbling through this, getting lucky. You're still far more impressive than I've ever been.":
            $ Jean.change_face("worried2")

            ch_Jean "You really think I'm impressive. . . ?" 
            
            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_202 
        "Okay, but it's not like I'll be catching up to you any time soon.":
            $ Jean.change_face("worried1")

            ch_Jean "I know, I know. . ." 
            
            call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_203
        "Oh please, you're probably the most powerful person I've ever met. So what if things aren't going fast enough for you.":
            $ Jean.change_face("angry1", eyes = "right")

            ch_Jean "You wouldn't get it. . ." 
            
            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_204

    $ Jean.change_face("worried1", eyes = "right")

    ch_Jean "I'm sorry for getting mad."

    $ Jean.change_face("worried1")

    ch_Jean "It's not like any of this is your fault."
    ch_Jean "You don't need me venting at you."
    ch_Jean "But I'm here if you need someone to vent to yourself, got it?" 

    $ Jean.change_face("confused1")

    $ temp = Jean.petname.capitalize()

    menu:
        extend ""
        "You shouldn't bottle your feelings up just for my sake. I'm here for you as well. . .":
            $ Jean.change_face("worried2")

            ch_Jean "But, I'm the one who's supposed to take care of you. . ." 
            
            $ Jean.change_face("worried1", mouth = "smirk") 
            
            ch_Jean "Thanks, [Jean.Player_petname]." 
            
            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_205 
            call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_206
        "I appreciate it. Might have to take you up on that. . . everything has been so stressful lately.":
            $ Jean.change_face("worried1", mouth = "smirk")

            ch_Jean "Any time, [Jean.Player_petname]. . ." 
            
            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_207
        "Thanks, I guess. . . I'll be fine.":
            $ Jean.change_face("angry1", eyes = "right")

            ch_Jean "Whatever. . ." 
            
            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_208

    $ Jean.change_face("smirk1")

    ch_Jean "That's enough for today, and I really need a shower." 
    ch_Jean "Catch you later."

    call remove_Characters(Jean) from _call_remove_Characters_60

    $ ongoing_Event = False

    return