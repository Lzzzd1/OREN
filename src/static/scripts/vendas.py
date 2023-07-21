from browser import ajax, bind, document, console


def to_float(num):
    try:
        numero = float(num)
    except ValueError:
        numero = float(0)
    finally:
        return numero


def ajax_preco(id):
    try:
        ajax.get(f'/api/preco/{id}', oncomplete=calcular, cache=True)
    except Exception as e:
        print(type(e).__name__)


def calcular(req):
    if req.status == 404:
        console.clear()
        document['total'].text = 'Total: R$0,00'
        return True
    ipt_desconto = document['desconto']
    desconto = ipt_desconto.value
    valor = to_float(req.json['preco']) - to_float(desconto)
    document['total'].text = f'Total: R${valor}'


@bind(document['produto'], 'change')
def get_preco(evt):
    ajax_preco(evt.currentTarget.value)


@bind(document['desconto'], 'input')
def get_desconto(evt):
    ajax_preco(document['produto'].value)
