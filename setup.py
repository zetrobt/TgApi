from setuptools import setup, find_packages

setup(
    name="TgApi",
    version="1.7",
    description="Experimental library for working with Telegram in Python",
    url="https://github.com/zetrobt/TgApi",
    download_url="https://github.com/zetrobt/TgApi/releases/latest",
    author="zetro.",
    author_email="me@zetro.ga",
    license="MIT",
    python_requires="~=3.7",
    packages=find_packages(),
    zip_safe=False,
    install_requires=["requests"]
)