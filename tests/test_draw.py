import os
import pytest
import matplotlib
matplotlib.use("Agg")

from triangle.draw import draw_triangle
from matplotlib.figure import Figure


def test_draw_returns_figure_and_saves(tmp_path):
    fig = draw_triangle(3, 4, 5)
    assert isinstance(fig, Figure)
    out = tmp_path / "tri.png"
    fig2 = draw_triangle(3, 4, 5, output_path=str(out))
    assert isinstance(fig2, Figure)
    assert out.exists()


def test_draw_invalid_raises():
    with pytest.raises(ValueError):
        draw_triangle(1, 2, 3)
