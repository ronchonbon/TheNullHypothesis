init -1:
        
    default Cain = create_Cain()
    
    define Cain_color = "#b31b1b"
    define ch_Cain = Character("[Cain.tag]")

init -2 python:

    def create_Cain():
        Cain = NPCClass("Cain", voice = ch_Cain)
        
        Cain.full_name = "Cain Marko"
        Cain.call_sign = "Juggernaut"

        Cameos.append(Cain.tag)

        all_Characters.append(Cain)

        return Cain

label update_Cain:

    return