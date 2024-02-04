# test_dashboard.py

import pytest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dashboard import degree_range, rot_text, gauge

# Test de la fonction degree_range
def test_degree_range():
    n = 4
    ranges, mid_points = degree_range(n)
    assert len(ranges) == n
    assert len(mid_points) == n


def test_rot_text():
    assert rot_text(-45) == -135

# Test de la fonction gauge
def test_gauge():
    arrow = 0.3
    fig, ax = plt.subplots()
    ax = gauge(arrow=arrow, ax=ax)
    assert ax is not None  



