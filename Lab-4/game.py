from board import Board
from ai import AI


class Battleship:
    def __init__(self):
        self.player = Board()
        self.enemy = Board()
        self.ai = AI()
        self._setup()

    def _setup(self):
        self.player.place_ship({(1, 1), (1, 2), (1, 3)})
        self.player.place_ship({(4, 0), (4, 1)})
        self.player.place_ship({(0, 5)})

        self.enemy.place_ship({(2, 2), (2, 3), (2, 4)})
        self.enemy.place_ship({(4, 0), (5, 0)})
        self.enemy.place_ship({(0, 5)})

    def show(self):
        remaining = sum(
            len(ship["cells"] - ship["hits"])
            for ship in self.enemy.ships
        )

        print("\nYour shots are coordinates like 2,3.")
        print("Enemy ship cells remaining:", remaining)

    def run(self):
        print("Battleship")

        while True:
            self.show()

            raw = input("> ").strip().lower()

            if raw == "q":
                print("Game quit.")
                return

            try:
                r, c = map(int, raw.split(","))
                pos = (r - 1, c - 1)
            except ValueError:
                print("Use row,col.")
                continue

            if not (0 <= pos[0] < Board.SIZE and 0 <= pos[1] < Board.SIZE):
                print("Outside board.")
                continue

            result = self.enemy.fire(pos)

            if result == "REPEAT":
                print("Already fired there.")
                continue

            if result == "HIT":
                print("HIT!")
            elif result == "SUNK":
                print("HIT! You sank a ship.")
            else:
                print("MISS!")

            if self.enemy.all_sunk():
                print("You sank the entire fleet. You win!")
                return

            ai_pos = self.ai.choose()

            if ai_pos is None:
                print("AI has no remaining shots.")
                return

            print(
                "AI fired at",
                f"{ai_pos[0] + 1},{ai_pos[1] + 1}"
            )

            ai_result = self.player.fire(ai_pos)

            if ai_result == "HIT":
                print("AI scored a hit.")
                self.ai.record_hit(ai_pos)

            elif ai_result == "SUNK":
                print("AI sank one of your ships.")
                self.ai.record_hit(ai_pos)

            elif ai_result == "MISS":
                print("AI missed.")