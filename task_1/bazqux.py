seq_100 = list(range(1, 101))

bazqux = []
for x in seq_100:
    if x % 3 == 0:
        if x % 5 == 0:
            bazqux.append('BazQux')
        else:
            bazqux.append('Baz')
    elif x % 5 == 0:
        bazqux.append('Qux')
    else:
        bazqux.append(x)

print(' '.join(str(x) for x in seq_100))
print(' '.join(str(x) for x in bazqux))
