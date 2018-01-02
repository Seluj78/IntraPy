from distutils.core import setup
setup(
  name='IntraPy',
  packages=['IntraPy'],
  version='0.1.7.1',
  description='A Python Library to use easily the 42 API',
  author='Jules Lasne',
  author_email='jlasne@student.42.fr',
  url='https://github.com/seluj78/IntraPy',
  download_url='https://github.com/seluj78/IntraPy/archive/0.1.7.1.tar.gz',
  keywords=['42', 'API', 'python'],
  install_requires=[
    'json',
    'requests',
    'python-decouple',
  ],
  classifiers=[],
)
