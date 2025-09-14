def get_lots(atr_value):
    if atr_value < 15:
        return 10
    elif 15 <= atr_value <= 25:
        return 5
    else:
        return 2
