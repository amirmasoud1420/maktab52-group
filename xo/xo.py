from typing import Literal, Union, Optional


class _Player:
    def __init__(self, name: str, sign: Literal['x', 'o']) -> None:
        self.name = name
        self.sign = str(sign).lower()


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


class FinishedGameError(Exception):
    "mark: dar zamin k bazi tamoom shde ..."
    pass


class InvalidCellError(Exception):
    "mark: Che por bashe, che addesh eshtabah bashe va ..."
    pass


class InvalidPlayer(Exception):
    "mark: palyere voroodi eshtebah bashad!!!"
    pass

class UnFinishedGameError(Exception):
    "winner: zamani raise mishe k, bazi tamoom nashode bahe, vali winner() ..."
    pass

class _XOGame(_XOTable):

    def __init__(self, player1: _Player, player2: _Player) -> None:
        super(_XOGame, self).__init__()
        self.player1 = player1
        self.player2 = player2

    def _calculate_result(self):

        # super().__init__()

        if all(self.xo_map[k] == "x" for k in range(1, 4)):
            print("X WON")  # First Row
            return 'x'
        if all(self.xo_map[k] == "o" for k in range(1, 4)):
            print("O WON")  # First Row
            return 'o'
        if all(self.xo_map[k] == "x" for k in range(4, 7)):
            print("X WON")  # Second Row
            return 'x'
        if all(self.xo_map[k] == "o" for k in range(4, 7)):
            print("O WON")  # Second Row
            return 'o'
        if all(self.xo_map[k] == "x" for k in range(7, 10)):
            print("X WON")  # Third Row
            return 'x'
        if all(self.xo_map[k] == "o" for k in range(7, 10)):
            print("O WON")  # Third Row
            return 'o'
        if all(self.xo_map[k] == "x" for k in [1, 4, 7]):
            print("X WON")  # First Column
            return 'x'
        if all(self.xo_map[k] == "o" for k in [1, 4, 7]):
            print("O WON")  # First Column
            return 'o'
        if all(self.xo_map[k] == "x" for k in [2, 5, 8]):
            print("X WON")  # Second Column
            return 'x'
        if all(self.xo_map[k] == "o" for k in [2, 5, 8]):
            print("O WON")  # Second Column
            return 'o'
        if all(self.xo_map[k] == "x" for k in [3, 6, 9]):
            print("X WON")  # Third Column
            return 'x'
        if all(self.xo_map[k] == "o" for k in [3, 6, 9]):
            print("O WON")  # Third Column
            return 'o'
        if all(self.xo_map[k] == "x" for k in [1, 5, 9]):
            print("X WON")  # First Diagonal
            return 'x'
        if all(self.xo_map[k] == "o" for k in [1, 5, 9]):
            print("O WON")  # First Diagonal
            return 'o'
        if all(self.xo_map[k] == "x" for k in [3, 5, 7]):
            print("X WON")  # Second Diagonal
            return 'x'
        if all(self.xo_map[k] == "o" for k in [3, 5, 7]):
            print("O WON")  # Second Diagonal
            return 'o'

        if all(self.xo_map[k] for k in range(1, 10)):  # checks weather the table is full or not
            print("game over without winner")
            return 'eq'
        else: return False

    def mark(self, cell_no, player: Union[_Player, Literal['x', 'o'], int]):
        if self._calculate_result():
            raise FinishedGameError('The Game is Finished!!!')
        if not isinstance(cell_no, int):
            raise InvalidCellError('Invalid cell number!!!')
        if not (1 <= cell_no <= 9):
            raise InvalidCellError('Invalid cell number!!!')
        if self.xo_map[cell_no]:
            raise InvalidCellError('Invalid cell number!!!')
        if not (str(player) in 'xoXO' or player == 1 or player == 2 or isinstance(player, _Player)):
            raise InvalidPlayer("Invalid player")
        if player == 1 or player == 'x' or player == 'X':
            super(_XOGame, self).mark(cell_no, 'x')
        elif player == 2 or player == 'o' or player == 'O':
            super(_XOGame, self).mark(cell_no, 'o')
        elif isinstance(player, _Player):
            if player.sign == 'x':
                super(_XOGame, self).mark(cell_no, 'x')
            elif player.sign == 'o':
                super(_XOGame, self).mark(cell_no, 'o')

    def winner(self) -> Optional[_Player]:
        if not self._calculate_result():
            raise UnFinishedGameError("Game is not finished")
        if self._calculate_result()=='o':
            return self.player1 if self.player1.sign=='o' else self.player2
        elif self._calculate_result()=='x':
            return self.player1 if self.player1.sign=='x' else self.player2
        else:
            return 'eq'



class Match:
    def __init__(self,player1:_Player,player2:_Player,sets:int=3,turn=1):
        self.player1,self.player2=player1,player2
        self.sets=sets
        self.xogame=_XOGame(self.player1,self.player2)
        self.turn=turn
    def play(self):
        while not self.xogame._calculate_result():
            cell = input(f'')




# x= _XOGame(_Player('akbar','x'),_Player('mmd','o'))
# x.mark(1,'X')
# x.mark(5,'X')
# x.mark(9,'X')
#
# print(x._calculate_result())
# print(x)
print(__name__)