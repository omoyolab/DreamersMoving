from django.forms import ModelForm
from dreamer.models import Contact, Quote, Review

class ContactFrom(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'



class QuoteFrom(ModelForm):
    class Meta:
        model = Quote
        fields = '__all__'



class ReviewFrom(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'