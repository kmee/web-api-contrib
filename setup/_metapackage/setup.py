import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-web-api-contrib",
    description="Meta package for oca-web-api-contrib Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-endpoint_product_catalog',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
