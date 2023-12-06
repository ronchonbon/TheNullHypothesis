init python:
    
    def check_predicted_images(loading = False):
        temp = renpy.list_files()
        file_list = []

        for file in temp:
            if ".webp" in file:
                file_list.append(file)

        for C in all_Characters:
            if C in Sprites:
                if C in active_Companions:
                    predict_images(C, file_list)
                elif C in active_NPCs:
                    renpy.start_predict(f"characters/{C.tag}/images/*.webp")
                else:
                    if C in all_Companions:
                        renpy.stop_predict(f"characters/{C.tag}/images/standing/*.webp")
                        renpy.stop_predict(f"characters/{C.tag}/images/doggy/*.webp")
                        renpy.stop_predict(f"characters/{C.tag}/images/hands_and_knees/*.webp")
                        renpy.stop_predict(f"characters/{C.tag}/images/masturbation/*.webp")
                        renpy.stop_predict(f"characters/{C.tag}/images/missionary/*.webp")
                    else:
                        renpy.stop_predict(f"characters/{C.tag}/images/*.webp")

        # if loading:
        #     renpy.pause(hard = True, predict = True)

        return

    def predict_images(Character, file_list):
        possible_poses = ["doggy", "hands_and_knees", "masturbation", "missionary"]
        poses = ["standing"]

        for pose in possible_poses:
            if approval_check(Character, threshold = pose):
                poses.append(pose)

        files_to_predict = []
        files_to_forget = []

        for pose in poses:
            for file in file_list:
                if f"characters/{Character.tag}/images/" in file and f"/{pose}/" in file:
                    if pose == "standing" or pose == Character.position:
                        files_to_predict.append(file)
                    # elif Character.location == Player.location:
                    #     files_to_predict.append(file)
                    else:
                        files_to_forget.append(file)
        
        for file in files_to_forget:
            renpy.stop_predict(file)

        for file in files_to_predict:
            predict = False

            checklist = [
                "body.webp",
                "ground_shadow.webp",
                "arm",
                "breasts",
                "pubes",
                "head",
                "hair",
                "brows_",
                "eyes_",
                "mouth_",
                "blush",

                "/torso",
                "hand",
                "thumb",
                "/ass",
                "/thighs",
                "/right_leg",
                "/right_foot",
                "/left_leg",
                "/left_foot",
                "pussy",
                "anus",
                "/mask",
                "tongue",

                "makeup",
                "tan_lines",
                "spunk",
                "creampie",

                "dildo",
                "vibrator",

                "claw",
                "psychic"]

            for item in checklist:
                if item in file:
                    predict = True

                    break

            if not predict:
                if "male" in file or "cock" in file:
                    if Player.skin_color in file:
                        predict = True

            if not predict:
                if "piercing" in file:
                    if "nipple" in file:
                        if "barbell" in file and Character.piercings["nipple"] in ["barbell", "both"]:
                            predict = True

                        if "ring" in file and Character.piercings["nipple"] in ["ring", "both"]:
                            predict = True

                    if "labia" in file:
                        if "barbell" in file and Character.piercings["labia"] in ["barbell", "both"]:
                            predict = True

                        if "ring" in file and Character.piercings["labia"] in ["ring", "both"]:
                            predict = True

                    if "belly" in file:
                        if Character.piercings["belly"]:
                            predict = True

            if not predict:
                if renpy.get_screen("Wardrobe_screen") and focused_Character == Character:
                    for C in Character.Wardrobe.Clothes.values():
                        if C.string and C.string in file:
                            predict = True

                            break
                else:
                    for Outfit_type in ["outdoor_Outfit", "indoor_Outfit", "private_Outfit", "gym_Outfit", "superhero_Outfit", "swimming_Outfit", "date_Outfit", "sleeping_Outfit"]:
                        Outfit = getattr(Character.Wardrobe, Outfit_type)

                        for C in Outfit.Clothes.values():
                            if C.string and C.string in file:
                                predict = True

                                break

            if predict:
                renpy.start_predict(file)
            else:
                renpy.stop_predict(file)

        return