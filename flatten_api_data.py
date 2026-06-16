def flatten_data(api_data):
    '''making api_data into flattened dictionary in list = fd
    so sqlite can put it in a table'''
    fd = []

    for dictionary in api_data:
       d = {'id' : dictionary['id'],
        'name' : dictionary['name'],
        'username' : dictionary['username'],
        'email' : dictionary['email'],
        'city' : dictionary['address']['city'],
        'company_name' : dictionary['company']['name']}
       fd.append(d)

    return fd





