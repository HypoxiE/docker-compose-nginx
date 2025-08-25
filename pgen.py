# Код для генерации портов для служб в nginx.conf

import random
import re

with open("nginx.conf") as file:
	busy_ports = {443, 80}
	for line in file.readlines():
		match = re.match(r'^\s*listen\s+(\d+)\s*;', line)
		if match:
			port = int(match.group(1))
			busy_ports = busy_ports | {port}

	available = [x for x in range(5000, 65535 + 1) if x not in busy_ports]
	if available:
		number = random.choice(available)
		print(number)
	else:
		print("Нет доступных портов")
