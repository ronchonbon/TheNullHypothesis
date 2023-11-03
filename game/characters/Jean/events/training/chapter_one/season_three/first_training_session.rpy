init python:

    def Jean_chapter_one_season_three_first_training_session():
        label = "Jean_chapter_one_season_three_first_training_session"

        conditions = [
            "season == 3",
            "not Jean.History.check('trained_with_Player', tracker = 'season')",
            "Player.training == Jean and Jean.training"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Jean_chapter_one_season_three_first_training_session:
    $ ongoing_Event = True

    $ Jean.change_face("angry1")

    ch_Player "Are you okay. . . ?"
    ch_Jean "Ugh, no."
    ch_Jean "I'm still mad at you for almost dying again."
    ch_Jean "Especially when It's only been a few months since the last time!"

    menu:
        extend ""
        "I'm not thrilled about it either. . . but if anything, I'm stronger for it now.":
            $ Jean.change_face("worried1")

            ch_Jean "If that's what it takes for you to get stronger. . ." 
            
            $ Jean.change_face("worried1", eyes = "right") 
            
            ch_Jean "Just let me be strong enough for the both of us. . ." 
            
            call change_Girl_stat(Jean, "love", 5) from _call_change_Girl_stat_184
            call change_Girl_stat(Jean, "trust", 5) from _call_change_Girl_stat_185
        "How do you think I feel?! This time was much worse too. . .":
            $ Jean.change_face("worried2")

            ch_Jean "I'm just glad you're okay. . . and maybe with this new ability of yours, next time won't be so bad. . ." 
            
            $ Jean.change_face("worried1", eyes = "right") 
            
            ch_Jean "I hope there isn't a next time." 
            
            call change_Girl_stat(Jean, "love", 10) from _call_change_Girl_stat_186
        "If I can get over it, so can you. Plus, it only made me stronger in the end.":
            $ Jean.change_face("angry1", eyes = "right")

            ch_Jean "Ugh, at least you're making it easier to not feel bad for you." 
            
            $ Jean.change_face("worried1", eyes = "right") 
            
            ch_Jean "Not by much. . ." 
            
            call change_Girl_stat(Jean, "love", -5) from _call_change_Girl_stat_187 
            call change_Girl_stat(Jean, "trust", 5) from _call_change_Girl_stat_188

    $ Jean.change_face("confused1")

    ch_Jean "What the hell's the deal with this new ability of yours anyway?"
    ch_Jean "It hasn't been too difficult keeping it off, right?"
    ch_Player "Not really, seems like getting it to turn off was the hard part."
    ch_Player "It also feels distinct. . . like it's separate from my nullification."

    $ Jean.change_face("angry1")

    ch_Jean "This better not be a thing with you. . ."
    ch_Jean "Having to almost die in order to get stronger."

    $ Jean.change_face("worried1")

    ch_Jean "I kinda think it might be, though."
    ch_Player "You do?"
    ch_Jean "Yeah, I've been giving it some thought since last time."
    ch_Jean "First it was your healing thing, and now this."
    ch_Jean "What if they're, like, a response to getting hurt."

    $ Jean.change_face("worried2")

    ch_Jean "Your power figures out a way to grow, in order to keep you alive. . ."
    ch_Player "Well, shit. . . that would kinda suck. . ."

    $ Jean.change_face("worried1")

    ch_Jean "It's just a theory, and it also doesn't entirely explain everything."
    ch_Jean "Like why wouldn't it improve your current healing ability, instead of giving you this absorption thing."
    ch_Player "I. . . might have an idea about that. . ."

    $ Jean.change_face("confused1")

    menu:
        extend ""
        "It has to do with who my friends are.":
            $ Jean.change_face("confused2")

            ch_Player "Well, the fact that they're all mutants." 
            
            $ Jean.change_face("confused1") 
            
            call change_Girl_stat(Jean, "trust", 5) from _call_change_Girl_stat_189
        "It has to do with me being scared shitless.":
            $ Jean.change_face("worried2")

            ch_Player "Well. . . actually not really. . ." 
            
            $ Jean.change_face("confused1")
        "It has to do with women.":
            $ Jean.change_face("perplexed")

            ch_Player "I mean. . . in a way. . ." 
            
            $ Jean.change_face("confused1")

    ch_Jean "What are you talking about?"
    ch_Player "So, I noticed a pattern."

    $ Jean.change_face("worried1")

    ch_Player "Both times, when I got messed, I had other people's power in mind when it happened."

    $ Jean.change_face("surprised3")

    ch_Player "During the Juggernaut thing, I was thinking about how useful a healing ability like [Laura.name]'s would be."
    ch_Player "And now, with these Sentinels, I was thinking about Rogue."
    ch_Player "Where she can steal someone else's strength. . ."

    $ Jean.change_face("surprised2")

    ch_Jean "So you think. . ."
    ch_Player "Yeah. . . my own power took inspiration. . . and now I'm like this."

    $ Jean.change_face("confused1")

    ch_Jean "Huh. . ."
    ch_Jean "Well, that could be it. . ."
    ch_Player "Doesn't really explain my nullification. . . but it's the best I've got."

    $ Jean.change_face("smirk1")

    ch_Jean "I don't really think we're gonna get anywhere with all this speculation, let's get to the training, okay?"
    ch_Player "Good idea."

    $ Jean.change_face("confused1")

    ch_Jean "Since you said the new power feels like its own thing, can you try only turning your nullification back on?"

    $ Jean.change_face("confused1", mouth = "smirk")

    ch_Jean "I think you should see X-23 about training the new thing. . ."
    ch_Player "Probably for the best."
    ch_Player "Here, let me try."

    $ fade_to_black(0.4)

    "You close your eyes and look for the powers within you."
    "Just like you said, they're distinct from one another and have a significantly different feel."
    "One feels like it's hungry, as if it wants to take everything in."
    "The other feels the opposite, like it wants to stop anything from coming close."

    $ Player.power = 25
    
    "With some mental effort, you try only activating your nullification."

    show expression "images/effects/zing.webp" as zing onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    "You instantly feel a presence right in front of your face, followed by a thud."

    call Jean_activate_psychic from _call_Jean_activate_psychic_19

    $ fade_in_from_black(0.4)

    $ Jean.change_face("happy")

    ch_Jean "Looks like it worked!"
    "You look down and realize the thud was a tennis ball falling to the floor."

    $ Jean.change_face("smirk2")

    $ Player.power = 0

    call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_19

    ch_Jean "I was floating it right in front of your face, and you didn't even notice."
    ch_Player "When I did notice, it was much more apparent than before."

    $ Jean.change_face("confused1")

    ch_Jean "Oh?"
    ch_Player "Yeah, it felt clear and obvious where the tennis ball was, instead of barely perceptible."

    $ Jean.change_face("confused1", mouth = "smirk")

    ch_Jean "Hmm. . . and the new ability?"
    ch_Player "Feels fine."
    ch_Player "Doesn't seem like using one at a time is an issue."

    $ Jean.change_face("sly")

    ch_Jean "Let's test a few more things out."

    $ Player.power = 25

    $ fade_to_black(0.4)

    "You spend the next hour testing out your new control."
    "Turning the nullification on and off again gets easier each time you do it."
    "[Jean.name] even has you keep it off during sparring today, and she uses every advantage her powers can give her."
    "Despite your physical prowess, it's not even a contest."
    "By the end, she tries showing off her own progress, but loses control more than once."

    $ fade_in_from_black(0.4)

    $ Player.power = 0

    $ Jean.change_face("angry1", eyes = "right")

    ch_Jean "Goddamnit. . ."
    ch_Jean "You're doing so much better, and I'm barely any different."
    ch_Player "You sho-"

    $ Jean.change_face("angry1")

    ch_Jean "And don't tell me I shouldn't compare myself to you."
    ch_Jean "You can't understand how frustrating this is. . ."
    ch_Player ". . ."

    $ Jean.change_face("angry1", eyes = "right")

    pause 1.0

    $ Jean.change_face("worried1", eyes = "right")

    ch_Jean "I'm sorry."

    $ Jean.change_face("worried1")

    ch_Jean "I shouldn't be taking it out on you. . . just really stressed out lately. . ."
    ch_Player "It's okay, [Jean.petname]."

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Jean "Thanks, [Jean.Player_petname]."
    ch_Jean "I need to go study now, or something."
    ch_Jean "Anything to distract me."
    ch_Jean "I'll see you later."

    call remove_Characters(Jean) from _call_remove_Characters_57

    $ ongoing_Event = False

    return