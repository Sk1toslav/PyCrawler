import math


def compute_fov(
    game_map: list[list[int]],
    player_x: int,
    player_y: int,
    radius: int = 6,
) -> set[tuple[int, int]]:
    """Vypočítá množinu souřadnic (x, y), na které hráč aktuálně vidí."""
    visible_tiles: set[tuple[int, int]] = {(player_x, player_y)}

    map_height = len(game_map)
    map_width = len(game_map[0])

    for angle_deg in range(360):
        rad = math.radians(angle_deg)
        dx = math.cos(rad)
        dy = math.sin(rad)

        x = player_x + 0.5
        y = player_y + 0.5

        for _ in range(radius * 2):
            x += dx * 0.5
            y += dy * 0.5

            tile_x = int(x)
            tile_y = int(y)

            if not (0 <= tile_x < map_width and 0 <= tile_y < map_height):
                break

            if (tile_x - player_x) ** 2 + (tile_y - player_y) ** 2 > radius ** 2:
                break

            visible_tiles.add((tile_x, tile_y))

            if game_map[tile_y][tile_x] == 1:
                break

    return visible_tiles