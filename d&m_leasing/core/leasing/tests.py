from django.test import TestCase, Client
from . import models
from django.urls import reverse
# tests: views, models


class CardModelTest(TestCase):

    def setUp(self):
        models.Card.objects.create(
            car_name='test',
            card_number='1234567890123456',
            owner_name='jack',
            date='12/12',
            cvv=123
        )

    def test_create_card(self):
        card = models.Card.objects.filter(car_name='test').first()
        self.assertEqual(card.car_name, 'test')
        self.assertEqual(card.card_number, '1234567890123456')
        self.assertEqual(card.owner_name, 'jack')
        self.assertEqual(card.date, '12/12')
        self.assertEqual(card.cvv, 123)

    def tearDown(self):
        models.Card.objects.filter(car_name='test').delete()


class FeedbackModelTest(TestCase):

    def setUp(self):
        models.Feedback.objects.create(
            name='test',
            email='<EMAIL>',
            text='test'
        )

    def test_create_question(self):
        question = models.Feedback.objects.filter(name='test').first()
        self.assertEqual(question.name, 'test')
        self.assertEqual(question.email, '<EMAIL>')
        self.assertEqual(question.text, 'test')

    def tearDown(self):
        models.Feedback.objects.filter(name='test').delete()


class ContactsViewTest(TestCase):

    def test_contacts_get(self):
        client = Client()
        response = client.get(reverse('contacts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/contacts.html')

    def test_contacts_post(self):
        client = Client()
        response = client.post(reverse('contacts'), data={'name': 'test', 'email': '<EMAIL>', 'text': 'test'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contacts'))


class FinanceViewTest(TestCase):

    def test_finance_get(self):
        client = Client()
        response = client.get(reverse('finance'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/finance.html')

    def test_finance_post(self):
        client = Client()
        response = client.post(reverse('finance'), data={'card-car': 'test', 'card-number': '1234567890123456', 'card-name': 'jack', 'card-expiry': '12/12', 'card-cvv': 123})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('finance'))


