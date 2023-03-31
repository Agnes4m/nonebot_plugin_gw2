from setuptools import setup, find_packages

setup(
    name='nonebot-plugin-gw2',
    version='0.0.1',
    description='gw2 plugin for NoneBot',
    author='Agnes_Digital',
    author_email='Z735803792@163.com',
    url='https://github.com/Umamusume-Agnes-Digital/nonebot_plugin_gw2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'nonebot2>=2.0.0rc3',
        'nonebot-adapter-onebot>=2.1.5',
        'asyncio>=3.4.3',
        'httpx>=0.23.3'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
