{
	'name':'My BookStore',
	'summary':"Manage your books",
	'depends':['base','decimal_precision'],
	'data':[
		'security/groups.xml',
		'views/library_book.xml',
		'security/ir.model.access.csv',
		'data/demo.xml',
		'data/res_partner.xml',
		'views/library_loan_wizard.xml',
		'views/list_all_customers.xml',
		],
}
