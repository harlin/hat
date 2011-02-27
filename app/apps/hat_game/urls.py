# -*- coding: utf-8 -*-
"""
    urls
    ~~~~

    URL definitions.

    :copyright: TODO.
    :license: TODO.
"""
from tipfy import Rule


def get_rules(app):
    """Returns a list of URL rules for the Hat Game application.

    :param app:
        The WSGI application instance.
    :return:
        A list of class:`tipfy.Rule` instances.
    """
    rules = [
        Rule('/', endpoint='hat-home', handler='apps.hat_game.handlers.HomePageHandler'),
        Rule('/new', endpoint='hat-new-game', handler='apps.hat_game.handlers.CreateNewGameHandler'),
        Rule('/join', endpoint='hat-join-game', handler='apps.hat_game.handlers.JoinGameHandler'),
        Rule('/game/<game_number>', endpoint='hat-game-main', handler='apps.hat_game.handlers.GameMainHandler'),
    ]

    return rules
