init -1:

    default Hank = create_Hank()

init -2 python:

    def create_Hank():
        Hank = NPCClass("Hank")

        Hank.full_name = "Henry 'Hank' McCoy"
        Hank.call_sign = "Beast"

        Hank.database_type = "ally"

        return Hank

label update_Hank:
    $ Hank.full_name = "Henry 'Hank' McCoy"
    $ Hank.call_sign = "Beast"

    $ Hank.database_type = "ally"

    return