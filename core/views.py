from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContatoFormulario, ProdutoModelForm
from django.core.mail.message import EmailMessage

def index(request):
    return render(request, 'index.html')

def contato(request):
    if request.method == 'POST':
        form = ContatoFormulario(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email_cliente = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']
            corpo_email = f"Nome: {nome}\nE-mail: {email_cliente}\nAssunto: {assunto}\nMensagem: {mensagem}"

            email_objeto = EmailMessage(
                subject=assunto,
                body=corpo_email,
                from_email="rodrigoteixeira165@gmail.com",
                to=[email_cliente],
                bcc=["bcc@example.com"],
                reply_to=["rodrigoteixeira165@gmail.com"],
                headers={"Message-ID": "foo"},
            )

            email_objeto.send(fail_silently=False)
            messages.success(request, 'Mensagem enviada')
            return redirect('contato')

    else:
        form = ContatoFormulario()

    return render(request, 'contato.html', {'form': form})

def produto(request):
    return render(request, 'produto.html')

def cadastro(request):
    if request.method == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cadastro')
    else:
        form = ProdutoModelForm()

    return render(request, 'cadastro.html', {'form': form})