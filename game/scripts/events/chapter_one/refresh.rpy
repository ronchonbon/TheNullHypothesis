label start_chapter_one_season_one:
    $ save_name = Player.full_name + "\nChapter I: Fall" + f"\nDay {season_day}"

    $ available_songs.append("Almost an Ending")
    $ available_songs.append("Danger Room")
    $ available_songs.append("Day to Day")
    $ available_songs.append("Evening")
    $ available_songs.append("Investigation")
    $ available_songs.append("Main Theme")
    $ available_songs.append("Rain")

    $ available_ringtones.append(0)
    $ available_ringtones.append(1)
    
    $ HumHumPool.update(
        HumHumThreadClass(
            "butt_itches", [
                HumHumClass(Logan, "My butt itches."),
                HumHumClass(Charles, "I wish I could feel my butt itch."),
                HumHumClass(Scott, "Professor! That's entirely inappropriate for someone of your station!"),
                HumHumClass(Charles, "I'm sorry everyone. Scott chose to be the fun police. Please halt all fun.")]))

    $ HumHumPool.update(
        HumHumThreadClass(
            "study_hard", [
                HumHumClass(Jean, "Make sure to study hard for your exams everyone!"),
                HumHumClass(Scott, "You're posting on social media instead of studying?"),
                HumHumClass(Jean, "So are you Scott! Excuse me for trying to be supportive of other students!")]))

    $ HumHumPool.update(
        HumHumThreadClass(
            "hot_cocoa", [
                HumHumClass(Jean, "Nothing beats a good cup of hot cocoa while studying.")]))

    $ HumHumPool.update(
        HumHumThreadClass(
            "garden", [
                HumHumClass(Ororo, "Today has been wonderful for the garden. The plants seem very pleased!")]))

    $ HumHumPool.update(
        HumHumThreadClass(
            "no_more_bamf", [
                HumHumClass(Kurt, "I already told, no more free teleports anymore! Stop asking!")]))

    $ HumHumPool.update(
        HumHumThreadClass(
            "smiley_face", [
                HumHumClass(Logan, "First person to put a smiley face on the back of Charles's head (with proof) gets an A in my class"),
                HumHumClass(Charles, "You do realize I can read minds, don't you?"),
                HumHumClass(Logan, "Make it an A+")]))

    $ HumHumPool.update(
        HumHumThreadClass(
            "try_beard", [
                HumHumClass(Kurt, "Zee latest issue of X-Men has me wearing a beard. . . I wonder if I should try it out?")]))

    $ HumHumPool.update(
        HumHumThreadClass(
            "badger_lived", [
                HumHumClass(Jean, "What the heck was that noise outside?!"),
                HumHumClass(Laura, "Don't worry about it"),
                HumHumClass(Jean, "Is Rogue screaming?!"),
                HumHumClass(Laura, "The important thing is that the badger lived.")]))

    $ HumHumPool.update(
        HumHumThreadClass(
            "new_student", [
                HumHumClass(Charles, "Just a brief announcement: we will have another new student joining us in the next few days."),
                HumHumClass(Charles, "He has already had an unfortunate run-in with some unfriendly individuals."),
                HumHumClass(Charles, "If we could all do our best to make him feel welcome, both he and I would greatly appreciate it.")]))
    
    $ HumHumPool.update(
        HumHumThreadClass(
            "Evan_rumors", [
                HumHumClass(Evan, "So. . . anyone hear anything about the new kid? Heard some interesting rumors about him."),
                HumHumClass(Kurt, "Looked into it already, don't get too excited, it turns out zat's actually a tail."),
                HumHumClass(Evan, "Not that kid and not those rumors!")]))

    $ HumHumPool.update(
        HumHumThreadClass(
            "rumor_control", [
                HumHumClass(Ororo, "The Professor has asked me to address some rumors."),
                HumHumClass(Ororo, "Yes, the new student appears to be able to able to 'turn off' the powers and abilities of other mutants."),
                HumHumClass(Ororo, "No, we're not sure how, this is as new to us as it is to anyone."),
                HumHumClass(Ororo, "And no, we don't know what that means exactly for other students."),
                HumHumClass(Ororo, "Until we do some further study, certain classes, such as flight training, will be put on hold for safety reasons.")]))
    
    return

label start_chapter_one_season_two:
    $ save_name = Player.full_name + "\nChapter I: Winter" + f"\nDay {season_day}"

    $ available_songs.append("Juggernaut")

    $ available_ringtones.append(2)

    $ HumHumPool.update(
        HumHumThreadClass(
            "special_assembly", [
                HumHumClass(Ororo, "There will be a special assembly at 12pm today to discuss recent events."),
                HumHumClass(Ororo, "All classes and activities will be cancelled until further notice.")]))

    $ HumHumPool.update(
        HumHumThreadClass(
            "defense_and_training", [
                HumHumClass(Logan, "Runnin' extra defense and trainin' sessions all day Sat/Sun."),
                HumHumClass(Logan, "Attendance ain't mandatory yet, but we've all had it too easy fer too long. That changes now.")]))

    # if Rogue in Partners:
    #     $ HumHumPool.update(
    #         HumHumThreadClass(
    #             "Evan_steal_your_powers", [
    #                 HumHumClass(Evan, "Shame Mr. Steal-Your-Powers didn't get to Juggernaut before he trashed the b-ball court."),
    #                 HumHumClass(Evan, "That's my plans for the weekend ruined!"),
    #                 HumHumClass(Rogue, "Not his fault, he did what he could."),
    #                 HumHumClass(Rogue, "And if you call him out like that again, Ms. Steal-Your-Powers here'll show y'all what that's really like"),
    #                 HumHumClass(Charles, "Both of you stop immediately: Rogue, to my office now, Evan, we'll have words later.")]))

    return

label start_chapter_one_season_three:
    $ save_name = Player.full_name + "\nChapter I: Spring" + f"\nDay {season_day}"

    $ available_songs.append("Sentinels")

    $ HumHumPool.update(
        HumHumThreadClass(
            "school_lockdown", [
                HumHumClass(Charles, "The school is in lockdown mode effective immediately. All on-duty staff and active team members, report to my office at once. All other students, head directly to the Danger Room."),
                HumHumClass(Charles, "The lockdown has been lifted, but we urge continued vigilance.")]))

    $ HumHumPool.update(
        HumHumThreadClass(
            "expanded_training", [
                HumHumClass(Logan, "That's it, trainin' sessions are gettin' ramped up. Everyone is expected to attend at least 3-4 sessions *a week*. This is *not* up for debate.")]))

    $ HumHumPool.update(
        HumHumThreadClass(
            "medbay", [
                HumHumClass(Ororo, "Admission to the medical bay will be by appointment only for the forseeable future. If you require treatment, please speak to a member of staff.")]))

    $ HumHumPool.update(
        HumHumThreadClass(
            "missing_Laura", [
                HumHumClass(Kurt, "Anyone seen Laura lately? I don't believe she vas wounded in zat. . . incident at zee mall, but if anyone knows where she is, could you let me know?"),
                HumHumClass(Laura, "Fine. Working on something important. Do not disturb.")]))

    $ HumHumPool.update(
        HumHumThreadClass(
            "counselor_talk", [
                HumHumClass(Ororo, "For anyone affected by the recent attack, we have enlisted the help of a counselor. Attendance is not mandatory, but will be encouraged if we feel you could benefit.")]))

    $ HumHumPool.update(
        HumHumThreadClass(
            "new_schedule", [
                HumHumClass(Charles, "Classes will resume next week. New schedules will be sent to each student. If you have any issues or queries, please come see me or your professors.")]))
        
    $ HumHumPool.update(
        HumHumThreadClass(
            "Null_recovery", [
                HumHumClass(Jean, f"Good news, looks like {Player.first_name} is out of the woods! He just woke up half an hour ago. Only allowed a few visitors right now, so if you want to pass on a message, just tell me or Rogue.")]))

    $ HumHumPool.update(
        HumHumThreadClass(
            "Kurt_worries", [
                HumHumClass(Kurt, "Word of advice, any of our more 'exotic'-looking bruder und schwestern planning on visiting town any time soon, be wary."),
                HumHumClass(Kurt, "I was getting some very. . . upset looks today from some of the people. Take care, meine freunde.")])) 
    
    $ HumHumPool.update(
        HumHumThreadClass(
            "Scott_worries", [
                HumHumClass(Scott, "Be careful if you're going into town. Seeing some angry faces with anti-mutant placards out there. And they're gaining friends."),
                HumHumClass(Scott, "Don't try and debate or engage with them, no matter what, just update each other with their whereabouts and get out of there.")]))

    $ HumHumPool.update(
        HumHumThreadClass(
            "hologram_development", [
                HumHumClass(Hank, "If we have any technologically-gifted students on campus this year, I would be eternally grateful if you could assist me with a project I'm working on."),
                HumHumClass(Hank, "Still very much in the early phases, but it could pay enormous dividends for your fellow students."),
                HumHumClass(Kurt, "Do we get credit for helping? >:p"),
                HumHumClass(Hank, "Is the eternal adoration of countless mutants worldwide not enough?"),
                HumHumClass(Kurt, "No, I get plenty of that already. But I could always use a pass in science.")]))

    $ HumHumPool.update(
        HumHumThreadClass(
            "new_powers", [
                HumHumClass(Evan, "Okay, I'm calling B.S. on this: apparently, the new kid is just growing new powers out of his a$$?"),
                HumHumClass(Evan, "What kinda nonsense is this?!"),
                HumHumClass(Armando, ":("),
                HumHumClass(Evan, "C'mon Darwin, you know I don't mean you!")]))

    return

label start_chapter_one_season_four:
    $ save_name = Player.full_name + "\nChapter I: Summer" + f"\nDay {season_day}"

    $ HumHumPool.update(
        HumHumThreadClass(
            "Logan_hunting", [
                HumHumClass(Ororo, "The mandatory training sessions are being paused: Professor Logan will be out of town for the next week on business."),
                HumHumClass(Ororo, "He has also asked me to remind you all that if you see him in or around town this week: 'No. No, you absolutely did not.'")]))

    $ HumHumPool.update(
        HumHumThreadClass(
            "town_offlimits", [
                HumHumClass(Charles, "Excursions into town will be temporarily suspended until the current panic settles."),
                HumHumClass(Charles, "We will, however, be organising group runs into the city as and when possible."),
                HumHumClass(Charles, "Further details and signup sheets will be available on the school portal.")]))

    $ HumHumPool.update(
        HumHumThreadClass(
            "group_activities", [
                HumHumClass(Scott, "As of today, I don't want to see anyone walking around alone, even on campus."),
                HumHumClass(Scott, "I want everyone in groups of three *minimum*."),
                HumHumClass(Scott, "Look out for each other out there.")]))

    return