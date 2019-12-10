from random import choice


def dirty_function(n, *args):
    return [choice(args) for _ in range(n)]


if __name__ == '__main__':
    print(dirty_function(3, 'aaaaaaa', 'bbbbbbbbb', 'ccccccccccc', 'dddddddd', 'eee', 'fffffffff'))

    lst = ['0000000', '11111111', '22222222222', '3333333', '44444444',
           '555555555', '666666666666', '777777777', '88888888888', '9999',
           '000', '111111', '222222', '3333333', '444',
           '555555555', '666666', '77777777', '88888', '9999999999']

    list_F = dirty_function(100, *lst)
    print(len(lst), len(list_F), list_F)
