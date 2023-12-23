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
        elif face == "happy":
            brows = "neutral"
            eyes = "neutral"
            mouth = "smile"
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
            mouth = "neutral"
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