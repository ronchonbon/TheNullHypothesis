label flirt(Character):
    $ flirting = True

    while flirting:
        $ flirting_type = None

        menu:
            "Tell her you love her" if EventScheduler.Events[f"{Character.tag}_I_love_you"].completed:
                $ flirting_type = "r"

                $ Character.History.update("told_Player_loves_them")
            "Pay her a compliment":
                $ flirting_type = "a"
            "Try a cheesy pickup line":
                $ flirting_type = "b"
            "Look into her eyes and smile" if Character.location == Player.location:
                $ flirting_type = "c"
            "Ask to hold hands" if Character.location == Player.location and approval_check(Character, threshold = "flirting_d"):
                $ flirting_type = "d"
            "Ask for a hug" if Character.location == Player.location and approval_check(Character, threshold = "flirting_f"):
                $ flirting_type = "f"
            "Ask if she wants a massage" if Character.location == Player.location and approval_check(Character, threshold = "flirting_g"):
                $ flirting_type = "g"
            "Put an arm around her" if Character.location == Player.location and approval_check(Character, threshold = "flirting_i"):
                $ flirting_type = "i"
            "Ask for a kiss. . ." if Character.location == Player.location and approval_check(Character, threshold = "flirting_ea"):
                menu:
                    "Ask for a kiss. . ."
                    "On the cheek" if approval_check(Character, threshold = "flirting_ea"):
                        $ flirting_type = "ea"
                    "On the lips" if approval_check(Character, threshold = "flirting_eb"):
                        $ flirting_type = "eb"
                    "Back":
                        pass
            "Kiss her. . ." if Character.location == Player.location and approval_check(Character, threshold = "flirting_oa"):
                menu:
                    "Kiss her. . ."
                    "On the cheek" if approval_check(Character, threshold = "flirting_oa"):
                        $ flirting_type = "oa"
                    "On the lips" if approval_check(Character, threshold = "flirting_ob"):
                        $ flirting_type = "ob"
                    "Back":
                        pass
            "Run a hand through her hair" if Character.location == Player.location and approval_check(Character, threshold = "flirting_h"):
                $ flirting_type = "h"
            # "Ask to see. . ." if Character.location == Player.location and approval_check(Character, threshold = "flirting_ja"):
            #     menu:
            #         "Ask to see. . ."
            #         "Her bra" if approval_check(Character, threshold = "flirting_ja"):
            #             $ flirting_type = "ja"
            #         "Her underwear" if approval_check(Character, threshold = "flirting_jb"):
            #             $ flirting_type = "jb"
            #         "Her breasts" if approval_check(Character, threshold = "flirting_jc"):
            #             $ flirting_type = "jc"
            #         "Her pussy" if approval_check(Character, threshold = "flirting_jd"):
            #             $ flirting_type = "jd"
            #         "Back":
            #             pass
            # "Take a look at. . ." if Character.location == Player.location and approval_check(Character, threshold = "flirting_pa"):
            #     menu:
            #         "Take a look at. . ."
            #         "Her bra" if approval_check(Character, threshold = "flirting_pa"):
            #             $ flirting_type = "pa"
            #         "Her underwear" if approval_check(Character, threshold = "flirting_pb"):
            #             $ flirting_type = "pb"
            #         "Her breasts" if approval_check(Character, threshold = "flirting_pc"):
            #             $ flirting_type = "pc"
            #         "Her pussy" if approval_check(Character, threshold = "flirting_pd"):
            #             $ flirting_type = "pd"
            #         "Back":
            #             pass
            # "Ask for. . ." if Character.location == Player.location and approval_check(Character, threshold = "flirting_ka"):
            #     menu:
            #         "Ask for. . ."
            #         "Her bra" if approval_check(Character, threshold = "flirting_ka"):
            #             $ flirting_type = "ka"
            #         "Her underwear" if approval_check(Character, threshold = "flirting_kb"):
            #             $ flirting_type = "kb"
            #         "Back":
            #             pass
            "Smack her ass" if Character.location == Player.location and approval_check(Character, threshold = "flirting_l"):
                $ flirting_type = "l"
            # "Ask if you can fondle. . ." if Character.location == Player.location and approval_check(Character, threshold = "flirting_ma"):
            #     menu:
            #         "Ask if you can fondle. . ."
            #         "Her breasts" if approval_check(Character, threshold = "flirting_ma"):
            #             $ flirting_type = "ma"
            #         "Her ass" if approval_check(Character, threshold = "flirting_mb"):
            #             $ flirting_type = "mb"
            #         "Her crotch" if approval_check(Character, threshold = "flirting_mc"):
            #             $ flirting_type = "mc"
            #         "Back":
            #             pass
            # "Fondle. . ." if Character.location == Player.location and approval_check(Character, threshold = "flirting_na"):
            #     menu:
            #         "Fondle. . ."
            #         "Her breasts" if approval_check(Character, threshold = "flirting_na"):
            #             $ flirting_type = "na"
            #         "Her ass" if approval_check(Character, threshold = "flirting_nb"):
            #             $ flirting_type = "nb"
            #         "Her crotch" if approval_check(Character, threshold = "flirting_nc"):
            #             $ flirting_type = "nc"
            #         "Back":
            #             pass
            "Chastise her playfully" if Character in [Rogue] and approval_check(Character, threshold = "flirting_qa"):
                menu:
                    "Chastise her playfully"
                    "You've been a bad girl." if approval_check(Character, threshold = "flirting_qa"):
                        $ flirting_type = "qa"
                    "You need to work on satisfying my needs more." if approval_check(Character, threshold = "flirting_qb"):
                        $ flirting_type = "qb"
                    "I don't know if you deserve my attention right now, I'm disappointed in you." if approval_check(Character, threshold = "flirting_qc"):
                        $ flirting_type = "qc"
                    "Back":
                        return
            "Encourage her free use of you" if Character in [Laura] and approval_check(Character, threshold = "flirting_qa"):
                $ dice_roll = renpy.random.randint(1, 3)

                if dice_roll == 1:
                    $ flirting_type = "qa"
                elif dice_roll == 2:                        
                    $ flirting_type = "qb"
                elif dice_roll == 3:
                    $ flirting_type = "qc"
            "Express your thanks for having such a great big sister" if Character in [Jean] and approval_check(Character, threshold = "flirting_qa"):
                $ dice_roll = renpy.random.randint(1, 3)

                if dice_roll == 1:
                    $ flirting_type = "qa"
                elif dice_roll == 2:                        
                    $ flirting_type = "qb"
                elif dice_roll == 3:
                    $ flirting_type = "qc"
            "Back":
                $ flirting = False

        if flirting and flirting_type:
            if approval_check(Character, threshold = f"flirting_{flirting_type}"):
                call change_Character_stat(Character, "love", eval(f"{Character.tag}_flirting_bonuses[flirting_type]")[0])
                call change_Character_stat(Character, "trust", eval(f"{Character.tag}_flirting_bonuses[flirting_type]")[1])
            else:
                call change_Character_stat(Character, "love", eval(f"{Character.tag}_flirting_penalties[flirting_type]")[0])
                call change_Character_stat(Character, "trust", eval(f"{Character.tag}_flirting_penalties[flirting_type]")[1])

            call expression f"{Character.tag}_flirt_{flirting_type}" from _call_expression_213

            $ Character.History.update("flirted_with")

            $ Player.History.update("flirted")

            if Character.location == Player.location and Player.location in public_locations:
                $ Character.History.update("flirted_with_in_public")
                
                $ Player.History.update("flirted_in_public")

            python:
                for C in Partners:
                    if C != Character and (not C.History.check("told_wants_multiple_partners") or Character not in C.knows_about):
                        C.History.update("cheated_on_flirting")

                        if not Player.History.check(f"cheated_on_{C.tag}_date", tracker = "recent"):
                            Player.History.update(f"cheated_on_{C.tag}_with_{other_C.tag}_flirting")

                        if Character.location == Player.location and Player.location in public_locations:
                            C.History.update("cheated_on_flirting_in_public")

                            if not Player.History.check(f"cheated_on_{C.tag}_date", tracker = "recent"):
                                Player.History.update(f"cheated_on_{C.tag}_with_{other_C.tag}_flirting_in_public")

            $ Player.temp = Character

            call check_for_Events(flirting = True) from _call_check_for_Events

            $ flirting = False

    return