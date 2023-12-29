init -1:

    default Scott = create_Scott()

init -2 python:

    def create_Scott():
        Scott = NPCClass("Scott")

        Scott.full_name = "Scott Summers"
        Scott.call_sign = "Cyclops"

        Scott.database_type = "ally"

        return Scott

label update_Scott:
    $ Scott.full_name = "Scott Summers"
    $ Scott.call_sign = "Cyclops"

    $ Scott.database_type = "ally"

    return