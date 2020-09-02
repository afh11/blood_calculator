import pytest

@pytest.mark.parametrize("HDL, expected", [
	(70, 'Normal'),
	(45, 'Borderline Low'),
	(10, 'Low'),
])

def test_check_HDL_(HDL, expected):
	from calculator import check_HDL
	result = check_HDL(HDL)
	assert result == expected

