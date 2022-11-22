#  -*- coding: utf-8 -*-
from behave import *
from chess import Chess, BoardState, PiecesSet, Rules

# 8 ║♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
# 7 ║♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
# 6 ║… … … … … … … …
# 5 ║… … … … … … … …
# 4 ║… … … … … … … …
# 3 ║… … … … … … … …
# 2 ║♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
# 1 ║♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖
#  —╚═══════════════
#  ——a b c d e f g h

@given(u'you are starting a game of chess')
def step_impl(context):
    context.chess = Chess()

@when(u'you start a game')
def step_impl(context):
    context.chess.start_new_game()
    assert context.chess.game_active == True

@then(u'the board exists')
def step_impl(context):
    assert context.chess.board is not None

@then(u'it is the correct size')
def step_impl(context):
    assert len(context.chess.board) == 8
    for board_row in context.chess.board:
        assert len(board_row) == 8

@then(u'there is the correct number of pieces')
def step_impl(context):
    rules = context.chess.Rules
    expected_pieces = [8, 2, 2, 2, 1, 1]
    for piece in rules.list_of_pieces:
        for number in expected_pieces:
            pass


@then(u'the score is set to zero')
def step_impl(context):
    assert(context.chess.score == 0)

@given(u'that you have a set of pieces')
def step_impl(context):
    context.chess = Chess()
    set_of_pieces = PiecesSet()
    assert(len(set_of_pieces.full_set()) == 32)
    assert(len(set_of_pieces.full_set("Pawns")) == 16)
    assert(len(set_of_pieces.full_set("Pawns", "White")) == 8)

@when(u'the game is about to start')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the game is about to start')

@then(u'all of the pieces are put in their correct places')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then all of the pieces are put in their correct places')

@then(u'none of the pieces are in wrong places')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then none of the pieces are in wrong places')

@given(u'a piece is on the board')
def step_impl(context):
    context.chess = Chess()
    piece = context.chess.piece("b", 8)
    assert(piece["color"] == "Black")
    assert(piece["type"] == "Pawn")

@when(u'you move it to a valid position')
def step_impl(context):
    raise NotImplementedError(u'STEP: you move it to a valid position')

@then(u'it changes positions')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then it changes positions')

@then(u'your turn ends')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then your turn ends')

@given(u'two pieces')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given two pieces')

@when(u'one piece takes another')
def step_impl(context):
    raise NotImplementedError(u'STEP: When one piece takes another')

@then(u'the defender\'s space is occupied by the attacker')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the defender\'s space is occupied by the attacker')

@then(u'the defending piece is removed from play')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the defending piece is removed from play')
