label chapter_1_sunbathing_narrations(sunbathing_Characters = None):
    if len(sunbathing_Characters) > 1:
        "You and the girls grab some loungers and lay in the sun next to each other."
    elif len(sunbathing_Characters) == 1:
        "You and [sunbathing_Characters[0].name] grab a couple of loungers and lay in the sun next to each other."
    else:
        "You lay lazily in the sun."

    return