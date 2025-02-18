from setuptools import setup, find_packages

setup(
    name="fluorescent-charge",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'opencv-python>=4.5.0',
        'numpy>=1.19.0',
        'pyyaml>=5.4.0',
    ],
    entry_points={
        'console_scripts': [
            'fluorescent-charge=src.main:main',
        ],
    },
    author="zuquanzhi",
    author_email="zuquanzhi@qq.com",
    description="A tool for enhancing fluorescent effects in videos and images",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    # url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)