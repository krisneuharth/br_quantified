from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the requirements from the requirements file
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    install_requires = [line.strip() for line in f.readlines()]

setup(
    name="br_quantified",
    version="0.0.1",
    description="",
    url="https://github.com/krisneuharth/br_quantified",
    long_description="",
    author="krisneuharth",
    author_email="kris.neuharth@gmail.com",
    maintainer="kris.neuharth@gmail.com",
    maintainer_email="kris.neuharth@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=install_requires,
    test_suite="nose.collector",
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
    ],
)
