# --Exception--

def create_fraction(number):
    try:
        if number >= 0:
            result = 1 / number
        else:
            raise ValueError('''Number is too small, can't use it''')
    except ZeroDivisionError:
        result = 'Infinit'
        print('''Can't use 0 divider.''')
    except ValueError:
        raise
    except:
        result = 0
        print('This is an unknown error.')

    return result

print(create_fraction(3))
#print(create_fraction(-1))
print(create_fraction(0))
print('Done')