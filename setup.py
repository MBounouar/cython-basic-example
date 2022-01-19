#!/usr/bin/env python

from setuptools import Extension, setup
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import numpy


ext_options = dict(
    compiler_directives=dict(profile=True, language_level="3"),
    annotate=True,
)
ext_modules = [
    Extension(
        name="hello",
        sources=["hello.pyx"],
        # sources=["hello.pyx", "spam.c"],
        # extra_compile_args=["-fopenmp"],
        # extra_link_args=["-fopenmp"],
        language="c",
        define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
        include_dirs=[numpy.get_include()],
    ),
    Extension(
        name="mview",
        sources=["mview.pyx"],
        language="c",
        define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
        include_dirs=[numpy.get_include()],
    ),
]
for ext_module in ext_modules:
    ext_module.cython_directives = dict(language_level="3")


setup(
    # cmdclass=LazyBuildExtCommandClass(),
    cmdclass={"build_ext": build_ext},
    ext_modules=cythonize(
        ext_modules,
        compiler_directives=dict(language_level="3"),
        force=True,
    ),
)
