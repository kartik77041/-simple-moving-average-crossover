import read
import proj
record =read.final
def test_string_datetime():
    for i in record:
        assert type(proj.string_datetime())==type(i[0])==str

def test_string_instrument():
    for i in record:
        assert type(proj.string_instrument())==type(i[6])==str

def test_float_close():
    for i in record:
        assert type(proj.float_close())==type(i[1])==float

def test_float_high():
    for i in record:
        assert type(proj.float_high())==type(i[2])==float

def test_float_low():
    for i in record:
        assert type(proj.float_low())==type(i[3])==float

def test_float_open():
    for i in record:
        assert type(proj.float_open())==type(i[4])==float

def test_int_volume():
    for i in record:
        assert type(proj.int_volume())==type(i[5])==int