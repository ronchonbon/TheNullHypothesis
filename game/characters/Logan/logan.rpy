init -1:

    default Logan = create_Logan()
    
    define Logan_color = "#bca10a"
    define ch_Logan = Character("[Logan.tag]")

init -2 python:

    def create_Logan():
        Logan = NPCClass("Logan", voice = ch_Logan)

        Logan.full_name = "Logan"
        Logan.call_sign = "Wolverine"

        Cameos.append(Logan.tag)

        all_Characters.append(Logan)

        return Logan

label update_Logan:

    return