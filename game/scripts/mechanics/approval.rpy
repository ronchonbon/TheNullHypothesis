define massive_stat = 50
define large_stat = 25
define medium_stat = 10
define small_stat = 5
define tiny_stat = 1

define max_stats = [250, 500, 750, 1000]

init python:

    def approval_check(Companion, flavor = None, threshold = None, extra_condition = None):
        if Companion not in all_Companions:
            return 0

        if flavor is not None:
            value = getattr(Companion, flavor)
        else:
            value = Companion.love + Companion.trust

        if extra_condition:
            conditions = eval(f"{Companion.tag}_conditions")

            if extra_condition in conditions.keys():
                for condition in conditions[extra_condition]:
                    if not eval(condition):
                        return False

        if not threshold:
            return value
        elif isinstance(threshold, str):
            if Companion.love >= eval(f"{Companion.tag}_thresholds['{threshold}'][0]") and Companion.trust >= eval(f"{Companion.tag}_thresholds['{threshold}'][1]"):
                conditions = eval(f"{Companion.tag}_conditions")

                if threshold not in conditions.keys():
                    return True
                else:
                    for condition in conditions[threshold]:
                        if not eval(condition):
                            return False

                    return True
        elif isinstance(threshold, float) or isinstance(threshold, int):
            if value >= threshold:
                return True
        elif len(threshold) > 1:
            if Companion.love >= threshold[0] and Companion.trust >= threshold[1]:
                return True
        else:
            error("Something unexpected happened.")
                
        return False

    def sort_Characters_by_approval(Characters):
        if Characters in all_Characters or len(Characters) <= 1:
            return Characters

        renpy.random.shuffle(Characters)

        sorted_Characters = [Characters[0]]

        Characters.remove(Characters[0])

        for C in Characters:
            for c in range(len(sorted_Characters)):
                if approval_check(C) > approval_check(sorted_Characters[c]):
                    sorted_Characters.insert(c, C)

                    break

            if C not in sorted_Characters:
                sorted_Characters.append(C)

        return sorted_Characters

label change_Player_stat(flavor, update):
    $ stat = getattr(Player, flavor)

    $ stat += update

    $ stat = 100 if stat > 100 else stat

    $ setattr(Player, flavor, stat)

    return

label change_Companion_stat(Companion, flavor, update, alternate_values = None):
    if not alternate_values:
        $ alternate_values = {}

    if Companion in alternate_values.keys():
        $ check = alternate_values[Companion][0]
        $ update = alternate_values[Companion][1]

    $ stat = getattr(Companion, flavor)

    if update:
        if flavor == "love":
            $ shade = "#c11b17"
        elif flavor == "trust":
            $ shade = "#2554c7"
        elif flavor == "desire":
            $ shade = "#f3a3b3"

        if flavor in ["love", "trust"]:
            if update > 0:
                $ update *= Player.stat_modifier*Companion.stat_modifier
            elif update < 0:
                $ update *= 1.0 - (Player.stat_modifier*Companion.stat_modifier - 1.0)

            if flavor == "love":
                if Player.location == Companion.location and Player.sweat >= Player.sweaty_threshold:
                    if update > 0:
                        $ update *= 0.8
                    elif update < 0:
                        $ update *= 1.2

            $ update = int(update)

            $ list_of_Companions = eval(f"ch{chapter}_Companions")

            if Companion in list_of_Companions:
                $ update = max_stats[season - 1] - stat if stat + update >= max_stats[season - 1] else update
            else:
                $ update = 1000 - stat if stat + update >= 1000 else update
        else:
            if Player.location == Companion.location and Player.sweat >= Player.sweaty_threshold:
                if update > 0:
                    $ update *= 0.75
                elif update < 0:
                    $ update *= 1.25

            $ update = int(update)

            $ update = 100 - stat if stat + update >= 100 else update

        $ update = -stat if stat + update <= 0 else update

        if update:
            $ stat += update

            $ setattr(Companion, flavor, stat)
            
            if Companion.desire >= 75:
                $ Companion.grool = 2
            elif Companion.desire >= 50:
                $ Companion.grool = 1
            else:
                $ Companion.grool = 0

            $ Companion.check_statuses()

            if flavor == "desire":
                if not Action_screen_showing:
                    if Companion.desire >= 90:
                        $ update_messages.append("{color=%s}%s{/color} {color=%s}is really squirming{/color}" % (eval(f"{Companion.tag}_color"), Companion.name, shade))
                    elif Companion.desire >= 75:
                        $ update_messages.append("{color=%s}%s{/color} {color=%s}crosses and uncrosses her legs{/color}" % (eval(f"{Companion.tag}_color"), Companion.name, shade))
                    elif Companion.desire >= 50:
                        $ update_messages.append("{color=%s}%s{/color} {color=%s}looks at you intensely{/color}" % (eval(f"{Companion.tag}_color"), Companion.name, shade))
                    elif Companion.desire >= 25:
                        $ update_messages.append("{color=%s}%s{/color} {color=%s}fidgets a little{/color}" % (eval(f"{Companion.tag}_color"), Companion.name, shade))
                    # elif Companion.desire >= 10:
                    #     $ update_messages.append("{color=%s}%s{/color} {color=%s}seems distracted{/color}" % (eval(f"{Companion.tag}_color"), Companion.name, shade))
            else:
                if update > 0:
                    $ update_messages.append("{color=%s}%s{/color} gained {color=%s}%s %s{/color}" % (eval(f"{Companion.tag}_color"), Companion.name, shade, update, flavor.capitalize()))
                elif update < 0:
                    $ update_messages.append("{color=%s}%s{/color} lost {color=%s}%s %s{/color}" % (eval(f"{Companion.tag}_color"), Companion.name, shade, -update, flavor.capitalize()))

    $ EventScheduler.update_conditions()
    
    return