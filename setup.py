from setuptools import setup, find_packages


REQUIREMENTS = [
    # 'gpiozero',
    # 'Adafruit_Python_DHT',
    'PyYAML',
    'tornado',
    # 'wgstatus',
]


setup(
    name='RContext',
    version='0.5.0',
    url='https://github.com/IoT-Grupo4/Roteador',
    author='IoT-Grupo4',
    description='Uses the context environment information approach to networks routing analysis',
    license=open('LICENSE').read(),
    packages=find_packages(),
    include_package_data=False,
    entry_points={'console_scripts': [
        'rcontext = main:main',
    ]},
    zip_safe=True,
    # long_description=open('README.md').read(),
    install_requires=REQUIREMENTS,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
