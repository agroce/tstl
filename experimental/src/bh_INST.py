import covertool
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
        covertool.cover("bh.py:59")
        self.ref      = node
        covertool.cover("bh.py:60")
        self.get_heap = get_heap
        covertool.cover("bh.py:61")
        self.in_tree  = True

    def __str__(self):
        covertool.cover("bh.py:64")
        if self.in_tree:
            covertool.cover("bh.py:65")
            return "<BinomialHeap Reference to '%s'>" % str(self.ref.val)
        else:
            covertool.cover("bh.py:67")
            return "<stale BinomialHeap Reference>"

    def decrease(self, new_key):
        covertool.cover("bh.py:70")
        "Update the priority of the referenced item to a lower value."
        covertool.cover("bh.py:71")
        assert self.in_tree
        covertool.cover("bh.py:72")
        assert self.ref.ref == self
        covertool.cover("bh.py:73")
        self.ref.decrease(new_key)

    def delete(self):
        """Remove the referenced item from the heap.
        """
        covertool.cover("bh.py:78")
        self.decrease(self)
        covertool.cover("bh.py:79")
        v = self.get_heap().extract_min()
        covertool.cover("bh.py:80")
        assert not self.in_tree
        covertool.cover("bh.py:81")
        assert v is self.ref.val

    def in_heap(self, heap):
        """Returns True if the referenced item is part of the BinomialHeap 'heap';
        False otherwise.
        """
        covertool.cover("bh.py:87")
        return self.in_tree and self.get_heap() == heap

    def __lt__(self, other):
        covertool.cover("bh.py:90")
        "Behaves like negative infinity: always True."
        covertool.cover("bh.py:91")
        return True

    def __gt__(self, other):
        covertool.cover("bh.py:94")
        "Behaves like negative infinity: always False."
        covertool.cover("bh.py:95")
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
        covertool.cover("bh.py:112")
        "Internal node of the heap. Don't use directly."
        def __init__(self, get_heap, key, val=None):
            covertool.cover("bh.py:114")
            self.degree = 0
            covertool.cover("bh.py:115")
            self.parent = None
            covertool.cover("bh.py:116")
            self.next   = None
            covertool.cover("bh.py:117")
            self.child  = None
            covertool.cover("bh.py:118")
            self.key    = key
            covertool.cover("bh.py:119")
            self.ref    = ItemRef(self, get_heap)
            covertool.cover("bh.py:120")
            if val == None:
                covertool.cover("bh.py:121")
                val = key
            covertool.cover("bh.py:122")
            self.val    = val

        def getStrKey(x):
            covertool.cover("bh.py:125")
            if x:
                covertool.cover("bh.py:126")
                return str(x.key)
            else:
                covertool.cover("bh.py:128")
                return 'NIL'
            
        def __str__(self):
            covertool.cover("bh.py:131")
            return '(%s, c:%s, n:%s)' % (getStrKey(self), getStrKey(self.child), getStrKey(self.next))

        def link(self, other):
            covertool.cover("bh.py:134")
            "Makes other a subtree of self."
            covertool.cover("bh.py:135")
            other.parent  = self
            covertool.cover("bh.py:136")
            other.next    = self.child
            covertool.cover("bh.py:137")
            self.child    = other
            covertool.cover("bh.py:138")
            self.degree  += 1

        def decrease(self, new_key):
            covertool.cover("bh.py:141")
            node = self
            covertool.cover("bh.py:142")
            assert new_key < node.key
            covertool.cover("bh.py:143")
            node.key = new_key
            covertool.cover("bh.py:144")
            cur    = node
            covertool.cover("bh.py:145")
            parent = cur.parent
            covertool.cover("bh.py:146")
            while parent and cur.key < parent.key:
                # need to bubble up
                # swap refs
                covertool.cover("bh.py:149")
                parent.ref.ref, cur.ref.ref = cur, parent
                covertool.cover("bh.py:150")
                parent.ref, cur.ref         = cur.ref, parent.ref
                # now swap keys and payload
                covertool.cover("bh.py:152")
                parent.key, cur.key         = cur.key, parent.key
                covertool.cover("bh.py:153")
                parent.val, cur.val         = cur.val, parent.val
                # step up
                covertool.cover("bh.py:155")
                cur    = parent
                covertool.cover("bh.py:156")
                parent = cur.parent

        @staticmethod
        def roots_merge(h1, h2):
            """Merge two lists of heap roots, sorted by degree.
            Returns the new head.
            """
            covertool.cover("bh.py:163")
            if not h1:
                covertool.cover("bh.py:164")
                return h2
            covertool.cover("bh.py:165")
            if not h2:
                covertool.cover("bh.py:166")
                return h1
            covertool.cover("bh.py:167")
            if h1.degree < h2.degree:
                covertool.cover("bh.py:168")
                h  = h1
                covertool.cover("bh.py:169")
                h1 = h.next
            else:
                covertool.cover("bh.py:171")
                h  = h2
                covertool.cover("bh.py:172")
                h2 = h2.next
            covertool.cover("bh.py:173")
            p = h
            covertool.cover("bh.py:174")
            while h2 and h1:
                covertool.cover("bh.py:175")
                if h1.degree < h2.degree:
                    covertool.cover("bh.py:176")
                    p.next = h1
                    covertool.cover("bh.py:177")
                    h1 = h1.next
                else:
                    covertool.cover("bh.py:179")
                    p.next = h2
                    covertool.cover("bh.py:180")
                    h2 = h2.next
                covertool.cover("bh.py:181")
                p = p.next
            covertool.cover("bh.py:182")
            if h2:
                covertool.cover("bh.py:183")
                p.next = h2
            else:
                covertool.cover("bh.py:185")
                p.next = h1
            covertool.cover("bh.py:186")
            return h

        @staticmethod
        def roots_reverse(h):
            """Reverse the heap root list.
            Returns the new head. Also clears parent references.
            """
            covertool.cover("bh.py:193")
            if not h:
                covertool.cover("bh.py:194")
                return None
            covertool.cover("bh.py:195")
            tail = None
            covertool.cover("bh.py:196")
            next = h
            covertool.cover("bh.py:197")
            h.parent = None
            covertool.cover("bh.py:198")
            while h.next:
                covertool.cover("bh.py:199")
                next = h.next
                covertool.cover("bh.py:200")
                h.next = tail
                covertool.cover("bh.py:201")
                tail   = h
                covertool.cover("bh.py:202")
                h = next
                covertool.cover("bh.py:203")
                h.parent = None
            covertool.cover("bh.py:204")
            h.next = tail
            covertool.cover("bh.py:205")
            return h

    class __Ref(object):
        def __init__(self, h):
            covertool.cover("bh.py:209")
            self.heap = h
            covertool.cover("bh.py:210")
            self.ref  = None
        def get_heap_ref(self):
            covertool.cover("bh.py:212")
            if not self.ref:
                covertool.cover("bh.py:213")
                return self
            else:
                # compact
                covertool.cover("bh.py:216")
                self.ref  = self.ref.get_heap_ref()
                covertool.cover("bh.py:217")
                return self.ref
        def get_heap(self):
            covertool.cover("bh.py:219")
            return self.get_heap_ref().heap

    def __init__(self, lst=[]):
        """Populate a new heap with the (key, value) pairs in 'lst'.
        If the elements of lst are not subscriptable, then they are treated as
        opaque elements and inserted into the heap themselves.
        """
        covertool.cover("bh.py:226")
        self.head = None
        covertool.cover("bh.py:227")
        self.size = 0
        covertool.cover("bh.py:228")
        self.ref  = BinomialHeap.__Ref(self)
        covertool.cover("bh.py:229")
        for x in lst:
            covertool.cover("bh.py:230")
            try:
                covertool.cover("bh.py:231")
                self.insert(x[0], x[1])
            except TypeError:
                covertool.cover("bh.py:233")
                self.insert(x)

    def insert(self, key, value=None):
        """Insert 'value' in to the heap with priority 'key'. If 'value' is omitted,
        then 'key' is used as the value.
        Returns a reference (of type ItemRef) to the internal node in the tree.
        Use this reference to delete the key or to change its priority.
        """
        covertool.cover("bh.py:241")
        n = BinomialHeap.Node(self.ref.get_heap, key, value)
        covertool.cover("bh.py:242")
        self.__union(n)
        covertool.cover("bh.py:243")
        self.size += 1
        covertool.cover("bh.py:244")
        return n.ref

    def union(self, other):
        """Merge 'other' into 'self'. Returns None.
        Note: This is a destructive operation; 'other' is an empty heap afterwards.
        """
        covertool.cover("bh.py:250")
        assert (self != other)
        covertool.cover("bh.py:251")
        self.size = self.size + other.size
        covertool.cover("bh.py:252")
        h2        = other.head
        covertool.cover("bh.py:253")
        self.__union(h2)
        covertool.cover("bh.py:254")
        other.ref.ref = self.ref
        covertool.cover("bh.py:255")
        other.__init__()

    def min(self):
        """Returns the value with the minimum key (= highest priority) in the heap
        without removing it, or None if the heap is empty.
        """
        covertool.cover("bh.py:261")
        pos = self.__min()
        covertool.cover("bh.py:262")
        if pos:
            covertool.cover("bh.py:263")
            return pos[0].val
        else:
            covertool.cover("bh.py:265")
            return None

    def extract_min(self):
        """Returns the value with the minimum key (= highest priority) in the heap
        AND removes it from the heap, or None if the heap is empty.
        """
        # find mininum
        covertool.cover("bh.py:272")
        pos = self.__min()
        covertool.cover("bh.py:273")
        if not pos:
            covertool.cover("bh.py:274")
            return None
        else:
            covertool.cover("bh.py:276")
            (x, prev) = pos
            # remove from list
            covertool.cover("bh.py:278")
            if prev:
                covertool.cover("bh.py:279")
                prev.next = x.next
            else:
                covertool.cover("bh.py:281")
                self.head = x.next
            covertool.cover("bh.py:282")
            kids = BinomialHeap.Node.roots_reverse(x.child)
            covertool.cover("bh.py:283")
            self.__union(kids)
            covertool.cover("bh.py:284")
            x.ref.in_tree = False
            covertool.cover("bh.py:285")
            self.size -= 1
            covertool.cover("bh.py:286")
            return x.val

    def __nonzero__(self):
        """True if the heap is not empty; False otherwise."""
        return self.head != None

    def __iter__(self):
        """Returns a _destructive_ iterator over the values in the heap.
        covertool.cover("bh.py:294")
        This violates the iterator protocol slightly, but is very useful.
        """
        return self

    def __len__(self):
        """Returns the number of items in this heap."""
        covertool.cover("bh.py:300")
        return self.size

    def __setitem__(self, key, value):
        """Insert.
        H[key] = value  is equivalent to  H.insert(key, value)
        """
        covertool.cover("bh.py:306")
        self.insert(key, value)

    def __iadd__(self, other):
        """Merge.
        a += b  is equivalent to  a.union(b).
        """
        covertool.cover("bh.py:312")
        self.union(other)
        covertool.cover("bh.py:313")
        return self

    def next(self):
        """Returns the value with the minimum key (= highest priority) in the heap
        AND removes it from the heap; raises StopIteration if the heap is empty.
        """
        covertool.cover("bh.py:319")
        if self.head:
            covertool.cover("bh.py:320")
            return self.extract_min()
        else:
            covertool.cover("bh.py:322")
            raise StopIteration

    def __contains__(self, ref):
        """Test whether a given reference 'ref' (of ItemRef) is in this heap.
        """
        covertool.cover("bh.py:327")
        if type(ref) != ItemRef:
            covertool.cover("bh.py:328")
            raise TypeError, "Expected an ItemRef"
        else:
            covertool.cover("bh.py:330")
            return ref.in_heap(self)

    def __min(self):
        covertool.cover("bh.py:333")
        if not self.head:
            covertool.cover("bh.py:334")
            return None
        covertool.cover("bh.py:335")
        min  = self.head
        covertool.cover("bh.py:336")
        min_prev = None
        covertool.cover("bh.py:337")
        prev = min
        covertool.cover("bh.py:338")
        cur  = min.next
        covertool.cover("bh.py:339")
        while cur:
            covertool.cover("bh.py:340")
            if cur.key < min.key:
                covertool.cover("bh.py:341")
                min = cur
                covertool.cover("bh.py:342")
                min_prev = prev
            covertool.cover("bh.py:343")
            prev = cur
            covertool.cover("bh.py:344")
            cur  = cur.next
        covertool.cover("bh.py:345")
        return (min, min_prev)

    def __union(self, h2):
        covertool.cover("bh.py:348")
        if not h2:
            # nothing to do
            covertool.cover("bh.py:350")
            return
        covertool.cover("bh.py:351")
        h1 = self.head
        covertool.cover("bh.py:352")
        if not h1:
            covertool.cover("bh.py:353")
            self.head = h2
            covertool.cover("bh.py:354")
            return
        covertool.cover("bh.py:355")
        h1 = BinomialHeap.Node.roots_merge(h1, h2)
        covertool.cover("bh.py:356")
        prev = None
        covertool.cover("bh.py:357")
        x    = h1
        covertool.cover("bh.py:358")
        next = x.next
        covertool.cover("bh.py:359")
        while next:
            covertool.cover("bh.py:360")
            if x.degree != next.degree or \
                    (next.next and next.next.degree == x.degree):
                covertool.cover("bh.py:362")
                prev = x
                covertool.cover("bh.py:363")
                x    = next
            elif x.key <= next.key:
                # x becomes the root of next
                covertool.cover("bh.py:366")
                x.next = next.next
                covertool.cover("bh.py:367")
                x.link(next)
            else:
                # next becomes the root of x
                covertool.cover("bh.py:370")
                if not prev:
                    # update the "master" head
                    covertool.cover("bh.py:372")
                    h1 = next
                else:
                    # just update previous link
                    covertool.cover("bh.py:375")
                    prev.next = next
                covertool.cover("bh.py:376")
                next.link(x)
                # x is not toplevel anymore, update ref by advancing
                covertool.cover("bh.py:378")
                x = next
            covertool.cover("bh.py:379")
            next = x.next
        covertool.cover("bh.py:380")
        self.head = h1

def heap(lst=[]):
    """Create a new heap. lst should be a sequence of (key, value) pairs.
    Shortcut for BinomialHeap(lst)
    """
    covertool.cover("bh.py:386")
    return BinomialHeap(lst)

covertool.cover("bh.py:388")
if __name__ == "__main__":
    covertool.cover("bh.py:389")
    tokens1 = [(24, 'all'), (16, 'star'), (9, 'true.\nSinging'), (7, 'clear'),
               (25, 'praises'), (13, 'to'), (5, 'Heel'),
               (6, 'voices\nRinging'), (26, 'thine.'), (21, 'shine\nCarolina'),
               (117, 'Rah,'), (102, 'Tar'), (108, 'bred\nAnd'), (125, 'Rah!'),
               (107, 'Heel'), (118, 'Rah,'), (111, "die\nI'm"),
               (115, 'dead.\nSo'), (120, 'Rah,'), (121, "Car'lina-lina\nRah,"),
               (109, 'when'), (105, 'a'), (123, "Car'lina-lina\nRah!"),
               (110, 'I'), (114, 'Heel'), (101, 'a'), (106, 'Tar'),
               (18, 'all\nClear'), (14, 'the')]
    covertool.cover("bh.py:398")
    tokens2 = [(113, 'Tar'), (124, 'Rah!'), (112, 'a'), (103, 'Heel'),
               (104, "born\nI'm"), (122, 'Rah,'), (119, "Car'lina-lina\nRah,"),
               (2, 'sound'), (20, 'radiance'), (12, 'N-C-U.\nHail'),
               (10, "Carolina's"), (3, 'of'), (17, 'of'),
               (23, 'gem.\nReceive'), (19, 'its'), (0, '\nHark'),
               (22, 'priceless'), (4, 'Tar'), (1, 'the'), (8, 'and'),
               (15, 'brightest'), (11, 'praises.\nShouting'),
               (100, "\nI'm"), (116, "it's")]
    covertool.cover("bh.py:406")
    h1 = heap(tokens1)
    covertool.cover("bh.py:407")
    h2 = heap(tokens2)
    covertool.cover("bh.py:408")
    h3 = heap()
    covertool.cover("bh.py:409")
    line = "\n==================================="
    covertool.cover("bh.py:410")
    h3[90]  = line
    covertool.cover("bh.py:411")
    h3[-2]  = line
    covertool.cover("bh.py:412")
    h3[200] = line
    covertool.cover("bh.py:413")
    h3[201] = '\n\n'
    covertool.cover("bh.py:414")
    t1ref = h3.insert(1000, "\nUNC Alma Mater:")
    covertool.cover("bh.py:415")
    t2ref = h3.insert(120, "\nUNC Fight Song:")
    covertool.cover("bh.py:416")
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
        covertool.cover("bh.py:440")
        ref.delete()
    covertool.cover("bh.py:441")
    for x in h1:
        covertool.cover("bh.py:442")
        print x,

