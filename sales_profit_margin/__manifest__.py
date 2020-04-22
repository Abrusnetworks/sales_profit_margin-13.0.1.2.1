# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details
{
    'name': 'Sales Profit Margin',
    'summary': 'Sales Profit Margin',
    'version': '13.0.1.0.0',
    'category': 'Sales',
    'website': 'https://www.abrusnetworks.com',
    'description': """Sales Profit Margin.""",
    'images': ['static/description/banner.jpg'],
    'author': 'Abrus Networks',
    'company': 'Abrus Networks',
    'maintainer': 'Abrus Networks',
    'installable': True,
    'depends': [
        'base',
        'sale',
        'sale_management',
    ],
    'data': [
        'views/sale_order_views.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}