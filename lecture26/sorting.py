def swap(myList, ind1, ind2):
    """ Swap 2 entries in a list.

    Args:
        myList (list): The list in which to perform a swap.
            This parameter is updated in-place, swapping
            the value at ind1 with the value at ind2.

        ind1 (int): The index of the first item to swap.

        ind2 (int): The index of the second item to swap.

    Returns:
        list: a pointer to myList (not needed since myList was
        updated in-place).

    """

    tmp = myList[ind1]
    myList[ind1] = myList[ind2]
    myList[ind2] = tmp
    return myList

def insert(myList, nextInd):
    """ Insert the value at an index into an already sorted sub-list.

    Args:
        myList (list): The list in which to perform the insertion.
            All the values in myList[:nextInd] are already sorted.
            myList is updated in-place so that myList[nextInd] is
            inserted into the sublist, leaving myList[:nextInd+1]
            sorted.

        nextInd (int): The index of the item to insert into the
            already sorted sublist.

    Returns:
        list: a pointer to myList (not needed since myList was
        updated in-place).

    """

    i = nextInd
    while i > 0 and myList[i-1] > myList[i]:
        swap(myList, i-1, i)
        i = i - 1
    return myList

def merge(list1, list2):
    """ Merge two lists that are already sorted.

    Args:

        list1 (list): An already-sorted list.

        list2 (list): An already-sorted list.

    Returns:
        list: The merged list, which is also sorted.

    """

    # Initialize counters
    i = 0
    j = 0
    # Initialize empty list
    newList = []
    # Loop over all indices in list1 and list2
    while i < len(list1) or j < len(list2):
        if i >= len(list1):
            newList.append(list2[j])
            j = j + 1
        elif j >= len(list2):
            newList.append(list1[i])
            i = i + 1
        elif list1[i] < list2[j]:
            newList.append(list1[i])
            i = i + 1
        else:
            newList.append(list2[j])
            j = j + 1
    return newList

def BubbleSort(myList):
    """ Sort a list in ascending order using the algorithm bubble sort.

    Args:
        myList (list): The list to sort. Contains n numerical values,
            in any order. This list will be updated in-place.

    Returns:
        list: a pointer to myList (not needed since myList was
        updated in-place).

    """

    didSwap = True
    while didSwap:
        didSwap = False
        for i in range(len(myList)-1):
            if myList[i] > myList[i+1]:
                myList = swap(myList, i, i+1)
                didSwap = True
    return myList

def SelectionSort(myList):
    """ Sort a list in ascending order using the algorithm selection sort.

    Args:
        myList (list): The list to sort. Contains n numerical values,
            in any order. This list will be updated in-place.

    Returns:
        list: a pointer to myList (not needed since myList was
        updated in-place).

    """

    for i in range(len(myList)):
        end = len(myList) - 1 - i
        maxInd = end
        for j in range(end):
            if myList[j] > myList[maxInd]:
                maxInd = j
        myList = swap(myList, maxInd, end)
    return myList

def InsertionSort(myList):
    """ Sort a list in ascending order using the algorithm insertion sort.

    Args:
        myList (list): The list to sort. Contains n numerical values,
            in any order. This list will be updated in-place.

    Returns:
        list: a pointer to myList (not needed since myList was
        updated in-place).

    """

    for i in range(len(myList)):
        insert(myList, i)
    return myList

def MergeSort(myList):
    """ Sort a list in ascending order using the algorithm merge sort.

    Args:
        myList (list): The list to sort. Contains n numerical values,
            in any order. This list will be updated in-place.

    Returns:
        list: a pointer to myList (not needed since myList was
        updated in-place).

    """

    if len(myList) > 1:
        middle = len(myList) // 2
        return merge(MergeSort(myList[:middle]), MergeSort(myList[middle:]))
    else:
        return myList
