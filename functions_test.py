from Functions import numbers,count_spaces, calc_avrg


def test_numbers(): # Függvény = teszteset
    result = numbers(2, 3) # Tesztelendő függvény meghíváas
    assert result == 5

def test_numbers_zero(): # Függvény = teszteset
    result = numbers(0, 0) # Tesztelendő függvény meghíváas
    assert result == 0

def test_numbers_mixed(): # Függvény = teszteset
    result = numbers(5, -3) # Tesztelendő függvény meghíváas
    assert result == 2

def test_count_spaces():
    result = count_spaces("h h h h ")
    assert result == 4

def test_count_spaces():
    result = count_spaces("hhhh")
    assert result == 0

def test_calc_avrg():
    result = calc_avrg ("")
    assert result == 3