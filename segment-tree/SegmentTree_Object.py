class SegmentTree:
    
    def __init__(self, array, merge, lo: int = None, hi: int = None):
        """Constructs the Segment Tree on the array structure with the merge function on interval [lo, hi].

        Args:
            array (List[Any]): The array of items to be processed in the Segment Tree
            merge (Callable[[Any, Any], Any]): The merge function that the Segment Tree utilizes to build and update the tree
            lo (int): The integer lower bound of the array to be built
            hi (int): The integer higher bound of the array to be built
        """
        self.N = len(array)
        MAXN = self.N * 4
        self.data = [0] * MAXN
        self.merge_ = merge
        
        if lo == None:
            lo = 0
        
        if hi == None:
            hi = self.N - 1
        
        self.build_(array, 1, lo, hi)

    
    def build_(self, array, idx: int, lo: int, hi: int):
        """Builds the Segment Tree with array on interval [lo, hi].

        Args:
            array (List[Any]): The array of items to be processed
            idx (int): The index of the Segment Tree you want to start at (defaults to 1 for root)
            lo (int): The integer lower bound of the array to be built
            hi (int): The integer higher bound of the array to be built
        """

        if lo == hi:
            self.data[idx] = array[lo]
        else:
            mid = (lo + hi) // 2
            self.build_(array, idx * 2, lo, mid)
            self.build_(array, idx * 2 + 1, mid + 1, hi)
            self.data[idx] = self.merge_(self.data[idx * 2], self.data[idx * 2 + 1])
    
    def query_(self, idx: int, q_lo: int, q_hi: int, lo: int, hi: int):
        """Queries the Segment Tree from interval [lo, hi], given the node with the overall interval of [q_lo, q_hi].

        Args:
            idx (int): The index of the Segment Tree you want to start at (defaults to 1 for root)
            q_lo (int): The integer lower bound of the query
            q_hi (int): The integer upper bound of the query
            lo (int): The integer lower bound of the subtree
            hi (int): The integer upper bound of the subtree
        """

        if q_lo > q_hi:
            return 0

        if lo == q_lo and hi == q_hi:
            return self.data[idx]
        else:
            mid = (lo + hi) // 2
            return self.merge_(self.query_(idx * 2, q_lo, min(q_hi, mid), lo, mid), self.query_(idx * 2 + 1, max(q_lo, mid + 1), q_hi, mid + 1, hi))

    def update_(self, idx: int, lo: int, hi: int, pos: int, new_ele):
        """Updates the Segment Tree at position pos with new_ele, given the Segment Tree bounds of [lo, hi].

        Args:
            idx (int): The index of the Segment Tree you want to start at (defaults to 1 for root)
            lo (int): The integer lower bound of the subtree
            hi (int): The integer upper bound of the subtree
            pos (int): Array position to be updated
            new_ele (Any): The new element to be updated in the Segment Tree at pos
        """

        if lo == hi:
            self.data[idx] = new_ele
        else:
            mid = (lo + hi) // 2
            if pos <= mid:
                self.update_(idx * 2, lo, mid, pos, new_ele)
            else:
                self.update_(idx * 2 + 1, mid + 1, hi, pos, new_ele)

            self.data[idx] = self.merge_(self.data[idx * 2], self.data[idx * 2 + 1])

    def query(self, q_lo: int, q_hi: int, lo: int = None, hi: int = None):
        """Queries the entire Segment Tree with query bounds of [q_lo, q_hi], given the Segment Tree bounds of [lo, hi].

        Args:
            q_lo (int): The integer lower bound of the query
            q_hi (int): The integer upper bound of the query
            lo (int): Optional, the integer lower bound of the Segment Tree (defaults to 0)
            hi (int): Optional, the integer upper bound of the Segment Tree (defaults to N - 1)
        """

        if lo == None:
            lo = 0
        if hi == None:
            hi = self.N - 1

        return self.query_(1, q_lo, q_hi, lo, hi)
    
    def update(self, idx: int, val: int, lo: int = None, hi: int = None):
        """Updates the entire Segment Tree at position idx with value val, given the Segment Tree bounds of [lo, hi].

        Args:
            idx (int): The index of the Segment Tree you want to start at (defaults to 1 for root)
            val (Any): The new element to be updated in the Segment Tree at idx
            lo (int): Optional, the integer lower bound of the Segment Tree (defaults to 0)
            hi (int): Optional, The integer upper bound of the Segment Tree (defaults to N - 1)
        """

        if lo == None:
            lo = 0
        if hi == None:
            hi = self.N - 1

        self.update_(1, lo, hi, idx, val)