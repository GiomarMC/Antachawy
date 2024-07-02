from setuptools import setup, find_packages

setup(
    name = "antachawy",
    version = "0.0.1",
    packages = find_packages(where="include"),
    package_dir = {"": "include"},

    author = "Giomar Muñoz, Melany Cahuana, Andrea Cuela",
    author_email = "gmunozcu@unsa.edu.pe",
    url = "https://github.com/GiomarMC/Antachawy.git",
    description = "Antachawy compiler package",
    license = "MIT",
    #entry_points = {
     #   "console_scripts": [
      #      "antachawy = src.main:main"
       # ],
    #},
)