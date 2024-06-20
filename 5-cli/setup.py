from setuptools import setup

setup(
    name="employee_cli",
    version="0.1",
    py_modules=["employee_cli"],
    install_requires=[
        "requests",
    ],
    entry_points="""
        [console_scripts]
        employee=employee_cli:main
    """,
)
