

from setuptools import setup, find_packages

setup(

    name = "Boids",
    description = "A package to animate a flock of boids",
    version = "0.1.0",
    author = "James Scott",
    author_email = "jas15@ic.ac.uk",
    entry_points = {
        'console_scripts': ['boids = boids.code.command_line:main']
    },
    packages = find_packages(exclude = ['*test']),
    install_requires = ['argparse'],
    license = 'MIT',
    include_package_data = True

)
