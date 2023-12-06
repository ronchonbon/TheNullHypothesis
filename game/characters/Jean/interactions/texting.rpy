label Jean_texting(message):
    python:
        for E in Jean.timed_text_options.keys():
            for text in Jean.timed_text_options[E]:
                if message == text:
                    renpy.call(f"{E}_response")

    if Jean.timed_text_options:
        call Jean_text_ignored from _call_Jean_text_ignored

        $ Jean.timed_text_options = {}

    if message == "how are you?":
        $ selected_Event = EventScheduler.choose_Event(texting = True)

        if selected_Event:
            call start_Event(selected_Event) from _call_start_Event_1
        else:
            if time_index == 3:
                if approval_check(Jean, threshold = "talk_late"):
                    call Jean_text_how_are_you_late_accept from _call_Jean_text_how_are_you_late_accept
                else:
                    if approval_check(Jean, threshold = "friendship"):
                        call Jean_text_how_are_you_late_reject from _call_Jean_text_how_are_you_late_reject
                    else:
                        if Jean.History.check("said_too_late_to_text", tracker = "recent") == 1:
                            call Jean_text_how_are_you_late_reject_asked_once from _call_Jean_text_how_are_you_late_reject_asked_once
                        elif Jean.History.check("said_too_late_to_text", tracker = "recent") > 1:
                            call Jean_text_how_are_you_late_reject_asked_twice from _call_Jean_text_how_are_you_late_reject_asked_twice
                        else:
                            call Jean_text_how_are_you_late_reject from _call_Jean_text_how_are_you_late_reject_1

                    $ Jean.History.update("said_too_late_to_text")
            else:
                $ status = Jean.get_status()

                if status:
                    call expression f"Jean_text_how_are_you_{status}" from _call_expression_9
                elif approval_check(Jean, threshold = "love"):
                    call Jean_text_how_are_you_love from _call_Jean_text_how_are_you_love
                elif Jean in Partners:
                    call Jean_text_how_are_you_relationship from _call_Jean_text_how_are_you_relationship
                else:
                    call Jean_text_how_are_you from _call_Jean_text_how_are_you

        $ Jean.History.update("sent_how_are_you_text")

    if "good morning" in message:
        $ status = Jean.get_status()

        if status:
            call expression f"Jean_text_good_morning_{status}" from _call_expression_10
        elif approval_check(Jean, threshold = "love"):
            call Jean_text_good_morning_love from _call_Jean_text_good_morning_love
        elif Jean in Partners:
            call Jean_text_good_morning_relationship from _call_Jean_text_good_morning_relationship
        else:
            call Jean_text_good_morning from _call_Jean_text_good_morning

        $ Jean.History.update("sent_good_morning_text")

    if "goodnight" in message:
        $ status = Jean.get_status()

        if status:
            call expression f"Jean_text_goodnight_{status}" from _call_expression_11
        elif approval_check(Jean, threshold = "love"):
            call Jean_text_goodnight_love from _call_Jean_text_goodnight_love
        elif Jean in Partners:
            call Jean_text_goodnight_relationship from _call_Jean_text_goodnight_relationship
        else:
            call Jean_text_goodnight from _call_Jean_text_goodnight

        $ Jean.History.update("said_goodnight")

    if message == "wanna come over?":
        call summon(Jean) from _call_summon

    if message in ["want to go on a date tonight?", "free tonight for that date?"]:
        call Jean_text_ask_on_date from _call_Jean_text_ask_on_date

    return

label Jean_text_how_are_you:
    call receive_text(Jean, "Pretty good <3") from _call_receive_text_100
    call receive_text(Jean, "So much studying. . .") from _call_receive_text_101
    
    call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_255

    return

label Jean_text_how_are_you_late_accept:
    call receive_text(Jean, "Not bad") from _call_receive_text_102
    call receive_text(Jean, "Was planning on studying a bit more") from _call_receive_text_103
    call receive_text(Jean, "I guess I could just do it tomorrow if you wanted to talk <3") from _call_receive_text_104

    call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_256

    return

label Jean_text_how_are_you_late_reject:
    call receive_text(Jean, "Tired") from _call_receive_text_105
    call receive_text(Jean, "Gotta get up early tomorrow to study") from _call_receive_text_106

    return

label Jean_text_how_are_you_late_reject_asked_once:
    call receive_text(Jean, "I'm about to put my phone down") from _call_receive_text_107
    call receive_text(Jean, "Just text me tomorrow") from _call_receive_text_108

    return

label Jean_text_how_are_you_late_reject_asked_twice:
    call receive_text(Jean, "Stopppp!") from _call_receive_text_109
    call receive_text(Jean, "I'm going to bed") from _call_receive_text_110

    return

label Jean_text_how_are_you_relationship:
    call receive_text(Jean, "Way too busy") from _call_receive_text_111
    call receive_text(Jean, "Ughhh, I just want to hang out with you") from _call_receive_text_112

    call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_257

    return

label Jean_text_how_are_you_love:
    call receive_text(Jean, "I'm having [Player.first_name] withdrawal") from _call_receive_text_113
    call receive_text(Jean, "I know you miss me too") from _call_receive_text_114

    $ Jean.mandatory_text_options = ["we just saw each other, but yeah. . . I miss you", "you know I always miss you", "chill, I just saw you earlier"]
    $ temp = Jean.mandatory_text_options[:]

    while Jean.mandatory_text_options:
        pause

    if Jean.text_history[-1][1] == temp[0]:
        call receive_text(Jean, "I might just skip studying and come find you") from _call_receive_text_115
    elif Jean.text_history[-1][1] == temp[1]:
        call receive_text(Jean, "You better come by later <3") from _call_receive_text_116

        call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_258
    elif Jean.text_history[-1][1] == temp[2]:
        call receive_text(Jean, "Don't have to be an ass") from _call_receive_text_117

        call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_259

    return

label Jean_text_how_are_you_mad:
    call receive_text(Jean, "I'm angry") from _call_receive_text_118
    call receive_text(Jean, "If you couldn't tell") from _call_receive_text_119

    return

label Jean_text_how_are_you_hearbroken:
    call receive_text(Jean, "Fine") from _call_receive_text_120
    call receive_text(Jean, "Well") from _call_receive_text_121
    call receive_text(Jean, "Not fine") from _call_receive_text_122
    call receive_text(Jean, "Never mind") from _call_receive_text_123

    return

label Jean_text_how_are_you_horny:
    call receive_text(Jean, "I can't keep my mind off you") from _call_receive_text_124
    call receive_text(Jean, "Stop messing with my head!") from _call_receive_text_125
    call receive_text(Jean, "<3") from _call_receive_text_126
    
    call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_260

    return

label Jean_text_how_are_you_nympho:
    call receive_text(Jean, "I am NOT okay") from _call_receive_text_127
    call receive_text(Jean, "I'm all") from _call_receive_text_128
    call receive_text(Jean, "You know") from _call_receive_text_129
    call receive_text(Jean, "I need some attention") from _call_receive_text_130

    call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_261

    return

label Jean_text_good_morning:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Jean, "Morning! <3") from _call_receive_text_131
    elif dice_roll == 2:
        call receive_text(Jean, "Good morning to you too <3") from _call_receive_text_132
    elif dice_roll == 3:
        call receive_text(Jean, "Hey! <3") from _call_receive_text_133
        call receive_text(Jean, "It is a good morning, I slept great") from _call_receive_text_134

    call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_262

    return

label Jean_text_good_morning_relationship:
    call receive_text(Jean, "Morning [Jean.Player_petname]! <3") from _call_receive_text_135

    call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_263

    return

label Jean_text_good_morning_love:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        call receive_text(Jean, "Morning [Jean.Player_petname] <3") from _call_receive_text_136
        call receive_text(Jean, "I love you so much") from _call_receive_text_137

        call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_264
    elif dice_roll == 2:
        call receive_text(Jean, "Morning") from _call_receive_text_138
        call receive_text(Jean, "I had a dream where you. . .") from _call_receive_text_139
        call receive_text(Jean, "You still love me") from _call_receive_text_140
        call receive_text(Jean, "Right?") from _call_receive_text_141

        $ Jean.mandatory_text_options = ["yes", "more than ever, why?", "huh?"]
        $ temp = Jean.mandatory_text_options[:]

        while Jean.mandatory_text_options:
            pause

        if Jean.text_history[-1][1] == temp[0]:
            call receive_text(Jean, "Good <3") from _call_receive_text_142
        elif Jean.text_history[-1][1] == temp[1]:
            call receive_text(Jean, "Just bad dreams") from _call_receive_text_143

            call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_265
        elif Jean.text_history[-1][1] == temp[2]:
            call receive_text(Jean, "Whatever, never mind") from _call_receive_text_144

            call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_266

    return

label Jean_text_good_morning_mad:
    call receive_text(Jean, "Yeah, no") from _call_receive_text_145
    call receive_text(Jean, "Get a clue") from _call_receive_text_146

    return

label Jean_text_good_morning_hearbroken:
    call receive_text(Jean, "I guess so. . .") from _call_receive_text_147

    return

label Jean_text_good_morning_horny:
    call receive_text(Jean, "Hey there [Jean.Player_petname]") from _call_receive_text_148
    call receive_text(Jean, "You reading my mind or something?") from _call_receive_text_149
    call receive_text(Jean, "Was just thinking about you ;)<3") from _call_receive_text_150

    call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_267

    return

label Jean_text_good_morning_nympho:
    call receive_text(Jean, "Ugh why aren't you in bed with me rn") from _call_receive_text_151
    call receive_text(Jean, "Then it would be a great morning ;)") from _call_receive_text_152

    call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_268

    return

label Jean_text_goodnight:
    if Jean.behavior == "studying":
        $ dice_roll = renpy.random.randint(1, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        call receive_text(Jean, "Goodnight! <3") from _call_receive_text_153
    elif dice_roll == 2:
        call receive_text(Jean, "Night!") from _call_receive_text_154
        call receive_text(Jean, "Sweet dreams [Jean.Player_petname] <3") from _call_receive_text_155
    elif dice_roll == 3:
        call receive_text(Jean, "You're going to bed?") from _call_receive_text_156
        call receive_text(Jean, "I still have so much studying to do. . .") from _call_receive_text_157

    call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_269

    return

label Jean_text_goodnight_relationship:
    call receive_text(Jean, "Aw") from _call_receive_text_158
    call receive_text(Jean, "Goodnight!") from _call_receive_text_159

    call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_270

    return

label Jean_text_goodnight_love:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        call receive_text(Jean, "Goodnight [Jean.Player_petname]") from _call_receive_text_160
        call receive_text(Jean, "I love you <3") from _call_receive_text_161

        call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_271
    elif dice_roll == 2:
        call receive_text(Jean, "You're going to sleep?") from _call_receive_text_162
        call receive_text(Jean, "You should be in MY bed") from _call_receive_text_163

        $ Jean.mandatory_text_options = ["maybe some other day", "I know, I'm sorry. maybe tomorrow?", "then you shouldn't hog the damn blanket so much"]
        $ temp = Jean.mandatory_text_options[:]

        while Jean.mandatory_text_options:
            pause
        
        if Jean.text_history[-1][1] == temp[0]:
            pass
        elif Jean.text_history[-1][1] == temp[1]:
            call receive_text(Jean, "We'll see") from _call_receive_text_164
            call receive_text(Jean, "If you're good") from _call_receive_text_165
            call receive_text(Jean, "Don't worry, I still love you <3") from _call_receive_text_166

            call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_272
        elif Jean.text_history[-1][1] == temp[2]:
            call receive_text(Jean, "Ugh") from _call_receive_text_167
            call receive_text(Jean, "Whatever") from _call_receive_text_168

            call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_273

    return

label Jean_text_goodnight_mad:
    call receive_text(Jean, "How about no") from _call_receive_text_169
    call receive_text(Jean, "Not good") from _call_receive_text_170

    return

label Jean_text_goodnight_hearbroken:
    call receive_text(Jean, "Oh") from _call_receive_text_171
    call receive_text(Jean, "You're going to bed?") from _call_receive_text_172
    call receive_text(Jean, "Okay") from _call_receive_text_173

    return

label Jean_text_goodnight_horny:
    call receive_text(Jean, "Not gonna stop by before bed?") from _call_receive_text_174
    call receive_text(Jean, "Maybe tomorrow ;)") from _call_receive_text_175
    call receive_text(Jean, "Goodnight!") from _call_receive_text_176

    call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_274

    return

label Jean_text_goodnight_nympho:
    call receive_text(Jean, "Tired already?") from _call_receive_text_177
    call receive_text(Jean, "Damn") from _call_receive_text_178
    call receive_text(Jean, "Was hoping to spend some. . . time with you") from _call_receive_text_179
    call receive_text(Jean, "Better at least find me tomorrow <3") from _call_receive_text_180

    call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_275

    return

label Jean_text_ignored:
    call receive_text(Jean, "Cool. . .") from _call_receive_text_181

    call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_276

    return

label Jean_text_ask_on_date:
    if Player.date_planned or 2 in Player.schedule.keys() or 3 in Player.schedule.keys():
        call receive_text(Jean, "Nooo, I'm busy tonight :((") from _call_receive_text_293

        "You already have plans this evening."

        return
    
    if time_index > 2:
        call receive_text(Jean, "Not enough time tonight, but maybe tomorrow?") from _call_receive_text_182

        $ Jean.History.update("said_no_to_date")
        
        return
        
    if not Jean.History.check("went_on_date_with_Player"):
        if Player.cash < 130:
            call receive_text(Jean, "Nooo, I'm busy tonight :((") from _call_receive_text_183

            "First dates can be pretty expensive. . . you should probably save up at least $130 just to be sure."

            $ Jean.History.update("said_no_to_date")

            return

        $ Player.date_planned[Jean] = "Player_initiated_primary"

        call receive_text(Jean, "Great!") from _call_receive_text_184

        $ phone_interactable = False

        if time_index == 2:
            call receive_text(Jean, "Meet me outside your room <3") from _call_receive_text_185

            if Player.location == "bg_hallway":
                call send_text(Jean, "way ahead of you") from _call_send_text_10
                call receive_text(Jean, "Sweet") from _call_receive_text_186
                call receive_text(Jean, "I'll be right there!") from _call_receive_text_187
            else:
                call receive_text(Jean, "I'm excited!") from _call_receive_text_188

                $ Jean.mandatory_text_options = ["I am too!", f"see you then, {Jean.petname}"]
                $ temp = Jean.mandatory_text_options[:]

                while Jean.mandatory_text_options:
                    pause

                if Jean.text_history[-1][1] == temp[0]:
                    call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_277
        else:
            call receive_text(Jean, "Meet me outside your room later <3") from _call_receive_text_189
            call receive_text(Jean, "I'm excited!") from _call_receive_text_190

            $ Jean.mandatory_text_options = ["I am too!", f"see you then, {Jean.petname}"]
            $ temp = Jean.mandatory_text_options[:]

            while Jean.mandatory_text_options:
                pause

            if Jean.text_history[-1][1] == temp[0]:
                call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_278

        $ phone_interactable = True
            
        if time_index == 2:
            $ ongoing_Event = True
            
            pause 1.0
            
            hide screen phone_screen

            if Party:
                call Characters_leave(Party) from _call_Characters_leave

            if Player.location != "bg_hallway":
                if Player.location != Player.home:
                    "You head straight to your room."

                    $ fade_to_black(0.4)
                    
                    $ Player.location = "traveling"

                    call remove_Characters(location = "traveling") from _call_remove_Characters_321

                    $ fade_in_from_black(0.4)

                    call receive_text(Jean, "Wya???") from _call_receive_text_191
                    call open_texts(Jean) from _call_open_texts_4

                    pause

                    call send_text(Jean, "On my way!") from _call_send_text_11

                    pause 2.0
                    
                    hide screen phone_screen

                    "You pick up the pace."

                $ Party = []
                
                call remove_Characters(location = "bg_hallway") from _call_remove_Characters_64
                call send_Characters(Jean, "bg_hallway", behavior = "on_date") from _call_send_Characters_62
                call set_the_scene(location = "bg_hallway") from _call_set_the_scene_71

                $ Jean.change_face("confused1", mouth = "smirk")

                ch_Jean "Finally."

            $ EventScheduler.Events["Jean_first_date"].start()
    else:
        if Player.cash < 40:
            call receive_text(Jean, "Nooo, I'm busy tonight :((") from _call_receive_text_192

            "You sure you have enough money to take her on a date? Try saving up at least $40."

            $ Jean.History.update("said_no_to_date")

            return

        $ phone_interactable = False
    
        if Jean.status["mad"] or Jean.status["heartbroken"]:
            call receive_text(Jean, "Cant") from _call_receive_text_193
            call receive_text(Jean, "I have to study") from _call_receive_text_194
                
            $ Jean.History.update("said_no_to_date")
        elif Jean.status["horny"] or Jean.status["nympho"]:
            call receive_text(Jean, "Aww, I had. . . other plans for you tonight") from _call_receive_text_195
            call receive_text(Jean, "But I do love dates with you") from _call_receive_text_196
            call receive_text(Jean, "Let's just make sure to get back early ;)") from _call_receive_text_197

            $ Player.date_planned[Jean] = "Player_initiated_primary"
        else:
            if renpy.random.random() > 0.5 or Jean.History.check("studied", tracker = "daily"):
                $ dice_roll = renpy.random.randint(1, 2)
            else:
                $ dice_roll = renpy.random.randint(1, 4)

            if dice_roll == 1:
                call receive_text(Jean, "Of course!") from _call_receive_text_198
                call receive_text(Jean, "I'll see you tonight") from _call_receive_text_199

                $ Player.date_planned[Jean] = "Player_initiated_primary"
            elif dice_roll == 2:
                call receive_text(Jean, "I was just about to text you!") from _call_receive_text_200
                call receive_text(Jean, "See you tonight :)") from _call_receive_text_201

                $ Player.date_planned[Jean] = "Player_initiated_primary"
            elif dice_roll == 3:
                $ Jean.schedule[2] = [Jean.home, "studying"]
                
                call receive_text(Jean, "I wish, I really have to study tonight") from _call_receive_text_202
                call receive_text(Jean, "You'll ask me again tomorrow, right?") from _call_receive_text_203
                
                $ Jean.History.update("said_no_to_date")
            elif dice_roll == 4:
                $ Jean.schedule[2] = [Jean.home, "studying"]

                call receive_text(Jean, f"We can't go on a date tonight, {Jean.Player_petname}") from _call_receive_text_204
                call receive_text(Jean, "We're studying together") from _call_receive_text_205
                call send_text(Jean, "we are?") from _call_send_text_12
                call receive_text(Jean, ". . .") from _call_receive_text_206

                $ Jean.mandatory_text_options = ["I mean. . . of course we are. . .", "I. . . can't tonight"]
                $ temp = Jean.mandatory_text_options[:]

                while Jean.mandatory_text_options:
                    pause

                if Jean.text_history[-1][1] == temp[0]:
                    $ Player.schedule[2] = [
                        ["Player.location != Jean.home", "renpy.say(None, 'You head to your study session with [Jean.name].')"],
                        ["Jean.location != Jean.home", "renpy.call('send_Characters', Jean, Jean.home, behavior = 'studying')"],
                        ["Player.location != Jean.home", "renpy.call('set_the_scene', location = Jean.home)"],
                        ["True", "renpy.call('actually_study', Jean)"]]
                else:
                    call receive_text(Jean, ". . .") from _call_receive_text_207

                    $ Jean.History.update("Player_rejected_studying")
                
                $ Jean.History.update("said_no_to_date")

        $ phone_interactable = True

    return