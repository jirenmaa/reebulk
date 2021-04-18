from setuptools import setup
setup(
    name = 'reebulk',
    version = '0.1.0',
    packages = ['reebulk'],
    entry_points = {
        'console_scripts': [
            'reebulk = reebulk.main:main'
        ],
    },
    install_requires=[
        "Pillow==8.0.0",
        "tqdm==4.43.0"
    ]
)