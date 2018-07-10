from core import *


def test_new_gladiator():
    assert new_gladiator(93, 78, 7, 10) == {
        'health': 93,
        'rage': 78,
        'damage low': 7,
        'damage high': 10
    }
    assert new_gladiator(74, 54, 4, 34) == {
        'health': 74,
        'rage': 54,
        'damage low': 4,
        'damage high': 34
    }
    assert new_gladiator(68, 48, 18, 38) == {
        'health': 68,
        'rage': 48,
        'damage low': 18,
        'damage high': 38
    }


def test_attack_100_rage():

    attacker = {'health': 93, 'rage': 100, 'damage low': 10, 'damage high': 10}

    defender = {'health': 90, 'rage': 0, 'damage low': 10, 'damage high': 50}

    attack(attacker, defender)

    assert attacker['rage'] == 0
    assert defender['health'] == 80


def test_attack_0_rage():
    attacker = {'health': 97, 'rage': 0, 'damage low': 10, 'damage high': 10}

    defender = {'health': 90, 'rage': 10, 'damage low': 10, 'damage high': 50}

    attack(attacker, defender)

    assert attacker['rage'] == 15
    assert defender['health'] == 80


def test_heal_10_health():
    attacker = {'health': 45, 'rage': 40, 'damage low': 10, 'damage high': 10}

    heal(attacker)

    assert attacker['health'] == 50
    assert attacker['rage'] == 30


def test_heal_0_health():
    attacker = {'health': 93, 'rage': 0, 'damage low': 10, 'damage high': 10}

    heal(attacker)

    assert attacker['health'] == 93
    assert attacker['rage'] == 0


def test_is_dead():
    assert not is_dead({'health': 100})
    assert is_dead({'health': 0})
    assert is_dead({'health': -1})
    assert not is_dead({'health': 1})
