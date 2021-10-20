from odoo import api, fields, models

class Library(models.Model):
    _name = 'library.info'

    name = fields.Char('Name')
    author = fields.Char('Author')
    book_id = fields.Char('Book Id')
    book_name = fields.Char('Book name')
    book_type = fields.Char('Book type')

    library_ids = fields.One2many(comodel_name='student.info', inverse_name='student1_id', string='Students')
    # issue_date = fields.Date('Issue date')
    # return_date = fields.Date('Return date')
    # student1_id = fields.one2Many(comodel_name='student.info')

    def write(self, vals):
        print('Vals',vals)
        if vals:
            vals.update({'book_type': 'Fun'})
        return super(Library, self).write(vals)

    @api.model
    def create(self, vals):
        print('CREATE CALL', vals)
        print('Create working')
        vals['book_type'] = 'Mystery'
        return super(Library, self).create(vals)