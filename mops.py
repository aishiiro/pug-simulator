import streamlit as lit
import numpy as np
from PIL import Image
import os

class Мопс:

    def __init__(self):
        self.хвост = 'короткий'
        self.ебало = 'приплюснуто'
        self.глаза = 'косят пиздец'

    def __repr__(self):
        return str(f'Типичный, сука, Мопс: хвост - {self.хвост}, ебало - {self.ебало}, глаза {self.глаза}')

    def пук(self):
        return str('Поздравляю, ваш мопс НАПЕРДЕЛ')

    def хрюк(self):
        return str('Хрюкает как свинья!')

    def чих(self):
        return str('Вас обчихали, все ебло в соплях')

мопс = Мопс()

os.getcwd()
lit.title('Симулятор Мопса v0.0.0.1')

image = lit.file_uploader('mps.jpg', type='jpg')

if image is not None:
    img = Image.open(image)
    lit.image(img, caption=f'На фото: {мопс}')

    options = lit.sidebar.radio('Что сделает мопс?',['Пукнет', 'Хрюкнет', 'Чихнет'])

    if options == 'Пукнет':
        lit.markdown(f'{мопс.пук()}:shit:')
    elif options == 'Хрюкнет':
        lit.markdown(f'{мопс.хрюк()}:pig:')
    elif options == 'Чихнет':
        lit.markdown(f'{мопс.чих()}:sneezing_face:')