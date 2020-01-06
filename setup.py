import setuptools
from azskpy.constants import __name__, __version__

setuptools.setup(
		name=__name__,
		version=__version__,
		description="Foo Bar",
		author="AzSK Dev Team",
		author_email="mayurk",
		url="https://127.0.0.1",
		packages=setuptools.find_packages(),
		install_requires=[
			"pandas"
		]
)
