 #-*- coding: utf-8 -*-
# Feature: Rules of chess
#   In order to play chess
#   As a chess player
#   I want to be able to move pieces on a chess board with victory conditions

#   @wip
#   Scenario: Starting the game
#     Given you are starting a game of chess
#     When you start a game
#     Then the board exists
#     And it is the correct size
#     And there is the correct number of pieces
#     And the score is set to zero

#   @wip
#   Scenario: Setting up the board
#     Given that you have a set of pieces
#     When the game is about to start
#     Then all of the pieces are put in their correct places
#     And none of the pieces are in wrong places

#   Scenario: Moving a piece
#     Given a piece is on the board
#     When you move it to a valid position
#     Then it changes positions
#     And your turn ends

#   Scenario: Taking a piece
#     Given two pieces
#     When one piece takes another
#     Then the defender's space is occupied by the attacker
#     And the defending piece is removed from play
#     And your turn ends

# 

class BoardState:
    def __init__(self):
        self.pieces = {}
        self.pieces["Pawns"] = 8
        self.pieces["Rooks"] = 2

    def number_of_pieces(self, piece):
        return self.pieces[piece]

    def set_piece(self, piece, position):
        pass

    def move_piece(self, piece, position):
        pass

    def get_piece(self, position):
        pass

class Rules:
    def __init__(self):
        pass

class PiecesSet:
    def __init__(self):
        pass

    def setup_pieces(self):
        pass

    def starting_locations(self, color, piece):
        pass

class Chess:
    def __init__(self):
        self.board = []
        self.board_state = BoardState()
        self.rules = Rules()
        self.pieces_set = PiecesSet()

    def start_new_game(self):
        self.board = [[0 for x in range(8)] for y in range(8)]

    
    

    # from behave import given, when, then
# from chess import Chess, BoardState, Rules, PiecesSet
# from hamcrest import *

# @given('you are starting a game of chess')
# def step_impl(context):
#     context.game = Chess()

# @when('you start a game')
# def step_impl(context):
#     context.game.start_new_game()

# @then('the board exists')
# def step_impl(context):
#     assert_that(context.game.board, is_not(None))

# @then('it is the correct size')
# def step_impl(context):
#     assert_that(context.game.board, has_length(8))
#     for row in context.game.board:
#         assert_that(row, has_length(8))

# @then('there is the correct number of pieces')
# def step_impl(context):
#     assert_that(context.game.board_state.number_of_pieces("Pawns"), equal_to(8))
#     assert_that(context.game.board_state.number_of_pieces("Rooks"), equal_to(2))
#     assert_that(context.game.board_state.number_of_pieces("Knights"), equal_to(2))
#     assert_that(context.game.board_state.number_of_pieces("Bishops"), equal_to(2))
#     assert_that(context.game.board_state.number_of_pieces("Kings"), equal_to(1))
#     assert_that(context.game.board_state.number_of_pieces("Queens"), equal_to(1))

# @then('the score is set to zero')
# def step_impl(context):
#     assert_that(context.game.score, equal_to(0))

# @given('that you have a set of pieces')
# def step_impl(context):
#     context.pieces = PiecesSet()

# @when('the game is about to start')
# def step_impl(context):
#     context.pieces.setup_pieces()

# @then('all of the pieces are put in their correct places')
# def step_impl(context):
#     assert_that(context.pieces.starting_locations(color="White", piece="Pawns"), equal_to(["a2","b2","c2","g2","e2","f2","g2","h2"]))
#     assert_that(context.pieces.starting_locations(color="White", piece="Rooks"), equal_to(["a1","h1"]))
#     assert_that(context.pieces.starting_locations(color="White", piece="Knights"), equal_to(["b1","g1"]))
#     assert_that(context.pieces.starting_locations(color="White", piece="Bishops"), equal_to(["c1","f1"]))
#     assert_that(context.pieces.starting_locations(color="White", piece="Kings"), equal_to(["d1"]))
#     assert_that(context.pieces.starting_locations(color="White", piece="Queens"), equal_to(["e1"]))
#     assert_that(context.pieces.starting_locations(color="Black", piece="Pawns"), equal_to(["a7","b7","c7","g7","e7","f7","g7","h7"]))
#     assert_that(context.pieces.starting_locations(color="Black", piece="Rooks"), equal_to(["a8","h8"]))
#     assert_that(context.pieces.starting_locations(color="Black", piece="Knights"), equal_to(["b8","g8"]))
#     assert_that(context.pieces.starting_locations(color="Black", piece="Bishops"), equal_to(["c8","f8"]))
#     assert_that(context.pieces.starting_locations(color="Black", piece="Kings"), equal_to(["d8"]))
#     assert_that(context.pieces.starting_locations(color="Black", piece="Queens"), equal_to(["e8"]))

# @then('none of the pieces are in wrong places')
# def step_impl(context):
#     assert_that(context.pieces.starting_locations(color="White", piece="Pawns"), is_not(["a1","b1","c1","g1","e1","f1","g1","h1"]))
#     assert_that(context.pieces.starting_locations(color="White", piece="Rooks"), is_not(["a2","h2"]))
#     assert_that(context.pieces.starting_locations(color="White", piece="Knights"), is_not(["b2","g2"]))
#     assert_that(context.pieces.starting_locations(color="White", piece="Bishops"), is_not(["c2","f2"]))
#     assert_that(context.pieces.starting_locations(color="White", piece="Kings"), is_not(["d2"]))
#     assert_that(context.pieces.starting_locations(color="White", piece="Queens"), is_not(["e2"]))
#     assert_that(context.pieces.starting_locations(color="Black", piece="Pawns"), is_not(["a8","b8","c8","g8","e8","f8","g8","h8"]))
#     assert_that(context.pieces.starting_locations(color="Black", piece="Rooks"), is_not(["a7","h7"]))
#     assert_that(context.pieces.starting_locations(color="Black", piece="Knights"), is_not(["b7","g7"]))
#     assert_that(context.pieces.starting_locations(color="Black", piece="Bishops"), is_not(["c7","f7"]))
#     assert_that(context.pieces.starting_locations(color="Black", piece="Kings"), is_not(["d7"]))
#     assert_that(context.pieces.starting_locations(color="Black", piece="Queens"), is_not(["e7"]))

# @given('a piece is on the board')
# def step_impl(context):
#     context.game = Chess()
#     context.game.start_new_game()
#     context.game.board_state.set_piece("a2", "Pawn")

# @when('you move it to a valid position')
# def step_impl(context):
#     context.game.board_state.move_piece("a2", "a3")

# @then('it changes position')
# def step_impl(context):
#     assert_that(context.game.board_state.get_piece("a3"), equal_to("Pawn"))

# @then('your turn ends')
# def step_impl(context):
#     assert_that(context.game.turn, equal_to("Black"))

# @given('two pieces')
# def step_impl(context):
#     context.game = Chess()
#     context.game.start_new_game()
#     context.game.board_state.set_piece("a2", "Pawn")
#     context.game.board_state.set_piece("a3", "Pawn")

# @when('one piece takes another')
# def step_impl(context):
#     context.game.board_state.move_piece("a2", "a3")

# @then('the defender\'s space is occupied by the attacker')
# def step_impl(context):
#     assert_that(context.game.board_state.get_piece("a3"), equal_to("Pawn"))

# @then('the defending piece is removed from play')
# def step_impl(context):
#     assert_that(context.game.board_state.get_piece("a2"), equal_to(None))

# @then('it changes positions')
# def step_impl(context):
#     assert_that(context.game.board_state.get_piece("a3"), equal_to("Pawn"))