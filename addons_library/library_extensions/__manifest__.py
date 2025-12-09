{
    'name': 'Library Extensions',
    'version': '1.0',
    'summary': 'Pre-assessment exercise for Odev Solutions',
    'description': """
This module extends the Library module with additional features.

Features:

- Add author field to books
- Add book categories
""",
    'category': 'Library',
    'author': 'arroweney',
    'website': 'https://www.guthib.com',
    'depends': ['library'],
    'data': [
        'security/ir.model.access.csv',
        'views/book_category_view.xml',
        'views/library_book_inherit_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3',
}