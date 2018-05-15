from odoo import models,fields,api
class BookCategory(models.Model):
	_name='library.book.category'
	name = fields.Char('Category')
	