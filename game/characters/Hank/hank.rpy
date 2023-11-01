init -1:

    default Hank = create_Hank()

init -2 python:

    def create_Hank():
        Hank = NPCClass("Hank")

        Hank.full_name = "Henry 'Hank' McCoy"
        Hank.call_sign = "Beast"

        return Hank

label update_Hank:

    return