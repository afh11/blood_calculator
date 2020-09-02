import pytest
#function that receipes two tuples and an x value and returns the y value.
@pytest.mark.parametrize("x1, y1, x2, y2, x3, x4", [
	(1, 10, 4, 25, 6, 35),
])
def test_return_y(x1, y1, x2, y2, x3, x4):
	from line import return_y
	result = return_y(x1, y1, x2, y2, x3)
	expected == x4
	assert result == expected
