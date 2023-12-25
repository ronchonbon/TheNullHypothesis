init python:

    def Rogue_shaving():
        label = "Rogue_shaving"

        conditions = [
            "'pubic' in Rogue.body_hair_to_shave.keys()",

            "Rogue.location in bedrooms"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Rogue_shaving:
    $ Rogue.body_hair_growing["pubic"] = False
    $ Rogue.body_hair["pubic"] = Rogue.body_hair_to_shave["pubic"]
    $ Rogue.body_hair_to_shave["pubic"] = False

    return

init python:

    def Rogue_growing_back():
        label = "Rogue_growing_back"

        conditions = [
            "'pubic' in Rogue.body_hair_to_grow.keys()"]

        automatic = True

        return EventClass(label, conditions, automatic = automatic)

label Rogue_growing_back:

    return

init python:

    def Rogue_grown_back():
        label = "Rogue_grown_back"

        conditions = [
            "EventScheduler.Events['Rogue_growing_back'].completed",
            "day - EventScheduler.Events['Rogue_growing_back'].completed_when >= 2"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Rogue_grown_back:
    if day - EventScheduler.Events['Rogue_growing_back'].completed_when >= 7:
        $ Rogue.body_hair_growing["pubic"] = False
        $ Rogue.body_hair["pubic"] = Rogue.body_hair_to_grow["pubic"]
        $ Rogue.body_hair_to_grow["pubic"] = False

        $ EventScheduler.Events["Rogue_growing_back"].completed_when = 1e8
    else:
        $ Rogue.body_hair_growing["pubic"] = True

    return
