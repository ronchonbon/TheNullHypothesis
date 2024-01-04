init python:

    def Ororo_shaving():
        label = "Ororo_shaving"

        conditions = [
            "'pubic' in Ororo.body_hair_to_shave.keys()",

            "Ororo.location in bedrooms"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Ororo_shaving:
    $ Ororo.body_hair_growing["pubic"] = False
    $ Ororo.body_hair["pubic"] = Ororo.body_hair_to_shave["pubic"]
    $ Ororo.body_hair_to_shave["pubic"] = False

    return

init python:

    def Ororo_growing_back():
        label = "Ororo_growing_back"

        conditions = [
            "'pubic' in Ororo.body_hair_to_grow.keys()"]

        automatic = True

        return EventClass(label, conditions, automatic = automatic)

label Ororo_growing_back:

    return

init python:

    def Ororo_grown_back():
        label = "Ororo_grown_back"

        conditions = [
            "EventScheduler.Events['Ororo_growing_back'].completed",
            "day - EventScheduler.Events['Ororo_growing_back'].completed_when >= 2"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Ororo_grown_back:
    if day - EventScheduler.Events['Ororo_growing_back'].completed_when >= 7:
        $ Ororo.body_hair_growing["pubic"] = False
        $ Ororo.body_hair["pubic"] = Ororo.body_hair_to_grow["pubic"]
        $ Ororo.body_hair_to_grow["pubic"] = False

        $ EventScheduler.Events["Ororo_growing_back"].completed_when = 1e8
    else:
        $ Ororo.body_hair_growing["pubic"] = True

    return
