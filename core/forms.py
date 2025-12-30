from django import forms
from .models import Produto

class ContatoFormulario(forms.Form):
    nome = forms.CharField(
        label='Nome',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'})
    )
    email = forms.EmailField(
        label='E-mail',
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    assunto = forms.CharField(
        label='Assunto',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    mensagem = forms.CharField(label='Mensagem',
                               widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    )

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'estoque': forms.NumberInput(attrs={'class': 'form-control', 'step': '1', 'min': '0'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control', 'acept': 'image/*'})
        }