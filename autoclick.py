import random
import pyautogui as py

collect_exp_points = (464,213)
click_me = (490, 430)
buy_these_y_axis = 635
buy_these_x_axis_lower_range = 150
#buy_these_x_axis_upper_range = 650
buy_these_x_axis_upper_range = 446 # Use this to avoid clicking the waterfall
buy_these_x_step_size = 10
console_position = ( 1500, 500 )
while True:
    for i in range( 2000 ):
        py.PAUSE = 0.01

        py.click(x=collect_exp_points[0],y=collect_exp_points[1])
        py.click(x=click_me[0],y=click_me[1])
        py.click(x=random.randrange(buy_these_x_axis_lower_range,buy_these_x_axis_upper_range,buy_these_x_step_size),y=buy_these_y_axis)
    py.click(x=console_position[0],y=console_position[1])
    a = input( '> ' )
