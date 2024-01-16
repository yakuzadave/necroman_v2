import random
import d20

def roll_d6():
    """Roll a six-sided dice and return the result."""
    return d20.roll('1d6').total


def roll_injury_dice():
    """Roll an injury dice and return the outcome."""
    outcomes = ['Flesh Wound', 'Out of Action', 'Out of Action', 'Down', 'Down', 'Serious Injury']
    return random.choice(outcomes)

# Test the functions
def test_dice_rolls():
    """Test the roll_d6 and roll_injury_dice functions."""
    assert roll_d6() in range(1, 7)
    assert roll_injury_dice() in ['Flesh Wound', 'Out of Action', 'Down', 'Serious Injury']


# roll_d6_result = roll_d6()
# roll_injury_dice_result = roll_injury_dice()

# roll_d6_result, roll_injury_dice_result

if __name__ == '__main__':
    test_dice_rolls()
    print('Tests passed!')

