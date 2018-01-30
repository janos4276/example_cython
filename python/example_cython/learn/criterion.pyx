cimport example_cython.sklearn.tree.dummy

cdef class FaabCriterion(Dummy):
    def __cinit__(self):
        self.public_faab_five = 5.0
        self.private_faab_five = 5

