import pytest, EXAPunks

registers [X, T]

def test_ADDI() :
    EXAPunks.ADDI(5, X)
    assert reg in registers
