
users =  {
        'first_name': 'daniel',
        'last_name': 'hafez',
        'id': 1
    }, {
        'first_name': 'john',
        'last_name': 'guitar',
        'id': 2
    }, {
        'first_name': 'michael',
        'last_name': 'jax',
        'id': 3
    },{
        'first_name': 'jimmy',
        'last_name': 'hendrix',
        'id': 4
    }, {
        'first_name': 'max',
        'last_name': 'pezzali',
        'id': 5
    }, {
        'first_name': 'eric',
        'last_name': 'clapton',
        'id': 6
    }




instruments_data = {
    1: {
        'id': 1,
        'name': 'guitar',
        'user': [users[0]],
        'youtube': 'https://www.youtube.com/watch?v=w4a2ge9N31E'
    },
    2: {
        'id': 2,
        'name': 'piano',
        'user': [users[1], users[2]],
        'youtube': 'https://www.youtube.com/watch?v=w4a2ge9N31E'

    },
    3: {
        'id': 3,
        'name': 'bass',
        'user': [users[2], users[3]],
        'youtube': 'https://www.youtube.com/watch?v=w4a2ge9N31E'
    },
    4: {
        'id': 4,
        'name': 'violin',
        'user': [users[0], users[4]],
        'youtube': 'https://www.youtube.com/watch?v=w4a2ge9N31E'
    }
}