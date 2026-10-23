import sys
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 32

GRID_WIDTH = SCREEN_WIDTH // TILE_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // TILE_SIZE

COLOR_BG = (20, 20, 20)
COLOR_GRID = (40, 40, 40)
COLOR_WALL = (100, 100, 100)
COLOR_PLAYER = (50, 205, 50)

TEST_MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


class Player:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, dx: int, dy: int, game_map: list[list[int]]):
        new_x = self.x + dx
        new_y = self.y + dy

        if 0 <= new_y < len(game_map) and 0 <= new_x < len(game_map[0]):
            if game_map[new_y][new_x] != 1:
                self.x = new_x
                self.y = new_y

    def render(self, screen: pygame.Surface):
        player_rect = pygame.Rect(
            self.x * TILE_SIZE,
            self.y * TILE_SIZE,
            TILE_SIZE,
            TILE_SIZE
        )
        pygame.draw.rect(screen, COLOR_PLAYER, player_rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("PyCrawler - Milestone 1")
    clock = pygame.time.Clock()

    player = Player(x=1, y=1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                dx, dy = 0, 0
                if event.key in (pygame.K_w, pygame.K_UP):
                    dy = -1
                elif event.key in (pygame.K_a, pygame.K_LEFT):
                    dx = -1
                elif event.key in (pygame.K_s, pygame.K_DOWN):
                    dy = 1
                elif event.key in (pygame.K_d, pygame.K_RIGHT):
                    dx = 1

                player.move(dx, dy, TEST_MAP)

        screen.fill(COLOR_BG)

        for row_idx, row in enumerate(TEST_MAP):
            for col_idx, tile in enumerate(row):
                if tile == 1:
                    wall_rect = pygame.Rect(
                        col_idx * TILE_SIZE,
                        row_idx * TILE_SIZE,
                        TILE_SIZE,
                        TILE_SIZE
                    )
                    pygame.draw.rect(screen, COLOR_WALL, wall_rect)

        for x in range(0, SCREEN_WIDTH, TILE_SIZE):
            pygame.draw.line(screen, COLOR_GRID, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            pygame.draw.line(screen, COLOR_GRID, (0, y), (SCREEN_WIDTH, y))

        player.render(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()