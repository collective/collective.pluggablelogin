from setuptools import setup, find_packages

version = '1.0'

setup(name='collective.pluggablelogin',
      version=version,
      description="Turns the login form into a portlet manager for easier customization",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='David Glick, Groundwire',
      author_email='dglick@gmail.com',
      url='http://github.com/collective/collective.pluggablelogin',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.CMFPlone',
      ],
      extras_require={
        'test': ['plone.app.testing'],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
