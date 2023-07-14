from browser import document, bind
from browser.html import DIV


@bind('input[type="email"]', 'focus')
def login(_):
    document.select_one('label[for="usuario"]').text = 'Seu nome de usuário ;)'


@bind('input[type="email"]', 'blur')
def login_blur(_):
    document.select_one('label[for="usuario"]').text = 'Usuário'


@bind('input[type="password"]', 'focus')
def login_blur(_):
    document.select_one('label[for="senha"]').text = 'Não conte para ninguém!'


@bind('input[type="password"]', 'blur')
def login_blur(_):
    document.select_one('label[for="senha"]').text = 'Senha'


@bind('input[type="checkbox"]', 'change')
def login_blur(evt):
    if evt.currentTarget.checked:
        document.select_one('div.form-check') <= DIV('Lembraremos ;)', Class='lembrete')
    else:
        try:
            document.select_one('div.lembrete').remove()
        except AttributeError:
            pass

if document.select_one('input[type="checkbox"]').checked:
    document.select_one('div.form-check') <= DIV('Lembraremos ;)', Class='lembrete')