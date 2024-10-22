from cProfile import label

from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome',max_length=100)
    email = forms.EmailField(label='Email',max_length=100)
    assunto = forms.CharField(label='Assunto',max_length=100)
    mensagem = forms.CharField(label='Mensagem',max_length=100, widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome:{nome}\n Email:{email}\n Assunto:{assunto}\n Mensagem:{mensagem}'
        mail = EmailMessage(
            subject='Email enviado pelo sistema',
            body=conteudo,
            from_email='Contato@dominio.com.br',
            to=['contato@enviandoEmail',],
            headers={'Replay-To':email}
        )
        mail.send()

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','preco','estoque','imagem']