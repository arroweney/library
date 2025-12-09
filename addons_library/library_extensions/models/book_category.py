from odoo import models, fields, api

class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'Book Category'
    _order = 'name'  
    
    name = fields.Char(
        string='Category Name',
        required=True,
        help='Name of the book category (e.g., Fiction, Science, History)'
    )

    description = fields.Text(
        string='Description',
        help='Details about this category'
    )

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Category name must be unique.'),
    ]