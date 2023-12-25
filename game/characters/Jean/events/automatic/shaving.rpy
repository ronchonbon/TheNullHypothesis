init python:

    def Jean_shaving():
        label = "Jean_shaving"

        conditions = [
            "'pubic' in Jean.body_hair_to_shave.keys()",
            
            "Jean.location in bedrooms"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Jean_shaving:
    $ Jean.body_hair_growing["pubic"] = False
    $ Jean.body_hair["pubic"] = Jean.body_hair_to_shave["pubic"]
    $ Jean.body_hair_to_shave["pubic"] = False

    return

init python:

    def Jean_growing_back():
        label = "Jean_growing_back"

        conditions = [
            "'pubic' in Jean.body_hair_to_grow.keys()"]

        automatic = True

        return EventClass(label, conditions, automatic = automatic)

label Jean_growing_back:

    return

init python:

    def Jean_grown_back():
        label = "Jean_grown_back"

        conditions = [
            "day - EventScheduler.Events['Jean_growing_back'].completed_when >= 2"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Jean_grown_back:
    if day - EventScheduler.Events["Jean_growing_back"].completed_when >= 7:
        $ Jean.body_hair_growing["pubic"] = False
        $ Jean.body_hair["pubic"] = Jean.body_hair_to_grow["pubic"]
        $ Jean.body_hair_to_grow["pubic"] = False

        $ EventScheduler.Events["Jean_growing_back"].completed_when = 1e8
    else:
        $ Jean.body_hair_growing["pubic"] = True

    return
