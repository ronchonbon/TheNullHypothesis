init python:

    import math

    def sex_faces(Character):
        if hookup_length >= max_hookup_length*math.sqrt(Character.max_stamina) and Character.desire <= 75:
            brows = None
            eyes = None
            mouth = None

            dice_roll = renpy.random.randint(1, 2)

            if dice_roll == 1:
                brows = "neutral"
            elif dice_roll == 2:
                brows = "cocked"

            dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                eyes = "left"
            elif dice_roll == 2:
                eyes = "right"
            elif dice_roll == 3:
                eyes = "neutral"

            if not Character.mouth_Actions:
                dice_roll = renpy.random.randint(1, 2)

                if dice_roll == 1:
                    mouth = "frown"
                elif dice_roll == 2:
                    mouth = "neutral"

            Character.change_face(brows = brows, eyes = eyes, mouth = mouth)
        elif Character.desire >= 90 or Character.History.check("orgasmed", tracker = "recent") >= 2:
            eyes = None
            mouth = None

            dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                eyes = "down"
            elif dice_roll == 2:
                eyes = "up"
            elif dice_roll == 3:
                eyes = "sexy"

            if not Character.mouth_Actions:
                dice_roll = renpy.random.randint(1, 3)

                if dice_roll == 1:
                    mouth = "lipbite"
                elif dice_roll == 2:
                    mouth = "open"
                elif dice_roll == 3:
                    mouth = "agape"

            Character.change_face(brows = "worried", eyes = eyes, mouth = mouth, blush = 3)
        elif Character.desire >= 75 or Character.History.check("orgasmed", tracker = "recent"):
            eyes = None
            mouth = None

            dice_roll = renpy.random.randint(1, 2)

            if dice_roll == 1:
                eyes = "down"
            elif dice_roll == 2:
                eyes = "sexy"

            if not Character.mouth_Actions:
                dice_roll = renpy.random.randint(1, 2)

                if dice_roll == 1:
                    mouth = "lipbite"
                elif dice_roll == 2:
                    mouth = "open"

            Character.change_face(brows = "worried", eyes = eyes, mouth = mouth, blush = 2)
        elif Character.desire >= 50:
            eyes = None
            mouth = None

            dice_roll = renpy.random.randint(1, 2)

            if dice_roll == 1:
                eyes = "down"
            elif dice_roll == 2:
                eyes = "sexy"

            if not Character.mouth_Actions:
                dice_roll = renpy.random.randint(1, 3)

                if dice_roll == 1:
                    mouth = "lipbite"
                elif dice_roll == 2:
                    mouth = "open"
                elif dice_roll == 3:
                    mouth = "smirk"

            Character.change_face(brows = "neutral", eyes = eyes, mouth = mouth, blush = 1)
        else:
            eyes = None
            mouth = None

            dice_roll = renpy.random.randint(1, 2)

            if dice_roll == 1:
                eyes = "neutral"
            elif dice_roll == 2:
                eyes = "sexy"

            if not Character.mouth_Actions:
                dice_roll = renpy.random.randint(1, 3)

                if dice_roll == 1:
                    mouth = "lipbite"
                elif dice_roll == 2:
                    mouth = "smirk"
                elif dice_roll == 3:
                    mouth = "happy"

            Character.change_face(brows = "neutral", eyes = eyes, mouth = mouth)

        return

    def orgasm_faces(Character):
        if Character.History.check("orgasmed_with_Player", tracker = "recent") >= 2:
            brows = None
            eyes = None
            mouth = None

            dice_roll = renpy.random.randint(1, 2)

            if dice_roll == 1:
                brows = "raised"
            elif dice_roll == 2:
                brows = "worried"

            dice_roll = renpy.random.randint(1, 2)

            if dice_roll == 1:
                eyes = "wide"
            elif dice_roll == 2:
                eyes = "up"

            if not Character.mouth_Actions:
                dice_roll = renpy.random.randint(1, 2)

                if dice_roll == 1 and brows == "worried" and eyes == "up":
                    mouth = "tongue"
                else:
                    mouth = "agape"

            Character.change_face(brows = brows, eyes = eyes, mouth = mouth, blush = 3)
        elif Character.History.check("orgasmed_with_Player", tracker = "recent"):
            brows = None
            eyes = None
            mouth = None

            dice_roll = renpy.random.randint(1, 2)

            if dice_roll == 1:
                brows = "raised"
            elif dice_roll == 2:
                brows = "worried"

            dice_roll = renpy.random.randint(1, 2)

            if dice_roll == 1:
                eyes = "closed"
            elif dice_roll == 2:
                eyes = "sexy"

            if not Character.mouth_Actions:
                dice_roll = renpy.random.randint(1, 2)

                if dice_roll == 1:
                    mouth = "open"
                elif dice_roll == 2:
                    mouth = "agape"

            Character.change_face(brows = brows, eyes = eyes, mouth = mouth, blush = 2)
        else:
            brows = None
            eyes = None
            mouth = None

            dice_roll = renpy.random.randint(1, 2)

            if dice_roll == 1:
                brows = "raised"
            elif dice_roll == 2:
                brows = "worried"

            dice_roll = renpy.random.randint(1, 2)

            if dice_roll == 1:
                eyes = "closed"
            elif dice_roll == 2:
                eyes = "sexy"

            if not Character.mouth_Actions:
                dice_roll = renpy.random.randint(1, 2)

                if dice_roll == 1:
                    mouth = "open"
                elif dice_roll == 2:
                    mouth = "lipbite"

            Character.change_face(brows = brows, eyes = eyes, mouth = mouth, blush = 1)

        return