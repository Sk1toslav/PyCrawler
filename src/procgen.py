import random


class Rect:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

    @property
    def center(self) -> tuple[int, int]:
        center_x = (self.x1 + self.x2) // 2
        center_y = (self.y1 + self.y2) // 2
        return center_x, center_y

    def intersects(self, other: "Rect") -> bool:
        return (
            self.x1 - 1 <= other.x2
            and self.x2 + 1 >= other.x1
            and self.y1 - 1 <= other.y2
            and self.y2 + 1 >= other.y1
        )


def generate_dungeon(
    max_rooms: int,
    room_min_size: int,
    room_max_size: int,
    map_width: int,
    map_height: int,
) -> tuple[list[list[int]], tuple[int, int], tuple[int, int]]:
    """Vygeneruje náhodnou mapu podzemí s garantovanými místnostmi a chodbami."""

    rooms: list[Rect] = []
    dungeon_map = [[1 for _ in range(map_width)] for _ in range(map_height)]

    for _ in range(max_rooms):
        w = random.randint(room_min_size, room_max_size)
        h = random.randint(room_min_size, room_max_size)

        x = random.randint(1, map_width - w - 1)
        y = random.randint(1, map_height - h - 1)

        new_room = Rect(x, y, w, h)

        if any(new_room.intersects(other_room) for other_room in rooms):
            continue

        for row in range(new_room.y1, new_room.y2):
            for col in range(new_room.x1, new_room.x2):
                dungeon_map[row][col] = 0

        if len(rooms) > 0:
            prev_x, prev_y = rooms[-1].center
            new_x, new_y = new_room.center

            if random.choice([True, False]):
                for col in range(min(prev_x, new_x), max(prev_x, new_x) + 1):
                    dungeon_map[prev_y][col] = 0
                for row in range(min(prev_y, new_y), max(prev_y, new_y) + 1):
                    dungeon_map[row][new_x] = 0
            else:
                for row in range(min(prev_y, new_y), max(prev_y, new_y) + 1):
                    dungeon_map[row][prev_x] = 0
                for col in range(min(prev_x, new_x), max(prev_x, new_x) + 1):
                    dungeon_map[new_y][col] = 0

        rooms.append(new_room)

    if len(rooms) < 2:
        return generate_dungeon(
            max_rooms, room_min_size, room_max_size, map_width, map_height
        )

    player_start = rooms[0].center
    stairs_pos = rooms[-1].center

    return dungeon_map, player_start, stairs_pos