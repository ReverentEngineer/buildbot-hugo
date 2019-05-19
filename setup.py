from setuptools import setup

setup(
    name = 'buildbot-hugo',
    packages = ['buildbot_hugo'],
    version = '0.1.0',
    description = 'Hugo buildstep for Buildbot',
    author = 'Jeff Hill',
    author_email = 'jeff@reverentengineer.com',
    url = 'https://github.com/ReverentEngineer/buildbot-hugo',
    keywords = ['buildbot', 'hugu', 'ci', 'continuous integration'],
    classifiers = [
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Build Tools',
      'License :: OSI Approved :: Apache Software License',
      'Programming Language :: Python :: 3',
      ],
    entry_points = {
        'buildbot.steps': [
            'Hugo = buildbot_hugo:Hugo'
        ]
    },
    install_requires = ['buildbot'],
)
