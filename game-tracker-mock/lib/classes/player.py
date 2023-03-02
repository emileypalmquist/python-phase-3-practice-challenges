from classes.result import Result


class Player:
    def __init__(self, username):
        self.username = username

    def get_username(self):
        return self._username

    def set_username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        # else:
        #     raise Exception(
        #         "username not string or not within 2-16 characters")

    username = property(get_username, set_username)

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return [result.game for result in self.results()]

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return len([game_played for game_played in self.games_played() if game_played == game])

    def add_result(self, game, score):
        Result(self, game, score)
