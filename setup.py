from setuptools import setup
import os, subprocess


# Define a function to run after installation to generate _utils.py
def post_install() -> None:
    # Check if _utils.py exists or not
    if not os.path.exists('_utils.py'):
        # Execute _gen.py to generate _utils.py
        subprocess.run(['python', '_gen.py'])


setup(
    name='xterm',
    version='1.0.3',
    description='A Python Package For Font Unicode Conversion',
    author='Mmdrza',
    author_email='Pymmdrza@Gmail.Com',
    packages=['xterm'],
    install_requires=[
        # Add dependencies here if you have any
    ],
    entry_points={
        'console_scripts': [
            # Define the post-install script to run
        ],
    },
    python_requires='>=3.7',
    # Add any other keywords for your package here
    keywords=['xterm', 'font', 'unicode', 'conversion'],
    license='MIT License',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/pyxTerm/xTerm',
    classmethods=['install', post_install()],
    project_urls={
        'Source Code': 'https://github.com/pyxTerm/xTerm',
        'Bug Tracker': 'https://github.com/pyxTerm/xTerm/issues',
    },
    zip_safe=False

)
