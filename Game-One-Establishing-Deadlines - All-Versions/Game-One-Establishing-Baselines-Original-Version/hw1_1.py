# Olivia Riley 
# Game One, Part 1
# September 12, 2022

speed_light = 299792458
conversion_light_year = 9.461 * (10**15)
conversion_year_seconds = 31557600

def star_travel_time(distance,percent_speed):
    '''Calculates how much time will pass for astronaughts on way to star'''

    # Calculating factor based on percent speed 

    percent_speed = percent_speed * 0.01

    velocity = speed_light * percent_speed

    velocity_squared = velocity ** 2
    speed_light_squared = speed_light ** 2

    factor_under = 1 - (velocity_squared / speed_light_squared)
    factor_under_sqrt = factor_under ** (1/2)

    factor = 1 / factor_under_sqrt

    # Conversions / calculating time in years

    distance = distance * conversion_light_year
    speed = percent_speed * speed_light
    time = distance / speed
    time = time / conversion_year_seconds

    time_factor = time / factor

    # Displaying time result in years

    print(time_factor, "Years")
  

# Calling function star_travel_time
# Prior to running module, enter your desired distance (in light years) and percent speed, respectively. Click run, then start debugging. 
# Your answer should be desplayed in the terminal below.

star_travel_time(4.4,50)

# inputing 0 will result in the printing of nothing because on line 29, the percent_speed equaling 0 will cause time on line 30 to be undefined because an integer/0 is not possible without limits.
# inputing 100 will also result in the printing of nothing because on line 14, the percent speed will be 1, causing the factor_under variable to hold the value 0, making factor on line 30 an undefined value. 

