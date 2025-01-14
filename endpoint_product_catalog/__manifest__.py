# Copyright 2024 Camptocamp SA (<https://camptocamp.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Endpoint Product Catalog",
    "version": "14.0.1.0.0",
    "author": "Camptocamp, Odoo Community Association (OCA)",
    "maintainers": ["SilvioC2C", "simahawk"],
    "website": "https://github.com/OCA/web-api-contrib",
    "summary": "Handle endpoints for product catalogs",
    "depends": ["endpoint", "product_assortment"],
    "data": [
        "views/endpoint_endpoint.xml",
        "views/ir_filters.xml",
    ],
    "license": "AGPL-3",
    "installable": True,
}
