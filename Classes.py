"""
Key class   : game
            :Library

"""

from __future__ import annotations
import math
from typing import List, Optional


def merge(lst1: list, lst2: list) -> list:
    """Return a sorted list with the elements in <lst1> and <lst2>.
    """

    i1 = 0
    i2 = 0
    new_list = []

    while i1 < len(lst1) and i2 < len(lst2):
        if lst1[i1] < lst2[i2]:
            new_list.append(lst1[i1])
            i1 += 1
        else:
            new_list.append(lst2[i2])
            i2 += 1

    new_list.extend(lst1[i1:])
    new_list.extend(lst2[i2:])

    return new_list


class Game:
    """
    Holds all information about a particular game

    Attributes:

    Name of game|
        following are lists of raw info
    genre exemplar|
    influence|
    gameplay|
    themes|
    functionality|
    fun|
        These are repeated for average scores as well

    """

    _raw_data: List[str]

    # This way of holding the lists is garbage, a nested list or dictionary of lists would have been far better
    # but I can't be bothered to refactor this
    _name: str
    _genre: list[int]
    _influence: list[int]
    _gameplay: list[int]
    _themes: list[int]
    _functionality: list[int]
    _fun: list[int]

    # if I were to redo this projects, these variables would be in a list or dictionary as doing them this way
    # is awful
    _average_genre: int
    _average_influence: int
    _average_gameplay: int
    _average_themes: int
    _average_functionality: int
    _average_fun: int

    _total_score: int

    def __init__(self, data: list[str]):
        self._raw_data = data

        workable_data = data

        self._name = workable_data[0]
        self._genre = [int(workable_data[1])]
        self._influence = [int(workable_data[2])]
        self._gameplay = [int(workable_data[3])]
        self._themes = [int(workable_data[4])]
        self._functionality = [int(workable_data[5])]
        self._fun = [int(workable_data[6])]

        self._average_genre = 0
        self._average_influence = 0
        self._average_gameplay = 0
        self._average_themes = 0
        self._average_functionality = 0
        self._average_fun = 0

        self._total_score = 0

    def __iter__(self):
        return self._total_score

    def __lt__(self, other):
        return self.get_total_score() > other.get_total_score()

    def get_name(self) -> str:
        return self._name

    def get_genre(self) -> list[int]:
        return self._genre

    def get_influence(self) -> list[int]:
        return self._influence

    def get_gameplay(self) -> list[int]:
        return self._gameplay

    def get_themes(self) -> list[int]:
        return self._themes

    def get_functionality(self) -> list[int]:
        return self._functionality

    def get_fun(self) -> list[int]:
        return self._fun

    def add_genre(self, genre: int):
        self._genre.append(genre)

    def add_influence(self, genre: int):
        self._influence.append(genre)

    def add_gameplay(self, genre: int):
        self._gameplay.append(genre)

    def add_themes(self, genre: int):
        self._themes.append(genre)

    def add_functionality(self, genre: int):
        self._functionality.append(genre)

    def add_fun(self, genre: int):
        self._fun.append(genre)

    def add_data(self, data: list[str]):
        self.add_genre(int(data[1]))
        self.add_influence(int(data[2]))
        self.add_gameplay(int(data[3]))
        self.add_themes(int(data[4]))
        self.add_functionality(int(data[5]))
        self.add_fun(int(data[6]))

    def update_averages(self):
        total = 0
        for genre in self.get_genre():
            total += genre
        self._average_genre = math.floor(total / len(self.get_genre()))

        total = 0
        for influence in self.get_influence():
            total += influence
        self._average_influence = math.floor(total / len(self.get_influence()))

        total = 0
        for gameplay in self.get_gameplay():
            total += gameplay
        self._average_gameplay = math.floor(total / len(self.get_gameplay()))

        total = 0
        for theme in self.get_themes():
            total += theme
        self._average_themes = math.floor(total / len(self.get_themes()))

        total = 0
        for functionality in self.get_functionality():
            total += functionality
        self._average_functionality = math.floor(total / len(self.get_functionality()))

        total = 0
        for fun in self.get_fun():
            total += fun
        self._average_fun = math.floor(total / len(self.get_fun()))

    def get_genre_average(self) -> int:
        return self._average_genre

    def get_influence_average(self) -> int:
        return self._average_influence

    def get_gameplay_average(self) -> int:
        return self._average_gameplay

    def get_themes_average(self) -> int:
        return self._average_themes

    def get_functionality_average(self) -> int:
        return self._average_functionality

    def get_fun_average(self) -> int:
        return self._average_fun

    def calculate_total_score(self):
        # each aspect is currently rated equally as the project is ongoing.
        self._total_score = math.floor((1 * self.get_genre_average()) + (1 * self.get_influence_average()) +
                                       (1 * self.get_gameplay_average()) + (1 * self.get_themes_average()) +
                                       (1 * self.get_functionality_average()) + (1 * self.get_fun_average()))

    def get_total_score(self) -> int:
        return self._total_score


class Library:
    """
    hold a list of games, and their names

    """

    _games = list[Game]
    _names = list[str]

    def __init__(self):
        self._games = []
        self._names = []

    def get_names(self) -> list[str]:
        return self._names

    def add_game(self, data: str):
        workable_data = data.split(sep="|")

        if len(workable_data) >= 7:  # This confirms the data is in a workable form for the rest of the calculations

            for x in range(6):
                try:
                    if int(workable_data[x + 1]) > 100:
                        workable_data[x + 1] = 100
                    if int(workable_data[x + 1]) < 0:
                        workable_data[x + 1] = 0
                except ValueError:
                    workable_data[x + 1] = 0

            exists = False
            found_name = []
            for name in self.get_names():
                if name == workable_data[0]:
                    exists = True
                    found_name = name

            if not exists:
                game = Game(workable_data)
                self._games.append(game)
                self._names.append(game.get_name())
            elif exists:
                game = self.get_game_with_name(found_name)
                game.add_data(workable_data)

    def add_from_file(self, data: list[str]):
        for line in data[1:]:
            if len(line) > 0:
                self.add_game(line)

    def get_games(self) -> list[Game]:
        return self._games

    def get_game_with_name(self, name: str) -> Game:
        for game in self.get_games():
            if game.get_name() == name:
                return game

    def load_files_into_library(self, file_names: list[str]):
        for file in file_names:
            f = open("Data" + file, "r")
            t = f.read()
            lines = t.split(sep="\n")
            self.add_from_file(lines)
            f.close()

    def update_averages(self):
        for game in self.get_games():
            game.update_averages()

    def update_total_scores(self):
        for game in self.get_games():
            game.calculate_total_score()

    def sort_games(self):
        sorted_games = []

        for game in self.get_games():
            sorted_games = merge([game], sorted_games)

        self._games = sorted_games

        new_names = []
        for game in sorted_games:
            new_names.append(game.get_name())
        self._names = new_names

    def update(self):
        self.update_averages()
        self.update_total_scores()
        self.sort_games()

    def display(self):
        for entry in self.get_games():
            print(f"{entry.get_name(): <50}{str(entry.get_total_score()) + ' ' + str(len(entry.get_genre())) : >40}")
