import numpy as np

class Dice:
    """
    Object and utility class for simulating dice rolls.

    Invoking rolls is fairly ergonomic thanks to an abuse of Python's special functions.
    Right multiplication to a Dice instance by an integer specifies the number of dice.
    Left multiplication to a Dice instance by an integer specifies the number of faces.

    More concretely, to roll four twenty-sided dice (commonly notated as "4d20"):
    >>> d = Dice()
    >>> 4*d*20
    array([11, 15, 18,  7])

    If the number of dice is not specified (e.g. `d*20`), it defaults to 1.
    A `Dice` instance resets itself after each roll, and thus can be reused ad infinitum.

    """
    @staticmethod
    def roll_ability_scores():
        rolls = np.random.randint(1, 7, (6, 4))
        rolls.sort()
        rolls = rolls[:, 1:].sum(axis=-1)
        rolls.sort()
        return rolls[::-1]

    @staticmethod
    def roll_hit_points(num_faces, con, level):
        return num_faces + con \
             + np.random.randint(1, num_faces+1, level-1).sum() \
             + con*(level-1)

    def __init__(self):
        self.num_dice = 1

    def __rmul__(self, num_dice):
        if not isinstance(num_dice, int):
            raise ValueError("number of dice must be an integer")
        self.num_dice = num_dice
        return self

    def __mul__(self, num_faces):
        if not isinstance(num_faces, int):
            raise ValueError("number of faces must be an integer")
        rolls = np.random.randint(1, num_faces+1, self.num_dice)
        self.num_dice = 1
        return rolls
