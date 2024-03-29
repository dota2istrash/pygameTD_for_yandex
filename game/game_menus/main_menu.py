import sys
import pygame as pg

from utils.SETTINGS import COLOURS, SCREEN_HEIGHT, SCREEN_WIDTH
from utils.helper_classes import Vec
from utils.text_functions import outline_text


def main_menu(img):
	start_game = False
	screen_width = SCREEN_WIDTH
	screen_height = SCREEN_HEIGHT
	screen = pg.display.set_mode((screen_width, screen_height))
	screen_rect = screen.get_rect()

	name_font = pg.font.Font(None, 125)
	font = pg.font.Font(None, 45)
	name_font.set_bold(True)
	font.set_bold(True)
	game_name = outline_text(name_font, "Castle Defender", COLOURS["white"], COLOURS["black"])
	g_rect = game_name.get_rect(center = screen_rect.midtop + Vec(0, screen_height//4))
	instruction = outline_text(font, "Press any button to PLAY", COLOURS["green"], COLOURS["black"])
	i_rect = instruction.get_rect(center = screen_rect.center)
	quit = outline_text(font, "Press 'Esc' to QUIT", COLOURS["crimson"], COLOURS["black"])
	q_rect = quit.get_rect(center = screen_rect.midbottom + Vec(0, -screen_height//4))

	fade = pg.surface.Surface((screen_width, screen_height))
	fade.fill(COLOURS["black"])
	fade.set_alpha(100)

	while not start_game:
		# shorten the pg get pressed function to 'keyPress'
		keyPress = pg.key.get_pressed()

		# Start event loop.
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()

			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					sys.exit()

				else:
					screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
					return True

		screen.blit(img, screen_rect)
		screen.blit(fade, screen_rect)
		screen.blit(game_name, g_rect)
		screen.blit(instruction, i_rect)
		screen.blit(quit, q_rect)

		pg.display.set_caption("Foxy Towers")
		pg.display.update()
