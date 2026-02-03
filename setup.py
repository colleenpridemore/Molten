"""
OpenClaw Identity Framework Setup
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="openclaw-identity",
    version="0.1.0",
    author="Colleen Pridemore",
    author_email="colleenpridemore@users.noreply.github.com",
    description="OpenClaw Identity Mini-Framework for AI agents with Aethel & Vix integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/colleenpridemore/Molten",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.9",
    install_requires=[
        "pyyaml>=6.0.1",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "flake8>=6.1.0",
            "black>=23.7.0",
            "mypy>=1.5.0",
        ],
    },
    include_package_data=True,
    package_data={
        "openclaw_identity": ["*.yaml", "handshakes/*.json"],
    },
)
