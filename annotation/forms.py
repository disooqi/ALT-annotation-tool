# -*- coding:utf-8 -*-
from django import forms
from django.forms import TextInput
from .models import Token, TokenOccurrence


# class DefaultAnnotationForm(forms.Form):
#     coda = forms.CharField(label='CODA', max_length=15,
#                            widget=forms.TextInput(attrs={'placeholder': 'CODA', 'aria-describedby': 'helpBlock_coda',
#                                                          'class': 'form-control'}))
#     segmentation = forms.CharField(label='Segmentation', max_length=15, widget=forms.TextInput(
#         attrs={'placeholder': 'Segmentation', 'aria-describedby': 'helpBlock_seg',
#                'class': 'form-control'}))
#     pos = forms.CharField(label='POS', max_length=15, widget=forms.TextInput(
#         attrs={'placeholder': 'Part-of-speech', 'aria-describedby': 'helpBlock_pos',
#                'class': 'form-control'}))
#     ambiguity = forms.BooleanField(label=u'ملتبس', initial=False, required=False)
#
#     def process_labels(self):
#         cd = self.cleaned_data
#         print cd

class TokenForm(forms.ModelForm):
    class Meta:
        model = Token
        fields = ['default_coda', 'default_segmentation', 'default_pos', 'ambiguous']
        widgets = {
            'default_pos': TextInput(
                attrs={'autocomplete': 'off', 'spellcheck': 'false', 'id': "suggestionsTB",
                       'class': "typeahead form-control", 'dir': 'rtl'}),
        }


class TokenOccurrenceForm(forms.ModelForm):
    class Meta:
        model = TokenOccurrence
        fields = ['coda', 'segmentation', 'pos']
        widgets = {
            'coda': TextInput(
                attrs={'class': "form-control", 'dir': 'rtl'}),
            'segmentation': TextInput(
                attrs={'class': "form-control", 'dir': 'rtl'}),
            'pos': TextInput(
                attrs={'autocomplete': 'off', 'spellcheck': 'false', 'id': "suggestionsTB",
                       'class': "typeahead form-control", 'dir': 'rtl'}),

        }
