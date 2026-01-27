class sports:
    def cricket(self,batter):
        self.batter=batter
    def football(self,striker):
        self.striker=striker
    def show_cricket(self):
        return self.batter
    def show_football(self):
        return self.striker
    def make_call(self):
        print("makeing phone call")
    def play_game(self):
        print("playing game")
c1=sports()
c1.make_call()
c1.play_game()