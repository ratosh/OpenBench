FRAMEWORK_REPO_URL = 'http://github.com/ratosh/OpenBench/'

FRAMEWORK_DEFAULTS = {

    'config' : {

        # Framework source, must be changed for your instance
        'framework'   : 'http://github.com/ratosh/OpenBench/',

        # Default to uci since everyone uses it
        'protocol'    : 'uci',

        # Defaults for Short Time Control tests (default on newTest)
        'stc'         : {
            'threads'     : 1,
            'hash'        : 8,
            'timecontrol' : '10.0+0.05',
        },

        # Defaults for Long Time Control tests (ease of submitting LTC)
        'ltc'         : {
            'threads'     : 1,
            'hash'        : 64,
            'timecontrol' : '60.0+0.3',
        },

        # SPRT bounds and confidence values
        'elolower'    : -1.5,
        'eloupper'    : 4.5,
        'alpha'       : 0.1,
        'beta'        : 0.1,

        # Configured engines for the framework. To scale NPS for your engine,
        # in order to match the time controls used here, do the following.
        # Average a few bench runs for the latest version of Ethereal. Now
        # take a few bench runs for the latest version of the new engine.
        # Scale your NPS to match Ethereal's NPS of 1,750,000
        'engines'     : {
            'Ethereal' : {
                'name'    : 'Ethereal',
                'source'  : 'https://github.com/AndyGrant/Ethereal',
                'nps'     : 1500000,
                'default' : False,
            },

            'Laser' : {
                'name'    : 'Laser',
                'source'  : 'https://github.com/jeffreyan11/uci-chess-engine',
                'nps'     : 625000,
                'default' : False,
            },

            'Pirarucu' : {
                'name'    : 'Pirarucu',
                'source'  : 'https://github.com/ratosh/pirarucu',
                'nps'     : 400000,
                'default' : True,
            },
        },

        # Book confgiruation. When addding a book, follow the provided template.
        # The SHA is defined by hashlib.sha256(book).hexdigest(). OpenBench.py
        # (Client File) has an example to show you how to find a hash digest
        'books' : {
            '2moves_v1.pgn' : {
                'name'    : '2moves_v1.pgn',
                'sha'     : '46aed7f2696618b2b914942032957b7a97a8f343bf54ba83e20a47818f0d42e0',
                'source'  : FRAMEWORK_REPO_URL + 'raw/master/Books/2moves_v1.pgn',
                'default' : False,
            },

            '2moves_v2.pgn' : {
                'name'    : '2moves_v2.pgn',
                'sha'     : 'c88dffb891e3cf126711792fb2e12a2fc97be3d995ba7bf44e49efe6f524b3bf',
                'source'  : FRAMEWORK_REPO_URL + 'raw/master/Books/2moves_v2.pgn',
                'default' : True,
            },

            '8moves_v3.pgn' : {
                'name'    : '8moves_v3.pgn',
                'sha'     : '04fcce1488a94f3b7795cef6f74d89016eb278328897c1018e6162c5967273f5',
                'source'  : FRAMEWORK_REPO_URL + 'raw/master/Books/8moves_v3.pgn',
                'default' : False,
            }
        },
    }
}
