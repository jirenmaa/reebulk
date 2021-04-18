from setuptools import setup, find_packages


setup(
    name="reebulk",
    version="0.1.0",
    author="ahmad alwi",
    author_email="ahmadalwiam@gmail.com",
    description="bulk image resizer implemented in python",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["reebulk = reebulk.main:main"],
    },
    keywords=["pytohn", "pillow", "bulk"],
    install_requires=["Pillow==8.0.0", "tqdm==4.43.0"],
)