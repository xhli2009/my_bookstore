{
	'name':'My BookStore',
	'summary':"Manage your books",
	'category':'Library',
	'depends':['base','decimal_precision'],
	'data':[
	#	'security/groups.xml',
		'security/library_security.xml',
		'views/library_book.xml',
		'security/ir.model.access.csv',
		'data/demo.xml',
		'data/res_partner.xml',
		'views/library_loan_wizard.xml',
		'views/list_all_customers.xml',
	#	'security/ir.model.access.csv',
		],
}
