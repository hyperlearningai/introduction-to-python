import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="myutils-hyperlearningai",
    version="0.0.1",
    author="Jillur Quddus",
    author_email="contactus@hyperlearning.ai",
    description="Collection of useful tools for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hyperlearningai/introduction-to-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
