fields = {
    'username': {
        'type': 'string',
        'required': True,
        'minlength': 1,
        'maxlength': 50,
        'forbidden': ['root', 'admin'],
    },
    'password': {
        'type': 'string',
        'required': True,
        'maxlength': 128,
    },
    'email': {
        'type': 'string',
        'required': True,
        'maxlength': 128,
        'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
    },
    'timezone': {
        'type': 'string',
        'required': True,
        'maxlength': 128,
        'nullable': False
    }
}

rules = {
    'login': {
        'username': {
            **fields['username'],
            'forbidden': [],
        },
        'password': fields['password'],
        'timezone': fields['timezone']
    },
    'store': {
        'username': fields['username'],
        'password': fields['username'],
        'email': fields['email'],
    },
    'update': {
        'username': fields['username'],
        'password': {
            **fields['username'],
            'required': False,
            'empty': True,
        },
        'email': fields['email'],
    }
}