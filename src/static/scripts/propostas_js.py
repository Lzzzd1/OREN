from browser import document, bind

tags_i = document.select('.ti-arrow-down')


def show_pags(evt):
    evt.currentTarget.parent.select_one('.pagamentos').style.display = None
    evt.currentTarget.class_name = 'ti-arrow-narrow-up'


for i in tags_i:
    i.bind('click', show_pags)
