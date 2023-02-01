from setuptools import setup

setup(
    name='simple-translate-pipeline',
    version='0.1.0',
    description='Scrapy translation pipeline',
    author='Roman Kasianenko',
    author_email='kasyan.ua@gmail.com',
    url='https://github.com/Roman-Kasianenko/simple-translation-pipeline',
    python_requires=">=3.6",
    packages=[
        'simple_translation_pipeline'
    ],
    install_requires=[
        'translators',
        'cryptography==38.0.4'
    ],
)
