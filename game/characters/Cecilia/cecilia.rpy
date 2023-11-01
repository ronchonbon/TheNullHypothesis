init -1:
        
    default Cecilia = create_Cecilia()
    
    define Cecilia_color = "#4123ad"
    define ch_Cecilia = Character("[Cecilia.tag]")

init -2 python:

    def create_Cecilia():
        Cecilia = NPCClass("Cecilia", voice = ch_Cecilia)
        
        Cecilia.full_name = "Cecilia Reyes"
        Cecilia.call_sign = "Cecilia Reyes"

        Cast.append(Cecilia.tag)

        all_Characters.append(Cecilia)

        return Cecilia

label update_Cecilia:

    return