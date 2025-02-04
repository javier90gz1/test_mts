from odoo.tests.common import TransactionCase


class TestHelpDeskTicket(TransactionCase):

    def setUp(self):
        super(TestHelpDeskTicket, self).setUp()
        # Crea a user to asign
        self.user_demo = self.env.ref('base.user_demo')
        # Create a client example
        self.partner_demo = self.env['res.partner'].create({
            'name': 'Cliente Demo',
        })
        # Create a new ticket example
        self.ticket = self.env['helpdesk.ticket'].create({
            'name': 'Ticket de Prueba',
            'client_id': self.partner_demo.id,
            'description': '<p>Descripción del ticket de prueba.</p>',
            'user_assigned_id': self.user_demo.id,
        })

    def test_action_check_done(self):
        # Check Initial state
        self.assertEqual(self.ticket.state, 'new', "El estado inicial debe ser 'new'.")
        # Call to method change state to 'done'
        self.ticket.action_check_done()

        # check if state change succesfully
        self.assertEqual(self.ticket.state, 'done', "Después de action_check_done, el estado debe ser 'done'.")
    def test_action_check_in_progress(self):
        # Verifica el estado inicial
        self.assertEqual(self.ticket.state, 'new', "El estado inicial debe ser 'new'.")

        # Call to method change state to 'in_progress'
        self.ticket.action_check_in_progress()

        # Check the correct answer
        self.assertEqual(self.ticket.state, 'in_progress', "Después de action_check_in_progress, el estado debe ser 'in_progress'.")
    def test_ticket_flow(self):
        # Initial state
        self.assertEqual(self.ticket.state, 'new', "El estado inicial debe ser 'new'.")

        # Change to 'in_progress'
        self.ticket.action_check_in_progress()
        self.assertEqual(self.ticket.state, 'in_progress', "El estado debe ser 'in_progress'.")

        # Change to 'done'
        self.ticket.action_check_done()
        self.assertEqual(self.ticket.state, 'done', "El estado debe ser 'done'.")
