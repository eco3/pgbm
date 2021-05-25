import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
	name="pgbm",
	version="0.1",
	description="Probabilistic Gradient Boosting Machines in Pytorch",
	author="Olivier Sprangers",
	author_email="o.r.sprangers@uva.nl",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elephaint/pgbm",
    packages=setuptools.find_packages(where="src"),
    include_package_data = True,
	package_dir={"": "src"},
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: Apache 2.0",
         "Operating System :: OS Independent"],
    python_requires='>=3.8')