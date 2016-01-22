from distutils.core import setup, Extension

pyshoco = Extension('pyshoco', sources = ['pyshoco.c', 'shoco.c'], include = ['shoco.h'], include_dirs = ['.'], extra_compile_args = ['-std=c99'])

setup(name = 'pyshoco', version = '1.0', description = 'Shoco Python wrapper module', ext_modules = [pyshoco], author = 'R. Rowe', author_email = 'mega.gamer05@gmail.com', url = 'https://testpypi.python.org/pypi/pyshoco/1.0')