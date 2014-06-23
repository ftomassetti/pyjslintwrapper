try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A wrapper around JSLint, written in Python',
    'author': 'Federico Tomassetti',
    'url': 'https://github.com/ftomassetti/pyjslintwrapper',
    'author_email': 'Federico Tomassetti',
    'version': '0.1',
    'install_requires': ['nose','pydiffparser'],
    'packages': ['pyjslintwrapper'],
    'scripts': [],
    'name': 'pyjslintwrapper',
    'classifiers': [
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha']
}

setup(**config)