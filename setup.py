from distutils.core import setup, Extension
from Cython.Build import cythonize

ext_utils = Extension('utils.anonymiser',
                      sources=['utils/cython/anonymiser.pyx', 'utils/cython/Anonymiser.cpp'],
                      libraries=['ssl', 'crypto'],
                      extra_compile_args=['-std=c++11 -fno-strict-prototypes'],
                      language='c++',
)


setup(name='example_cython',
      ext_modules=cythonize([ext_utils])
)
