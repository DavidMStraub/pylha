from setuptools import setup, find_packages

setup(name='pylha',
      version='0.4',
      author='David M. Straub',
      author_email='david.straub@tum.de',
      url='https://github.com/DavidMStraub/pylha',
      description='A Python package to convert data files in SLHA and similar formats to Python objects, JSON, or YAML.',
      license='MIT',
      packages=['pylha'],
      package_data={
      'pylha':['tests/data/*',
              ]
      },
      install_requires=['pyyaml'],
    )
