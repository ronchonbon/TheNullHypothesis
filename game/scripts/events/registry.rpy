init python:

    def all_Events():
        Events = [
            inclement_weather(),

            Player_forgot_to_shower(),
            Player_something_scheduled(),
            
            ch1_season_one_complete(),
            ch1_season_one_progress(),
            ch1_Juggernaut_attack(),
            
            ch1_season_two_complete(),
            ch1_season_two_progress(),
            ch1_Sentinel_attack(),

            ch1_season_three_complete(),
            ch1_season_three_progress(),
            ch1_mutant_hate()]

        return Events

    def all_Quests():
        Quests = [
            attend_class_weekly(),

            ch1_season_one_main_Quest(),
            ch1_season_two_main_Quest(),
            ch1_season_three_main_Quest(),
            ch1_season_four_main_Quest()]

        return Quests