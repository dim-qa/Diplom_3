import string
import random


letters = string.ascii_lowercase
random_mail = ''.join(random.choice(letters) for _ in range(8))
email = f'{random_mail+"@yandex.ru"}'
random_password = ''.join(random.choice(letters) for _ in range(8))
random_name = ''.join(random.choice(letters) for _ in range(8))

ORDER_READY_TEXT = 'Ваш заказ начали готовить'
POP_UP_DETAIL = 'Cостав'
WAIT_TIME = 10
