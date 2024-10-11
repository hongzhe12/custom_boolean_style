# -*- coding: utf-8 -*-
{
    'name': "custom_boolean_style",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_boolean_style/static/src/js/late_order_boolean_field.js',  # 启用自定义 JS 文件
            'custom_boolean_style/static/src/xml/late_order_boolean_field.xml',
            'custom_boolean_style/static/src/css/late_order_boolean_field.css',
            'custom_boolean_style/static/src/scss/custom.css',
        ],
    },
}
