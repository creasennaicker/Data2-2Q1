def fibonacci(fin: float) -> float:
    """
    build a classic fibonacci function - No RECURSION
    """

    x = []

    if x in fin == 0:
        return 0
    elif fin == 1:
        return 1
    else:
        return fibonacci(fin - 1) + fibonacci(fin - 2)


