init -1:
        
    default Sentinel = create_Sentinel()
    
    define Sentinel_color = "#491e39"
    define ch_Sentinel = Character("[Sentinel.tag]")

init -2 python:

    def create_Sentinel():
        Sentinel = NPCClass("Sentinel", voice = ch_Sentinel)
        
        Sentinel.full_name = "Sentinel"
        Sentinel.call_sign = "Sentinel"

        Cameos.append(Sentinel.tag)

        all_Characters.append(Sentinel)

        return Sentinel

label update_Sentinel:

    return