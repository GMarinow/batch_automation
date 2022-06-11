import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="batch_automation",
    version="0.0.3",
    author="Georgi Marinov",
    author_email="georgi.marinow@gmail.com",
    description="Batch Automation Tools and Packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GMarinow/batch_automation",
    project_urls={
        "Bug Tracker": "https://github.com/GMarinow/batch_automation/issues",
    },
    install_requires=[
        'google-api-python-client',
        'google-auth-httplib2',
        'google-auth-oauthlib',
        'google',
        'pymongo==3.6',
        'dnspython',
        'PyYAML'
    ],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.6',
    ],
    license="Apache Software License 2.0",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)