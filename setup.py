from distutils.core import setup
setup(
  name = 'django-wham',
  packages = ['wham'],
  version = '0.1',
  description = 'Rest APIs disguised as Django ORM Models',
  author = 'Michael Bylstra',
  author_email = 'mbylstra@gmail.com',
  url = 'https://github.com/mbylstra/django-wham',
  download_url = 'https://github.com/mbylstra/django-wham/tarball/0.1',
  keywords = ['django', 'rest', 'orm'],
  install_requires=[
      'requests',
  ],
  classifiers = [],
)