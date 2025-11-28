def classify_triangle(a, b, c):
    """Classify a triangle by side lengths.

    Returns 'equilateral', 'isosceles', or 'scalene'.
    Raises ValueError for non-positive sides or if the sides cannot form a triangle.
    """
    try:
        sides = [float(a), float(b), float(c)]
    except Exception:
        raise ValueError("sides must be numbers")

    if any(s <= 0 for s in sides):
        raise ValueError("side lengths must be positive")

    sides.sort()
    if sides[0] + sides[1] <= sides[2]:
        raise ValueError("sides do not form a triangle")

    a, b, c = sides
    if a == b == c:
        return "equilateral"
    if a == b or b == c or a == c:
        return "isosceles"
    return "scalene"
