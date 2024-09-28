from setuptools import setup, find_packages

setup(
    name="zip-cracker",
    version="1.0",
    description="A simple ZIP password cracker",
    py_modules=["zip_cracker"],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'zipcracker=zip_cracker:main',
        ],
    }
)
