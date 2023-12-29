init -1:

    default Evan = create_Evan()

init -2 python:

    def create_Evan():
        Evan = NPCClass("Evan")

        Evan.full_name = "Evan Daniels"
        Evan.call_sign = "Spyke"

        Evan.database_type = "ally"

        return Evan

label update_Evan:
    $ Evan.full_name = "Evan Daniels"
    $ Evan.call_sign = "Spyke"

    $ Evan.database_type = "ally"

    return