from distutils.core import setup, Extension
from Cython.Build import cythonize

ext_utils = Extension('utils.anon',
                      sources=['utils/cython/anon.pyx', 'utils/cython/Anonymiser.cpp'],
                      #include_dirs=['utils/cython'],
                      libraries=['ssl', 'crypto'],
                      extra_compile_args=['-std=c++11', '-Os'],
                      language='c++',
                      )

setup(name='example_cython',
      packages=['utils'],
      #package_dirs=['utils'],
      #package_data={'utils': ['cython/*.h', 'cython/*.c', 'cython/*.cpp', 'cython/*.pyx']},
      ext_modules=cythonize([ext_utils]),
      )
