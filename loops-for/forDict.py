def reverse_dict(d):
    n = {}
    for i in d.keys():
        n.update({d[i]:i})
    return n
    # swap keys and values within dict and return dict
