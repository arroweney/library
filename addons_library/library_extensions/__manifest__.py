{
    'name': 'Library Extensions',
    'version': '1.0',
    'summary': 'Extensions for Main Library',
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
        'views/book_author_view.xml',
        'views/book_category_view.xml',
        'views/library_menu.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}