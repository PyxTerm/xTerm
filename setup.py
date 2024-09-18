from setuptools import setup
import os


# Define a function to run after installation to generate _utils.py
def getReadme():
    current = os.path.dirname(os.path.realpath(__file__))
    fPath = os.path.join(current, "README.md")
    with open(fPath, 'r') as fm:
        return fm.read()


setup(
    name='xTerm',
    version="1.0.9",
    description='A Python Package For Font Unicode Conversion',
    author='Mmdrza',
    author_email='Pymmdrza@Gmail.Com',
    packages=['xterm'],
    install_requires=[],
    entry_points={'console_scripts': []},
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
    long_description=getReadme(),
    long_description_content_type='text/markdown',
    url='https://github.com/PyxTerm/xTerm',
    project_urls={
        'Source Code': 'https://github.com/PyxTerm/xTerm',
        'Bug Tracker': 'https://github.com/PyxTerm/xTerm/issues',
    },
    zip_safe=False

)
