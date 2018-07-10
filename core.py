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
        defender['health'] -= randint(attacker['damage high'],
                                      attacker['damage low'])
        attacker['rage'] = 0
    else:
        defender['health'] -= randint(attacker['damage high'],
                                      attacker['damage low'])
        attacker['rage'] += 15


def heal(gladiator):
    """{dictionary} -> None
    Returns the increased health and the cost of rage.
    """
    if gladiator['rage'] > 10:
        gladiator['health'] += gladiator['rage']
        gladiator['rage'] -= 10
    else:
        gladiator


def is_dead(gladiator):
    """{key} -> bool
    Returns True iff gladiator has no health.
    """
