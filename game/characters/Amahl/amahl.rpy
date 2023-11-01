init -1:
        
    default Amahl = create_Amahl()
    
    define Amahl_color = "#592c99"
    define ch_Amahl = Character("[Amahl.tag]")

init -2 python:

    def create_Amahl():
        Amahl = NPCClass("Amahl", voice = ch_Amahl)
        
        Amahl.full_name = "Amahl Farouk"
        Amahl.call_sign = "Shadow King"

        Cameos.append(Amahl.tag)

        all_Characters.append(Amahl)

        return Amahl

label update_Amahl:

    return