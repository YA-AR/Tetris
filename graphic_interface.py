import pygame
from tetris_logic import Logic

# The configuration
config = {
    'cell_size': 20,
    'cols': Logic.N,
    'rows': Logic.M,
    'delay': 750,
    'maxfps': 30
}

colors = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 150, 0),
    (0, 0, 255),
    (255, 120, 0),
    (255, 255, 0),
    (180, 0, 255),
    (0, 220, 220)]


class TetrisApp:
    def __init__(self, weights, flag = False):

        self.draw = flag

        if self.draw:
            pygame.init()

        self.width = config['cell_size'] * config['cols']
        self.height = config['cell_size'] * config['rows']
        self.logic = Logic(weights)
        if self.draw:
            self.s = pygame.display.set_mode((self.width, self.height))
            colour = pygame.color.Color('#646400')
            pygame.event.set_blocked(pygame.MOUSEMOTION)  # We do not need
        # mouse movement
        # events, so we
        # block them.
        self.init_game()
        self.ret = self.run()

    def init_game(self):
        if self.draw:
            self.draw_matrix(self.logic.screen)

    def draw_matrix(self, matrix):
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                pygame.draw.rect(self.s,
                                     colors[matrix[x][y]],
                                     (y * config['cell_size'],
                                      x * config['cell_size'],
                                      1*config['cell_size'],
                                      1*config['cell_size']), 0)

    def run(self):
        pygame.time.set_timer(pygame.USEREVENT + 1, config['delay'])
        shape, column = self.logic.get_next_shape_version_and_column()
        if not (0 <= column < Logic.N and column + len(shape) < Logic.N):
            return 0
        while self.logic.move_down(shape, [0, column]):
            if self.draw:
                self.draw_matrix(self.logic.screen)
                pygame.display.update()
                pygame.time.delay(50)
            rows_exploded = self.logic.check_for_rows_and_explode()
            if rows_exploded > 0:
                self.logic.score += Logic.SCORE_PER_ROW * Logic.COMBO ** rows_exploded
                if self.draw:
                    pygame.time.delay(50)
            shape, column = self.logic.get_next_shape_version_and_column()
            upcoming_shape = self.logic.get_upcoming_shapes()
            if self.draw:
                pygame.time.delay(50)
        if self.draw:
            pygame.time.delay(100)
            pygame.quit()
        return self.logic.score


def graphic(weights, draw):
    a = TetrisApp(weights, draw)
    return a.ret




