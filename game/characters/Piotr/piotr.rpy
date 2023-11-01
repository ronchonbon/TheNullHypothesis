init -1:
        
    default Piotr = create_Piotr()
    
    define Piotr_color = "#606060"
    define ch_Piotr = Character("[Piotr.tag]")

init -2 python:

    def create_Piotr():
        Piotr = NPCClass("Piotr", voice = ch_Piotr)
        
        Piotr.full_name = "Piotr Rasputin"
        Piotr.call_sign = "Colossus"

        Cast.append(Piotr.tag)

        all_Characters.append(Piotr)

        return Piotr

label update_Piotr:

    return