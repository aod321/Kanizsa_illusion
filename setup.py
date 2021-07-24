from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
# Get the long description from the README file
long_description = (here/'README.md').read_text(encoding='utf-8')

setup(
    name='kanizsa',
    version='0.0.1',
    keywords='kanizsa, illusion',
    description='A Python library for simply generating Kanizsa illusion graphics (triangles and rectangles).',
    license='MIT License',
    author='Zi Yin',
    author_email='myinzi123@gmail.com',
    package_dir={'': 'src'},  # Optional
    packages=find_packages(where='src'),
    python_requires='>=3.6, <4',
    include_package_data=True,
    platforms='any',
    install_requires=['numpy>=1.12.1', 'matplotlib==3.3.1', 'typeguard==2.12.1'],
)
