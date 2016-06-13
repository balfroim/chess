 #-*- coding: utf-8 -*-
class Chess:

    def __init__(self):
        self.BoardState = self.BoardState()
        self.Rules = Rules()
        self.score = 0
        self.default_state = 0
        self.num_rows = 8
        self.game_active = False
        self.board = [ [self.default_state] * self.num_rows] * self.num_rows

    def start_new_game(self):
        self.game_active = True

    def piece(self, column, row):
        return {"color": "Black", "type": "Pawn"}

    class BoardState:

        def __init__(self):
            self.pawns = [1] * 16
            self.rooks = [2] * 4
            self.knights = [3] * 4
            self.bishops = [4] * 4
            self.king = [5] * 2
            self.queen = [6] * 2

    class Pieces_Set:

        def __init__(self):
            pass

        def full_set(self, type="All", color="All"):
            if type is "Pawns" and color is "All":
                return [1] * 16
            if color is "White" and type is "Pawns":
                return [1] * 8
            else:
                return [1] * 32

    class Rules:

        def __init__(self, game="Chess"):
            self.game = game
            self.list_of_pieces = ([
                "Pawns",
                "Rooks",
                "Knights",
                "Bisops",
                "Kings",
                "Queen",
            ])

        def number_of_pieces(self, *piece):
            if self.game == "Chess":
                pieces_per_player = ({
                "Pawns": 8,
                "Rooks": 2,
                "Knights": 2,
                "Bisops": 2,
                "Kings": 1,
                "Queen": 1,
                })
                return pieces_per_player[piece]
            else:
                return "This game is not supported"

        def starting_locations(self, **parameters):
            if self.game == "Chess":
                if parameters["color"] == "White":
                    pieces_locations = ({
                    "Pawns": ["a2","b2","c2","g2","e2","f2","g2","h2"],
                    "Rooks": ["a1","h1"],
                    "Knights": ["b1","g1"],
                    "Bisops": ["c1","f1"],
                    "Kings": ["d1"],
                    "Queen": ["e1"],
                    })
                    return pieces_per_player[parameters["piece"]]
                if parameters["color"] == "Black":
                    pieces_locations = ({
                    "Pawns": ["a7","b7","c7","g7","e7","f7","g7","h7"],
                    "Rooks": ["a8","h8"],
                    "Knights": ["b8","g8"],
                    "Bisops": ["c8","f8"],
                    "Kings": ["d8"],
                    "Queen": ["e8"],
                    })
                    return pieces_per_player[parameters["piece"]]
                else:
                    return "Incorrect color or piece code"
            else:
                return "This game is not supported"
