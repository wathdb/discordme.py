from setuptools import setup, find_packages

setup(
    name="discordme",
    version="0.2.7",
    author="wathD",
    author_email="wathd_developement@proton.me",
    description="Une bibliothèque Python open-source permetant d'interagir simplement avec Discord",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/wathdb/discordme.py",
    packages=find_packages(),
    install_requires=[],  # Ajoutez des dépendances ici
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
