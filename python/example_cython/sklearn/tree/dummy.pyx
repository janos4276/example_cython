cdef class Dummy:
    def __cinit(self):
        self.dummy = 10.0

    cpdef hello(self):
        print('Hello World')