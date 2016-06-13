Feature: Rules of chess
  In order to play chess
  As a chess player
  I want to be able to move pieces on a chess board with victory conditions

  @wip
  Scenario: Starting the game
    Given you are starting a game of chess
    When you start a game
    Then the board exists
    And it is the correct size
    And there is the correct number of pieces
    And the score is set to zero

  @wip
  Scenario: Setting up the board
    Given that you have a set of pieces
    When the game is about to start
    Then all of the pieces are put in their correct places
    And none of the pieces are in wrong places

  Scenario: Moving a piece
    Given a piece is on the board
    When you move it to a valid position
    Then it changes positions
    And your turn ends

  Scenario: Taking a piece
    Given two pieces
    When one piece takes another
    Then the defender's space is occupied by the attacker
    And the defending piece is removed from play
    And your turn ends
