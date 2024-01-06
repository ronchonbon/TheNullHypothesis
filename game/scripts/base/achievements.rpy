init -2:

    define achievements = {

        "Welcome to the Institute": {
            "description": "Complete the Prologue",
            "condition": "day",
            "goal": 3,
            "points": 5,
            "secret": True},

        "I'm the Juggernaut, Bitch!": {
            "description": "Survive your encounter with the Juggernaut",
            "condition": "EventScheduler.Events['ch1_Juggernaut_attack'].completed",
            "goal": 1,
            "points": 5,
            "secret": True},

        "Another Day at the Mall": {
            "description": "Attend the Winter Super Sale at the mall",
            "condition": "EventScheduler.Events['ch1_Sentinel_attack'].completed",
            "goal": 1,
            "points": 5,
            "secret": True},

        "They Fear What They Don't Understand": {
            "description": "Witness the darker side of homo sapiens sapiens",
            "condition": "EventScheduler.Events['ch1_mutant_hate'].completed",
            "goal": 1,
            "points": 5,
            "secret": True},

        "Something Bigger Than Yourself": {
            "description": "Reach level 5",
            "condition": "Player.level",
            "goal": 5,
            "points": 5,
            "secret": False},

        "Mutant-in-Training": {
            "description": "Reach level 10",
            "condition": "Player.level",
            "goal": 10,
            "points": 5,
            "secret": False},

        "On the Path": {
            "description": "Reach level 15",
            "condition": "Player.level",
            "goal": 15,
            "points": 5,
            "secret": False},

        "Mutant and Proud": {
            "description": "Reach level 20",
            "condition": "Player.level",
            "goal": 20,
            "points": 10,
            "secret": False},

        "Paragon of Mutantkind": {
            "description": "Reach level 25",
            "condition": "Player.level",
            "goal": 25,
            "points": 20,
            "secret": False},

        "A God Among Insects": {
            "description": "Reach level 30",
            "condition": "Player.level",
            "goal": 30,
            "points": 40,
            "secret": False},

        "Evolution Never Stops": {
            "description": "Unlock a new mutant ability",
            "condition": "Player.History.check('bought_skill')",
            "goal": 1,
            "points": 5,
            "secret": True},

        "Gonna Need a Patreon": {
            "description": "Have an account balance of $500",
            "condition": "Player.cash",
            "goal": 500,
            "points": 5,
            "secret": False},

        "Pocket Change": {
            "description": "Have an account balance of $1000",
            "condition": "Player.cash",
            "goal": 1000,
            "points": 5,
            "secret": False},

        "Got a Bigger Wallet": {
            "description": "Have an account balance of $5000",
            "condition": "Player.cash",
            "goal": 5000,
            "points": 10,
            "secret": False},

        "High-Roller": {
            "description": "Have an account balance of $10k",
            "condition": "Player.cash",
            "goal": 10000,
            "points": 20,
            "secret": False},

        "Retirement Plan": {
            "description": "Have an account balance of $50k",
            "condition": "Player.cash",
            "goal": 50000,
            "points": 40,
            "secret": False},

        "Gloves Are Coming Off": {
            "description": "Reach 500 Trust with [Rogue.name]",
            "condition": "Rogue.trust",
            "goal": 500,
            "points": 5,
            "secret": False},

        "It's Not Just a Phase": {
            "description": "Reach 1000 Trust with [Rogue.name]",
            "condition": "Rogue.trust",
            "goal": 1000,
            "points": 10,
            "secret": False},

        "I Want to Hold Your Hand": {
            "description": "Reach 500 Love with [Rogue.name]",
            "condition": "Rogue.love",
            "goal": 500,
            "points": 5,
            "secret": False},

        "Big Titty Goth GF": {
            "description": "Reach 1000 Love with [Rogue.name]",
            "condition": "Rogue.love",
            "goal": 1000,
            "points": 10,
            "secret": False},

        "First Friend": {
            "description": "Reach 500 Trust with [Laura.name]",
            "condition": "Laura.trust",
            "goal": 500,
            "points": 5,
            "secret": False},

        "What Is a BFF?": {
            "description": "Reach 1000 Trust with [Laura.name]",
            "condition": "Laura.trust",
            "goal": 1000,
            "points": 10,
            "secret": False},

        "All These Strange Feelings": {
            "description": "Reach 500 Love with [Laura.name]",
            "condition": "Laura.love",
            "goal": 500,
            "points": 5,
            "secret": False},

        "Indomitable Love": {
            "description": "Reach 1000 Love with [Laura.name]",
            "condition": "Laura.love",
            "goal": 1000,
            "points": 10,
            "secret": False},

        "Bird in a Cage": {
            "description": "Reach 500 Trust with [Jean.name]",
            "condition": "Laura.trust",
            "goal": 500,
            "points": 5,
            "secret": False},

        "New Priorities": {
            "description": "Reach 1000 Trust with [Jean.name]",
            "condition": "Jean.trust",
            "goal": 1000,
            "points": 10,
            "secret": False},

        "Stoking the Flames": {
            "description": "Reach 500 Love with [Jean.name]",
            "condition": "Jean.love",
            "goal": 500,
            "points": 5,
            "secret": False},

        "Deep in the Red": {
            "description": "Reach 1000 Love with [Jean.name]",
            "condition": "Jean.love",
            "goal": 1000,
            "points": 10,
            "secret": False},

        "It's the Thought That Counts": {
            "description": "Give a gift",
            "condition": "Player.History.check('gave_gift')",
            "goal": 1,
            "points": 5,
            "secret": False},

        "Aw, You Shouldn't Have": {
            "description": "Give 10 gifts",
            "condition": "Player.History.check('gave_gift')",
            "goal": 10,
            "points": 5,
            "secret": False},

        "Friends with Benefits": {
            "description": "Give 25 gifts",
            "condition": "Player.History.check('gave_gift')",
            "goal": 25,
            "points": 10,
            "secret": False},

        "Ho-Ho-Ho": {
            "description": "Give 50 gifts",
            "condition": "Player.History.check('gave_gift')",
            "goal": 50,
            "points": 20,
            "secret": False},

        "First Paycheck": {
            "description": "Work for Xavier",
            "condition": "Player.History.check('worked')",
            "goal": 1,
            "points": 5,
            "secret": False},

        "New Hire": {
            "description": "Work for Xavier 10 times",
            "condition": "Player.History.check('worked')",
            "goal": 10,
            "points": 5,
            "secret": False},

        "Seasoned Worker": {
            "description": "Work for Xavier 25 times",
            "condition": "Player.History.check('worked')",
            "goal": 25,
            "points": 10,
            "secret": False},

        "Busy Bee": {
            "description": "Work for Xavier 50 times",
            "condition": "Player.History.check('worked')",
            "goal": 50,
            "points": 20,
            "secret": False},

        "Rise and Grind": {
            "description": "Work for Xavier 100 times",
            "condition": "Player.History.check('worked')",
            "goal": 100,
            "points": 40,
            "secret": False},

        "Risin' Up, Back On the Streets": {
            "description": "Train 10 times",
            "condition": "Player.History.check('trained')",
            "goal": 10,
            "points": 5,
            "secret": False},

        "Did My Time, Took My Chances": {
            "description": "Train 25 times",
            "condition": "Player.History.check('trained')",
            "goal": 25,
            "points": 5,
            "secret": False},

        "Went the Distance, Now I'm Back on My Feet": {
            "description": "Train 50 times",
            "condition": "Player.History.check('trained')",
            "goal": 50,
            "points": 10,
            "secret": False},

        "Just a Man and His Will to Survive": {
            "description": "Train 100 times",
            "condition": "Player.History.check('trained')",
            "goal": 100,
            "points": 20,
            "secret": False},

        "What's A Hypothesis?": {
            "description": "Study 10 times",
            "condition": "Player.History.check('studied')",
            "goal": 10,
            "points": 5,
            "secret": False},

        "Bookworm": {
            "description": "Study 25 times",
            "condition": "Player.History.check('studied')",
            "goal": 25,
            "points": 5,
            "secret": False},

        "Serial Reader": {
            "description": "Study 50 times",
            "condition": "Player.History.check('studied')",
            "goal": 50,
            "points": 10,
            "secret": False},

        "Star Pupil": {
            "description": "Study 100 times",
            "condition": "Player.History.check('studied')",
            "goal": 100,
            "points": 20,
            "secret": False},

        "Pond Man": {
            "description": "Swim 10 times",
            "condition": "Player.History.check('swam')",
            "goal": 10,
            "points": 5,
            "secret": False},

        "Sea Man": {
            "description": "Swim 25 times",
            "condition": "Player.History.check('swam')",
            "goal": 25,
            "points": 5,
            "secret": False},

        "Aqua Man": {
            "description": "Swim 50 times",
            "condition": "Player.History.check('swam')",
            "goal": 50,
            "points": 10,
            "secret": False},

        "Bronze Shower": {
            "description": "Bath 10 times",
            "condition": "Player.History.check('showered')",
            "goal": 10,
            "points": 5,
            "secret": False},

        "Silver Shower": {
            "description": "Bath 25 times",
            "condition": "Player.History.check('showered')",
            "goal": 25,
            "points": 5,
            "secret": False},

        "Golde. . . Wait": {
            "description": "Bath 50 times",
            "condition": "Player.History.check('showered')",
            "goal": 50,
            "points": 10,
            "secret": False},

        "Date Night": {
            "description": "Go on a date for the first time",
            "condition": "Player.History.check('went_on_date')",
            "goal": 1,
            "points": 5,
            "secret": False},

        "First Blood!": {
            "description": "Have sex with a virgin",
            "condition": "Player.History.check('took_virginity')",
            "goal": 1,
            "points": 5,
            "secret": True},

        "Double Kill!": {
            "description": "Have two romantic partners",
            "condition": "len(Partners)",
            "goal": 2,
            "points": 5,
            "secret": True},

        "Triple Kill!": {
            "description": "Have three romantic partners",
            "condition": "len(Partners)",
            "goal": 3,
            "points": 5,
            "secret": True},

        "Aim for the Tits, Hawkeye": {
            "description": "Cum on someone's tits 10 times",
            "condition": "Player.History.check('cumshot_breasts')",
            "goal": 10,
            "points": 5,
            "secret": True}
            
            }