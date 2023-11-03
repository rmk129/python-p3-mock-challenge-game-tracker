class Game:
    def __init__(self, title):
        self._title = None
        self.title = title
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if self._title == None:
            if isinstance(title, str) and len(title) > 0:
                self._title = title

    def results(self):
        from classes.many_to_many import Result
        all_results = []
        for results in Result.all:
            if results.game == self:
                all_results.append(results)
        return all_results

    def players(self):
        from classes.many_to_many import Result
        all_players = set()
        for results in Result.all:
            if results.game == self:
                all_players.add(results.player)
        return list(all_players)

    def average_score(self, player):
        from classes.many_to_many import Result
        all_scores = []
        total_score = 0
        for results in Result.all:
            if results.player == player:
                all_scores.append(results.score)
        for score in all_scores:
            total_score += score
        average = total_score / len(all_scores)
        return average


class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username) in range(2, 17):
            self._username = username

    def results(self):
        from classes.many_to_many import Result
        all_results = []
        for results in Result.all:
            if results.player == self:
                all_results.append(results)
        return all_results



    def games_played(self):
        from classes.many_to_many import Result
        all_games = set()
        for results in Result.all:
            if results.player == self:
                all_games.add(results.game)
        return list(all_games)

    def played_game(self, game):
        from classes.many_to_many import Result
        all_games = set()
        for results in Result.all:
            if results.player == self:
                all_games.add(results.game)
        if game in all_games:
            return True
        else:
            return False

        

    def num_times_played(self, game):
        from classes.many_to_many import Result
        all_games = []
        number_game = 0
        for results in Result.all:
            if results.player == self:
                all_games.append(results.game)
        for games in all_games:
            if game == games:
                number_game += 1
        return number_game
        

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self._score = None
        self.score = score
        self.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if self._score == None:
            if isinstance(score, int) and score in range(1, 5001):
                self._score = score
            
    
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
