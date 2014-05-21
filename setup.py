from setuptools import setup, find_packages

setup(name='ssl_api',
      version='0.2.3',
      description="A certificate-authority API.",
      long_description="",
      classifiers=[],
      keywords='ssl openssl ca certificate authority api',
      author='Dustin Oprea',
      author_email='myselfasunder@gmail.com',
      url='https://github.com/dsoprea/SslApi',
      license='GPL 2',
      packages=find_packages(exclude=['dev']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            'Jinja2==2.7.2',
            'M2Crypto==0.22.3',
            'MarkupSafe==0.21',
            'cffi==0.8.2',
            'cryptography==0.4',
            'pyOpenSSL==0.14',
            'pyasn1==0.1.7',
            'pyasn1-modules==0.0.5',
            'pycparser==2.10',
            'six==1.6.1',
            'web.py==0.37',
      ],
      scripts=[
            'scripts/ca_create_identity',
            'scripts/ca_sign_subordinate',
            'scripts/ca_get_path',
      ]
)
