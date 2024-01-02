init -1:

    default Laura = create_Laura()
    
    define Laura_color = "#bca10a"
    define ch_Laura = Character("[Laura.tag]")

init -2 python:

    def create_Laura():
        Laura = CompanionClass("Laura", voice = ch_Laura)

        Laura.full_name = "Laura Kinney"
        Laura.public_name = "X-23"
        Laura.call_sign = "X-23"

        Laura.database_type = "ally"
        
        Laura.default_body_hair = {
            "pubic": "hairy",
            "anus": None,
            "armpits": None}

        Laura.Player_petname = Player.first_name
        Laura.Player_petnames.append(Player.first_name)
        Laura.Player_petnames.append("guy")

        Laura.body_hair = Laura.default_body_hair
        Laura.desired_body_hair = Laura.default_body_hair

        Laura.give_trait("virgin")

        Cast.append(Laura.tag)
        Sprites.append(Laura)

        all_Characters.append(Laura)
        all_Companions.append(Laura)
        Students.append(Laura)

        ch1_Companions.append(Laura)

        bedrooms.append(Laura.home)

        return Laura

    def Laura_faces(face):
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
            mouth = "happy"
        elif face == "appalled3":
            brows = "furrowed"
            eyes = "wide"
            mouth = "open"
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
            mouth = "open"
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
            mouth = "neutral"
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
        elif face == "snarl":
            brows = "furrowed"
            eyes = "squint"
            mouth = "snarl"
        elif face == "surprised1":
            brows = "raised"
            eyes = "neutral"
            mouth = "neutral"
        elif face == "surprised2":
            brows = "raised"
            eyes = "wide"
            mouth = "neutral"
        elif face == "surprised3":
            brows = "raised"
            eyes = "wide"
            mouth = "open"
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
            mouth = "happy"
        elif face == "worried4":
            brows = "worried"
            eyes = "wide"
            mouth = "open"
        else:
            return "wrong", "wrong", "wrong", 0

        return brows, eyes, mouth, blush

    def Laura_arms(pose):
        if pose == "neutral":
            left_arm = "neutral"
            right_arm = "neutral"
        elif pose == "angry":
            left_arm = "fist"
            right_arm = "fist"
        elif pose == "bra":
            left_arm = "bra"
            right_arm = "bra"
        elif pose == "claws":
            left_arm = "claws"
            right_arm = "claws"
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
        elif pose == "X":
            left_arm = "X"
            right_arm = "X"
        else:
            return "wrong", "wrong"

        return left_arm, right_arm

    def Laura_locations():
        possible_locations = []

        possible_locations.append(Laura.home)

        if time_index < 3 and weather != "rain":
            possible_locations.append("bg_campus")

        if time_index < 2 and weekday < 5:
            possible_locations.append("bg_classroom")
            possible_locations.append("bg_classroom")

        if time_index < 3 and Laura.location != "bg_lockers" and not Laura.History.check("trained_with_Player", tracker = "daily"):
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
            if (Laura in Partners or Laura.status["nympho"] or approval_check(Laura, threshold = "love")) and renpy.random.random() > 0.85:
                if (Player.location not in bedrooms or Player.location == Player.home) and (Player.location != "bg_shower_Player" or Laura.check_traits("has_keys_to_Players_room")):
                    possible_locations.append(Player.location)

                if Laura.check_traits("has_keys_to_Players_room"):
                    possible_locations.append(Player.home)

        return possible_locations

label update_Laura:
    $ Laura.full_name = "Laura Kinney"
    $ Laura.public_name = "X-23"
    $ Laura.call_sign = "X-23"

    $ Laura.database_type = "ally"
    
    $ Laura.default_body_hair = {
        "pubic": "hairy",
        "anus": None,
        "armpits": None}

    $ Laura.sprite_anchor = Laura_standing_anchor
    $ Laura.sprite_position[1] = Laura_standing_height
    $ Laura.sprite_zoom = Laura_standing_zoom

    return

label Laura_unsheathes_claws(hand = "both"):
    pause 0.2

    if hand == "both":
        $ Laura.give_trait("left_claw")
        $ Laura.give_trait("right_claw")
    elif hand == "left":
        $ Laura.give_trait("left_claw")
    elif hand == "right":
        $ Laura.give_trait("right_claw")

    $ Laura.give_trait("unsheathing_claws")

    show expression "images/effects/snikt.webp" as snikt onlayer effects:
        anchor (0.5, 0.5) pos (0.675, 0.25)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.5 alpha 1.0
        ease 2.0 alpha 0.0

    $ renpy.pause(0.1, hard = True)

    $ Laura.remove_trait("unsheathing_claws")

    return

label Laura_sheathes_claws(hand = "both"):
    if hand == "both":
        $ Laura.remove_trait("left_claw")
        $ Laura.remove_trait("right_claw")
    elif hand == "left":
        $ Laura.remove_trait("left_claw")
    elif hand == "right":
        $ Laura.remove_trait("right_claw")

    $ Laura.give_trait("sheathing_claws")

    show expression "images/effects/snakt.webp" as snakt onlayer effects:
        anchor (0.5, 0.5) pos (0.675, 0.25)

        zoom 0.5
        alpha 0.0
        ease 0.01 alpha 1.0
        ease 0.5 zoom 0.0 alpha 0.0

    $ renpy.pause(0.51, hard = True)

    $ Laura.remove_trait("sheathing_claws")

    pause 0.5
    
    return