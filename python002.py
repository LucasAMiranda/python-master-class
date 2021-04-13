capital = ''
def get_capital(capital):
    if capital ==  'France':
        return 'paris'
    elif capital == 'India':
        return 'New Delhi'
    elif capital == 'UK':
        return 'Londres'
    else:
        return None

print(get_capital(str('France')))