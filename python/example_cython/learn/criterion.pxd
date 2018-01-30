from example_cython.sklearn.tree.dummy cimport Dummy

cdef class FaabCriterion(Dummy):
    cdef public double public_faab_five
    cdef int private_faab_five