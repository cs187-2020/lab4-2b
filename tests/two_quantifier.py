test = {   'name': 'two_quantifier',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> isinstance(two(lambda x: x in Flight, lambda y: (y, NewYork) in Destination), bool) \\\n'
                                               '... and isinstance(two(lambda x: x in Flight and (x, London) in Origin,\n'
                                               '...     lambda y: there_exists(lambda z: z in Capital,\n'
                                               '...                            lambda w: (y, w) in Destination)), bool) \\\n'
                                               '... and two(lambda x: x in Flight, lambda y: (y, NewYork) in Destination)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
