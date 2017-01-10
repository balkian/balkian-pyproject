import pip
from setuptools import setup
from pip.req import parse_requirements
# parse_requirements() returns generator of pip.req.InstallRequirement objects

try:
    install_reqs = parse_requirements(
        "requirements.txt", session=pip.download.PipSession())
    test_reqs = parse_requirements(
        "test-requirements.txt", session=pip.download.PipSession())
except AttributeError:
    install_reqs = parse_requirements("requirements.txt")
    test_reqs = parse_requirements("test-requirements.txt")

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
install_reqs = [str(ir.req) for ir in install_reqs]
test_reqs = [str(ir.req) for ir in test_reqs]

from {{ cookiecutter.repo_name }} import __version__

setup(
    name='{{cookiecutter.repo_name}}',
    packages=['{{cookiecutter.repo_name}}'],  # this must be the same as the name above
    version=__version__,
    description='''{{cookiecutter.project_short_description}}''',
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    # use the URL to the github repo
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    download_url=('https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}'
                  '/archive/{}.tar.gz'.format(__version__)),
    package_dir={'{{ cookiecutter.repo_name }}': '{{ cookiecutter.repo_name }}'},
    keywords='{{ cookiecutter.repo_name }}',
    install_requires=install_reqs,
    tests_require=test_reqs,
    setup_requires=['pytest-runner', ],
    include_package_data=True,
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License'
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ],
)
