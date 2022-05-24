from datetime import datetime
from random import choice

phone_note = {'Jotaro': '380958373914',
              'Polnareff': '380667892344'}
first_start = False
correct_work = False


def input_error(main):
	def inner():
		result = False
		try:
			result = main()
		except IndexError:
			print("Не введено имя или номер телефона.\nПример: \n*команда* *имя* *номер телефона*")
		except KeyError:
			print("Такого имени в сохранённом списке нет.")
		except ValueError:
			print("Неверно введена команда для операции.")

		return result

	return inner


def create_record(name: str, number: str):
	if name in phone_note.keys():
		return False
	phone_note[name] = number
	return True


def read_record(name: str):
	return phone_note[name]


def update_record(name: str, number: str):
	if name not in phone_note.keys():
		return False
	phone_note[name] = number
	return True


def delete_record(name: str):
	if not read_record(name):
		return False
	phone_note.pop(name)
	return True


def read_all_records():
	return phone_note


@input_error
def main() -> bool:
	global first_start
	while 1 + 1 == 2:
		if not first_start:
			current_time = datetime.now()

			if current_time.hour in range(5, 13):
				print("Доброе утро и добро пожаловать в ваш телефонный секретарь.")
			elif current_time.hour in range(12, 19):
				print("Добрый день и добро пожаловать в ваш телефонный секретарь.")
			elif current_time.hour in range(18, 24):
				print("Добрый вечер и добро пожаловать в ваш телефонный секретарь.")
			elif current_time.hour in range(0, 6):
				print("Доброй ночи и добро пожаловать в ваш телефонный секретарь.")
			print("Пожалуйста, введите одну из следующих команд:\n"
			      "'Hello', 'Привет' -- чтобы поздороваться узнать один из нескольких интересных фактов.\n"
			      "'Goodbye', 'Пока' -- чтобы попрощаться и закрыть программу.\n"
			      "'Help' -- чтобы вывести на экран список моих возможностей.")
			first_start = True
		insert_coin = input(">>> ")
		insert_coin = insert_coin.lower().strip()
		if insert_coin in ('привет', 'hello', 'hi'):
			facts_tuple = ('Международный телефонный код Антарктиды - 672',
			               'Среднее облако весит порядка 500 тонн, столько же весят 80 слонов.',
			               'У медуз нет мозгов и кровеносных сосудов.', 'До 17 века термометры заполняли коньяком.',
			               'Лимон содержит больше сахара, чем клубника.',
			               'Самый долгий полёт курицы продолжался 13 секунд.',
			               'На Юпитере регулярно идут алмазные дожди.',
			               'У жирафа и человека одинаковое количество шейных позвонков.',
			               'Изначально, отвертка была изобретена для выковыривания гвоздей, шуруп был изобретен на 100 лет позже.')
			print(f'Что ж, привет ещё раз! А вы знали, например такое: \n{choice(facts_tuple)} ')
			continue
		elif insert_coin in ('.', 'goodbye', 'close', 'exit', 'пока', 'close', 'quit'):
			print("Берегите себя и всего вам наилучшего!")
			first_start = False
			break
		elif insert_coin == 'help':
			print(
				'Вам доступно пять команд:\nНачните строку с "add" и, через пробел, укажите имя и номер телефона, который желаете записать.\n'
				'Начните строку с "change" и, через пробел, укажите имя человека, чей номер вы хотели бы изменить и номер телефона, НА который хотели бы изменить текущий.\n'
				'Начните строку с "phone", и, через пробел, укажите имя человека, чей номер вы хотели бы увидеть.\n'
				'Начните строку с "show all", чтобы вывести все прежде внесённые записи.\n'
				'Начните строку с "delete" и, через пробел, укажите имя человека, чьи контактные данные вы хотели бы удалить.')
		elif insert_coin.find('add', 0, 4) != -1:
			data_for_handle = insert_coin.split(' ')
			create_record(data_for_handle[1].title(), data_for_handle[2])
			print(f"Контакт {data_for_handle[1].title()} с номером {data_for_handle[2]} успешно создан!")
		elif insert_coin.find('change', 0, 7) != -1:
			data_for_handle = insert_coin.split(' ')
			if not update_record(data_for_handle[1].title(), data_for_handle[2]):
				raise KeyError
			print(f'Номер контакта {data_for_handle[1].title()} изменён на {data_for_handle[2]}.')
		elif insert_coin.find('phone', 0, 6) != -1:
			data_for_handle = insert_coin.split(' ')
			print('|{:^14}|'.format(read_record(data_for_handle[1].title())))
		elif insert_coin.find('show all', 0, 9) != -1:
			print('|{:^10}|{:^13}|'.format('Name:', 'Phone №:'))
			for k, v in read_all_records().items():
				print('|{:_<10}|{:_>13}|'.format(k, v))
		elif insert_coin.find('delete', 0, 7) != -1:
			data_for_handle = insert_coin.split(' ')
			delete_record(data_for_handle[1].title())
			print(f"Контакт {data_for_handle[1].title()} был успешно удалён.")
		elif insert_coin in ('', ' '):
			print("К сожалению, я не могу работать с пустой строкой.")
			continue
		else:
			raise ValueError
	return True


# Вывод результата.
if __name__ == '__main__':
	while not correct_work:
		correct_work = main()
