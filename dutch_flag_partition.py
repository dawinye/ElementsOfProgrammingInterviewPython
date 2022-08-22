def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]

    # Keep the following invariants during partitioning :
    # bottom group: A[: smaller ].
    # middle group: A[smaller:equal ].
    # unclassified group: A[equal:larger ].
    # top group: A[larger :].

    smaller, equal, larger= 0, 0, len(A)
    while equal < larger:
        
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] ==  pivot:
            equal += 1
        else:
            larger -= 1
            A[larger], A[equal] = A[equal], A[larger]