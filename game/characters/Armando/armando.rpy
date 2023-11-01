init -1:

    default Armando = create_Armando()

init -2 python:

    def create_Armando():
        Armando = NPCClass("Armando")

        Armando.full_name = "Armando Muñoz"
        Armando.call_sign = "Darwin"

        return Armando

label update_Armando:

    return