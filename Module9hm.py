contacts = {}
correct_work = False


def error_handler(func):
	def inner_function(*args, **kwargs):
		result = False
		try:
			result = func(*args, **kwargs)
		except IndexError:
			print("Give me name and phone please")
		except ValueError:
			print("Wrong command entered.")
		except KeyError:
			print("This name is not in list.")
		return result

	return inner_function


@error_handler
def adder(name: str, number: str):
	if name in contacts.keys():
		return False
	contacts[name] = number


@error_handler
def changer(name: str, number: str):
	if name not in contacts.keys():
		raise KeyError
	contacts[name] = number


def reader():
	return contacts


@error_handler
def main():
	while True:
		command = input(">>>  ").lower().strip()
		if command == 'hello':
			print('How can I help you?')
			continue
		elif command in ('.', 'goodbye', 'close', 'exit'):
			print('Goodbye!')
			break
		elif command.find('add', 0, 4) != -1:
			adder(command.split(' ')[1].title(), command.split(' ')[2])
		elif command.find('change', 0, 7) != -1:
			changer(command.split(' ')[1].title(), command.split(' ')[2])
		elif command.find('show all', 0, 9) != -1:
			for k, v in reader().items():
				print(k, v)
		else:
			raise ValueError
	return True


if __name__ == '__main__':
	while not correct_work:
		correct_work = main()
