from odoo import models,fields,api

class LibraryBookLoan(models.Model):
	_name='library.member'
#	_inherit='mail.thread'
	name = fields.Char('Name',required=True)
	email=fields.Char('Email address',required=True)
	loan_ids = fields.One2many('library.book.loan','member_id','Loans',domain=[('state','=','ongoing')])
	nb_late_loans =fields.Integer('Late loans',compute="_get_late_loans_count",)
	expected_return_date =fields.Date('Expected Return Date')

	@api.depends('loan_ids')
	def _get_late_loans_count(self):
		today =fields.Date.context_today(self)
		for rec in self:
			rec.nb_late_loans = self.env['library.book.loan'].search_count([('member_id','=',rec.id),('state','=','ongoing'),('expected_return_date','<',today),])

class LibraryLoanWizard(models.TransientModel):
	_name='library.loan.wizard'
	member_id=fields.Many2one('library.member',string='Member')
	books_ids = fields.Many2many('library.book',string='Books')

	@api.multi
	def record_loans(self):
		loan= self.env['library.book.loan']
		for wizard in self:
			member=wizard.member_id
			books = wizard.books_ids
			for book in books:
				loan.create({'member_id':member.id,'book_id':book.id})