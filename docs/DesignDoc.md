# Project Design Documentation

## Team Members:
    * Peter Carter
    * Nicholas Kelly
    * Arian Jahjaga

## Minimum Viable Product Summary


## Requirements
* Players can launch a Python executable from their desktop
* Players can select either to start a normal game, or against an AI
* Normal game play is a local game played on one computer, with two players
* AI game play is also local, but an AI makes moves for the selected color
* Game play follows the rules of the US Chess Federation

## Domain Model

![Domain Model of PythonChess](domain_model.png)

> Our model is comprised of the following pieces:

* Board: This represents a chess board. It is made up of 64 squares
* Square: A single square on a chess board. It has a color attribute, and a coordinate.
* Piece: This is a super class representing all chess pieces. It has a type attribute, color, and makes moves
* Pawn, Rook, King, Queen, Knight, Bishop: These will all be subclasses of Piece, with essentially unique interpretations of a 'move' function.
* Player: represents one of the two players in a game of chess.
* Move: represents the move of a piece from one spot to another.
* Ruleset: A set of rules that dictate if a move is legal

## Summary of Project Architecture

Write about the project architecture (pygame)

### Model View Controller

Write about the MVC design

