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


class TetrisApp(object):
    def __init__(self):
        pygame.init()
        self.width = config['cell_size'] * config['cols']
        self.height = config['cell_size'] * config['rows']
        self.logic = Logic()
        self.s = pygame.display.set_mode((self.width, self.height))
        colour = pygame.color.Color('#646400')
        pygame.event.set_blocked(pygame.MOUSEMOTION)  # We do not need
        # mouse movement
        # events, so we
        # block them.
        self.init_game()

    def init_game(self):
        self.draw_matrix(self.logic.screen)

    def draw_matrix(self, matrix):
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y]:
                    pygame.draw.rect(self.s,
                                     colors[matrix[x][y]],
                                     (y * config['cell_size'],
                                      x * config['cell_size'],
                                      1*config['cell_size'],
                                      1*config['cell_size']), 0)

    def run(self):
        pygame.time.set_timer(pygame.USEREVENT + 1, config['delay'])
        shape, column = self.logic.get_next_shape_version_and_column()
        upcoming_shape = self.logic.get_upcoming_shapes()
        # upcoming_shape = upcoming_shape[idx]
        if not (0 <= column < Logic.N and column + len(shape) < Logic.N):
            return 0
        while self.logic.move_down(shape, [column, 0]):
            self.draw_matrix(self.logic.screen)
            pygame.display.update()
            pygame.time.delay(100)
            rows_exploded = self.logic.check_for_rows_and_explode()
            if rows_exploded>0:
                self.logic.score += Logic.SCORE_PER_ROW * Logic.COMBO ** rows_exploded
            shape, column = self.logic.get_next_shape_version_and_column()
            upcoming_shape = self.logic.get_upcoming_shapes()
            if not (0 <= column < Logic.N and column + len(shape) < Logic.N):
                break
        pygame.time.delay(100)
        pygame.quit()
        return self.logic.score


if __name__ == '__main__':
    App = TetrisApp()
    print(App.run())
