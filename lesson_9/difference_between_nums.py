def difference(*args: float | int) -> int | float:
    if not args:
        return 0
    return round(max(args) - min(args), 2)
