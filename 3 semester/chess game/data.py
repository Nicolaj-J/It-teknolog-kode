from random import random


class chessboard():
    random = {
        "A" : 2,
        "B" : 52,
        "C" : 102,
        "D" : 152,
        "E" : 202,
        "F" : 252,
        "G" : 302,
        "H" : 352,
        "1" : 0,
        "2" : 50,
        "3" : 100,
        "4" : 150,
        "5" : 200,
        "6" : 250,
        "7" : 300,
        "8" : 350,

    }
    unicode = {
        "kingwhite" : "\u2654",
        "queenwhite": "\u2655",
        "rookwhite" : "\u2656",
        "bishopwhite":"\u2657",
        "knightwhite":"\u2658",
        "pawnwhite" : "\u2659",
        "kingblack" : "\u265A",
        "queenblack": "\u265B",
        "rookblack" : "\u265C",
        "bishopblack":"\u265D",
        "knightblack":"\u265E",
        "pawnblack" : "\u265F"


    }
    piecepos = {
        "pawnblack1" : "A7",
        "pawnblack2" : "B7",
        "pawnblack3" : "C7",
        "pawnblack4" : "D7",
        "pawnblack5" : "E7",
        "pawnblack6" : "F7",
        "pawnblack7" : "G7",
        "pawnblack8" : "H7",
        "rookblack1" : "A8",
        "knightblack1" : "B8",
        "bishopblack1" : "C8",
        "kingblack1" : "D8",
        "queenblack1": "E8",
        "bishopblack2" : "F8",
        "knightblack2" : "G8",
        "rookblack2" : "H8",
        "pawnwhite1" : "A2",
        "pawnwhite2" : "B2",
        "pawnwhite3" : "C2",
        "pawnwhite4" : "D2",
        "pawnwhite5" : "E2",
        "pawnwhite6" : "F2",
        "pawnwhite7" : "G2",
        "pawnwhite8" : "H2",
        "rookwhite1" : "A1",
        "knightwhite1" : "B1",
        "bishopwhite1" : "C1",
        "kingwhite1" : "D1",
        "queenwhite1" : "E1",
        "bishopwhite2" : "F1",
        "knightwhite2" : "G1",
        "rookwhite2" : "H1"
    }
    startpiecepos = {
        "pawnblack1" : "A7",
        "pawnblack2" : "B7",
        "pawnblack3" : "C7",
        "pawnblack4" : "D7",
        "pawnblack5" : "E7",
        "pawnblack6" : "F7",
        "pawnblack7" : "G7",
        "pawnblack8" : "H7",
        "rookblack1" : "A8",
        "knightblack1" : "B8",
        "bishopblack1" : "C8",
        "kingblack1" : "D8",
        "queenblack1": "E8",
        "bishopblack2" : "F8",
        "knightblack2" : "G8",
        "rookblack2" : "H8",
        "pawnwhite1" : "A2",
        "pawnwhite2" : "B2",
        "pawnwhite3" : "C2",
        "pawnwhite4" : "D2",
        "pawnwhite5" : "E2",
        "pawnwhite6" : "F2",
        "pawnwhite7" : "G2",
        "pawnwhite8" : "H2",
        "rookwhite1" : "A1",
        "knightwhite1" : "B1",
        "bishopwhite1" : "C1",
        "kingwhite1" : "D1",
        "queenwhite1" : "E1",
        "bishopwhite2" : "F1",
        "knightwhite2" : "G1",
        "rookwhite1" : "H1"
    }
    piecehighlight = {
        "highlight" : ""
    }
    def Lo(field):
        vandret = chessboard.random[field[0:1]]
        lodret = chessboard.random[field[1:2]]
        return vandret,lodret
    vandretpos = (("A",0,50),("B",50,100),("C",100,150),("D",150,200),("E",200,250),("F",250,300),("G",300,350),("H",350,400))
    lodretpos = ((1,0,50),(2,50,100),(3,100,150),(4,150,200),(5,200,250),(6,250,300),(7,300,350),(8,350,400))
    blackpawnposition = (("pawnblack1","A7"),("pawnblack2", "B7"),("pawnblack3","C7"),("pawnblack4","D7"),("pawnblack5","E7"),("pawnblack6","F7"),("pawnblack7","G7"),("pawnblack8","H7"))
    blackofficerpositions = (("rookblack1","A8"),("knightblack1","B8"),("bishopblack1","C8"),("kingblack1","D8"),("queenblack1","E8"),("bishopblack2","F8"),("knightblack2","G8"),("rookblack2","H8"))
    whitepawnposition = (("pawnwhite1","A2"),("pawnwhite2", "B2"),("pawnwhite3","C2"),("pawnwhite4","D2"),("pawnwhite5","E2"),("pawnwhite6","F2"),("pawnwhite7","G2"),("pawnwhite8","H2"))
    whiteofficerpositions =(("rookwhite1","A1"),("knightwhite1","B1"),("bishopwhite1","C1"),("kingwhite1","D1"),("queenwhite1","E1"),("bishopwhite2","F1"),("knightwhite2","G1"),("rookwhite1","H1"))
    startblackpawnposition = (("pawnblack1","A7"),("pawnblack2", "B6"),("pawnblack3","C7"),("pawnblack4","D7"),("pawnblack5","E7"),("pawnblack6","F7"),("pawnblack7","G7"),("pawnblack8","H7"))
    startblackofficerpositions = (("rookblack1","A8"),("knightblack1","B8"),("bishopblack1","C8"),("kingblack1","D8"),("queenblack1","E8"),("bishopblack2","F8"),("knightblack2","G8"),("rookblack1","H8"))
    startwhitepawnposition = (("pawnwhite1","A2"),("pawnwhite2", "B2"),("pawnwhite3","C2"),("pawnwhite4","D2"),("pawnwhite5","E2"),("pawnwhite6","F2"),("pawnwhite7","G2"),("pawnwhite8","H2"))
    startwhiteofficerpositions =(("rookwhite1","A1"),("knightwhite1","B1"),("bishopwhite1","C1"),("kingwhite1","D1"),("queenwhite1","E1"),("bishopwhite2","F1"),("knightwhite2","G1"),("rookwhite1","H1"))


def Get_piece(mouseposition):
    for key, value in chessboard.piecepos.items():
        if mouseposition == value:
            return key
