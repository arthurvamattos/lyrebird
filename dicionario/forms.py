from django.forms import ModelForm
from .models import Termo


# class SugestaoForm(ModelForm):
#    class Meta:
#        model = Sugestao
#        fields = '__all__'


class TermoForm(ModelForm):
    class Meta:
        model = Termo
        fields = '__all__'
        exclude = ['aprovado']

        labels = {
            'subarea': 'Subárea',
            'img': 'Imagem',
            'expressao': 'Expressão'
        }

    def save(self, commit=True):
        termo = super(TermoForm, self).save(commit=False)
        if commit:
            termo.save()
        return termo
