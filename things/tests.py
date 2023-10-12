"""from django.test import TestCase
from things.forms import ThingForm 
from things.models import Thing 
""
class thingFormTestCase(TestCase):
    #Unit tests of the Thing form.

    def setUp(self):
        self.form_input = {
            'name': 'iPhone 15', 
            'description': 'one of the best latest iPhones', 
            'quantity': '1'
        }

    def test_valid_thing_form(self):
        form = ThingForm(data=self.form_input)
        self.assertTrue(form.is_valid())"""""
