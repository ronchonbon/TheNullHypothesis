init python:

    def Laura_shaving():
        label = "Laura_shaving"

        conditions = [
            "'pubic' in Laura.body_hair_to_shave.keys()",

            "Laura.location in bedrooms"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Laura_shaving:
    $ Laura.body_hair_growing["pubic"] = False
    $ Laura.body_hair["pubic"] = Laura.body_hair_to_shave["pubic"]
    $ Laura.body_hair_to_shave["pubic"] = False

    return

init python:

    def Laura_growing_back():
        label = "Laura_growing_back"

        conditions = [
            "'pubic' in Laura.body_hair_to_grow.keys()"]

        automatic = True

        return EventClass(label, conditions, automatic = automatic)

label Laura_growing_back:

    return

init python:

    def Laura_grown_back():
        label = "Laura_grown_back"

        conditions = [
            "EventScheduler.Events['Laura_growing_back'].completed",
            "day - EventScheduler.Events['Laura_growing_back'].completed_when >= 2"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Laura_grown_back:
    if day - EventScheduler.Events['Laura_growing_back'].completed_when >= 7:
        $ Laura.body_hair_growing["pubic"] = False
        $ Laura.body_hair["pubic"] = Laura.body_hair_to_grow["pubic"]
        $ Laura.body_hair_to_grow["pubic"] = False

        $ EventScheduler.Events["Laura_growing_back"].completed_when = 1e8
    else:
        $ Laura.body_hair_growing["pubic"] = True

    return
