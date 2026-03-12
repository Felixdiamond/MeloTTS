import os 
from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        subprocess.run(["python", "-m", "unidic", "download"], check=False)

cwd = os.path.dirname(os.path.abspath(__file__))

with open('requirements.txt') as f:
    reqs = f.read().splitlines()

setup(
    name='melotts',
    cmdclass={'install': PostInstallCommand},
    version='0.1.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=reqs,
    package_data={
        '': ['*.txt', 'cmudict_*'],
    },
    entry_points={
        "console_scripts": [
            "melotts = melo.main:main",
            "melo = melo.main:main",
            "melo-ui = melo.app:main",
        ],
    },
)
