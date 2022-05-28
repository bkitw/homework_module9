contacts = {}
correct_work = False


def error_handler(func):
	def inner_function(*args, **kwargs):
		result = False
		try:
			result = func(*args, **kwargs)
		except TypeError:
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


@error_handler
def get_phone(name: str):
	return contacts[name]


@error_handler
def print_phone(name: str):
	what = get_phone(name)
	if what:
		print(what)


def reader():
	result = ''
	for name, number in contacts.items():
		result += name + ': ' + number + '\n'
	return result


def goodbye():
	print("Goodbye!")
	exit()


command_parser = {
	"add": adder,
	"change": changer,
	"show all": lambda: print(reader()),
	"phone": print_phone,
	'hello': lambda: print("how can I help you?"),
	'exit': goodbye,
	'goodbye': goodbye,
	'quit': goodbye,
	'close': goodbye,
	'.': goodbye
}


def parser(command):
	global correct_work
	for key in command_parser.keys():
		if command.startswith(key):
			new_line = command[len(key):].title()
			command_parser[key](*new_line.split())
			correct_work = True
			break


@error_handler
def main():
	global correct_work
	while True:
		command = input(">>>  ").lower().strip()
		parser(command)
		if not correct_work:
			raise ValueError


if __name__ == '__main__':
	while not correct_work:
		correct_work = main()
