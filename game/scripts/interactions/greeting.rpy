label Characters_greet_Player(greeting_Characters):
    if greeting_Characters in all_Characters:
        $ greeting_Characters = [greeting_Characters]

    $ sorted_Characters = sort_Characters_by_approval(greeting_Characters[:])[:]

    while sorted_Characters:
        if sorted_Characters[0] in all_Companions and approval_check(sorted_Characters[0], threshold = "friendship"):
            $ status = sorted_Characters[0].get_status()
                
            if status:
                call expression f"{sorted_Characters[0].tag}_greets_Player_{status}" from _call_expression_244
            elif approval_check(sorted_Characters[0], threshold = "love"):
                call expression f"{sorted_Characters[0].tag}_greets_Player_love" from _call_expression_245
            elif sorted_Characters[0] in Partners:
                call expression f"{sorted_Characters[0].tag}_greets_Player_relationship" from _call_expression_246
            else:
                call expression f"{sorted_Characters[0].tag}_greets_Player" from _call_expression_247
        elif sorted_Characters[0].behavior != "teaching":
            call expression f"{sorted_Characters[0].tag}_greets_Player" from _call_expression_248

        $ sorted_Characters.remove(sorted_Characters[0])

    return