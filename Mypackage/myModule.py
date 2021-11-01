def top_n(items, n):
    """ Return the top n items in an array in descending order.

    Args:
        items(array): list or an array like object
        n (int): number of items to return
    
    Return:
        top n items in an array in descending order

    E.gs:
        >>> top_n([8,3,4,7,2,9],3)
        [9,7,8]

    """

    for i in range(top_n):
        for j in range(len(items)-1-i):
            if items[j]>items[j+1]:
                items[j],items[j+1]=items[j+1],items[j]
    top_n = items[-n:]
    return
