from random import randint


def new_gladiator(health, rage, damage_low, damage_high):
    """(int, int, int, int) -> {dictionary}
    Returns a dictionary with 4 key-value pairs.
    """
    return {
        'health': health,
        'rage': rage,
        'damage low': damage_low,
        'damage high': damage_high
    }


def attack(attacker, defender):
    """({dictionary}, {dictionary}) -> None
    Returns the damage done on the defender and changes the rage.
    """
    if randint(1, 100) < attacker['rage']:
        defender['health'] - (attacker['damage high'], attacker['damage low'])
    else:
        defender['health'] - randint


def heal(gladiator):
    """{dictionary} -> None
    Returns the increased health and the cost of rage.
    """


def is_dead(gladiator):
    """{key} -> bool
    Returns True iff gladiator has no health.
    """
