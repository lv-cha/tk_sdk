import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="top-zx",
    version="0.1.1",
    author="lvcha",
    author_email="zhaoxicn@foxmail.com",
    description="Taobao SDK for taobao spreader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lv-cha/tk_sdk",
    packages=setuptools.find_packages(),
    license="Mulan",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)
