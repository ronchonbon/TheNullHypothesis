label Laura_steamy_romance_novel_shopping_accept:
    if EventScheduler.Events["Laura_boyfriend"].completed:
        $ Laura.change_face("confused1", eyes = "down")

        if "steamy_romance_novel" in Rogue.inventory.keys():
            ch_Laura "I think I have seen [Rogue.name] reading this one. . ." 

            $ Laura.change_face("confused1", eyes = "squint", blush = 1) 
            
            ch_Laura "She seems to {i}enjoy{/i} it very much. . ."
        else:
            ch_Laura "This is. . ." 
            
            $ Laura.change_face("confused1", eyes = "down", mouth = "lipbite", blush = 1) 
            
            ch_Laura "Oh. . ." 
            
            $ Laura.change_face("confused3", blush = 1) 
            
            ch_Laura "{i}That{/i} kind of book. . ."

        $ Laura.change_face("confused1", eyes = "down", mouth = "lipbite", blush = 1)

        ch_Laura "I may actually read this one."

        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "Thank you."

        call change_Character_stat(Laura, "love", 0) from _call_change_Character_stat_1481
        call change_Character_stat(Laura, "desire", 0) from _call_change_Character_stat_1482

        return True
    else:
        $ Laura.change_face("confused1", eyes = "down")

        ch_Laura "A book?"

        $ Laura.change_face("suspicious1")

        ch_Laura "I don't want it."

    return False

label Laura_steamy_romance_novel_shopping_reject:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "A book?"

    $ Laura.change_face("suspicious1")

    ch_Laura "I don't want it."

    return

label Laura_steamy_romance_novel_gift_accept:
    if EventScheduler.Events["Laura_boyfriend"].completed:
        $ Laura.change_face("confused1", eyes = "down")

        if "steamy_romance_novel" in Rogue.inventory.keys():
            ch_Laura "I think I have seen [Rogue.name] reading this one. . ." 

            $ Laura.change_face("confused1", eyes = "squint", blush = 1) 
            
            ch_Laura "She seems to {i}enjoy{/i} it very much. . ."
        else:
            ch_Laura "This is. . ." 
            
            $ Laura.change_face("confused1", eyes = "down", mouth = "lipbite", blush = 1) 
            
            ch_Laura "Oh. . ." 
            
            $ Laura.change_face("confused3", blush = 1) 
            
            ch_Laura "{i}That{/i} kind of book. . ."

        $ Laura.change_face("confused1", eyes = "down", mouth = "lipbite", blush = 1)

        ch_Laura "I may actually read this one."

        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "Thank you."

        call change_Character_stat(Laura, "love", 0) from _call_change_Character_stat_1483
        call change_Character_stat(Laura, "desire", 0) from _call_change_Character_stat_1484

        return True
    else:
        $ Laura.change_face("confused1", eyes = "down")

        ch_Laura "A book?"

        $ Laura.change_face("suspicious1")

        ch_Laura "I don't want it."

    return False

label Laura_steamy_romance_novel_gift_reject:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "A book?"

    $ Laura.change_face("suspicious1")

    ch_Laura "I don't want it."

    return