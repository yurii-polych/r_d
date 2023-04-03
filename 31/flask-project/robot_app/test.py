lst = ['name', 'users', 3]


def check_in_list():
    if 'user' not in lst:
        print('check func print')
        return 'there in not user in list'


def other_func():
    check_in_list()
    print('other func print')
    return 'other result'


print(other_func())
