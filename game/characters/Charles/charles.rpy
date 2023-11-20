init -1:
    
    default Charles = create_Charles()

    define Charles_color = "#1b867d"
    define ch_Charles = Character("[Charles.tag]")

    define Charles_standing_anchor = [int(1260*character_sampling), int(1792*character_sampling)]
    define Charles_standing_height = 0.35
    define Charles_standing_zoom = 0.35*character_adjustment

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