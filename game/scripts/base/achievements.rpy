init -2:

    define achievements = {

        "Aim for the tits, Hawkeye": {
            "description": "Cum on someone's tits 10 times",
            "condition": "Player.History.check('cumshot_breasts')",
            "goal": 10,
            "points": 5,
            "secret": False},

        "We're gonna need a Patreon": {
            "description": "Have an account balance of $500",
            "condition": "Player.cash",
            "goal": 500,
            "points": 5,
            "secret": False}}