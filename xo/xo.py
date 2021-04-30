from typing import Literal, Union, Optional


class _Player:
    def __init__(self, name: str, sign: Literal['x', 'o']) -> None:
        self.name = name
        self.sign = sign


class _XOTable:
    def __init__(self):
        self.xo_map = {k: None for k in range(1, 10)}  # {1:x, 2: None, 3: o, ...}

    def __str__(self):
        map = self.xo_map
        return """
 -----------------
|  {}  |  {}  |  {}  |
 -----------------
|  {}  |  {}  |  {}  |
 -----------------
|  {}  |  {}  |  {}  |
 -----------------
""".format(*[map[i] if map[i] else i for i in map])

    def mark(self, cell_no, sign: str):
        assert isinstance(cell_no, int) and 1 <= cell_no <= 9, "Enter a valid cell no [1, 9]"
        assert not self.xo_map[cell_no], "Cell is filled"
        sign = str(sign).lower()
        assert sign in 'xo', 'Invalid sign' + sign
        self.xo_map[cell_no] = sign


class _XOGame(_XOTable):
    class UnFinishedGameError(Exception):
        "winner: zamani raise mishe k, bazi tamoom nashode bahe, vali winner() ..."
        pass

    class FinishedGameError(Exception):
        "mark: dar zamin k bazi tamoom shde ..."
        pass

    class InvalidCellError(Exception):
        "mark: Che por bashe, che addesh eshtabah bashe va ..."
        pass

    class InvalidPlayer(Exception):
        "mark: palyere voroodi eshtebah bashad!!!"
        pass

    def __init__(self, player1: _Player, player2: _Player) -> None:
        super(_XOGame, self).__init__()
        self.player1 = player1
        self.player2 = player2

    def _calculate_result(self):

        super().__init__()

        if all(self.xo_map[k] == "X" for k in range(1, 3)):
            print("X WON")  # First Row
            return True
        if all(self.xo_map[k] == "O" for k in range(1, 3)):
            print("O WON")  # First Row
            return True
        if all(self.xo_map[k] == "X" for k in range(4, 6)):
            print("X WON")  # Second Row
            return True
        if all(self.xo_map[k] == "O" for k in range(4, 6)):
            print("O WON")  # Second Row
            return True
        if all(self.xo_map[k] == "X" for k in range(7, 9)):
            print("X WON")  # Third Row
            return True
        if all(self.xo_map[k] == "O" for k in range(7, 9)):
            print("O WON")  # Third Row
            return True
        if all(self.xo_map[k] == "X" for k in [1, 4, 7]):
            print("X WON")  # First Column
            return True
        if all(self.xo_map[k] == "O" for k in [1, 4, 7]):
            print("O WON")  # First Column
            return True
        if all(self.xo_map[k] == "X" for k in [2, 5, 8]):
            print("X WON")  # Second Column
            return True
        if all(self.xo_map[k] == "O" for k in [2, 5, 8]):
            print("O WON")  # Second Column
            return True
        if all(self.xo_map[k] == "X" for k in [3, 6, 9]):
            print("X WON")  # Third Column
            return True
        if all(self.xo_map[k] == "O" for k in [3, 6, 9]):
            print("O WON")  # Third Column
            return True
        if all(self.xo_map[k] == "X" for k in [1, 5, 9]):
            print("X WON")  # First Diagonal
            return True
        if all(self.xo_map[k] == "O" for k in [1, 5, 9]):
            print("O WON")  # First Diagonal
            return True
        if all(self.xo_map[k] == "X" for k in [3, 5, 7]):
            print("X WON")  # Second Diagonal
            return True
        if all(self.xo_map[k] == "O" for k in [3, 5, 7]):
            print("O WON")  # Second Diagonal
            return True

        if all(self.xo_map[k] for k in range(1, 10)):  # checks weather the table is full or not
            print("game over without winner")
            return True
        else: return False

    def mark(self, cell_no, player: Union[_Player, Literal['x', 'o'], int]):
        pass

    def winner(self) -> Optional[_Player]:
        pass
