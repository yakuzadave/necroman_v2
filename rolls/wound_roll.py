import d20

def wound_roll(strength, toughness):
    # Necromunda wound chart approximation
    roll = d20.roll('1d20').total
    if strength >= toughness + 2:
        return roll >= 2  # 2+ to wound
    elif strength > toughness:
        return roll >= 3  # 3+ to wound
    elif strength == toughness:
        return roll >= 4  # 4+ to wound
    elif strength + 1 == toughness:
        return roll >= 5  # 5+ to wound
    else:
        return roll >= 6  # 6+ to wound

if __name__ == "__main__":
    # Test the function
    result = wound_roll(4, 3)
    print(result)
