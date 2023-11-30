default temperature = [20, 20, 20, 20]
default weather = None

default rain_probability = 0.0
default snow_left = 0

init python:

    def clamp(n, min, max):
        if n < min:
            return min
        elif n > max:
            return max
        else:
            return n

    def set_temperature():
        global season
        
        global temperature

        if season == 1:
            base_temperature = 15.0 + renpy.random.gauss(0.0, 1.0)
            lower = -2.0
            upper = 17.0
        elif season == 2:
            base_temperature = 2.0 + renpy.random.gauss(0.0, 1.0)
            lower = -6.0
            upper = 9.0
        elif season == 3:
            base_temperature = 15.0 + renpy.random.gauss(0.0, 1.0)
            lower = 4.0
            upper = 28.0
        elif season == 4:
            base_temperature = 25.0 + renpy.random.gauss(0.0, 1.0)
            lower = 14.0
            upper = 32.0

        temperature[0] = clamp(round(base_temperature - 3.0*abs(renpy.random.gauss(0.0, 1.0)), 1), lower, upper)
        temperature[1] = clamp(round(base_temperature, 1), lower, upper)
        temperature[2] = clamp(round(base_temperature - 1.0*abs(renpy.random.gauss(0.0, 1.0)), 1), lower, upper)
        temperature[3] = clamp(round(base_temperature - 5.0*abs(renpy.random.gauss(0.0, 1.0)), 1), lower, upper)

        return

    def set_weather():
        global temperature
        global weather

        global rain_probability
        global snow_left

        if time_index == 0:
            set_temperature()

        weather = None

        if snow_left > 0:
            weather = "snow"
        else:
            if renpy.random.random() > 1.0 - rain_probability:
                weather = "rain"

                rain_probability = 0.0

            if temperature[time_index] < 0 and weather == "rain":
                weather = "snow"

                snow_left = int(5.0*renpy.random.random())
                snow_left = 2 if snow_left < 2 else snow_left

        return