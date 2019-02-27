"""视力普查仪setup脚本"""
from datetime import datetime as dt
from setuptools import setup, find_packages
import visualcensus.const as vcensus_const

PROJECT_NAME = 'Visual Census'
PROJECT_PACKAGE_NAME = 'visualcensus'
PROJECT_LICENSE = 'private'
PROJECT_AUTHOR = 'The Visual Census Authors'
PROJECT_COPYRIGHT = ' 2018-{}, {}'.format(dt.now().year, PROJECT_AUTHOR)
PROJECT_URL = 'https://izhen.tech/'
PROJECT_EMAIL = 'moilk@qq.com'

MIN_PY_VERSION = '.'.join(map(str, vcensus_const.REQUIRED_PYTHON_VER))

PACKAGES = find_packages(exclude=['tests', 'tests.*'])

REQUIRES = [
    'pyqt5==5.11.3',
    'RPi.GPIO>=0.6.3',
    'pip>=8.0.3',
    'loguru==0.2.0'

]

setup(
    name=PROJECT_PACKAGE_NAME,
    version=vcensus_const.__version__,
    url=PROJECT_URL,
    download_url=None,
    project_urls=None,
    author=PROJECT_AUTHOR,
    author_email=PROJECT_EMAIL,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIRES,
    python_requires='>={}'.format(MIN_PY_VERSION),
    test_suite='tests',
    entrt_points={
        'gui_scripts': [
            'vcensus = visualcensus.__main__:main'
        ]
    }
)
