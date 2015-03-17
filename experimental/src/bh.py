#!/usr/bin/env python
#
# Copyright (c) 2008, Bjoern B. Brandenburg <bbb [at] cs.unc.edu>
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS  PROVIDED BY THE COPYRIGHT HOLDERS  AND CONTRIBUTORS "AS IS"
# AND ANY  EXPRESS OR  IMPLIED WARRANTIES, INCLUDING,  BUT NOT LIMITED  TO, THE
# IMPLIED WARRANTIES  OF MERCHANTABILITY AND  FITNESS FOR A  PARTICULAR PURPOSE
# ARE  DISCLAIMED. IN NO  EVENT SHALL  THE COPYRIGHT  OWNER OR  CONTRIBUTORS BE
# LIABLE  FOR   ANY  DIRECT,  INDIRECT,  INCIDENTAL,   SPECIAL,  EXEMPLARY,  OR
# CONSEQUENTIAL  DAMAGES  (INCLUDING,  BUT   NOT  LIMITED  TO,  PROCUREMENT  OF
# SUBSTITUTE  GOODS OR SERVICES;  LOSS OF  USE, DATA,  OR PROFITS;  OR BUSINESS
# INTERRUPTION)  HOWEVER CAUSED  AND ON  ANY  THEORY OF  LIABILITY, WHETHER  IN
# CONTRACT,  STRICT  LIABILITY, OR  TORT  (INCLUDING  NEGLIGENCE OR  OTHERWISE)
# ARISING IN ANY  WAY OUT OF THE USE  OF THIS SOFTWARE, EVEN IF  ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

"""An implementation of Binomial Heaps.

From Wikipedia:
  A binomial heap is a heap similar to a binary heap but also supporting the
  operation of merging two heaps quickly. This is achieved by using a special
  tree structure.

  All of the following operations work in O(log n) time on a binomial heap with
  n elements:
    - Insert a new element to the heap
    - Find the element with minimum key
    - Delete the element with minimum key from the heap
    - Decrease key of a given element
    - Delete given element from the heap
    - Merge two given heaps to one heap

  More details: http://en.wikipedia.org/wiki/Binomial_heap

This implementation is based on the description in CLRS.
"""

class ItemRef(object):
    """Reference to an item in the heap. Used for decreasing keys and deletion.
    Do not use this class directly; only use instances returned by
    BinomialHeap.insert()!

    You should only use ItemRef.delete() and ItemRef.decrease(new_priority).
    """
    def __init__(self, node, get_heap):
        self.ref      = node
        self.get_heap = get_heap
        self.in_tree  = True

    def __str__(self):
        if self.in_tree:
            return "<BinomialHeap Reference to '%s'>" % str(self.ref.val)
        else:
            return "<stale BinomialHeap Reference>"

    def decrease(self, new_key):
        "Update the priority of the referenced item to a lower value."
        assert self.in_tree
        assert self.ref.ref == self
        self.ref.decrease(new_key)

    def delete(self):
        """Remove the referenced item from the heap.
        """
        self.decrease(self)
        v = self.get_heap().extract_min()
        assert not self.in_tree
        assert v is self.ref.val

    def in_heap(self, heap):
        """Returns True if the referenced item is part of the BinomialHeap 'heap';
        False otherwise.
        """
        return self.in_tree and self.get_heap() == heap

    def __lt__(self, other):
        "Behaves like negative infinity: always True."
        return True

    def __gt__(self, other):
        "Behaves like negative infinity: always False."
        return False


class BinomialHeap(object):
    """Usage:
    > H1 = BinomialHeap()
    > H1.insert(40, "fast.")
    > H1.insert(10, "Merging")
    > H2 = BinomialHeap([(30, "quite"), (20, "is")])
    > H1 += H2
    > for x in H1:
    >   print x,
     =>  "Merging is quite fast."

    """

    class Node(object):
        "Internal node of the heap. Don't use directly."
        def __init__(self, get_heap, key, val=None):
            self.degree = 0
            self.parent = None
            self.next   = None
            self.child  = None
            self.key    = key
            self.ref    = ItemRef(self, get_heap)
            if val == None:
                val = key
            self.val    = val

        def getStrKey(x):
            if x:
                return str(x.key)
            else:
                return 'NIL'
            
        def __str__(self):
            return '(%s, c:%s, n:%s)' % (getStrKey(self), getStrKey(self.child), getStrKey(self.next))

        def link(self, other):
            "Makes other a subtree of self."
            other.parent  = self
            other.next    = self.child
            self.child    = other
            self.degree  += 1

        def decrease(self, new_key):
            node = self
            assert new_key < node.key
            node.key = new_key
            cur    = node
            parent = cur.parent
            while parent and cur.key < parent.key:
                # need to bubble up
                # swap refs
                parent.ref.ref, cur.ref.ref = cur, parent
                parent.ref, cur.ref         = cur.ref, parent.ref
                # now swap keys and payload
                parent.key, cur.key         = cur.key, parent.key
                parent.val, cur.val         = cur.val, parent.val
                # step up
                cur    = parent
                parent = cur.parent

        @staticmethod
        def roots_merge(h1, h2):
            """Merge two lists of heap roots, sorted by degree.
            Returns the new head.
            """
            if not h1:
                return h2
            if not h2:
                return h1
            if h1.degree < h2.degree:
                h  = h1
                h1 = h.next
            else:
                h  = h2
                h2 = h2.next
            p = h
            while h2 and h1:
                if h1.degree < h2.degree:
                    p.next = h1
                    h1 = h1.next
                else:
                    p.next = h2
                    h2 = h2.next
                p = p.next
            if h2:
                p.next = h2
            else:
                p.next = h1
            return h

        @staticmethod
        def roots_reverse(h):
            """Reverse the heap root list.
            Returns the new head. Also clears parent references.
            """
            if not h:
                return None
            tail = None
            next = h
            h.parent = None
            while h.next:
                next = h.next
                h.next = tail
                tail   = h
                h = next
                h.parent = None
            h.next = tail
            return h

    class __Ref(object):
        def __init__(self, h):
            self.heap = h
            self.ref  = None
        def get_heap_ref(self):
            if not self.ref:
                return self
            else:
                # compact
                self.ref  = self.ref.get_heap_ref()
                return self.ref
        def get_heap(self):
            return self.get_heap_ref().heap

    def __init__(self, lst=[]):
        """Populate a new heap with the (key, value) pairs in 'lst'.
        If the elements of lst are not subscriptable, then they are treated as
        opaque elements and inserted into the heap themselves.
        """
        self.head = None
        self.size = 0
        self.ref  = BinomialHeap.__Ref(self)
        for x in lst:
            try:
                self.insert(x[0], x[1])
            except TypeError:
                self.insert(x)

    def insert(self, key, value=None):
        """Insert 'value' in to the heap with priority 'key'. If 'value' is omitted,
        then 'key' is used as the value.
        Returns a reference (of type ItemRef) to the internal node in the tree.
        Use this reference to delete the key or to change its priority.
        """
        n = BinomialHeap.Node(self.ref.get_heap, key, value)
        self.__union(n)
        self.size += 1
        return n.ref

    def union(self, other):
        """Merge 'other' into 'self'. Returns None.
        Note: This is a destructive operation; 'other' is an empty heap afterwards.
        """
        assert (self != other)
        self.size = self.size + other.size
        h2        = other.head
        self.__union(h2)
        other.ref.ref = self.ref
        other.__init__()

    def min(self):
        """Returns the value with the minimum key (= highest priority) in the heap
        without removing it, or None if the heap is empty.
        """
        pos = self.__min()
        if pos:
            return pos[0].val
        else:
            return None

    def extract_min(self):
        """Returns the value with the minimum key (= highest priority) in the heap
        AND removes it from the heap, or None if the heap is empty.
        """
        # find mininum
        pos = self.__min()
        if not pos:
            return None
        else:
            (x, prev) = pos
            # remove from list
            if prev:
                prev.next = x.next
            else:
                self.head = x.next
            kids = BinomialHeap.Node.roots_reverse(x.child)
            self.__union(kids)
            x.ref.in_tree = False
            self.size -= 1
            return x.val

    def __nonzero__(self):
        """True if the heap is not empty; False otherwise."""
        return self.head != None

    def __iter__(self):
        """Returns a _destructive_ iterator over the values in the heap.
        This violates the iterator protocol slightly, but is very useful.
        """
        return self

    def __len__(self):
        """Returns the number of items in this heap."""
        return self.size

    def __setitem__(self, key, value):
        """Insert.
        H[key] = value  is equivalent to  H.insert(key, value)
        """
        self.insert(key, value)

    def __iadd__(self, other):
        """Merge.
        a += b  is equivalent to  a.union(b).
        """
        self.union(other)
        return self

    def next(self):
        """Returns the value with the minimum key (= highest priority) in the heap
        AND removes it from the heap; raises StopIteration if the heap is empty.
        """
        if self.head:
            return self.extract_min()
        else:
            raise StopIteration

    def __contains__(self, ref):
        """Test whether a given reference 'ref' (of ItemRef) is in this heap.
        """
        if type(ref) != ItemRef:
            raise TypeError, "Expected an ItemRef"
        else:
            return ref.in_heap(self)

    def __min(self):
        if not self.head:
            return None
        min  = self.head
        min_prev = None
        prev = min
        cur  = min.next
        while cur:
            if cur.key < min.key:
                min = cur
                min_prev = prev
            prev = cur
            cur  = cur.next
        return (min, min_prev)

    def __union(self, h2):
        if not h2:
            # nothing to do
            return
        h1 = self.head
        if not h1:
            self.head = h2
            return
        h1 = BinomialHeap.Node.roots_merge(h1, h2)
        prev = None
        x    = h1
        next = x.next
        while next:
            if x.degree != next.degree or \
                    (next.next and next.next.degree == x.degree):
                prev = x
                x    = next
            elif x.key <= next.key:
                # x becomes the root of next
                x.next = next.next
                x.link(next)
            else:
                # next becomes the root of x
                if not prev:
                    # update the "master" head
                    h1 = next
                else:
                    # just update previous link
                    prev.next = next
                next.link(x)
                # x is not toplevel anymore, update ref by advancing
                x = next
            next = x.next
        self.head = h1

def heap(lst=[]):
    """Create a new heap. lst should be a sequence of (key, value) pairs.
    Shortcut for BinomialHeap(lst)
    """
    return BinomialHeap(lst)

if __name__ == "__main__":
    tokens1 = [(24, 'all'), (16, 'star'), (9, 'true.\nSinging'), (7, 'clear'),
               (25, 'praises'), (13, 'to'), (5, 'Heel'),
               (6, 'voices\nRinging'), (26, 'thine.'), (21, 'shine\nCarolina'),
               (117, 'Rah,'), (102, 'Tar'), (108, 'bred\nAnd'), (125, 'Rah!'),
               (107, 'Heel'), (118, 'Rah,'), (111, "die\nI'm"),
               (115, 'dead.\nSo'), (120, 'Rah,'), (121, "Car'lina-lina\nRah,"),
               (109, 'when'), (105, 'a'), (123, "Car'lina-lina\nRah!"),
               (110, 'I'), (114, 'Heel'), (101, 'a'), (106, 'Tar'),
               (18, 'all\nClear'), (14, 'the')]
    tokens2 = [(113, 'Tar'), (124, 'Rah!'), (112, 'a'), (103, 'Heel'),
               (104, "born\nI'm"), (122, 'Rah,'), (119, "Car'lina-lina\nRah,"),
               (2, 'sound'), (20, 'radiance'), (12, 'N-C-U.\nHail'),
               (10, "Carolina's"), (3, 'of'), (17, 'of'),
               (23, 'gem.\nReceive'), (19, 'its'), (0, '\nHark'),
               (22, 'priceless'), (4, 'Tar'), (1, 'the'), (8, 'and'),
               (15, 'brightest'), (11, 'praises.\nShouting'),
               (100, "\nI'm"), (116, "it's")]
    h1 = heap(tokens1)
    h2 = heap(tokens2)
    h3 = heap()
    line = "\n==================================="
    h3[90]  = line
    h3[-2]  = line
    h3[200] = line
    h3[201] = '\n\n'
    t1ref = h3.insert(1000, "\nUNC Alma Mater:")
    t2ref = h3.insert(120, "\nUNC Fight Song:")
    bad   = [h3.insert(666, "Dook"),
             h3.insert(666, "Go Devils!"),
             h3.insert(666, "Blue Devils") ]

    ref = bad[0]
    print "%s: \n\tin h1: %s\n\tin h2: %s\n\tin h3: %s" % \
        (str(ref), ref in h1, ref in h2, ref in h3)

    print "Merging h3 into h2..."
    h2 += h3

    print "%s: \n\tin h1: %s\n\tin h2: %s\n\tin h3: %s" % \
        (str(ref), ref in h1, ref in h2, ref in h3)

    print "Merging h2 into h1..."
    h1 += h2

    print "%s: \n\tin h1: %s\n\tin h2: %s\n\tin h3: %s" % \
        (str(ref), ref in h1, ref in h2, ref in h3)

    t1ref.decrease(-1)
    t2ref.decrease(99)

    for ref in bad:
        ref.delete()
    for x in h1:
        print x,

