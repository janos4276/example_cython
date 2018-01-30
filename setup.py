import logging
import sys

import numpy as np
from setuptools import Extension, find_packages, setup

logging.basicConfig()
logger = logging.getLogger(__file__)

try:
    import Cython.Build as CythonBuild
except ImportError:
    logger.fatal('Cython is required! Please install cython, e.g. pip install cython.')
    sys.exit(1)

NAME = 'example_cython'

MAJOR = 1
REVISION = 0
PATCH = 0
DEV = True

VERSION = '{major}.{revision}.{patch}'.format(major=MAJOR, revision=REVISION, patch=PATCH)
FULL_VERSION = VERSION
if DEV:
    FULL_VERSION += '.dev'

SETUP_REQUIRES = ['cython>=0.27.3',
                  ]

REQUIREMENTS = ['cython==0.27.3',
                'numpy==1.14.0',
                'scipy==1.0.0',
                'scikit-learn==0.19.1',
                ]

EXTENSIONS = list()
CMD_CLASS = dict()
CMD_OPTIONS = dict()

CYTHON_SOURCES_ROOT = 'python/example_cython/'
SKLEARN_SOURCE_ROOT = 'python/example_cython/sklearn/'
PYTHON_MODULES_ROOT = 'example_cython.'

COMPILER_ARGS = ['-O2',
                 ]

LIBRARIES = []
INCLUDE_DIRS = []

# Cython is a bit picky when it comes to naming extensions, pxd's, and pxy's.
# A pxy (implementation) will pick-up it's corresponding pxd (definition)
# only when the pxd name matches the package name.
#
# To include pxd across packages/modules add __init__.{py, pxd} to the package/
# module directories.
# Also, when rebuilding make sure to remove all generated c/cpp/h and so files
# to avoid linking issues etc.
ext_utils = Extension(PYTHON_MODULES_ROOT + 'utils.anon',
                      sources=[CYTHON_SOURCES_ROOT + 'utils/anon.pyx',
                               CYTHON_SOURCES_ROOT + 'utils/cpp/Anonymiser.cpp',
                               ],
                      include_dirs=[],
                      libraries=['ssl', 'crypto'] + LIBRARIES,
                      extra_compile_args=['-std=c++11'] + COMPILER_ARGS,
                      language='c++',
                      )

ext_sklearn_utils = Extension(PYTHON_MODULES_ROOT + 'sklearn.tree._utils',
                              sources=[SKLEARN_SOURCE_ROOT + 'tree/_utils.pyx',
                                       ],
                              include_dirs=INCLUDE_DIRS,
                              libraries=LIBRARIES,
                              extra_compile_args=COMPILER_ARGS,
                              )

ext_sklearn_criterion = Extension(PYTHON_MODULES_ROOT + 'sklearn.tree._criterion',
                                  sources=[SKLEARN_SOURCE_ROOT + 'tree/_criterion.pyx',
                                           ],
                                  include_dirs=INCLUDE_DIRS,
                                  libraries=LIBRARIES,
                                  extra_compile_args=COMPILER_ARGS,
                                  )

ext_dummy = Extension(PYTHON_MODULES_ROOT + 'sklearn.tree.dummy',
                      sources=[SKLEARN_SOURCE_ROOT + 'tree/dummy.pyx',
                               ],
                      include_dirs=INCLUDE_DIRS,
                      libraries=LIBRARIES,
                      extra_compile_args=COMPILER_ARGS,
                      )

ext_learn = Extension(PYTHON_MODULES_ROOT + 'learn.criterion',
                      sources=[CYTHON_SOURCES_ROOT + 'learn/criterion.pyx',
                               ],
                      include_dirs=INCLUDE_DIRS,
                      libraries=LIBRARIES,
                      extra_compile_args=COMPILER_ARGS,
                      )

EXTENSIONS += [ext_utils, ext_dummy, ext_learn]
CMD_CLASS['build_ext'] = CythonBuild.build_ext
CMD_OPTIONS['build_ext'] = ''


def setup_package():
    setup(name=NAME,
          version=VERSION,
          license='',
          author='Jan Mennis Amoraal',
          description='A Python/Cython example.',
          python_requires='>=3.5',
          package_dir={'': 'python'},
          packages=find_packages(where='python'),
          setup_requires=SETUP_REQUIRES,
          install_requires=REQUIREMENTS,
          ext_modules=EXTENSIONS,
          cmdclass=CMD_CLASS,
          command_options=CMD_OPTIONS,
          )


if __name__ == '__main__':
    setup_package()
