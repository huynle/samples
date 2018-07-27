"""
This is my docstring
"""


class Apple(object):
    """
    Other is my object docstring
    """

    def __init__(self, color):
        self._color = color
        self._expiration_date = None

    def color(self):
        """
        this is my doc

        """
        return "Color is {}".format(self._color)

    def set_expire(self, date):
        """
        This is my set expiration date docstring
        """
        self._expiration_date = "2018-07-26"


class MyApple(object):

    def __init__(self, color):
        self._color = color
