from setuptools import setup, find_packages
setup(
    name="wxPython-common",
    version="3.0.2.0",
    description="Cross platform GUI toolkit for Python",
    author = "Robin Dunn",
    author_email = "Robin Dunn <robin@alldunn.com>",
    license = "wxWidgets Library License (LGPL derivative)",
    packages=find_packages(),
    include_package_data=True,
)
