from Tkinter import *
import math
master = Tk()

canvas_width = 1200
canvas_height = 1000
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()


line_depth = canvas_width / math.sqrt(3)
line_gap = math.tan(math.pi/6) * 96
line_depth += 0.5 * line_gap

num_lines = int((canvas_width+line_depth) / line_gap)


# Draw Isometric grid
for i in range(int(num_lines)):
    w.create_line(0, i*line_gap-line_depth, canvas_width, i*line_gap, fill="grey")
    w.create_line(0, i*line_gap, canvas_width, i*line_gap-line_depth, fill="grey")



# NUMBER EACH CELL
def label_all_cells():
    for i in range((canvas_width / 96) + 1):
        for j in range(int(canvas_height / line_gap) * 2 - 1):
            if j % 2 == 1:
                w.create_text(i*92.5+46, canvas_height - 0.5 * j * line_gap - 0.5 * line_gap, text = (i,j))     # NMAGIC NUMBERS FOR NOW.. the 92s should be 96s because 1in = 96px... But 92 works better.
            else:
                w.create_text(i*92.5+92, canvas_height - 0.5 * j * line_gap - 0.5 * line_gap, text = (i,j))

def label_single_cell(x,y,text):
    if y % 2 == 1:
        w.create_text(x*92.5+46, canvas_height - 0.5 * y * line_gap - 0.5 * line_gap, text = text)     # NMAGIC NUMBERS FOR NOW.. the 92s should be 96s because 1in = 96px... But 92 works better.
    else:
        w.create_text(y*92.5+92, canvas_height - 0.5 * y * line_gap - 0.5 * line_gap, text = text)

def draw_box_room(x,y,size):         # Takes XY of top central box and length of each size (assumes regular size)
    tip_x = x*92.5+46
    tip_y = canvas_height - 0.5 * y * line_gap - line_gap
    if y % 2 == 0:
        tip_x = tip_x + 46.25
    right_x = tip_x + 46.25 * size
    left_x = tip_x - 46.25 * size
    side_y = tip_y + line_gap * size * 0.5
    bottom_y = tip_y + line_gap * size
    w.create_line(tip_x, tip_y, right_x, side_y , fill="black", width=2)
    w.create_line(tip_x, tip_y, left_x, side_y, fill="black", width=2)
    w.create_line(left_x, side_y, tip_x, bottom_y, fill="black", width=2)
    w.create_line(right_x, side_y, tip_x, bottom_y, fill="black", width=2)

def get_box_points(x,y,point):          # returns X,Y of one point of a cell
    ret_x = x*92.5+46
    ret_y = canvas_height - 0.5 * y * line_gap - line_gap
    if y % 2 == 0:
        ret_x = ret_x + 46.25
    if point == "bottom":
        return ret_x, (ret_y+line_gap)
    elif point == "left":
        return (ret_x - 46.25), (ret_y + 0.5*line_gap)
    elif point == "right":
        return (ret_x + 46.25), (ret_y + 0.5*line_gap)
    return ret_x, ret_y


def draw_upleft_stairs(x1,y1,x2,y2):
    upper_bottom_x, upper_bottom_y = get_box_points(x1,y1,"bottom")
    upper_right_x, upper_right_y = get_box_points(x1,y1,"right")
    lower_top_x, lower_top_y = get_box_points(x2,y2,"top")
    lower_left_x, lower_left_y = get_box_points(x2,y2,"left")

    # Draw lower left outline
    w.create_line(upper_bottom_x, upper_bottom_y, upper_bottom_x, lower_left_y, dash=True, width=2)
    w.create_line(upper_bottom_x, upper_bottom_y+line_gap, lower_left_x, lower_left_y, dash=True, width=2)
    w.create_line(upper_bottom_x, upper_bottom_y, lower_left_x, lower_left_y, width=2)
    w.create_line(upper_right_x, upper_right_y, lower_top_x, lower_top_y, width=2)

    # Draw 'steps'
    x_diff = float(abs(upper_bottom_x - lower_left_x))
    y_diff = float(abs(upper_bottom_y - lower_left_y))
    print x_diff, y_diff
    for i in range(1,7):
        w.create_line(upper_right_x + float(i/7.0) * x_diff, upper_right_y + float(i/7.0) * y_diff, upper_bottom_x + float(i/7.0) * x_diff, upper_bottom_y + float(i/7.0) * y_diff, width=2)



draw_box_room(7,16,5)
draw_box_room(4,24,3)
draw_box_room(6,22,2)
draw_upleft_stairs(6,20,7,16)
draw_upleft_stairs(4,20,6,13)

label_all_cells()

mainloop()
