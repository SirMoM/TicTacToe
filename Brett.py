# -*- coding: utf-8 -*-

import pygame as pg
import sys

from Utility import Utility

__author__ = "Noah Ruben"
__copyright__ = "Noah Ruben"
__version__ = "v1.0"
__email__ = "noah.ruben@online.de"
__status__ = "development"


class Brett:
    display_Message = ""  # type: str

    font = pg.font.get_default_font()

    turn = 0

    next_Player = 0

    crosses = []

    circles = []

    mouse_Pos = []

    top_right = [250, 50]
    top_center = [150, 50]
    top_left = [50, 50]

    mid_right = [250, 150]
    mid_center = [150, 150]
    mid_left = [50, 150]

    bot_right = [250, 250]
    bot_center = [150, 250]
    bot_left = [50, 250]

    all_Positions = []

    def __init__(self):
        pg.init()
        print("Pygame init")

        # initialize pygame clock
        self.clock = pg.time.Clock()

        # initialize the screen with title
        self.screen = pg.display.set_mode((300, 300))
        pg.display.set_caption("Tick Tac Toe")

        # make the screen white
        self.screen.fill(Utility.green)

        # draw the game.view
        self.draw_board()

    def draw_board(self):
        print("drew board")
        self.draw_Tic_Tac_Toe_Grid()

    def update(self):
        """
        periodically updates the game, calls the graphics and receives user input
        """
        # sleep to make the game 60 fps
        self.clock.tick(30)

        # make the screen white
        self.screen.fill(Utility.green)

        # Win ?
        print("Cross Win: ", self.check_Win_Crosses)
        print("Cross Win: ", self.check_Win_Circles())

        # draw the board
        self.draw_board()
        self.show_win()

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                print("Mouse button down I repeat Mouse button down!")
                self.mouse_Pos = event.pos
                if self.next_Player == 0:
                    self.circles.append(self.get_Point_On_Board_From_Mouse_Pos(self.mouse_Pos))
                    self.next_Player = 1
                    self.turn += 1
                else:
                    self.crosses.append(self.get_Point_On_Board_From_Mouse_Pos(self.mouse_Pos))
                    self.next_Player = 0
                    self.turn += 1

            # quit if the quit button was pressed
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        self.draw_Player_Moves()

        # update the screen
        pg.display.flip()

    def draw_Tic_Tac_Toe_Grid(self):
        point_A_Line_A = [100, 25]
        point_B_Line_A = [100, 275]

        point_A_Line_B = [200, 25]
        point_B_Line_B = [200, 275]

        point_A_Line_C = [25, 100]
        point_B_Line_C = [275, 100]

        point_A_Line_D = [25, 200]
        point_B_Line_D = [275, 200]

        pg.draw.line(self.screen, Utility.black, point_A_Line_A, point_B_Line_A, 5)
        pg.draw.line(self.screen, Utility.black, point_A_Line_B, point_B_Line_B, 5)
        pg.draw.line(self.screen, Utility.black, point_A_Line_C, point_B_Line_C, 5)
        pg.draw.line(self.screen, Utility.black, point_A_Line_D, point_B_Line_D, 5)

    def draw_cross(self, position):
        point_A_Line_A = [position[0] - 40, position[1] - 40]
        point_B_Line_A = [position[0] + 40, position[1] + 40]

        point_A_Line_B = [position[0] + 40, position[1] - 40]
        point_B_Line_B = [position[0] - 40, position[1] + 40]

        pg.draw.line(self.screen, Utility.black, point_A_Line_A, point_B_Line_A, 5)

        pg.draw.line(self.screen, Utility.black, point_A_Line_B, point_B_Line_B, 5)

        print("drew cross")

    def draw_circle(self, position):
        print("drew cross")
        pg.draw.circle(self.screen, Utility.black, position, 40, 5)

    def draw_Player_Moves(self):
        if self.turn > 9:
            self.reset()

        for position in self.circles:
            self.draw_circle(position)

        for position in self.crosses:
            self.draw_cross(position)

    def get_Point_On_Board_From_Mouse_Pos(self, pos_mouse):
        if 200 < pos_mouse[0] < 300:
            if 0 < pos_mouse[1] < 100:
                return self.top_right
            elif 100 < pos_mouse[1] < 200:
                return self.mid_right
            elif 200 < pos_mouse[1] < 300:
                return self.bot_right
        elif 100 < pos_mouse[0] < 200:
            if 0 < pos_mouse[1] < 100:
                return self.top_center
            elif 100 < pos_mouse[1] < 200:
                return self.mid_center
            elif 200 < pos_mouse[1] < 300:
                return self.bot_center
        elif 0 < pos_mouse[0] < 100:
            if 0 < pos_mouse[1] < 100:
                return self.top_left
            elif 100 < pos_mouse[1] < 200:
                return self.mid_left
            elif 200 < pos_mouse[1] < 300:
                return self.bot_left

    @property
    def check_Win_Crosses(self):
        # Top Row
        if self.crosses.__contains__(self.top_left) and self.crosses.__contains__(
                self.top_center) and self.crosses.__contains__(self.top_right):
            return True
        # Mid Row
        elif self.crosses.__contains__(self.mid_left) and self.crosses.__contains__(
                self.mid_center) and self.crosses.__contains__(self.mid_right):
            return True
        # Bot Row
        elif self.crosses.__contains__(self.bot_left) and self.crosses.__contains__(
                self.bot_center) and self.crosses.__contains__(self.bot_right):
            return True
        # Left Collum
        elif self.crosses.__contains__(self.top_left) and self.crosses.__contains__(
                self.mid_left) and self.crosses.__contains__(self.bot_left):
            return True
        # Mid Collum
        elif self.crosses.__contains__(self.top_center) and self.crosses.__contains__(
                self.mid_center) and self.crosses.__contains__(self.bot_center):
            return True
        # Right Collum
        elif self.crosses.__contains__(self.top_left) and self.crosses.__contains__(
                self.mid_left) and self.crosses.__contains__(self.bot_left):
            return True
        # Right Diagonal
        elif self.crosses.__contains__(self.top_right) and self.crosses.__contains__(
                self.mid_center) and self.crosses.__contains__(self.bot_left):
            return True
        # Left Diagonal
        elif self.crosses.__contains__(self.top_left) and self.crosses.__contains__(
                self.mid_center) and self.crosses.__contains__(self.bot_right):
            return True
        else:
            return False

    def check_Win_Circles(self):
        # Top Row
        if self.circles.__contains__(self.top_left) and self.circles.__contains__(
                self.top_center) and self.circles.__contains__(self.top_right):
            return True
        # Mid Row
        elif self.circles.__contains__(self.mid_left) and self.circles.__contains__(
                self.mid_center) and self.circles.__contains__(self.mid_right):
            return True
        # Bot Row
        elif self.circles.__contains__(self.bot_left) and self.circles.__contains__(
                self.bot_center) and self.circles.__contains__(self.bot_right):
            return True
        # Left Collum
        elif self.circles.__contains__(self.top_left) and self.circles.__contains__(
                self.mid_left) and self.circles.__contains__(self.bot_left):
            return True
        # Mid Collum
        elif self.circles.__contains__(self.top_center) and self.circles.__contains__(
                self.mid_center) and self.circles.__contains__(self.bot_center):
            return True
        # Right Collum
        elif self.circles.__contains__(self.top_left) and self.circles.__contains__(
                self.mid_left) and self.circles.__contains__(self.bot_left):
            return True
        # Right Diagonal
        elif self.circles.__contains__(self.top_right) and self.circles.__contains__(
                self.mid_center) and self.circles.__contains__(self.bot_left):
            return True
        # Left Diagonal
        elif self.circles.__contains__(self.top_left) and self.circles.__contains__(
                self.mid_center) and self.circles.__contains__(self.bot_right):
            return True
        else:
            return False

    def reset(self):
        self.crosses = []
        self.circles = []
        self.turn = 0

    def show_win(self):
        self.screen.blit(self.screen, self, self.mid_center)
