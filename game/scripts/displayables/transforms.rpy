init -99:

    transform change_anchor(x, y):
        subpixel True
        transform_anchor True

        anchor (x, y)

    transform change_pos(x, y):
        subpixel True
        transform_anchor True

        pos (x, y)

    transform change_offset(x, y):
        subpixel True
        transform_anchor True

        offset (x, y)

    transform change_sprite_anchor(x, y):
        subpixel True
        transform_anchor True

        anchor (x, y)

    transform move_sprite(x, y, t = 0.0):
        subpixel True
        transform_anchor True

        ease t pos (x, y)

    transform zoom_sprite(factor, t = 0.0):
        subpixel True
        transform_anchor True
        
        ease t zoom factor

    transform rotate_sprite(theta, t = 0.0):
        subpixel True
        transform_anchor True
        
        ease t rotate theta
        
    transform hover:
        matrixcolor BrightnessMatrix(0.05)

    transform silhouette:
        matrixcolor TintMatrix(Color(rgb = (0.3, 0.4, 0.4)))*OpacityMatrix(0.95)*BrightnessMatrix(-0.9)

    transform color_shade(color_string):
        matrixcolor TintMatrix(color_string)*ContrastMatrix(0.0)

    transform morning:
        matrixcolor TintMatrix(Color(rgb = (1.0, 0.95, 0.9)))*BrightnessMatrix(0.04)

    transform daylight:
        matrixcolor TintMatrix(Color(rgb = (1.0, 1.0, 1.0)))*BrightnessMatrix(0.02)

    transform sunset:
        matrixcolor TintMatrix(Color(rgb = (1.0, 0.8, 0.65)))*BrightnessMatrix(0.01)

    transform moonlight:
        matrixcolor TintMatrix(Color(rgb = (0.5, 0.6, 1.0)))*BrightnessMatrix(0.0)

    transform raining:
        matrixcolor ContrastMatrix(0.9)*SaturationMatrix(0.8)

    transform indoors:
        matrixcolor TintMatrix(Color(rgb = (1.0, 1.0, 1.0)))*BrightnessMatrix(0.0)

    transform lights_off:
        matrixcolor TintMatrix(Color(rgb = (0.45, 0.45, 0.65)))*BrightnessMatrix(-0.07)

    transform candlelit:
        matrixcolor TintMatrix(Color(rgb = (1.0, 0.93, 0.93)))*BrightnessMatrix(-0.06)

    transform theater:
        matrixcolor TintMatrix(Color(rgb = (0.45, 0.45, 0.65)))*BrightnessMatrix(-0.05)

    transform red_lights:
        matrixcolor TintMatrix(Color(rgb=(1.0, 0.7, 0.7)))*BrightnessMatrix(0.0)

    transform shadow:
        matrixcolor ContrastMatrix(0.9)*SaturationMatrix(0.9)*BrightnessMatrix(-0.05)

    transform deep_shadow:
        matrixcolor ContrastMatrix(0.8)*SaturationMatrix(0.7)*BrightnessMatrix(-0.1)

    transform depth_of_field:
        blur 0

    transform love_color:
        matrixcolor TintMatrix("#c11b17")

    transform trust_color:
        matrixcolor TintMatrix("#2554c7")

    transform desire_color:
        matrixcolor TintMatrix("#f3a3b3")

    transform spinning_element:
        subpixel True
        transform_anchor True
        animation

        block:
            rotate 0
            linear 60.0 rotate 360
            repeat

    transform blurred_background:
        blur 100

    transform interface:
        transform_anchor True

        align (0.5, 0.5)
        zoom interface_adjustment

    transform customization_portrait:
        transform_anchor True

        align (0.5, 0.5)
        zoom 0.5

    transform database_photo:
        transform_anchor True

        align (0.5, 0.5)
        zoom 0.45

    transform call_photo:
        transform_anchor True

        align (0.5, 0.5)
        zoom 0.55

    transform humhum_photo:
        transform_anchor True

        align (0.5, 0.5)
        zoom 0.5

    transform phone_icon:
        transform_anchor True

        align (0.5, 0.5)
        zoom 0.5

    transform call_icon:
        transform_anchor True

        align (0.5, 0.5)
        zoom 0.35

    transform humhum_icon:
        transform_anchor True

        align (0.5, 0.5)
        zoom 0.18

    transform mini_humhum_icon:
        transform_anchor True

        align (0.5, 0.5)
        zoom 0.12

    transform map_icon:
        transform_anchor True

        align (0.5, 0.5)
        zoom 0.15

    transform Wardrobe_transform(t, a, xy, z):
        subpixel True
        transform_anchor True
        
        ease t anchor (a[0], a[1]) pos (xy[0], xy[1]) zoom z