class TictactoeGameEngine:
    def __init__(self):
        self.board = list('.'*9)
        self.current_turn='X'

    def get(self, row, col):
        row -=1
        col -=1
        return self.board[row*3+col]

    def set(self, row, col):
        if row<1 and row>3:
            return
        if col<1 and col>3:
            return
        if self.get(row, col) == '.':
            row -= 1
            col -= 1
            self.board[row * 3 + col] = self.current_turn
            self.current_turn = 'O' if self.current_turn == 'X' else 'X'
        # if self.current_turn == 'X':
        # if self.current_turn =='X':
        #     self.current_turn='O'
        # else:
        #     self.current_turn='X'

    @property
    def check_winner(self):

        #-
        for i in range(1,3+1):
            if self.get(i,1) == self.get(i,2) == self.get(i,3) !='.':
                return self.get(i,1)
        #| # for i in range(1,3+1):
            print(self.get(1,i), self.get(2,i), self.get(3,i))
            if self.get(1,i) == self.get(2,i)==self.get(3,i) !='.':
                return self.get(1,i)
        #/
        if self.get(1,3) == self.get(2,2) == self.get(3,1) !='.':
            return self.get(2,2)
        #\
        if self.get(1,1) == self.get(2,2) == self.get(3,3) !='.':
            return self.get(2,2)
        #무승부
        if not '.' in self.board:
            return 'd'



    def __str__(self):
        s = ''
        for i, v in enumerate(self.board):
            s +=v
            if i%3==2:
                s +='\n'
        return s

if __name__=='__main__':
    ttt_game_engine = TictactoeGameEngine()
    print(ttt_game_engine)
    ttt_game_engine.set(2,2)
    print(ttt_game_engine)
    print(ttt_game_engine.check_winner)
    ttt_game_engine.set(1,1)
    print(ttt_game_engine)
    print(ttt_game_engine.check_winner)
    ttt_game_engine.set(2, 1)
    print(ttt_game_engine)
    print(ttt_game_engine.check_winner)
    ttt_game_engine.set(1, 2)
    print(ttt_game_engine)
    print(ttt_game_engine.check_winner)
    ttt_game_engine.set(2, 3)
    print(ttt_game_engine)
    print(ttt_game_engine.check_winner)