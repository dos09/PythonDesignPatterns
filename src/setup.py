from setuptools import setup, find_packages
from design_patterns.version import __version__

if __name__ == '__main__':
    setup(
        name='PythonDesignPatterns',
        version=__version__,
        install_requires=[
            'click>=7.0'
        ],
        entry_points={
            'console_scripts': [
                'dp = design_patterns.main:run_cli'
            ]
        },
        packages=find_packages()
    )
