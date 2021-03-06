from distutils.core import setup

setup(
    name = 'Python X10',
    version = '0.1',
    
    author = 'Guillaume Libersat',
    description = 'A python module to control X10 appliances',
    license = 'GNU GPL',
    
    packages = ['x10', 'x10/controllers', 'x10/devices']
)