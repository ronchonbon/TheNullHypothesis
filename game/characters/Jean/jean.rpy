init -1:
    
    default Jean = create_Jean()
    
    define Jean_color = "#d92912"
    define ch_Jean = Character("[Jean.tag]")
    
init -2 python:

    def create_Jean():
        Jean = CompanionClass("Jean", voice = ch_Jean)

        Jean.full_name = "Jean Grey"
        Jean.public_name = "Jean"
        Jean.call_sign = "Marvel Girl"

        Jean.database_type = "ally"

        Jean.default_body_hair = {
            "pubic": "bush",
            "anus": None,
            "armpits": None}

        Jean.Player_petname = Player.first_name
        Jean.Player_petnames.append(Player.first_name)

        Jean.body_hair = Jean.default_body_hair
        Jean.desired_body_hair = Jean.default_body_hair

        Jean.whiteboard = "chemistry"

        Jean.give_trait("virgin")
        
        Cast.append(Jean.tag)
        Sprites.append(Jean)

        all_Characters.append(Jean)
        all_Companions.append(Jean)
        Students.append(Jean)

        ch1_Companions.append(Jean)

        bedrooms.append(Jean.home)

        return Jean

    def Jean_faces(face):
        blush = 0

        if face == "neutral":
            brows = "neutral"
            eyes = "neutral"
            mouth = "neutral"
        elif face == "angry1":
            brows = "furrowed"
            eyes = "neutral"
            mouth = "neutral"
        elif face == "angry2":
            brows = "furrowed"
            eyes = "neutral"
            mouth = "happy"
        elif face == "appalled1":
            brows = "furrowed"
            eyes = "wide"
            mouth = "neutral"
        elif face == "appalled2":
            brows = "furrowed"
            eyes = "wide"
            mouth = "open"
        elif face == "appalled3":
            brows = "furrowed"
            eyes = "wide"
            mouth = "agape"
        elif face == "confused1":
            brows = "cocked"
            eyes = "neutral"
            mouth = "neutral"
        elif face == "confused2":
            brows = "cocked"
            eyes = "wide"
            mouth = "neutral"
        elif face == "confused3":
            brows = "cocked"
            eyes = "wide"
            mouth = "agape"
        elif face == "devious":
            brows = "neutral"
            eyes = "squint"
            mouth = "smile"
        elif face == "furious":
            brows = "furrowed"
            eyes = "neutral"
            mouth = "frown"
        elif face == "grimace":
            brows = "furrowed"
            eyes = "closed"
            mouth = "lipbite"
        elif face == "happy":
            brows = "neutral"
            eyes = "neutral"
            mouth = "smile"
        elif face == "kiss1":
            brows = "worried"
            eyes = "closed"
            mouth = "kiss"
        elif face == "kiss2":
            brows = "neutral"
            eyes = "closed"
            mouth = "kiss"
        elif face == "manic":
            brows = "worried"
            eyes = "wide"
            mouth = "smile"
            blush = 1
        elif face == "perplexed":
            brows = "cocked"
            eyes = "wide"
            mouth = "open"
        elif face == "pleased1":
            brows = "raised"
            eyes = "neutral"
            mouth = "smirk"
        elif face == "pleased2":
            brows = "raised"
            eyes = "wide"
            mouth = "smirk"
        elif face == "sad":
            brows = "worried"
            eyes = "neutral"
            mouth = "frown"
        elif face == "sexy":
            brows = "neutral"
            eyes = "sexy"
            mouth = "lipbite"
        elif face == "sly":
            brows = "neutral"
            eyes = "squint"
            mouth = "smirk"
        elif face == "smirk1":
            brows = "neutral"
            eyes = "neutral"
            mouth = "happy"
        elif face == "smirk2":
            brows = "neutral"
            eyes = "neutral"
            mouth = "smirk"
        elif face == "surprised1":
            brows = "raised"
            eyes = "neutral"
            mouth = "open"
        elif face == "surprised2":
            brows = "raised"
            eyes = "wide"
            mouth = "open"
        elif face == "surprised3":
            brows = "raised"
            eyes = "wide"
            mouth = "agape"
        elif face == "suspicious1":
            brows = "furrowed"
            eyes = "squint"
            mouth = "neutral"
        elif face == "suspicious2":
            brows = "furrowed"
            eyes = "squint"
            mouth = "frown"
        elif face == "wink":
            brows = "wink"
            eyes = "wink"
            mouth = "kiss"
        elif face == "worried1":
            brows = "worried"
            eyes = "neutral"
            mouth = "neutral"
        elif face == "worried2":
            brows = "worried"
            eyes = "wide"
            mouth = "neutral"
        elif face == "worried3":
            brows = "worried"
            eyes = "wide"
            mouth = "open"
        elif face == "worried4":
            brows = "worried"
            eyes = "wide"
            mouth = "agape"
        else:
            return "wrong", "wrong", "wrong", 0

        return brows, eyes, mouth, blush

    def Jean_arms(pose):
        if pose == "neutral":
            left_arm = "neutral"
            right_arm = "neutral"
        elif pose == "angry":
            left_arm = "fist"
            right_arm = "fist"
        elif pose == "bra":
            left_arm = "bra"
            right_arm = "bra"
        elif pose == "come_here":
            left_arm = "fight"
            right_arm = "extended"
        elif pose == "crossed":
            left_arm = "crossed"
            right_arm = "crossed"
        elif pose == "fight":
            left_arm = "fight"
            right_arm = "fight"
        elif pose == "hips":
            left_arm = "hip"
            right_arm = "hip"
        elif pose == "plug":
            left_arm = "touch_ass"
            right_arm = "fist"
        elif pose == "psychic1":
            left_arm = "psychic1"
            right_arm = "psychic1"
        elif pose == "psychic2":
            left_arm = "psychic2"
            right_arm = "psychic2"
        elif pose == "sass":
            left_arm = "hip"
            right_arm = "neutral"
        elif pose == "shrug":
            left_arm = "extended"
            right_arm = "extended"
        elif pose == "sheepish":
            left_arm = "rub_neck"
            right_arm = "extended"
        elif pose == "touch_self":
            left_arm = "grope"
            right_arm = "touch_pussy"
        else:
            return "wrong", "wrong"

        return left_arm, right_arm

    def Jean_locations():
        possible_locations = []

        possible_locations.append(Jean.home)

        if time_index < 3 and weather != "rain":
            possible_locations.append("bg_campus")

        if time_index < 2 and weekday < 5:
            possible_locations.append("bg_classroom")
            possible_locations.append("bg_classroom")

        if time_index < 3 and Jean.location != "bg_lockers" and not Jean.History.check("trained_with_Player", tracker = "daily"):
            possible_locations.append("bg_danger")

        if time_index < 3:
            if time_index == 2:
                if temperature[time_index] > 22 and not weather and snow_left == 0:
                    possible_locations.append("bg_pool")

                possible_locations.append("bg_mall")
            elif weekday > 4:
                if temperature[time_index] > 22 and not weather and snow_left == 0:
                    possible_locations.append("bg_pool")

                possible_locations.append("bg_mall")

        if day > 3:
            if (Jean in Partners or Jean.status["nympho"] or approval_check(Jean, threshold = "love")) and renpy.random.random() > 0.85:
                if (Player.location not in bedrooms or Player.location == Player.home) and (Player.location != "bg_shower_Player" or Jean.check_traits("has_keys_to_Players_room")):
                    possible_locations.append(Player.location)

                if Jean.check_traits("has_keys_to_Players_room"):
                    possible_locations.append(Player.home)

        return possible_locations

label update_Jean:
    $ Jean.full_name = "Jean Grey"
    $ Jean.public_name = "Jean"
    $ Jean.call_sign = "Marvel Girl"

    $ Jean.database_type = "ally"

    $ Jean.default_body_hair = {
        "pubic": "bush",
        "anus": None,
        "armpits": None}
        
    $ Jean.sprite_anchor = Jean_standing_anchor
    $ Jean.sprite_position[1] = Jean_standing_height
    $ Jean.sprite_zoom = Jean_standing_zoom

    return

label Jean_activate_psychic:
    $ Jean.give_trait("psychic")
    $ Jean.give_trait("activating_psychic")

    $ renpy.pause(0.2, hard = True)

    $ Jean.remove_trait("activating_psychic")

    return

label Jean_deactivate_psychic:
    $ Jean.remove_trait("psychic")
    $ Jean.give_trait("deactivating_psychic")

    $ renpy.pause(0.2, hard = True)

    $ Jean.remove_trait("deactivating_psychic")

    return