init -2:

    define achievements = {

        "Aim for the tits, Hawkeye": {
            "description": "Cum on someone's tits 10 times",
            "condition": "Player.History.check('cumshot_breasts')",
            "goal": 10,
            "points": 5,
            "secret": False},

        "We're gonna need a Patreon": {
            "description": "Have an account balance of $100",
            "condition": "Player.cash",
            "goal": 100,
            "points": 5,
            "secret": False}}