# coding: utf-8
# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Product Category - Usage Group",
    "summary": "Restrict Usage of Product Categories to a given Group",
    "version": "8.0.1.0.0",
    "category": "Product",
    "author": "GRAP",
    "license": "AGPL-3",
    "depends": ["product"],
    "data": ["views/view_product_category.xml"],
    "demo": ["demo/res_groups.xml", "demo/product_category.xml"],
    "images": [
        "static/description/product_template_warning.png",
        "static/description/product_category_form.png",
    ],
    "installable": False,
}
