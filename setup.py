from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent
with open(HERE / 'requirements.txt') as f:
    requirements = f.read().splitlines()

VERSION = "0.0.1"

setup(
    name = "antachawy",
    version = VERSION,
    packages = find_packages(),
    include_package_data = True,
    author = "Giomar Muñoz, Melany Cahuana, Andrea Cuela",
    author_email = "gmunozcu@unsa.edu.pe",
    url = "https://github.com/GiomarMC/Antachawy.git",
    description = "Antachawy compiler package",
    license = "MIT",
    install_requires = requirements,
    entry_points = {
        'console_scripts': [
            'antachawy = antachawy.main:main',
        ],
    },
)