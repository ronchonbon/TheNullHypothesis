init python:

    def seen_bra_narrations(Character, proper_subject = True, undressing = True):
        if proper_subject:
            subject = Character.name
            object = Character.name
            owner = Character.name + "'s"
        else:
            subject = "she"
            object = "her"
            owner = "her"

        pool = []

        if undressing:
            pool.append(f"{subject.capitalize()} shows off her {Character.Clothes['bra'].short_name} as you eagerly look on.")

        if Character.desire >= 50:
            if undressing:
                pool.append(f"As she undresses, you can easily make out {owner} firm nipples through her {Character.Clothes['bra'].short_name}.")

        if Character.piercings["nipple"]:
            if Character.piercings["nipple"] in ["barbell", "ring"]:
                pool.append(f"You appreciate {owner} {Character.piercings['nipple']} piercings poking through her {Character.Clothes['bra'].short_name}.")
            else:
                pool.append(f"You appreciate {owner} piercings poking through her {Character.Clothes['bra'].short_name}.")

        return pool

    def seen_breasts_narrations(Character, proper_subject = True, undressing = True):
        if proper_subject:
            subject = Character.name
            object = Character.name
            owner = Character.name + "'s"
        else:
            subject = "she"
            object = "her"
            owner = "her"

        pool = []

        if undressing:
            pool.append(f"{owner.capitalize()} breasts rise and fall with each breath as she takes her {Character.Clothes['bra'].short_name} off.")

        if Character.desire >= 50:
            if undressing:
                pool.append(f"As she exposes her breasts, {owner} stiff nipples make your mouth water.")

        if Character.piercings["nipple"]:
            if Character.piercings["nipple"] in ["barbell", "ring"]:
                pool.append(f"You appreciate the light glinting off of {owner} {Character.piercings['nipple']} piercings.")
            else:
                pool.append(f"You appreciate the light glinting off of {owner} piercings.")

        return pool

    def seen_underwear_narrations(Character, proper_subject = True, undressing = True):
        if proper_subject:
            subject = Character.name
            object = Character.name
            owner = Character.name + "'s"
        else:
            subject = "she"
            object = "her"
            owner = "her"

        pool = []

        if undressing:
            pool.append(f"{subject.capitalize()} undresses, showing off her {Character.Clothes['underwear'].short_name}.")

        if Character.desire >= 50:
            if undressing:
                pool.append(f"You spot a damp spot on {owner} {Character.Clothes['underwear'].short_name} as she undresses.")

        if Character.piercings["labia"]:
            if Character.piercings["labia"] in ["barbell", "ring"]:
                pool.append(f"You appreciate {owner} {Character.piercings['labia']} piercing poking through her {Character.Clothes['underwear'].short_name}.")
            else:
                pool.append(f"You appreciate {owner} piercings poking through her {Character.Clothes['underwear'].short_name}.")

        return pool

    def seen_ass_narrations(Character, proper_subject = True, undressing = True):
        if proper_subject:
            subject = Character.name
            object = Character.name
            owner = Character.name + "'s"
        else:
            subject = "she"
            object = "her"
            owner = "her"

        pool = []

        if undressing:
            pool.append(f"{subject.capitalize()} playfully wiggles out of her clothes, showing off her perfect ass.")

        return pool

    def seen_pussy_narrations(Character, proper_subject = True, undressing = True):
        if proper_subject:
            subject = Character.name
            object = Character.name
            owner = Character.name + "'s"
        else:
            subject = "she"
            object = "her"
            owner = "her"

        pool = []

        if undressing:
            pool.append(f"{subject.capitalize()} undresses, showing off her perfect pussy.")

        if Character.desire >= 50:
            if undressing:
                pool.append(f"{owner.capitalize()} pussy is already glistening with moistness as she undresses.")

        if Character.piercings["labia"]:
            if Character.piercings["labia"] in ["barbell", "ring"]:
                pool.append(f"You stare appreciatively at {owner} {Character.piercings['labia']} piercing.")
            else:
                pool.append(f"You stare appreciatively at {owner} piercings.")

        return pool

    def seen_anus_narrations(Character, proper_subject = True, undressing = True):
        if proper_subject:
            subject = Character.name
            object = Character.name
            owner = Character.name + "'s"
        else:
            subject = "she"
            object = "her"
            owner = "her"

        pool = []

        pool.append(f"{subject.capitalize()} spreads her ass for you, showing off her perfect little hole.")

        return pool

    def seeing_penis_narrations(Character, proper_subject = True, undressing = True):
        if proper_subject:
            subject = Character.name
            object = Character.name
            owner = Character.name + "'s"
        else:
            subject = "she"
            object = "her"
            owner = "her"

        pool = []

        if Character.desire > 50:
            pool.append(f"{subject.capitalize()} looks lustfully at your hard cock.")

        return pool