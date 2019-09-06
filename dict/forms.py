from django import forms

from dict.models import Word


class SearchboxForm(forms.Form):
    searchbox = forms.CharField()


class AddWordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word', 'definition', 'translation', 'example']

    def add_word(self):
        word = self.cleaned_data['word']
        translation = self.cleaned_data['translation']
        definition = self.cleaned_data['definition']
        example = self.cleaned_data['example']
        word = Word.objects.create(
            word=word,
            translation=translation,
            definition=definition,
            example=example
        )
        word.save()
        return word
