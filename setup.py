from setuptools import find_packages, setup

with open('requirements.txt') as f:
    required = f.read().splitlines()
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pui_tk',
    version_config={
            "template": "{tag}",
            "dev_template": "{tag}.dev{ccount}+git.{sha}",
            "dirty_template": "{tag}.dev{ccount}+git.{sha}.dirty",
            "starting_version": "0.0.1",
            "version_callback": None,
            "version_file": None,
            "count_commits_from_version_file": False
        },
    setup_requires=['setuptools-git-versioning'],
    packages=find_packages(include=['pui_tk', 'pui_tk.widgets']),
    description='Python UI library based on Tkinter',
    author='A.Honda',
    author_email='andriy.gonda@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/AndriyGonda/pui-tk',
    license='MIT',
    install_requires=required,
    package_data={
        'pui_tk': ['icons/*']
    },
    platforms='any',
    python_requires='>=3.6'
)
