from setuptools import setup, find_packages

setup(
    name='eva_clip',
    version='0.0.1',
    packages=find_packages(include=['eva_clip*']),
    install_requires=[
        'xformers',
        'apex',
        'timm==0.5.4',
        'tqdm',
        'huggingface_hub',
        'transformers',
        'numpy',
        'einops',
        'ftfy',
        'regex',
    ],
)
