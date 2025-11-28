def draw_triangle(a, b, c, output_path=None):
    """Draw a triangle with side lengths `a`, `b`, `c`.

    Returns a `matplotlib.figure.Figure`. If `output_path` is provided,
    the figure is saved to that path (PNG).
    Raises ValueError for invalid triangle sides.
    """
    from math import sqrt

    # validate using the classifier (raises ValueError on invalid)
    from .triangle import classify_triangle

    classify_triangle(a, b, c)

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    a, b, c = float(a), float(b), float(c)

    # Place A at (0,0), B at (c,0). Compute C using distances to A (b) and B (a).
    A = (0.0, 0.0)
    B = (c, 0.0)
    # projection of AC onto AB
    x = (b * b + c * c - a * a) / (2 * c)
    y_sq = max(0.0, b * b - x * x)
    y = sqrt(y_sq)
    C = (x, y)

    fig, ax = plt.subplots()
    xs = [A[0], B[0], C[0], A[0]]
    ys = [A[1], B[1], C[1], A[1]]
    ax.plot(xs, ys, "-o")
    ax.set_aspect("equal")
    ax.axis("off")

    if output_path:
        fig.savefig(output_path)

    return fig
