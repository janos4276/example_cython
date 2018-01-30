# distutils: language = c++

from libcpp.string cimport string

cdef extern from 'cpp/Anonymiser.h' namespace 'adelost':
    cdef cppclass Anonymiser:
        Anonymiser(const string& salt)
        int hash(const string& pii)
        string digest() const

cdef class Anon:
    cdef Anonymiser *_this_ptr

    def __cinit__(self, bytes salt=b''):
        self._this_ptr = new Anonymiser(salt)

    def __dealloc__(self):
        if self._this_ptr != NULL:
            del self._this_ptr

    cpdef bytes digest(self, bytes pii):
        self._this_ptr.hash(pii)
        return <bytes> self._this_ptr.digest()

