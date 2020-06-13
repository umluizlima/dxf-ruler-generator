from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dxf-ruler-generator",
    version="0.0.4",
    author="Luiz Lima",
    author_email="umluizlima@gmail.com",
    license="MIT License",
    description="Custom sized rulers for digital fabrication.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/umluizlima/dxf-ruler-generator",
    python_requires=">=3.6.0",
    py_modules=['dxf_ruler_generator'],
    install_requires=['ezdxf'],
    entry_points={
        'console_scripts': [
            'dxf-ruler-generator=dxf_ruler_generator:run',
        ],
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
