init -1:

    default Evan = create_Evan()

init -2 python:

    def create_Evan():
        Evan = NPCClass("Evan")

        Evan.full_name = "Evan Daniels"
        Evan.call_sign = "Spyke"

        return Evan

label update_Evan:

    return