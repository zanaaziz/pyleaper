import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="pyleaper",
	version="1.0.0",
	author="Zana Daniel",
	author_email="contact@zanadaniel.com",
	description="A Python API for accessing your Leap Card balance, overview, and travel credit history.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/zanadaniel/pyleaper",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3.5",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	license='MIT',
	python_requires='>=3.5.2',
)
