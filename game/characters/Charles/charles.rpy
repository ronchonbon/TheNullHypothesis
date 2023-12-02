init -1:
    
    default Charles = create_Charles()

    define Charles_color = "#1b867d"
    define ch_Charles = Character("[Charles.tag]")

    define Charles_standing_anchor = [int(1260*character_sampling), int(1792*character_sampling)]
    define Charles_standing_height = 0.38
    define Charles_standing_zoom = 0.35*character_adjustment
    define Charles_standing_bottom = 0.983

init -2 python:

    def create_Charles():
        Charles = NPCClass("Charles", voice = ch_Charles)

        Charles.full_name = "Charles Xavier"
        Charles.call_sign = "Professor X"

        Charles.gives_quests = True

        Charles.psychic = False
        Charles.activating_psychic = False
        Charles.deactivating_psychic = False

        Cast.append(Charles.tag)
        Sprites.append(Charles)
        
        all_Characters.append(Charles)
        all_NPCs.append(Charles)
        Professors.append(Charles)

        bedrooms.append(Charles.home)

        return Charles

    def Charles_faces(face):
        if face == "neutral":
            mouth = "neutral"
            brows = "neutral"
            eyes = "neutral"
        elif face == "angry":
            brows = "furrowed"
            eyes = "neutral"
            mouth = "frown"
        elif face == "confused":
            brows = "furrowed"
            eyes = "squint"
            mouth = "neutral"
        elif face == "happy":
            brows = "neutral"
            eyes = "neutral"
            mouth = "smile"
        elif face == "sad":
            brows = "neutral"
            eyes = "neutral"
            mouth = "frown"
        elif face == "stunned":
            brows = "neutral"
            eyes = "up"
            mouth = "neutral"
        elif face == "surprised":
            brows = "raised"
            eyes = "wide"
            mouth = "neutral"
        else:
            return "wrong", "wrong", "wrong"

        return brows, eyes, mouth

    def Charles_arms(pose):
        return "neutral", "neutral"

    def Charles_locations():
        possible_locations = []

        possible_locations.append(Charles.home)

        if time_index < 2 and weekday < 5:
            possible_locations.append("bg_classroom")
            possible_locations.append("bg_classroom")
        
        if time_index < 3:
            possible_locations.append("bg_study")

            if time_index == 2:
                Charles.destination = "bg_study"

        elif Charles.tag == "Kurt":
            if time_index < 3 and weather != "rain":
                possible_locations.append("bg_campus")

            if time_index < 3:
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

        return possible_locations

label update_Charles:
    $ Charles.sprite_anchor = Charles_standing_anchor
    $ Charles.sprite_position[1] = Charles_standing_height
    $ Charles.sprite_zoom = Charles_standing_zoom

    return

label Charles_activate_psychic:
    $ Charles.psychic = True
    $ Charles.activating_psychic = True

    $ renpy.pause(0.5, hard = True)

    $ Charles.activating_psychic = False

    return

label Charles_deactivate_psychic:
    $ Charles.psychic = False
    $ Charles.deactivating_psychic = True

    $ renpy.pause(0.5, hard = True)

    $ Charles.deactivating_psychic = False

    return