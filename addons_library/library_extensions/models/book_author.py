from odoo import models, fields, api

class LibraryBook(models.Model):
    """Inherit library.book to add author and category fields"""
    _inherit = 'library.book'
    
    # Author field (from Task 2)
    author_id = fields.Many2one(
        'res.partner',
        string='Author',
        required=True,
        help='Select the author of this book',
        ondelete='restrict',
    )
    
    # Category field (Task 3)
    category_id = fields.Many2many(
        'library.book.category',  # Connect to our new model
        string='Categories',
        help='Select categories for this book',
    )
    