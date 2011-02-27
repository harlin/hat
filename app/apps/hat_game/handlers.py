# -*- coding: utf-8 -*-
"""
    handlers
    ~~~~~~~~

    Hat: the best word guessing game.

    :copyright: TODO.
    :license: TODO.
"""
from tipfy import RequestHandler, Response
from tipfy.ext.jinja2 import render_response


class HomePageHandler(RequestHandler):
    def get(self):
        """Simply returns a Response object with an placeholder text."""
        return Response('Home Page here! Welcome to HAT')

class CreateNewGameHandler(RequestHandler):
    def get(self):
        """Simply returns a Response object with an placeholder text."""
        return Response('Create New Game Page here! Welcome to HAT')

class JoinGameHandler(RequestHandler):
    def get(self):
        """Simply returns a Response object with an placeholder text."""
        return Response('Join Game Page here! Welcome to HAT')

class GameMainHandler(RequestHandler):
    def get(self, game_number=0):
        """Simply returns a Response object with an placeholder text."""
        return Response('This is game number %s' % game_number)

'''
class PrettyHelloWorldHandler(RequestHandler):
    def get(self):
        """Simply returns a rendered template with an enigmatic salutation."""
        return render_response('hello_world.html', message='Hello, World!')
'''
