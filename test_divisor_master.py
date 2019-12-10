# -*- coding: utf-8 -*-

import divisor_master as dm
from pn10k import PN10K
from functools import reduce
from operator import mul
from dirty_function import dirty_function

dm.MAX_NUMBER = PN10K[-1] + 1  # 104730
dm.prime_numbers = dm.init_prime_numbers(dm.MAX_NUMBER)


def test_init_prime_numbers():
    assert dm.prime_numbers == PN10K


def test_test_prime():
    for i in range(1, dm.MAX_NUMBER + 1):
        assert dm.test_prime(i) == (i in PN10K)


def test_list_divisor():
    # for i in range(2, dm.MAX_NUMBER + 1):  # Слишком долго ...
    for i in range(2, 1999 + 1):
        ls = dm.list_divisor(i)
        for j in range(2, i):
            assert (i % j == 0) == (j in ls)


def test_1_max_prime_divisor():
    for n in PN10K:
        assert dm.max_prime_divisor(n) is None


def test_2_max_prime_divisor():
    # for i in range(2, dm.MAX_NUMBER + 1):  # Слишком долго ...
    for i in range(2, 1999 + 1):
        ls = dm.list_divisor(i)
        if i not in PN10K:
            for j in ls[::-1]:
                if j in PN10K:
                    assert j == dm.max_prime_divisor(i)
                    break


def test_list_prime_numbers():
    # for i in range(2, dm.MAX_NUMBER + 1):  # Слишком долго ...
    for i in range(2, 1999 + 1):
        ls = dm.list_prime_numbers(i)
        if i in PN10K:
            assert ls == []
        else:
            assert i == reduce(mul, ls, 1)
            for j in ls:
                assert j in PN10K


def test_canonical_decomposition():
    # for i in range(2, dm.MAX_NUMBER + 1):  # Слишком долго ...
    for i in range(2, 1999 + 1):
        if i in PN10K:
            assert dm.canonical_decomposition(i) == ''
        else:
            assert eval(dm.canonical_decomposition(i)) == i


def test_max_divisor():
    # for i in range(2, dm.MAX_NUMBER + 1):  # Слишком долго ...
    for i in range(2, 1999 + 1):
        if i in PN10K:
            assert dm.max_divisor(i) is None
        else:
            ls = dm.list_prime_numbers(i)
            assert reduce(mul, ls[1:], 1) == dm.max_divisor(i)


def test_1_dirty_function():
    for _ in range(100):
        ls = dirty_function(1000, *PN10K)
        for i in ls:
            assert i in PN10K


def test_2_dirty_function():
    for i in range(1, len(PN10K) + 1):
        ls = dirty_function(i, *PN10K)
        assert len(ls) == i


# def test_bad():  # special bad test
#     assert False
