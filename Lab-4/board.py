class Board:
    SIZE = 6

    def __init__(self):
        self.ships = []
        self.shots = set()

    def place_ship(self, cells):
        self.ships.append({
            "cells": set(cells),
            "hits": set()
        })

    def fire(self, pos):
        if pos in self.shots:
            return "REPEAT"

        self.shots.add(pos)

        for ship in self.ships:
            if pos in ship["cells"]:
                ship["hits"].add(pos)

                if ship["cells"] <= ship["hits"]:
                    return "SUNK"

                return "HIT"

        return "MISS"

    def all_sunk(self):
        return all(ship["cells"] <= ship["hits"] for ship in self.ships)