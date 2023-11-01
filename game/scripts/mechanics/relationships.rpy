init python:

    def are_Characters_friends(Characters):
        not_friends = False

        for C in Characters:
            for other_C in Characters:
                if C != other_C:
                    if C in all_Girls:
                        if other_C not in C.likes.keys():
                            C.likes[other_C] = 0

                        if C.likes[other_C] < eval(f"{C.tag}_thresholds['friendship'][1]"):
                            not_friends = True
                                
        if not_friends:
            return False
        else:
            return True

    def are_Characters_in_Partners(Characters):
        not_in_Partners = False

        for C in Characters:
            if C not in Partners:
                return False

        return True
        
    def find_Friends(Character):
        Friends = []

        for C in all_Girls:
            if C != Character:
                if C not in Character.likes.keys():
                    Character.likes[C] = 0

                if Character not in C.likes.keys():
                    C.likes[Character] = 0

                if Character.likes[C] > eval(f"{Character.tag}_thresholds['friendship'][1]") and C.likes[Character] > eval(f"{C.tag}_thresholds['friendship'][1]"):
                    Friends.append(C)

        return Friends

    def group_Characters(Characters):
        grouped_Characters = None

        if len(Characters) > 2 and renpy.random.random() > 0.75:
            if are_Characters_friends(Characters[0:3]):
                grouped_Characters = Characters[0:3]

        if not grouped_Characters and len(Characters) > 1 and renpy.random.random() > 0.5:
            if are_Characters_friends(Characters[0:2]):
                grouped_Characters = Characters[0:2]

        if not grouped_Characters:
            grouped_Characters = [Characters[0]]

        return grouped_Characters