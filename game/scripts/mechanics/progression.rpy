define max_level = [5, 10, 15, 20, 25, 30]

label level_up:
    if Player.level < max_level[chapter - 1] and Player.XP >= Player.XP_goal:
        $ Player.level += 1
 
        $ update_messages.append("{color=%s}%s{/color} is now {color=%s}Level %s{/color}" % ("#feba00", Player.first_name, "#feba00", Player.level))

        if Player.level < 5:
            $ increase = 5
        elif Player.level < 10:
            $ increase = 10
        else:
            $ increase = 20

        $ Player.income += increase

        if Player.level > 10:
            if Player.level % 10 == 0:
                $ Player.max_stamina += 1
        elif Player.level == 5:
            $ Player.max_stamina += 1

        $ Player.XP_goal = int(1.75*Player.XP_goal)
    elif Player.level == max_level[chapter - 1]:
        $ Player.XP = Player.XP_goal

    python:
        for C in all_Companions:
            if C.level < max_level[chapter - 1] and C.XP >= C.XP_goal:
                C.level += 1

                update_messages.append("{color=%s}%s{/color} is now {color=%s}Level %s{/color}" % (eval(f"{C.tag}_color"), C.name, "#feba00", C.level))

                if C.level % 5 == 0:
                    C.max_stamina += 1

                C.XP_goal = int((1.75*C.XP_goal))
            elif C.level == max_level[chapter - 1]:
                C.XP = C.XP_goal

    $ EventScheduler.update_conditions()
    
    return