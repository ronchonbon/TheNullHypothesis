init python:

    def Laura_first_friend_part_one():
        label = "Laura_first_friend_part_one"

        conditions = [
            "QuestPool.Quests['Laura_friendship_Quest'].completed",

            "Player.location == Player.home and not Present",

            "Laura.is_in_normal_mood()"]

        waking = True

        priority = 1

        return EventClass(label, conditions, waking = waking, priority = priority)

label Laura_first_friend_part_one:
    $ ongoing_Event = True

    $ fade_in_from_black(0.4)

    "You wake up and start getting ready as usual."

    call knock_on_door(times = 4, intensity = 2.0) from _call_knock_on_door_10
    
    "You hear someone start banging on your door."
    ch_Player "Gimme a sec!"
    "The banging continues, if less forcefully."
    "You go over and open the door. [Laura.name] is there and pushes her way in."
    ch_Player "Uh, you can come in. . ."

    $ Laura.blush = 1

    call send_Characters(Laura, Player.home) from _call_send_Characters_108

    ch_Laura "Be my friend."
    ch_Player "Your friend? Wait, where's this coming from?"

    $ Laura.blush = 0

    ch_Laura "It's been made clear through our combat lessons that my upbringing was very. . . non-standard."

    $ Laura.change_face("confused1")

    ch_Laura "You've talked about having 'family' and so-called 'friends.'"

    $ Laura.change_face("angry1")

    ch_Laura "I was researching those terms, but I still don't understand. . ."
    
    $ Laura.change_face("smirk1")

    ch_Laura "So you will be my first friend and explain things to me."

    $ chatting = True
    $ asked_about_friend = False
    $ asked_about_Ororo = False
    $ asked_why_me = False
    $ asked_meaning = False

    while chatting:
        menu:
            extend ""
            "You've never had a friend before?" if not asked_about_friend:
                call Laura_first_friend_part_one_1A from _call_Laura_first_friend_part_one_1A

                $ asked_about_friend = True
            "What about [Ororo.name]?" if asked_about_friend and not asked_about_Ororo:
                call Laura_first_friend_part_one_1B from _call_Laura_first_friend_part_one_1B

                $ asked_about_Ororo = True
            "Why me?" if not asked_why_me:
                $ Laura.change_face("neutral", blush = 1)

                ch_Laura "Other than [Ororo.public_name], I've interacted with you the most."
                ch_Laura "You're still weak, but at least you show some fortitude."

                $ Laura.eyes = "down"

                pause 1.0

                $ Laura.eyes = "neutral"

                call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_360

                $ Laura.change_face("smirk1", blush = 0)

                ch_Player "You don't really give me much choice during our lessons. . ."

                $ asked_why_me = True
            "So, you don't really know what it means to be a friend?" if not asked_meaning:
                ch_Laura "I know the word, but apparently not the concept."

                $ Laura.change_face("confused1")

                ch_Laura "It's like a companion or ally, no?"
                ch_Player "I guess you can think of it that way, but it's more than just spending time together or having the same enemies."
                ch_Player "Friends help each other out, even if it's not for personal gain."
                ch_Player "They also usually {i}enjoy{/i} spending time together and care about what happens to each other."

                $ Laura.change_face("perplexed")

                call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_361

                ch_Laura "I. . . don't fully understand, but I will try to {i}care{/i}."

                $ asked_meaning = True
            "Sure, I can be your friend.":
                $ Laura.change_face("pleased2")
                
                pause 1.0

                $ Laura.change_face("smirk2")

                ch_Laura "Good. Now that we are friends, you will answer this other question I have."

                $ Laura.change_face("neutral")

                $ chatting = False

    $ Laura.change_face("confused1")

    ch_Laura "What is the difference between 'friend,' and 'boy/girlfriend?'"
    ch_Laura "Since you are a boy and I am a girl, are we now 'boyfriend' and 'girlfriend?'"
    ch_Player "Oh boy. . ."

    $ Laura.change_face("perplexed")

    ch_Player "No, we are both only 'friends'. . . for now."

    $ Laura.change_face("angry1")

    ch_Player "I really think you should focus on just figuring out 'friend' for the time being."
    ch_Laura "Fine. Goodbye."

    call remove_Characters(Laura) from _call_remove_Characters_106
    
    ch_Player "Bye. . ."

    $ ongoing_Event = False
    
    return

label Laura_first_friend_part_one_1A:
    $ Laura.change_face("confused1")

    ch_Laura "I. . . only ever knew the doctors and scientists at the facility I was created in."
    ch_Laura "None of them fit the definition of 'friend.'"
    ch_Laura "There was one woman and her family. . . but they're. . ."

    $ Laura.change_face("angry1")

    ch_Laura ". . . never mind."

    $ Laura.change_face("angry2")

    menu:
        extend ""
        "I'm sorry, that must've been tough. . .":
            $ Laura.change_face("confused1")

            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_362

            ch_Laura "Why are you sorry?"
        "Makes sense, why you're. . .":
            $ Laura.change_face("confused1")

            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_363

            ch_Laura "Why I'm what?"
            ch_Player "Nothing. . ."

    return

label Laura_first_friend_part_one_1B:
    $ Laura.change_face("neutral")

    ch_Laura "After I escaped from the facility, I saved some people. . . fought many others. . . and came straight to the school."

    $ Laura.change_face("angry1")

    ch_Laura "I never knew anyone on the outside before, and [Ororo.public_name] tried to help."
    ch_Laura "Even after I tried to kill. . ."

    $ Laura.change_face("worried1")

    pause 1.0

    $ Laura.change_face("angry2")

    ch_Laura "I think that means she. . . cares about me. . . but I don't know how to care about her."

    $ Laura.change_face("confused1")

    menu:
        extend ""
        "I can try to help you learn.":
            $ Laura.change_face("surprised2")

            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_364
            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_365

            ch_Laura "So you are my friend now?"
        "Are you even capable of that?":
            $ Laura.change_face("angry1")

            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_366
            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_367

            ch_Laura "I. . . don't know."

    return

init python:

    def Laura_first_friend_part_two():
        label = "Laura_first_friend_part_two"

        conditions = [
            "EventScheduler.Events['Laura_first_friend_part_one'].completed",
            
            "Laura.location != Player.location and not get_Present(location = Player.destination)",
            
            "time_index >= 3",

            "Laura.is_in_normal_mood()"]

        waiting = True
        traveling = True

        priority = 1

        return EventClass(label, conditions, waiting = waiting, traveling = traveling, priority = priority)

label Laura_first_friend_part_two:
    $ ongoing_Event = True

    call receive_call(Laura, dialogue = f"Your phone starts buzzing - it's a call from {Laura.name}.") from _call_receive_call

    ch_Laura "Meet me in your room, now."
    ch_Player "Wh. . ."
    "*click*"
    "She hung up."

    call end_call(Laura) from _call_end_call

    if Player.location != Player.home:
        "You head over to your room."

        call remove_Characters(location = Player.home, fade = False) from _call_remove_Characters_107
        call set_the_scene(location = Player.home) from _call_set_the_scene_127

    call knock_on_door(times = 4, intensity = 2.0) from _call_knock_on_door_11

    "You wait for a couple minutes before someone starts banging on your door."
    "You open the door, and [Laura.name] pushes her way in again."

    $ Laura.change_face("appalled2", blush = 2)

    call send_Characters(Laura, Player.home) from _call_send_Characters_109

    ch_Player "What's wrong?"
    ch_Laura "I was doing more research. . . on 'boy/girlfriends.'"

    $ Laura.change_face("appalled1", blush = 1)

    ch_Laura "There was a video. . ."
    ch_Player "Uh oh."
    ch_Laura "They were touching each other's lips. . . and. . ."

    $ Laura.change_face("angry1", blush = 2)

    call change_Girl_stat(Laura, "desire", 0) from _call_change_Girl_stat_368

    ch_Laura "I stopped it when the female started removing her clothes."

    $ Laura.change_face("suspicious2", blush = 1)

    ch_Laura "How can two people make themselves so vulnerable with each other?"

    $ chatting = True
    $ explained_platonic = False

    while chatting:
        menu:
            extend ""
            "Explain the difference between platonic friends and relationships" if not explained_platonic:
                call Laura_first_friend_part_two_1A from _call_Laura_first_friend_part_two_1A

                $ explained_platonic = True
            "Recommend she talk to [Rogue.name] about it":
                ch_Player "I think it would probably be better for you to talk to another girl about this. . ."

                $ Laura.change_face("confused1")

                call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_369

                ch_Player "You should go see [Rogue.name], she's very nice, and I'm sure she wouldn't mind answering some questions."

                $ chatting = False

    $ Laura.change_face("neutral", blush = 1)

    ch_Laura "I will. . . talk to Rogue."
    ch_Laura "Goodnight."

    call remove_Characters(Laura) from _call_remove_Characters_108

    pause 1.0

    $ fade_to_black(0.4)

    pause 2.0

    $ fade_in_from_black(0.4)

    call receive_call(Rogue, dialogue = "As you're getting ready for bed, you get another call on your phone.") from _call_receive_call_1
    
    ch_Rogue "Hon', why did [Laura.public_name] march into my room and demand ah be her friend?"
    ch_Player "Heh, sorry about that."
    ch_Player "She had some questions about stuff that I thought might be better discussed with another girl. . ."
    ch_Player "She can be a bit rough around the edges, but she means well."

    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_370

    ch_Rogue ". . . Well ain't that sweet. Don't worry, ah'll help her out."
    ch_Player "Thanks, [Rogue.name]."
    ch_Rogue "Night hon'."

    call end_call(Rogue) from _call_end_call_1

    "It's getting late, so you go to sleep."

    if Rogue.likes[Laura] < Rogue_thresholds["friendship"][1]:
        $ Rogue.likes[Laura] = Rogue_thresholds["friendship"][1]

    if Laura.likes[Rogue] < Laura_thresholds["friendship"][1]:
        $ Laura.likes[Rogue] = Laura_thresholds["friendship"][1]

    call get_ready_for_bed from _call_get_ready_for_bed

    $ ongoing_Event = False
    
    return

label Laura_first_friend_part_two_1A:
    $ Laura.change_face("perplexed", blush = 0)

    ch_Player "Boyfriends and girlfriends trust each other, and some people enjoy doing things like that."
    ch_Laura "But why would they want to?"
    ch_Laura "It's completely counterintuitive to what scientists at the facility ingrained in me. . ."

    $ Laura.change_face("confused1")

    ch_Laura "The only time I've ever been near a man was when I had to. . . eliminate them."
    ch_Player "[Laura.name], the facility tried making you into a killing machine."
    ch_Player "They probably wanted to remove all your {i}human{/i} thoughts and feelings."
    ch_Player "Some people want to touch each other because it usually feels good - it's called sexual attraction."

    $ Laura.change_face("suspicious2", blush = 2)

    ch_Laura "Is that why I've felt the urge to touch you again since our first combat lesson?"
    ch_Laura "And why your scent is so. . . 'pleasing' to me?"

    $ Laura.blush = 3

    ch_Laura "Everyone else smells terrible in comparison. . ."

    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_371
    call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_372
    call change_Girl_stat(Laura, "desire", 0) from _call_change_Girl_stat_373

    ch_Player "{i}Ahem{/i}. . ."

    return

init python:

    def Laura_first_friend_part_three():
        label = "Laura_first_friend_part_three"

        conditions = [
            "day - EventScheduler.Events['Laura_first_friend_part_two'].completed_when > 2",

            "approval_check(Laura, threshold = 'dating')",
            
            "'bg_shower' not in Player.destination",
            "Player.destination not in bedrooms or 'bg_shower' not in Player.location",
            "not get_Present(location = Player.destination)",
            
            "time_index >= 3",

            "Laura.is_in_normal_mood()"]

        traveling = True

        priority = 1

        return EventClass(label, conditions, traveling = traveling, priority = priority)

label Laura_first_friend_part_three:
    $ ongoing_Event = True

    "As you walk through the halls of the mansion, you hear faint footsteps behind you."
    "You turn around, but it's too dark to see anything."
    "Must be your imagination."

    call remove_Characters(location = "bg_hallway", fade = False) from _call_remove_Characters_109
    call set_the_scene(location = "bg_hallway") from _call_set_the_scene_128

    "You get to your room and unlock the door."
    "You hear the footsteps again, but before you can even turn around. . ."

    $ Laura.destination = "bg_hallway"
    $ Laura.location = "bg_hallway"
    $ Laura.change_face("angry1")

    $ reset_behavior(Laura)
    
    call set_Character_Outfits(Laura) from _call_set_Character_Outfits_3

    call show_Character(Laura, x = stage_center, sprite_layer = 6, fade = False) from _call_show_Character_1

    ch_Player "Gah! What the fu. . ."
    ch_Laura "We are going to talk."
    "[Laura.name] appears suddenly and pushes your room open, dragging you inside."

    call set_the_scene(location = Player.home) from _call_set_the_scene_129
    call send_Characters(Laura, location = Player.home, behavior = False) from _call_send_Characters_258

    $ Laura.change_face("perplexed")

    ch_Player "What the hell, were you following me??"
    ch_Laura "Of course. Why were you startled?"

    $ Laura.change_face("confused1")

    pause 1.0

    $ Laura.change_face("angry1")

    ch_Laura "Is something wrong?"

    $ Laura.change_face("perplexed")

    ch_Player "Everything's fine, I'm startled because you came out of nowhere. . ."

    $ Laura.change_face("confused1")

    ch_Laura ". . . Why? We're friends, you should be at ease in my presence."

    $ Laura.change_face("neutral")

    ch_Player "I'll. . . explain later."
    ch_Player "What's this about?"

    $ Laura.change_face("neutral", eyes = "right", blush = 1)

    ch_Laura "I talked to [Rogue.public_name] as you suggested, about. . . {i}things{/i}."

    $ Laura.eyes = "neutral"

    ch_Player "'Things?'"
    ch_Laura "Things like what 'attraction' is."

    $ Laura.blush = 2

    ch_Laura "Or what the term 'crush' means."

    if approval_check(Rogue, "love", threshold = Rogue_thresholds["dating"][0]):
        $ Laura.change_face("confused1", blush = 1)

        ch_Laura "She also had a lot to say about you."
        ch_Player "Good things, I hope."

        $ Laura.change_face("suspicious2", blush = 0)

        call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_374
        call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_375

        ch_Laura "Very good things. . ."
        "[Laura.name] stares at you skeptically."
        ". . ."
        "It's starting to get uncomfortable."
        ch_Laura "Hmm. . ."

    $ Laura.change_face("neutral", eyes = "squint", blush = 1)

    ch_Laura "According to the criteria. . . I have a 'crush' on you."

    $ Laura.change_face("confused1")

    ch_Laura "Does that make you my 'boyfriend?'"

    $ Laura.change_face("angry1", blush = 0)

    ch_Laura "I still don't get these terms."

    $ chatting = True
    $ denied_boyfriend = False
    $ asked_stalking = False
    $ asked_crush = False
    $ said_crush = False

    while chatting:
        menu:
            extend ""
            "That doesn't make me your boyfriend. . ." if not denied_boyfriend:
                call Laura_first_friend_part_three_1A from _call_Laura_first_friend_part_three_1A

                $ denied_boyfriend = True
            "Why did you stalk me here?" if not asked_stalking:
                call Laura_first_friend_part_three_1B from _call_Laura_first_friend_part_three_1B
                
                $ asked_stalking = True
            "You have a crush on me?" if not asked_crush:
                $ Laura.change_face("angry1", blush = 1)

                ch_Laura "According to Rogue's definition. . ."
                ch_Laura "I've never experienced feelings like these before."

                $ Laura.eyes = "squint"

                ch_Laura "First the '{i}attraction{/i}' after we met, and I touched you the first time."
                ch_Laura "Even just your scent. . . makes me feel things."
                ch_Laura "Then you actually turned out to not be a wimp like everyone else at this school."

                $ Laura.blush = 2

                ch_Laura "Before you, no one could withstand my training for more than a session or two."

                $ Laura.change_face("furious", blush = 3)

                ch_Laura "There are other reasons for the 'crush'. . . that you don't need to know."

                $ asked_crush = True
            "I have a 'crush' on you too." if asked_crush and not said_crush:
                $ Laura.change_face("perplexed", blush = 1)

                ch_Laura "And this still doesn't mean you're my boyfriend?"
                ch_Player "No. . ."
                ch_Player "Like I said, there's still a few steps before we get there."

                $ Laura.change_face("confused1")

                ch_Laura "Tell me the next step."
                ch_Player "Well, we spend more time together. Get to know each other."
                ch_Player "People usually go on what's called a 'date.'"
                ch_Player "And don't worry, there's no expectation that we'll do anything like what you saw in that {i}video{/i} after a date."
                ch_Player "That comes later on if we're both ready."

                $ Laura.change_face("neutral")

                ch_Laura "Good."

                $ said_crush = True
                $ chatting = False

    $ Laura.change_face("smirk1")

    ch_Laura "Then we are going on this 'date.'"

    $ Laura.change_face("angry2")

    ch_Player "Do you even know what it entails?"

    $ Laura.blush = 1

    ch_Laura "I will look it up."
    ch_Laura "Text me when you're ready."

    $ Laura.change_face("neutral")

    ch_Player "Okay, okay, I will."
    ch_Laura "That is all."
    ch_Laura "Goodnight."

    call remove_Characters(Laura) from _call_remove_Characters_110

    $ Laura.text_options.insert(0, "ready for that date?")
    
    call get_ready_for_bed from _call_get_ready_for_bed_1

    $ ongoing_Event = False
    
    return

label Laura_first_friend_part_three_1A:
    menu:
        extend ""
        ". . . {i}{size=-5}yet{/size}{/i}.":
            $ Laura.change_face("suspicious2")

            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_376
        ". . .":
            pass

    ch_Player "Normally, 'boyfriend' would mean we're in a relationship."
    ch_Player "Starting a relationship is an entire process past friendship."

    $ Laura.change_face("confused1")

    ch_Laura "Explain."
    ch_Player "Fine, a relationship is like a mutual contract. . . of sorts."
    ch_Player "It starts with mutual attraction, or a 'crush.'"
    ch_Player "Then the attraction might turn into something more, like an emotional connection."

    $ Laura.change_face("neutral")

    ch_Laura "What causes it to turn into something more?"

    $ Laura.change_face("neutral", eyes = "squint")

    ch_Player "It happens naturally after people get to know each other."

    return

label Laura_first_friend_part_three_1B:
    $ Laura.change_face("perplexed")

    ch_Laura "Stalk?"

    $ Laura.change_face("confused1")

    ch_Laura "I've been following and watching you ever since we became friends, to protect you."
    ch_Player "Watching me?"

    $ Laura.change_face("neutral")

    ch_Laura "On the security monitors."
    
    $ Laura.change_face("confused1")

    ch_Laura "Do friends not normally watch over and protect each other?"

    menu:
        extend ""
        "I appreciate it. . . but no, that's not how friends normally do it. (discourage_quirk)":
            $ Laura.change_face("surprised1", blush = 1)

            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_377

            ch_Laura "You want me to stop?"
            ch_Player "You don't have to {i}constantly{/i} watch over me."
            ch_Player "But that doesn't mean friends won't still help and protect each other."
            ch_Laura "Fine."
        
            $ Laura.change_face("neutral")
            
            $ Laura.History.update("quirk_discouraged")
        "Uhh. . . no. That's kind of weird. (discourage_quirk)":
            $ Laura.change_face("angry1")

            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_378

            ch_Laura "Fine, then I will stop."
            ch_Player "Friends still help and protect each other."
            ch_Player "But in less. . . overbearing ways."

            $ Laura.change_face("neutral")
            
            $ Laura.History.update("quirk_discouraged")
        "Not normally in that way. . . but I like it. (encourage_quirk)":
            ch_Player "Knowing someone as capable as you is watching my back. . ."

            $ Laura.change_face("pleased1", blush = 1)

            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_379
            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_380

            ch_Laura "Good."

            $ Laura.change_face("smirk2")

            ch_Laura "I didn't plan on stopping."
            ch_Player ". . . Unless it's inconvenient for you."
            ch_Laura "It's not."

            $ Laura.change_face("smirk1", eyes = "squint", blush = 2)

            ch_Laura "I think this 'crush' also makes me. . . want to do it."

            $ Laura.History.update("quirk_encouraged")

    return