# install pytest (if you don't have it already)
# import pytest
# import the python file you want to test
# create a function that begins with 'test_'

import pytest, EXAPunks

def test_addi_with_args_1_and_2_expect_3() :
    EXAPunks.addi([1, 2, 'T'])
    assert EXAPunks.t == 3
