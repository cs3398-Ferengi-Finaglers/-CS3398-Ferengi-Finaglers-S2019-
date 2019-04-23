#widgets.py

from django.forms.widgets import NumberInput

class RatingInput(NumberInput):
	input_type = 'range'