# -*- coding: utf-8 -*-
{
    'name': "custom_boolean_style",

    'summary': "自定义布尔字段样式模块，提供了美化的、功能增强的布尔字段组件。",

    'description': """
        该模块实现了一个自定义布尔字段组件 `late_boolean`，
        具有动态状态文本和自定义样式，旨在提升 Odoo 表单视图的用户体验。
        用户可以通过简单的配置，在自定义模块中使用该布尔字段。
    """,
    'author': "hongzhe",
    'website': "https://github.com/hongzhe12/custom_boolean_style",

    # Categories can be used to filter modules in modules listing
    'category': 'User Interface',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web'],

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
            'custom_boolean_style/static/src/scss/custom.css',
            'custom_boolean_style/static/src/js/late_order_boolean_field.js',  # 启用自定义 JS 文件
            'custom_boolean_style/static/src/css/late_order_boolean_field.css',
            'custom_boolean_style/static/src/xml/late_order_boolean_field.xml',
        ],
    },
}
