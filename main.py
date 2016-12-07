import hashlib
from utils.anon import Anon

p_anon = hashlib.sha256
c_anon = Anon().digest

macs = ['0f:b2:5e:80:24:28',
        '75:39:86:8b:d4:60',
        '8c:bf:13:23:04:c2',
        '6f:c5:a7:58:00:76',
        'd8:19:7b:01:f6:33',
        '1d:06:e5:7b:86:0a',
        'a3:fc:43:2a:87:18',
        '8a:14:d7:9e:37:dc',
        '60:a6:a1:07:ff:a2',
        '7e:d7:bb:fa:d8:b1',
        '2e:f5:b8:13:70:3e',
        '1e:14:3b:62:3e:c2',
        '7a:c9:d6:52:67:0d',
        '2e:c7:b4:d0:cf:b3',
        '72:4d:8a:2d:48:63',
        'df:76:58:98:8a:c9',
        'd7:a8:dd:12:0a:1c',
        'd4:85:e5:ab:d7:4d',
        'b9:06:14:6d:d6:e3',
        '21:48:31:ac:76:79',
        '0f:56:f0:68:ee:7a',
        '31:c5:22:0f:d7:2d',
        '2c:ac:b2:12:57:8a',
        '5f:11:90:74:7f:66',
        '58:a0:af:89:4d:25',
        '03:5d:7b:f3:c6:6a',
        '6d:f8:30:90:07:08',
        'be:33:b4:71:46:0c',
        'fb:a5:1d:8c:19:9d',
        'f2:71:3e:a2:fb:8b'
        ]


def python_anon():
    for m in macs:
        # This is a bit slower
        # hashlib.sha256(m).hexdigest()
        # than
        p_anon(m).hexdigest()


def cpp_anon():
    for m in macs:
        c_anon(m)


if __name__ == '__main__':
    import timeit

    print(len(macs))

    number_of_experiments = 3
    number_of_trails = 1000

    print('Python:')
    print(p_anon('28:80:23:e7:1c:3c').hexdigest())
    python_time = min(timeit.repeat('python_anon()',
                                    setup='from __main__ import python_anon',
                                    repeat=number_of_experiments,
                                    number=number_of_trails
                                    )
                      )
    print('Python time: {time:.9f}'.format(time=python_time))

    print('\n')

    print('Cython:')
    print(c_anon('28:80:23:e7:1c:3c'))
    cython_time = min(timeit.repeat('cpp_anon()',
                                    setup='from __main__ import cpp_anon',
                                    repeat=number_of_experiments,
                                    number=number_of_trails
                                    )
                      )
    print('Cython time: {time:.9f}'.format(time=cython_time))

    print('\n')

    print("Speed gain: {gain:.3f}".format(gain=python_time / cython_time))
