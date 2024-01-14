lst = [6322, 1329, -4670, -8745, 1147, -2928, -4120] # enter your array here
assert len(lst) <= 7, 'array length must be between 0 and 7.'
if len(lst) < 7:
	lst.extend([0] * (7 - len(lst)))
sorted = [0] * 7

if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[5] and lst[0] <= lst[6]:
	sorted[0] = lst[0]

	if lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[5] and lst[1] <= lst[6]:
		sorted[1] = lst[1]

		if lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[5] and lst[2] <= lst[6]:
			sorted[2] = lst[2]

			if lst[3] <= lst[4] and lst[3] <= lst[5] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[4] <= lst[5] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[6] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[6] <= lst[4] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

			elif lst[4] <= lst[3] and lst[4] <= lst[5] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[3] <= lst[5] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[3] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

			elif lst[5] <= lst[3] and lst[5] <= lst[4] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[3] <= lst[4] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[6] <= lst[3] and lst[6] <= lst[4] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[3] <= lst[4] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[5] <= lst[3] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

		elif lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[5] and lst[3] <= lst[6]:
			sorted[2] = lst[3]

			if lst[2] <= lst[4] and lst[2] <= lst[5] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[4] <= lst[5] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[4] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[6] <= lst[4] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

			elif lst[4] <= lst[2] and lst[4] <= lst[5] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[2] <= lst[5] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[2] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

			elif lst[5] <= lst[2] and lst[5] <= lst[4] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[2] <= lst[4] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[6] <= lst[2] and lst[6] <= lst[4] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[2] <= lst[4] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

		elif lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[5] and lst[4] <= lst[6]:
			sorted[2] = lst[4]

			if lst[2] <= lst[3] and lst[2] <= lst[5] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[3] <= lst[5] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[3] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

			elif lst[3] <= lst[2] and lst[3] <= lst[5] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[2] <= lst[5] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[2] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

			elif lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[2] <= lst[3] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[2] <= lst[3] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

		elif lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[4] and lst[5] <= lst[6]:
			sorted[2] = lst[5]

			if lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[3] <= lst[4] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[2] <= lst[4] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[2] <= lst[3] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[2] <= lst[3] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[4] <= lst[2] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

		elif lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[4] and lst[6] <= lst[5]:
			sorted[2] = lst[6]

			if lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[3] <= lst[4] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[5] <= lst[3] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[2] <= lst[4] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[2] <= lst[3] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[2] <= lst[3] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[4] <= lst[2] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

	elif lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[5] and lst[2] <= lst[6]:
		sorted[1] = lst[2]

		if lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[5] and lst[1] <= lst[6]:
			sorted[2] = lst[1]

			if lst[3] <= lst[4] and lst[3] <= lst[5] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[4] <= lst[5] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[4] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[6] <= lst[4] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

			elif lst[4] <= lst[3] and lst[4] <= lst[5] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[3] <= lst[5] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[3] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

			elif lst[5] <= lst[3] and lst[5] <= lst[4] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[3] <= lst[4] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[6] <= lst[3] and lst[6] <= lst[4] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[3] <= lst[4] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[5] <= lst[3] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

		elif lst[3] <= lst[1] and lst[3] <= lst[4] and lst[3] <= lst[5] and lst[3] <= lst[6]:
			sorted[2] = lst[3]

			if lst[1] <= lst[4] and lst[1] <= lst[5] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[4] <= lst[5] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[4] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[6] <= lst[4] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

			elif lst[4] <= lst[1] and lst[4] <= lst[5] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[1] <= lst[5] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[1] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[4] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[1] <= lst[4] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[4] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[1] <= lst[4] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

		elif lst[4] <= lst[1] and lst[4] <= lst[3] and lst[4] <= lst[5] and lst[4] <= lst[6]:
			sorted[2] = lst[4]

			if lst[1] <= lst[3] and lst[1] <= lst[5] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[3] <= lst[5] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[3] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

			elif lst[3] <= lst[1] and lst[3] <= lst[5] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[1] <= lst[5] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[1] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[3] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[1] <= lst[3] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[3] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[1] <= lst[3] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

		elif lst[5] <= lst[1] and lst[5] <= lst[3] and lst[5] <= lst[4] and lst[5] <= lst[6]:
			sorted[2] = lst[5]

			if lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[3] <= lst[4] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[1] and lst[3] <= lst[4] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[1] <= lst[4] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[3] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[1] <= lst[3] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[3] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[1] <= lst[3] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

		elif lst[6] <= lst[1] and lst[6] <= lst[3] and lst[6] <= lst[4] and lst[6] <= lst[5]:
			sorted[2] = lst[6]

			if lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[3] <= lst[4] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[5] <= lst[3] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[1] and lst[3] <= lst[4] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[1] <= lst[4] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[3] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[1] <= lst[3] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[3] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[1] <= lst[3] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

	elif lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[5] and lst[3] <= lst[6]:
		sorted[1] = lst[3]

		if lst[1] <= lst[2] and lst[1] <= lst[4] and lst[1] <= lst[5] and lst[1] <= lst[6]:
			sorted[2] = lst[1]

			if lst[2] <= lst[4] and lst[2] <= lst[5] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[4] <= lst[5] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[4] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[6] <= lst[4] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

			elif lst[4] <= lst[2] and lst[4] <= lst[5] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[2] <= lst[5] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[2] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

			elif lst[5] <= lst[2] and lst[5] <= lst[4] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[2] <= lst[4] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[6] <= lst[2] and lst[6] <= lst[4] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[2] <= lst[4] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

		elif lst[2] <= lst[1] and lst[2] <= lst[4] and lst[2] <= lst[5] and lst[2] <= lst[6]:
			sorted[2] = lst[2]

			if lst[1] <= lst[4] and lst[1] <= lst[5] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[4] <= lst[5] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[4] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[6] <= lst[4] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

			elif lst[4] <= lst[1] and lst[4] <= lst[5] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[1] <= lst[5] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[1] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[4] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[1] <= lst[4] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[4] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[1] <= lst[4] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

		elif lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[5] and lst[4] <= lst[6]:
			sorted[2] = lst[4]

			if lst[1] <= lst[2] and lst[1] <= lst[5] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[2] <= lst[5] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[2] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[5] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[1] <= lst[5] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[1] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[1] <= lst[2] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[1] <= lst[2] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[4] and lst[5] <= lst[6]:
			sorted[2] = lst[5]

			if lst[1] <= lst[2] and lst[1] <= lst[4] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[2] <= lst[4] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[4] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[1] <= lst[4] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[1] <= lst[2] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[1] <= lst[2] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[4] and lst[6] <= lst[5]:
			sorted[2] = lst[6]

			if lst[1] <= lst[2] and lst[1] <= lst[4] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[2] <= lst[4] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[4] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[1] <= lst[4] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[1] <= lst[2] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[1] <= lst[2] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

	elif lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[5] and lst[4] <= lst[6]:
		sorted[1] = lst[4]

		if lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[5] and lst[1] <= lst[6]:
			sorted[2] = lst[1]

			if lst[2] <= lst[3] and lst[2] <= lst[5] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[3] <= lst[5] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[3] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

			elif lst[3] <= lst[2] and lst[3] <= lst[5] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[2] <= lst[5] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[2] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

			elif lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[2] <= lst[3] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[2] <= lst[3] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

		elif lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[5] and lst[2] <= lst[6]:
			sorted[2] = lst[2]

			if lst[1] <= lst[3] and lst[1] <= lst[5] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[3] <= lst[5] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[3] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

			elif lst[3] <= lst[1] and lst[3] <= lst[5] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[1] <= lst[5] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[1] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[3] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[1] <= lst[3] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[3] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[1] <= lst[3] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

		elif lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[5] and lst[3] <= lst[6]:
			sorted[2] = lst[3]

			if lst[1] <= lst[2] and lst[1] <= lst[5] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[2] <= lst[5] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[2] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[5] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[1] <= lst[5] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[1] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[1] <= lst[2] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[1] <= lst[2] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[6]:
			sorted[2] = lst[5]

			if lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[2] <= lst[3] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[1] <= lst[3] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[1] <= lst[2] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[3]:
				sorted[3] = lst[6]

				if lst[1] <= lst[2] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[3] <= lst[1] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[5]:
			sorted[2] = lst[6]

			if lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[2] <= lst[3] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[1] <= lst[3] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[1] <= lst[2] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[3]:
				sorted[3] = lst[5]

				if lst[1] <= lst[2] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[3] <= lst[1] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

	elif lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[4] and lst[5] <= lst[6]:
		sorted[1] = lst[5]

		if lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[6]:
			sorted[2] = lst[1]

			if lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[3] <= lst[4] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[2] <= lst[4] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[2] <= lst[3] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[2] <= lst[3] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[4] <= lst[2] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

		elif lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[6]:
			sorted[2] = lst[2]

			if lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[3] <= lst[4] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[1] and lst[3] <= lst[4] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[1] <= lst[4] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[3] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[1] <= lst[3] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[3] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[1] <= lst[3] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

		elif lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[6]:
			sorted[2] = lst[3]

			if lst[1] <= lst[2] and lst[1] <= lst[4] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[2] <= lst[4] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[4] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[1] <= lst[4] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[1] <= lst[2] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[1] <= lst[2] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[6]:
			sorted[2] = lst[4]

			if lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[2] <= lst[3] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[1] <= lst[3] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[1] <= lst[2] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[3]:
				sorted[3] = lst[6]

				if lst[1] <= lst[2] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[3] <= lst[1] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[4]:
			sorted[2] = lst[6]

			if lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[4]:
				sorted[3] = lst[1]

				if lst[2] <= lst[3] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[4] <= lst[2] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[4]:
				sorted[3] = lst[2]

				if lst[1] <= lst[3] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[4]:
				sorted[3] = lst[3]

				if lst[1] <= lst[2] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[3]:
				sorted[3] = lst[4]

				if lst[1] <= lst[2] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[3] <= lst[1] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

	elif lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[4] and lst[6] <= lst[5]:
		sorted[1] = lst[6]

		if lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[5]:
			sorted[2] = lst[1]

			if lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[3] <= lst[4] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[5] <= lst[3] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[2] <= lst[4] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[2] <= lst[3] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[2] <= lst[3] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[4] <= lst[2] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

		elif lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[5]:
			sorted[2] = lst[2]

			if lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[3] <= lst[4] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[5] <= lst[3] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[1] and lst[3] <= lst[4] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[1] <= lst[4] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[3] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[1] <= lst[3] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[3] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[1] <= lst[3] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

		elif lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[5]:
			sorted[2] = lst[3]

			if lst[1] <= lst[2] and lst[1] <= lst[4] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[2] <= lst[4] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[4] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[1] <= lst[4] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[1] <= lst[2] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[1] <= lst[2] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[5]:
			sorted[2] = lst[4]

			if lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[2] <= lst[3] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[1] <= lst[3] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[1] <= lst[2] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[3]:
				sorted[3] = lst[5]

				if lst[1] <= lst[2] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[3] <= lst[1] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[4]:
			sorted[2] = lst[5]

			if lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[4]:
				sorted[3] = lst[1]

				if lst[2] <= lst[3] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[4] <= lst[2] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[4]:
				sorted[3] = lst[2]

				if lst[1] <= lst[3] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[4]:
				sorted[3] = lst[3]

				if lst[1] <= lst[2] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[3]:
				sorted[3] = lst[4]

				if lst[1] <= lst[2] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[3] <= lst[1] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[5] and lst[1] <= lst[6]:
	sorted[0] = lst[1]

	if lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[5] and lst[0] <= lst[6]:
		sorted[1] = lst[0]

		if lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[5] and lst[2] <= lst[6]:
			sorted[2] = lst[2]

			if lst[3] <= lst[4] and lst[3] <= lst[5] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[4] <= lst[5] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[4] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[6] <= lst[4] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

			elif lst[4] <= lst[3] and lst[4] <= lst[5] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[3] <= lst[5] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[6] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[5] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

			elif lst[5] <= lst[3] and lst[5] <= lst[4] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[3] <= lst[4] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[6] <= lst[3] and lst[6] <= lst[4] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[3] <= lst[4] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[5] <= lst[3] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

		elif lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[5] and lst[3] <= lst[6]:
			sorted[2] = lst[3]

			if lst[2] <= lst[4] and lst[2] <= lst[5] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[4] <= lst[5] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[4] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[6] <= lst[4] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

			elif lst[4] <= lst[2] and lst[4] <= lst[5] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[2] <= lst[5] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[2] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

			elif lst[5] <= lst[2] and lst[5] <= lst[4] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[2] <= lst[4] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[6] <= lst[2] and lst[6] <= lst[4] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[2] <= lst[4] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

		elif lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[5] and lst[4] <= lst[6]:
			sorted[2] = lst[4]

			if lst[2] <= lst[3] and lst[2] <= lst[5] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[3] <= lst[5] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[3] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

			elif lst[3] <= lst[2] and lst[3] <= lst[5] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[2] <= lst[5] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[2] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

			elif lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[2] <= lst[3] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[2] <= lst[3] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

		elif lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[4] and lst[5] <= lst[6]:
			sorted[2] = lst[5]

			if lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[3] <= lst[4] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[2] <= lst[4] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[2] <= lst[3] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[2] <= lst[3] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[4] <= lst[2] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

		elif lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[4] and lst[6] <= lst[5]:
			sorted[2] = lst[6]

			if lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[3] <= lst[4] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[5] <= lst[3] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[2] <= lst[4] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[2] <= lst[3] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[2] <= lst[3] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[4] <= lst[2] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

	elif lst[2] <= lst[0] and lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[5] and lst[2] <= lst[6]:
		sorted[1] = lst[2]

		if lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[5] and lst[0] <= lst[6]:
			sorted[2] = lst[0]

			if lst[3] <= lst[4] and lst[3] <= lst[5] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[4] <= lst[5] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[4] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[6] <= lst[4] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

			elif lst[4] <= lst[3] and lst[4] <= lst[5] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[3] <= lst[5] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[3] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

			elif lst[5] <= lst[3] and lst[5] <= lst[4] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[3] <= lst[4] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[6] <= lst[3] and lst[6] <= lst[4] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[3] <= lst[4] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[5] <= lst[3] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

		elif lst[3] <= lst[0] and lst[3] <= lst[4] and lst[3] <= lst[5] and lst[3] <= lst[6]:
			sorted[2] = lst[3]

			if lst[0] <= lst[4] and lst[0] <= lst[5] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[4] <= lst[5] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[4] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[6] <= lst[4] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

			elif lst[4] <= lst[0] and lst[4] <= lst[5] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[0] <= lst[5] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[0] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[4] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[0] <= lst[4] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[4] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[0] <= lst[4] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

		elif lst[4] <= lst[0] and lst[4] <= lst[3] and lst[4] <= lst[5] and lst[4] <= lst[6]:
			sorted[2] = lst[4]

			if lst[0] <= lst[3] and lst[0] <= lst[5] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[3] <= lst[5] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[3] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

			elif lst[3] <= lst[0] and lst[3] <= lst[5] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[0] <= lst[5] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[0] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[3] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[0] <= lst[3] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[3] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[0] <= lst[3] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

		elif lst[5] <= lst[0] and lst[5] <= lst[3] and lst[5] <= lst[4] and lst[5] <= lst[6]:
			sorted[2] = lst[5]

			if lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[3] <= lst[4] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[0] and lst[3] <= lst[4] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[0] <= lst[4] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[3] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[0] <= lst[3] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[3] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[0] <= lst[3] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

		elif lst[6] <= lst[0] and lst[6] <= lst[3] and lst[6] <= lst[4] and lst[6] <= lst[5]:
			sorted[2] = lst[6]

			if lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[3] <= lst[4] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[5] <= lst[3] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[0] and lst[3] <= lst[4] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[0] <= lst[4] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[3] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[0] <= lst[3] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[3] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[0] <= lst[3] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

	elif lst[3] <= lst[0] and lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[5] and lst[3] <= lst[6]:
		sorted[1] = lst[3]

		if lst[0] <= lst[2] and lst[0] <= lst[4] and lst[0] <= lst[5] and lst[0] <= lst[6]:
			sorted[2] = lst[0]

			if lst[2] <= lst[4] and lst[2] <= lst[5] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[4] <= lst[5] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[4] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[6] <= lst[4] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

			elif lst[4] <= lst[2] and lst[4] <= lst[5] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[2] <= lst[5] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[2] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

			elif lst[5] <= lst[2] and lst[5] <= lst[4] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[2] <= lst[4] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[6] <= lst[2] and lst[6] <= lst[4] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[2] <= lst[4] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

		elif lst[2] <= lst[0] and lst[2] <= lst[4] and lst[2] <= lst[5] and lst[2] <= lst[6]:
			sorted[2] = lst[2]

			if lst[0] <= lst[4] and lst[0] <= lst[5] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[4] <= lst[5] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[4] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[6] <= lst[4] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

			elif lst[4] <= lst[0] and lst[4] <= lst[5] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[0] <= lst[5] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[0] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[4] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[0] <= lst[4] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[4] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[0] <= lst[4] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

		elif lst[4] <= lst[0] and lst[4] <= lst[2] and lst[4] <= lst[5] and lst[4] <= lst[6]:
			sorted[2] = lst[4]

			if lst[0] <= lst[2] and lst[0] <= lst[5] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[2] <= lst[5] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[2] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[5] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[0] <= lst[5] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[0] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[2] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[0] <= lst[2] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[2] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[0] <= lst[2] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[5] <= lst[0] and lst[5] <= lst[2] and lst[5] <= lst[4] and lst[5] <= lst[6]:
			sorted[2] = lst[5]

			if lst[0] <= lst[2] and lst[0] <= lst[4] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[2] <= lst[4] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[4] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[0] <= lst[4] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[2] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[0] <= lst[2] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[2] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[0] <= lst[2] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[6] <= lst[0] and lst[6] <= lst[2] and lst[6] <= lst[4] and lst[6] <= lst[5]:
			sorted[2] = lst[6]

			if lst[0] <= lst[2] and lst[0] <= lst[4] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[2] <= lst[4] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[4] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[0] <= lst[4] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[2] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[0] <= lst[2] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[2] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[0] <= lst[2] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

	elif lst[4] <= lst[0] and lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[5] and lst[4] <= lst[6]:
		sorted[1] = lst[4]

		if lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[5] and lst[0] <= lst[6]:
			sorted[2] = lst[0]

			if lst[2] <= lst[3] and lst[2] <= lst[5] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[3] <= lst[5] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[3] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

			elif lst[3] <= lst[2] and lst[3] <= lst[5] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[2] <= lst[5] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[2] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

			elif lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[2] <= lst[3] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[2] <= lst[3] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

		elif lst[2] <= lst[0] and lst[2] <= lst[3] and lst[2] <= lst[5] and lst[2] <= lst[6]:
			sorted[2] = lst[2]

			if lst[0] <= lst[3] and lst[0] <= lst[5] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[3] <= lst[5] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[3] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

			elif lst[3] <= lst[0] and lst[3] <= lst[5] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[0] <= lst[5] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[0] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[3] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[0] <= lst[3] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[3] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[0] <= lst[3] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

		elif lst[3] <= lst[0] and lst[3] <= lst[2] and lst[3] <= lst[5] and lst[3] <= lst[6]:
			sorted[2] = lst[3]

			if lst[0] <= lst[2] and lst[0] <= lst[5] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[2] <= lst[5] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[2] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[5] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[0] <= lst[5] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[0] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[2] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[0] <= lst[2] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[2] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[0] <= lst[2] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[5] <= lst[0] and lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[6]:
			sorted[2] = lst[5]

			if lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[2] <= lst[3] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[3] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[0] <= lst[3] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[2] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[0] <= lst[2] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[2] and lst[6] <= lst[3]:
				sorted[3] = lst[6]

				if lst[0] <= lst[2] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[6] <= lst[0] and lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[5]:
			sorted[2] = lst[6]

			if lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[2] <= lst[3] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[3] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[0] <= lst[3] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[2] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[0] <= lst[2] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[2] and lst[5] <= lst[3]:
				sorted[3] = lst[5]

				if lst[0] <= lst[2] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

	elif lst[5] <= lst[0] and lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[4] and lst[5] <= lst[6]:
		sorted[1] = lst[5]

		if lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[6]:
			sorted[2] = lst[0]

			if lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[3] <= lst[4] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[2] <= lst[4] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[2] <= lst[3] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[2] <= lst[3] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[4] <= lst[2] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

		elif lst[2] <= lst[0] and lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[6]:
			sorted[2] = lst[2]

			if lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[3] <= lst[4] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[0] and lst[3] <= lst[4] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[0] <= lst[4] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[3] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[0] <= lst[3] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[3] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[0] <= lst[3] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

		elif lst[3] <= lst[0] and lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[6]:
			sorted[2] = lst[3]

			if lst[0] <= lst[2] and lst[0] <= lst[4] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[2] <= lst[4] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[4] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[0] <= lst[4] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[2] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[0] <= lst[2] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[2] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[0] <= lst[2] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[4] <= lst[0] and lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[6]:
			sorted[2] = lst[4]

			if lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[2] <= lst[3] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[3] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[0] <= lst[3] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[2] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[0] <= lst[2] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[2] and lst[6] <= lst[3]:
				sorted[3] = lst[6]

				if lst[0] <= lst[2] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[6] <= lst[0] and lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[4]:
			sorted[2] = lst[6]

			if lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[4]:
				sorted[3] = lst[0]

				if lst[2] <= lst[3] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[4] <= lst[2] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[3] and lst[2] <= lst[4]:
				sorted[3] = lst[2]

				if lst[0] <= lst[3] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[2] and lst[3] <= lst[4]:
				sorted[3] = lst[3]

				if lst[0] <= lst[2] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[2] and lst[4] <= lst[3]:
				sorted[3] = lst[4]

				if lst[0] <= lst[2] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

	elif lst[6] <= lst[0] and lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[4] and lst[6] <= lst[5]:
		sorted[1] = lst[6]

		if lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[5]:
			sorted[2] = lst[0]

			if lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[3] <= lst[4] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[5] <= lst[3] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[2] <= lst[4] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[2] <= lst[3] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[2] <= lst[3] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[4] <= lst[2] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

		elif lst[2] <= lst[0] and lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[5]:
			sorted[2] = lst[2]

			if lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[3] <= lst[4] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[5] <= lst[3] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[0] and lst[3] <= lst[4] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[0] <= lst[4] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[3] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[0] <= lst[3] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[3] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[0] <= lst[3] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

		elif lst[3] <= lst[0] and lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[5]:
			sorted[2] = lst[3]

			if lst[0] <= lst[2] and lst[0] <= lst[4] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[2] <= lst[4] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[4] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[0] <= lst[4] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[2] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[0] <= lst[2] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[2] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[0] <= lst[2] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[4] <= lst[0] and lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[5]:
			sorted[2] = lst[4]

			if lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[2] <= lst[3] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[3] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[0] <= lst[3] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[2] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[0] <= lst[2] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[2] and lst[5] <= lst[3]:
				sorted[3] = lst[5]

				if lst[0] <= lst[2] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[5] <= lst[0] and lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[4]:
			sorted[2] = lst[5]

			if lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[4]:
				sorted[3] = lst[0]

				if lst[2] <= lst[3] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[4] <= lst[2] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[3] and lst[2] <= lst[4]:
				sorted[3] = lst[2]

				if lst[0] <= lst[3] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[2] and lst[3] <= lst[4]:
				sorted[3] = lst[3]

				if lst[0] <= lst[2] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[2] and lst[4] <= lst[3]:
				sorted[3] = lst[4]

				if lst[0] <= lst[2] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[5] and lst[2] <= lst[6]:
	sorted[0] = lst[2]

	if lst[0] <= lst[1] and lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[5] and lst[0] <= lst[6]:
		sorted[1] = lst[0]

		if lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[5] and lst[1] <= lst[6]:
			sorted[2] = lst[1]

			if lst[3] <= lst[4] and lst[3] <= lst[5] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[4] <= lst[5] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[4] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[6] <= lst[4] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

			elif lst[4] <= lst[3] and lst[4] <= lst[5] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[3] <= lst[5] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[6] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[5] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

			elif lst[5] <= lst[3] and lst[5] <= lst[4] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[3] <= lst[4] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[6] <= lst[3] and lst[6] <= lst[4] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[3] <= lst[4] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[5] <= lst[3] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

		elif lst[3] <= lst[1] and lst[3] <= lst[4] and lst[3] <= lst[5] and lst[3] <= lst[6]:
			sorted[2] = lst[3]

			if lst[1] <= lst[4] and lst[1] <= lst[5] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[4] <= lst[5] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[4] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[6] <= lst[4] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

			elif lst[4] <= lst[1] and lst[4] <= lst[5] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[1] <= lst[5] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[1] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[4] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[1] <= lst[4] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[4] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[1] <= lst[4] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

		elif lst[4] <= lst[1] and lst[4] <= lst[3] and lst[4] <= lst[5] and lst[4] <= lst[6]:
			sorted[2] = lst[4]

			if lst[1] <= lst[3] and lst[1] <= lst[5] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[3] <= lst[5] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[3] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

			elif lst[3] <= lst[1] and lst[3] <= lst[5] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[1] <= lst[5] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[1] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[3] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[1] <= lst[3] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[3] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[1] <= lst[3] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

		elif lst[5] <= lst[1] and lst[5] <= lst[3] and lst[5] <= lst[4] and lst[5] <= lst[6]:
			sorted[2] = lst[5]

			if lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[3] <= lst[4] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[1] and lst[3] <= lst[4] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[1] <= lst[4] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[3] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[1] <= lst[3] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[3] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[1] <= lst[3] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

		elif lst[6] <= lst[1] and lst[6] <= lst[3] and lst[6] <= lst[4] and lst[6] <= lst[5]:
			sorted[2] = lst[6]

			if lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[3] <= lst[4] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[5] <= lst[3] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[1] and lst[3] <= lst[4] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[1] <= lst[4] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[3] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[1] <= lst[3] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[3] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[1] <= lst[3] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

	elif lst[1] <= lst[0] and lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[5] and lst[1] <= lst[6]:
		sorted[1] = lst[1]

		if lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[5] and lst[0] <= lst[6]:
			sorted[2] = lst[0]

			if lst[3] <= lst[4] and lst[3] <= lst[5] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[4] <= lst[5] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[4] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[6] <= lst[4] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

			elif lst[4] <= lst[3] and lst[4] <= lst[5] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[3] <= lst[5] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[3] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

			elif lst[5] <= lst[3] and lst[5] <= lst[4] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[3] <= lst[4] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[6] <= lst[3] and lst[6] <= lst[4] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[3] <= lst[4] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[5] <= lst[3] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

		elif lst[3] <= lst[0] and lst[3] <= lst[4] and lst[3] <= lst[5] and lst[3] <= lst[6]:
			sorted[2] = lst[3]

			if lst[0] <= lst[4] and lst[0] <= lst[5] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[4] <= lst[5] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[4] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[6] <= lst[4] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

			elif lst[4] <= lst[0] and lst[4] <= lst[5] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[0] <= lst[5] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[0] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[4] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[0] <= lst[4] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[4] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[0] <= lst[4] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

		elif lst[4] <= lst[0] and lst[4] <= lst[3] and lst[4] <= lst[5] and lst[4] <= lst[6]:
			sorted[2] = lst[4]

			if lst[0] <= lst[3] and lst[0] <= lst[5] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[3] <= lst[5] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[3] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

			elif lst[3] <= lst[0] and lst[3] <= lst[5] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[0] <= lst[5] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[0] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[3] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[0] <= lst[3] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[3] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[0] <= lst[3] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

		elif lst[5] <= lst[0] and lst[5] <= lst[3] and lst[5] <= lst[4] and lst[5] <= lst[6]:
			sorted[2] = lst[5]

			if lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[3] <= lst[4] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[0] and lst[3] <= lst[4] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[0] <= lst[4] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[3] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[0] <= lst[3] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[3] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[0] <= lst[3] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

		elif lst[6] <= lst[0] and lst[6] <= lst[3] and lst[6] <= lst[4] and lst[6] <= lst[5]:
			sorted[2] = lst[6]

			if lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[3] <= lst[4] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[5] <= lst[3] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[0] and lst[3] <= lst[4] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[0] <= lst[4] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[3] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[0] <= lst[3] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[3] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[0] <= lst[3] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

	elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[4] and lst[3] <= lst[5] and lst[3] <= lst[6]:
		sorted[1] = lst[3]

		if lst[0] <= lst[1] and lst[0] <= lst[4] and lst[0] <= lst[5] and lst[0] <= lst[6]:
			sorted[2] = lst[0]

			if lst[1] <= lst[4] and lst[1] <= lst[5] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[4] <= lst[5] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[4] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[6] <= lst[4] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

			elif lst[4] <= lst[1] and lst[4] <= lst[5] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[1] <= lst[5] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[1] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[4] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[1] <= lst[4] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[4] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[1] <= lst[4] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

		elif lst[1] <= lst[0] and lst[1] <= lst[4] and lst[1] <= lst[5] and lst[1] <= lst[6]:
			sorted[2] = lst[1]

			if lst[0] <= lst[4] and lst[0] <= lst[5] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[4] <= lst[5] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[4] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[6] <= lst[4] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

			elif lst[4] <= lst[0] and lst[4] <= lst[5] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[0] <= lst[5] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[0] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[4] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[0] <= lst[4] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[4] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[0] <= lst[4] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

		elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[5] and lst[4] <= lst[6]:
			sorted[2] = lst[4]

			if lst[0] <= lst[1] and lst[0] <= lst[5] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[1] <= lst[5] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[1] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[5] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[0] <= lst[5] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[0] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[0] <= lst[1] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[1]:
					sorted[4] = lst[6]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[0] <= lst[1] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[1]:
					sorted[4] = lst[5]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[4] and lst[5] <= lst[6]:
			sorted[2] = lst[5]

			if lst[0] <= lst[1] and lst[0] <= lst[4] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[1] <= lst[4] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[4] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[0] <= lst[4] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[0] <= lst[1] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[1]:
					sorted[4] = lst[6]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[0] <= lst[1] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[1]:
					sorted[4] = lst[4]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[4] and lst[6] <= lst[5]:
			sorted[2] = lst[6]

			if lst[0] <= lst[1] and lst[0] <= lst[4] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[1] <= lst[4] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[4] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[0] <= lst[4] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[0] <= lst[1] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[1]:
					sorted[4] = lst[5]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[0] <= lst[1] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[1]:
					sorted[4] = lst[4]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

	elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[3] and lst[4] <= lst[5] and lst[4] <= lst[6]:
		sorted[1] = lst[4]

		if lst[0] <= lst[1] and lst[0] <= lst[3] and lst[0] <= lst[5] and lst[0] <= lst[6]:
			sorted[2] = lst[0]

			if lst[1] <= lst[3] and lst[1] <= lst[5] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[3] <= lst[5] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[3] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

			elif lst[3] <= lst[1] and lst[3] <= lst[5] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[1] <= lst[5] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[1] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[3] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[1] <= lst[3] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[3] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[1] <= lst[3] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

		elif lst[1] <= lst[0] and lst[1] <= lst[3] and lst[1] <= lst[5] and lst[1] <= lst[6]:
			sorted[2] = lst[1]

			if lst[0] <= lst[3] and lst[0] <= lst[5] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[3] <= lst[5] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[3] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

			elif lst[3] <= lst[0] and lst[3] <= lst[5] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[0] <= lst[5] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[0] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[3] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[0] <= lst[3] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[3] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[0] <= lst[3] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

		elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[5] and lst[3] <= lst[6]:
			sorted[2] = lst[3]

			if lst[0] <= lst[1] and lst[0] <= lst[5] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[1] <= lst[5] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[1] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[5] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[0] <= lst[5] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[0] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[0] <= lst[1] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[1]:
					sorted[4] = lst[6]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[0] <= lst[1] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[1]:
					sorted[4] = lst[5]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[3] and lst[5] <= lst[6]:
			sorted[2] = lst[5]

			if lst[0] <= lst[1] and lst[0] <= lst[3] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[1] <= lst[3] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[3] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[0] <= lst[3] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[0] <= lst[1] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[1]:
					sorted[4] = lst[6]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[3]:
				sorted[3] = lst[6]

				if lst[0] <= lst[1] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[1]:
					sorted[4] = lst[3]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[3] and lst[6] <= lst[5]:
			sorted[2] = lst[6]

			if lst[0] <= lst[1] and lst[0] <= lst[3] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[1] <= lst[3] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[3] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[0] <= lst[3] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[0] <= lst[1] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[1]:
					sorted[4] = lst[5]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[3]:
				sorted[3] = lst[5]

				if lst[0] <= lst[1] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[1]:
					sorted[4] = lst[3]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

	elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[3] and lst[5] <= lst[4] and lst[5] <= lst[6]:
		sorted[1] = lst[5]

		if lst[0] <= lst[1] and lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[6]:
			sorted[2] = lst[0]

			if lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[3] <= lst[4] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[1] and lst[3] <= lst[4] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[1] <= lst[4] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[3] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[1] <= lst[3] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[3] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[1] <= lst[3] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

		elif lst[1] <= lst[0] and lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[6]:
			sorted[2] = lst[1]

			if lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[3] <= lst[4] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[0] and lst[3] <= lst[4] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[0] <= lst[4] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[3] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[0] <= lst[3] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[3] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[0] <= lst[3] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

		elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[4] and lst[3] <= lst[6]:
			sorted[2] = lst[3]

			if lst[0] <= lst[1] and lst[0] <= lst[4] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[1] <= lst[4] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[4] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[0] <= lst[4] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[0] <= lst[1] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[1]:
					sorted[4] = lst[6]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[0] <= lst[1] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[1]:
					sorted[4] = lst[4]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[3] and lst[4] <= lst[6]:
			sorted[2] = lst[4]

			if lst[0] <= lst[1] and lst[0] <= lst[3] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[1] <= lst[3] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[3] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[0] <= lst[3] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[0] <= lst[1] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[1]:
					sorted[4] = lst[6]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[3]:
				sorted[3] = lst[6]

				if lst[0] <= lst[1] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[1]:
					sorted[4] = lst[3]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[3] and lst[6] <= lst[4]:
			sorted[2] = lst[6]

			if lst[0] <= lst[1] and lst[0] <= lst[3] and lst[0] <= lst[4]:
				sorted[3] = lst[0]

				if lst[1] <= lst[3] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[3] and lst[1] <= lst[4]:
				sorted[3] = lst[1]

				if lst[0] <= lst[3] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[4]:
				sorted[3] = lst[3]

				if lst[0] <= lst[1] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[1]:
					sorted[4] = lst[4]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[3]:
				sorted[3] = lst[4]

				if lst[0] <= lst[1] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[1]:
					sorted[4] = lst[3]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

	elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[3] and lst[6] <= lst[4] and lst[6] <= lst[5]:
		sorted[1] = lst[6]

		if lst[0] <= lst[1] and lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[5]:
			sorted[2] = lst[0]

			if lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[3] <= lst[4] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[5] <= lst[3] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[1] and lst[3] <= lst[4] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[1] <= lst[4] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[3] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[1] <= lst[3] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[3] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[1] <= lst[3] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

		elif lst[1] <= lst[0] and lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[5]:
			sorted[2] = lst[1]

			if lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[3] <= lst[4] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[5] <= lst[3] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[0] and lst[3] <= lst[4] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[0] <= lst[4] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[3] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[0] <= lst[3] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[3] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[0] <= lst[3] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

		elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[4] and lst[3] <= lst[5]:
			sorted[2] = lst[3]

			if lst[0] <= lst[1] and lst[0] <= lst[4] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[1] <= lst[4] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[4] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[0] <= lst[4] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[0] <= lst[1] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[1]:
					sorted[4] = lst[5]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[0] <= lst[1] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[1]:
					sorted[4] = lst[4]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[3] and lst[4] <= lst[5]:
			sorted[2] = lst[4]

			if lst[0] <= lst[1] and lst[0] <= lst[3] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[1] <= lst[3] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[3] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[0] <= lst[3] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[0] <= lst[1] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[1]:
					sorted[4] = lst[5]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[3]:
				sorted[3] = lst[5]

				if lst[0] <= lst[1] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[1]:
					sorted[4] = lst[3]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[3] and lst[5] <= lst[4]:
			sorted[2] = lst[5]

			if lst[0] <= lst[1] and lst[0] <= lst[3] and lst[0] <= lst[4]:
				sorted[3] = lst[0]

				if lst[1] <= lst[3] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[3] and lst[1] <= lst[4]:
				sorted[3] = lst[1]

				if lst[0] <= lst[3] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[4]:
				sorted[3] = lst[3]

				if lst[0] <= lst[1] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[1]:
					sorted[4] = lst[4]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[3]:
				sorted[3] = lst[4]

				if lst[0] <= lst[1] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[1]:
					sorted[4] = lst[3]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[5] and lst[3] <= lst[6]:
	sorted[0] = lst[3]

	if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[4] and lst[0] <= lst[5] and lst[0] <= lst[6]:
		sorted[1] = lst[0]

		if lst[1] <= lst[2] and lst[1] <= lst[4] and lst[1] <= lst[5] and lst[1] <= lst[6]:
			sorted[2] = lst[1]

			if lst[2] <= lst[4] and lst[2] <= lst[5] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[4] <= lst[5] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[4] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[6] <= lst[4] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

			elif lst[4] <= lst[2] and lst[4] <= lst[5] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[2] <= lst[5] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[2] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

			elif lst[5] <= lst[2] and lst[5] <= lst[4] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[2] <= lst[4] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[6] <= lst[2] and lst[6] <= lst[4] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[2] <= lst[4] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

		elif lst[2] <= lst[1] and lst[2] <= lst[4] and lst[2] <= lst[5] and lst[2] <= lst[6]:
			sorted[2] = lst[2]

			if lst[1] <= lst[4] and lst[1] <= lst[5] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[4] <= lst[5] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[4] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[6] <= lst[4] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

			elif lst[4] <= lst[1] and lst[4] <= lst[5] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[1] <= lst[5] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[1] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[4] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[1] <= lst[4] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[4] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[1] <= lst[4] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

		elif lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[5] and lst[4] <= lst[6]:
			sorted[2] = lst[4]

			if lst[1] <= lst[2] and lst[1] <= lst[5] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[2] <= lst[5] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[2] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[5] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[1] <= lst[5] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[1] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[1] <= lst[2] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[1] <= lst[2] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[4] and lst[5] <= lst[6]:
			sorted[2] = lst[5]

			if lst[1] <= lst[2] and lst[1] <= lst[4] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[2] <= lst[4] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[4] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[1] <= lst[4] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[1] <= lst[2] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[1] <= lst[2] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[4] and lst[6] <= lst[5]:
			sorted[2] = lst[6]

			if lst[1] <= lst[2] and lst[1] <= lst[4] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[2] <= lst[4] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[4] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[1] <= lst[4] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[1] <= lst[2] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[1] <= lst[2] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

	elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[4] and lst[1] <= lst[5] and lst[1] <= lst[6]:
		sorted[1] = lst[1]

		if lst[0] <= lst[2] and lst[0] <= lst[4] and lst[0] <= lst[5] and lst[0] <= lst[6]:
			sorted[2] = lst[0]

			if lst[2] <= lst[4] and lst[2] <= lst[5] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[4] <= lst[5] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[4] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[6] <= lst[4] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

			elif lst[4] <= lst[2] and lst[4] <= lst[5] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[2] <= lst[5] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[2] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

			elif lst[5] <= lst[2] and lst[5] <= lst[4] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[2] <= lst[4] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[6] <= lst[2] and lst[6] <= lst[4] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[2] <= lst[4] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

		elif lst[2] <= lst[0] and lst[2] <= lst[4] and lst[2] <= lst[5] and lst[2] <= lst[6]:
			sorted[2] = lst[2]

			if lst[0] <= lst[4] and lst[0] <= lst[5] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[4] <= lst[5] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[4] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[6] <= lst[4] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

			elif lst[4] <= lst[0] and lst[4] <= lst[5] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[0] <= lst[5] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[0] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[4] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[0] <= lst[4] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[4] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[0] <= lst[4] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

		elif lst[4] <= lst[0] and lst[4] <= lst[2] and lst[4] <= lst[5] and lst[4] <= lst[6]:
			sorted[2] = lst[4]

			if lst[0] <= lst[2] and lst[0] <= lst[5] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[2] <= lst[5] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[2] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[5] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[0] <= lst[5] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[0] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[2] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[0] <= lst[2] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[2] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[0] <= lst[2] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[5] <= lst[0] and lst[5] <= lst[2] and lst[5] <= lst[4] and lst[5] <= lst[6]:
			sorted[2] = lst[5]

			if lst[0] <= lst[2] and lst[0] <= lst[4] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[2] <= lst[4] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[4] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[0] <= lst[4] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[2] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[0] <= lst[2] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[2] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[0] <= lst[2] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[6] <= lst[0] and lst[6] <= lst[2] and lst[6] <= lst[4] and lst[6] <= lst[5]:
			sorted[2] = lst[6]

			if lst[0] <= lst[2] and lst[0] <= lst[4] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[2] <= lst[4] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[4] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[0] <= lst[4] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[2] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[0] <= lst[2] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[2] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[0] <= lst[2] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

	elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[4] and lst[2] <= lst[5] and lst[2] <= lst[6]:
		sorted[1] = lst[2]

		if lst[0] <= lst[1] and lst[0] <= lst[4] and lst[0] <= lst[5] and lst[0] <= lst[6]:
			sorted[2] = lst[0]

			if lst[1] <= lst[4] and lst[1] <= lst[5] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[4] <= lst[5] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[4] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[6] <= lst[4] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

			elif lst[4] <= lst[1] and lst[4] <= lst[5] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[1] <= lst[5] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[1] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[4] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[1] <= lst[4] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[4] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[1] <= lst[4] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

		elif lst[1] <= lst[0] and lst[1] <= lst[4] and lst[1] <= lst[5] and lst[1] <= lst[6]:
			sorted[2] = lst[1]

			if lst[0] <= lst[4] and lst[0] <= lst[5] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[4] <= lst[5] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[4] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[6] <= lst[4] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

			elif lst[4] <= lst[0] and lst[4] <= lst[5] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[0] <= lst[5] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[0] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[4] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[0] <= lst[4] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[4] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[0] <= lst[4] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

		elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[5] and lst[4] <= lst[6]:
			sorted[2] = lst[4]

			if lst[0] <= lst[1] and lst[0] <= lst[5] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[1] <= lst[5] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[1] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[5] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[0] <= lst[5] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[0] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[0] <= lst[1] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[1]:
					sorted[4] = lst[6]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[0] <= lst[1] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[1]:
					sorted[4] = lst[5]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[4] and lst[5] <= lst[6]:
			sorted[2] = lst[5]

			if lst[0] <= lst[1] and lst[0] <= lst[4] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[1] <= lst[4] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[4] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[0] <= lst[4] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[0] <= lst[1] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[1]:
					sorted[4] = lst[6]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[0] <= lst[1] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[1]:
					sorted[4] = lst[4]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[4] and lst[6] <= lst[5]:
			sorted[2] = lst[6]

			if lst[0] <= lst[1] and lst[0] <= lst[4] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[1] <= lst[4] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[4] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[0] <= lst[4] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[0] <= lst[1] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[1]:
					sorted[4] = lst[5]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[0] <= lst[1] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[1]:
					sorted[4] = lst[4]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

	elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[5] and lst[4] <= lst[6]:
		sorted[1] = lst[4]

		if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[5] and lst[0] <= lst[6]:
			sorted[2] = lst[0]

			if lst[1] <= lst[2] and lst[1] <= lst[5] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[2] <= lst[5] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[2] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[5] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[1] <= lst[5] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[1] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[1] <= lst[2] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[1] <= lst[2] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[5] and lst[1] <= lst[6]:
			sorted[2] = lst[1]

			if lst[0] <= lst[2] and lst[0] <= lst[5] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[2] <= lst[5] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[2] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[5] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[0] <= lst[5] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[0] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[2] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[0] <= lst[2] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[2] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[0] <= lst[2] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[5] and lst[2] <= lst[6]:
			sorted[2] = lst[2]

			if lst[0] <= lst[1] and lst[0] <= lst[5] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[1] <= lst[5] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[1] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[5] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[0] <= lst[5] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[0] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[0] <= lst[1] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[1]:
					sorted[4] = lst[6]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[0] <= lst[1] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[1]:
					sorted[4] = lst[5]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[6]:
			sorted[2] = lst[5]

			if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[1] <= lst[2] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[0] <= lst[2] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[0] <= lst[1] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[1]:
					sorted[4] = lst[6]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[2]:
				sorted[3] = lst[6]

				if lst[0] <= lst[1] and lst[0] <= lst[2]:
					sorted[4] = lst[0]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[2]:
					sorted[4] = lst[1]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

				elif lst[2] <= lst[0] and lst[2] <= lst[1]:
					sorted[4] = lst[2]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[5]:
			sorted[2] = lst[6]

			if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[1] <= lst[2] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[0] <= lst[2] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[0] <= lst[1] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[1]:
					sorted[4] = lst[5]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[2]:
				sorted[3] = lst[5]

				if lst[0] <= lst[1] and lst[0] <= lst[2]:
					sorted[4] = lst[0]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[2]:
					sorted[4] = lst[1]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

				elif lst[2] <= lst[0] and lst[2] <= lst[1]:
					sorted[4] = lst[2]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

	elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[4] and lst[5] <= lst[6]:
		sorted[1] = lst[5]

		if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[4] and lst[0] <= lst[6]:
			sorted[2] = lst[0]

			if lst[1] <= lst[2] and lst[1] <= lst[4] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[2] <= lst[4] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[4] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[1] <= lst[4] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[1] <= lst[2] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[1] <= lst[2] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[4] and lst[1] <= lst[6]:
			sorted[2] = lst[1]

			if lst[0] <= lst[2] and lst[0] <= lst[4] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[2] <= lst[4] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[4] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[0] <= lst[4] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[2] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[0] <= lst[2] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[2] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[0] <= lst[2] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[4] and lst[2] <= lst[6]:
			sorted[2] = lst[2]

			if lst[0] <= lst[1] and lst[0] <= lst[4] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[1] <= lst[4] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[4] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[0] <= lst[4] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[0] <= lst[1] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[1]:
					sorted[4] = lst[6]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[0] <= lst[1] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[1]:
					sorted[4] = lst[4]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[6]:
			sorted[2] = lst[4]

			if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[1] <= lst[2] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[0] <= lst[2] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[0] <= lst[1] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[1]:
					sorted[4] = lst[6]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[2]:
				sorted[3] = lst[6]

				if lst[0] <= lst[1] and lst[0] <= lst[2]:
					sorted[4] = lst[0]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[2]:
					sorted[4] = lst[1]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

				elif lst[2] <= lst[0] and lst[2] <= lst[1]:
					sorted[4] = lst[2]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[4]:
			sorted[2] = lst[6]

			if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[4]:
				sorted[3] = lst[0]

				if lst[1] <= lst[2] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[4]:
				sorted[3] = lst[1]

				if lst[0] <= lst[2] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[4]:
				sorted[3] = lst[2]

				if lst[0] <= lst[1] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[1]:
					sorted[4] = lst[4]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[2]:
				sorted[3] = lst[4]

				if lst[0] <= lst[1] and lst[0] <= lst[2]:
					sorted[4] = lst[0]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[2]:
					sorted[4] = lst[1]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

				elif lst[2] <= lst[0] and lst[2] <= lst[1]:
					sorted[4] = lst[2]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

	elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[4] and lst[6] <= lst[5]:
		sorted[1] = lst[6]

		if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[4] and lst[0] <= lst[5]:
			sorted[2] = lst[0]

			if lst[1] <= lst[2] and lst[1] <= lst[4] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[2] <= lst[4] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[4] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[1] <= lst[4] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[1] <= lst[2] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[1] <= lst[2] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[4] and lst[1] <= lst[5]:
			sorted[2] = lst[1]

			if lst[0] <= lst[2] and lst[0] <= lst[4] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[2] <= lst[4] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[4] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[0] <= lst[4] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[2] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[0] <= lst[2] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[2] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[0] <= lst[2] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[4] and lst[2] <= lst[5]:
			sorted[2] = lst[2]

			if lst[0] <= lst[1] and lst[0] <= lst[4] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[1] <= lst[4] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[4] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[0] <= lst[4] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[0] <= lst[1] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[1]:
					sorted[4] = lst[5]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[0] <= lst[1] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[1]:
					sorted[4] = lst[4]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[5]:
			sorted[2] = lst[4]

			if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[1] <= lst[2] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[0] <= lst[2] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[0] <= lst[1] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[1]:
					sorted[4] = lst[5]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[2]:
				sorted[3] = lst[5]

				if lst[0] <= lst[1] and lst[0] <= lst[2]:
					sorted[4] = lst[0]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[2]:
					sorted[4] = lst[1]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

				elif lst[2] <= lst[0] and lst[2] <= lst[1]:
					sorted[4] = lst[2]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[4]:
			sorted[2] = lst[5]

			if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[4]:
				sorted[3] = lst[0]

				if lst[1] <= lst[2] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[4]:
				sorted[3] = lst[1]

				if lst[0] <= lst[2] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[4]:
				sorted[3] = lst[2]

				if lst[0] <= lst[1] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[1]:
					sorted[4] = lst[4]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[2]:
				sorted[3] = lst[4]

				if lst[0] <= lst[1] and lst[0] <= lst[2]:
					sorted[4] = lst[0]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[2]:
					sorted[4] = lst[1]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

				elif lst[2] <= lst[0] and lst[2] <= lst[1]:
					sorted[4] = lst[2]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[5] and lst[4] <= lst[6]:
	sorted[0] = lst[4]

	if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[5] and lst[0] <= lst[6]:
		sorted[1] = lst[0]

		if lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[5] and lst[1] <= lst[6]:
			sorted[2] = lst[1]

			if lst[2] <= lst[3] and lst[2] <= lst[5] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[3] <= lst[5] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[3] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

			elif lst[3] <= lst[2] and lst[3] <= lst[5] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[2] <= lst[5] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[2] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

			elif lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[2] <= lst[3] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[2] <= lst[3] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

		elif lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[5] and lst[2] <= lst[6]:
			sorted[2] = lst[2]

			if lst[1] <= lst[3] and lst[1] <= lst[5] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[3] <= lst[5] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[3] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

			elif lst[3] <= lst[1] and lst[3] <= lst[5] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[1] <= lst[5] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[1] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[3] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[1] <= lst[3] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[3] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[1] <= lst[3] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

		elif lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[5] and lst[3] <= lst[6]:
			sorted[2] = lst[3]

			if lst[1] <= lst[2] and lst[1] <= lst[5] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[2] <= lst[5] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[2] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[5] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[1] <= lst[5] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[1] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[1] <= lst[2] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[1] <= lst[2] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[6]:
			sorted[2] = lst[5]

			if lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[2] <= lst[3] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[1] <= lst[3] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[1] <= lst[2] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[3]:
				sorted[3] = lst[6]

				if lst[1] <= lst[2] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[3] <= lst[1] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[5]:
			sorted[2] = lst[6]

			if lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[2] <= lst[3] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[1] <= lst[3] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[1] <= lst[2] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[3]:
				sorted[3] = lst[5]

				if lst[1] <= lst[2] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[3] <= lst[1] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

	elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[5] and lst[1] <= lst[6]:
		sorted[1] = lst[1]

		if lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[5] and lst[0] <= lst[6]:
			sorted[2] = lst[0]

			if lst[2] <= lst[3] and lst[2] <= lst[5] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[3] <= lst[5] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[3] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

			elif lst[3] <= lst[2] and lst[3] <= lst[5] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[2] <= lst[5] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[2] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

			elif lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[2] <= lst[3] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[2] <= lst[3] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

		elif lst[2] <= lst[0] and lst[2] <= lst[3] and lst[2] <= lst[5] and lst[2] <= lst[6]:
			sorted[2] = lst[2]

			if lst[0] <= lst[3] and lst[0] <= lst[5] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[3] <= lst[5] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[3] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

			elif lst[3] <= lst[0] and lst[3] <= lst[5] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[0] <= lst[5] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[0] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[3] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[0] <= lst[3] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[3] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[0] <= lst[3] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

		elif lst[3] <= lst[0] and lst[3] <= lst[2] and lst[3] <= lst[5] and lst[3] <= lst[6]:
			sorted[2] = lst[3]

			if lst[0] <= lst[2] and lst[0] <= lst[5] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[2] <= lst[5] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[2] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[5] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[0] <= lst[5] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[0] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[2] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[0] <= lst[2] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[2] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[0] <= lst[2] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[5] <= lst[0] and lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[6]:
			sorted[2] = lst[5]

			if lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[2] <= lst[3] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[3] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[0] <= lst[3] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[2] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[0] <= lst[2] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[2] and lst[6] <= lst[3]:
				sorted[3] = lst[6]

				if lst[0] <= lst[2] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[6] <= lst[0] and lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[5]:
			sorted[2] = lst[6]

			if lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[2] <= lst[3] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[3] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[0] <= lst[3] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[2] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[0] <= lst[2] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[2] and lst[5] <= lst[3]:
				sorted[3] = lst[5]

				if lst[0] <= lst[2] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

	elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[5] and lst[2] <= lst[6]:
		sorted[1] = lst[2]

		if lst[0] <= lst[1] and lst[0] <= lst[3] and lst[0] <= lst[5] and lst[0] <= lst[6]:
			sorted[2] = lst[0]

			if lst[1] <= lst[3] and lst[1] <= lst[5] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[3] <= lst[5] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[3] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

			elif lst[3] <= lst[1] and lst[3] <= lst[5] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[1] <= lst[5] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[1] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[3] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[1] <= lst[3] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[3] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[1] <= lst[3] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

		elif lst[1] <= lst[0] and lst[1] <= lst[3] and lst[1] <= lst[5] and lst[1] <= lst[6]:
			sorted[2] = lst[1]

			if lst[0] <= lst[3] and lst[0] <= lst[5] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[3] <= lst[5] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[3] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

			elif lst[3] <= lst[0] and lst[3] <= lst[5] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[0] <= lst[5] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[0] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[3] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[0] <= lst[3] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[3] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[0] <= lst[3] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

		elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[5] and lst[3] <= lst[6]:
			sorted[2] = lst[3]

			if lst[0] <= lst[1] and lst[0] <= lst[5] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[1] <= lst[5] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[1] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[5] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[0] <= lst[5] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[0] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[0] <= lst[1] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[1]:
					sorted[4] = lst[6]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[0] <= lst[1] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[1]:
					sorted[4] = lst[5]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[3] and lst[5] <= lst[6]:
			sorted[2] = lst[5]

			if lst[0] <= lst[1] and lst[0] <= lst[3] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[1] <= lst[3] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[3] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[0] <= lst[3] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[0] <= lst[1] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[1]:
					sorted[4] = lst[6]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[3]:
				sorted[3] = lst[6]

				if lst[0] <= lst[1] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[1]:
					sorted[4] = lst[3]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[3] and lst[6] <= lst[5]:
			sorted[2] = lst[6]

			if lst[0] <= lst[1] and lst[0] <= lst[3] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[1] <= lst[3] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[3] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[0] <= lst[3] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[0] <= lst[1] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[1]:
					sorted[4] = lst[5]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[3]:
				sorted[3] = lst[5]

				if lst[0] <= lst[1] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[1]:
					sorted[4] = lst[3]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

	elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[5] and lst[3] <= lst[6]:
		sorted[1] = lst[3]

		if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[5] and lst[0] <= lst[6]:
			sorted[2] = lst[0]

			if lst[1] <= lst[2] and lst[1] <= lst[5] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[2] <= lst[5] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[2] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[5] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[1] <= lst[5] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[1] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[1] <= lst[2] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[1] <= lst[2] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[5] and lst[1] <= lst[6]:
			sorted[2] = lst[1]

			if lst[0] <= lst[2] and lst[0] <= lst[5] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[2] <= lst[5] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[2] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[5] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[0] <= lst[5] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[0] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[2] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[0] <= lst[2] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[2] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[0] <= lst[2] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[5] and lst[2] <= lst[6]:
			sorted[2] = lst[2]

			if lst[0] <= lst[1] and lst[0] <= lst[5] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[1] <= lst[5] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[1] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[5] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[0] <= lst[5] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[5] <= lst[6]:
						sorted[5] = lst[5]
						sorted[6] = lst[6]

					elif lst[6] <= lst[5]:
						sorted[5] = lst[6]
						sorted[6] = lst[5]

				elif lst[5] <= lst[0] and lst[5] <= lst[6]:
					sorted[4] = lst[5]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[5]:
					sorted[4] = lst[6]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[6]:
				sorted[3] = lst[5]

				if lst[0] <= lst[1] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[1]:
					sorted[4] = lst[6]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[5]:
				sorted[3] = lst[6]

				if lst[0] <= lst[1] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[1]:
					sorted[4] = lst[5]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[6]:
			sorted[2] = lst[5]

			if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[1] <= lst[2] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[0] <= lst[2] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[0] <= lst[1] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[1]:
					sorted[4] = lst[6]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[2]:
				sorted[3] = lst[6]

				if lst[0] <= lst[1] and lst[0] <= lst[2]:
					sorted[4] = lst[0]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[2]:
					sorted[4] = lst[1]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

				elif lst[2] <= lst[0] and lst[2] <= lst[1]:
					sorted[4] = lst[2]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[5]:
			sorted[2] = lst[6]

			if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[1] <= lst[2] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[0] <= lst[2] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[0] <= lst[1] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[1]:
					sorted[4] = lst[5]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[2]:
				sorted[3] = lst[5]

				if lst[0] <= lst[1] and lst[0] <= lst[2]:
					sorted[4] = lst[0]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[2]:
					sorted[4] = lst[1]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

				elif lst[2] <= lst[0] and lst[2] <= lst[1]:
					sorted[4] = lst[2]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

	elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[6]:
		sorted[1] = lst[5]

		if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[6]:
			sorted[2] = lst[0]

			if lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[2] <= lst[3] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[1] <= lst[3] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[1] <= lst[2] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[3]:
				sorted[3] = lst[6]

				if lst[1] <= lst[2] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[3] <= lst[1] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[6]:
			sorted[2] = lst[1]

			if lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[2] <= lst[3] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[3] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[0] <= lst[3] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[2] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[0] <= lst[2] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[2] and lst[6] <= lst[3]:
				sorted[3] = lst[6]

				if lst[0] <= lst[2] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[6]:
			sorted[2] = lst[2]

			if lst[0] <= lst[1] and lst[0] <= lst[3] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[1] <= lst[3] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[3] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[0] <= lst[3] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[0] <= lst[1] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[1]:
					sorted[4] = lst[6]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[3]:
				sorted[3] = lst[6]

				if lst[0] <= lst[1] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[1]:
					sorted[4] = lst[3]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[6]:
			sorted[2] = lst[3]

			if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[1] <= lst[2] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[0] <= lst[2] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[0] <= lst[1] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[1]:
					sorted[4] = lst[6]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[2]:
				sorted[3] = lst[6]

				if lst[0] <= lst[1] and lst[0] <= lst[2]:
					sorted[4] = lst[0]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[2]:
					sorted[4] = lst[1]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

				elif lst[2] <= lst[0] and lst[2] <= lst[1]:
					sorted[4] = lst[2]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[3]:
			sorted[2] = lst[6]

			if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[3]:
				sorted[3] = lst[0]

				if lst[1] <= lst[2] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[3] <= lst[1] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[3]:
				sorted[3] = lst[1]

				if lst[0] <= lst[2] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[3]:
				sorted[3] = lst[2]

				if lst[0] <= lst[1] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[1]:
					sorted[4] = lst[3]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[2]:
				sorted[3] = lst[3]

				if lst[0] <= lst[1] and lst[0] <= lst[2]:
					sorted[4] = lst[0]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[2]:
					sorted[4] = lst[1]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

				elif lst[2] <= lst[0] and lst[2] <= lst[1]:
					sorted[4] = lst[2]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

	elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[5]:
		sorted[1] = lst[6]

		if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[5]:
			sorted[2] = lst[0]

			if lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[2] <= lst[3] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[1] <= lst[3] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[1] <= lst[2] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[3]:
				sorted[3] = lst[5]

				if lst[1] <= lst[2] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[3] <= lst[1] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[5]:
			sorted[2] = lst[1]

			if lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[2] <= lst[3] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[3] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[0] <= lst[3] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[2] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[0] <= lst[2] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[2] and lst[5] <= lst[3]:
				sorted[3] = lst[5]

				if lst[0] <= lst[2] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[5]:
			sorted[2] = lst[2]

			if lst[0] <= lst[1] and lst[0] <= lst[3] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[1] <= lst[3] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[3] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[0] <= lst[3] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[0] <= lst[1] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[1]:
					sorted[4] = lst[5]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[3]:
				sorted[3] = lst[5]

				if lst[0] <= lst[1] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[1]:
					sorted[4] = lst[3]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[5]:
			sorted[2] = lst[3]

			if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[1] <= lst[2] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[0] <= lst[2] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[0] <= lst[1] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[1]:
					sorted[4] = lst[5]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[2]:
				sorted[3] = lst[5]

				if lst[0] <= lst[1] and lst[0] <= lst[2]:
					sorted[4] = lst[0]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[2]:
					sorted[4] = lst[1]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

				elif lst[2] <= lst[0] and lst[2] <= lst[1]:
					sorted[4] = lst[2]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[3]:
			sorted[2] = lst[5]

			if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[3]:
				sorted[3] = lst[0]

				if lst[1] <= lst[2] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[3] <= lst[1] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[3]:
				sorted[3] = lst[1]

				if lst[0] <= lst[2] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[3]:
				sorted[3] = lst[2]

				if lst[0] <= lst[1] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[1]:
					sorted[4] = lst[3]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[2]:
				sorted[3] = lst[3]

				if lst[0] <= lst[1] and lst[0] <= lst[2]:
					sorted[4] = lst[0]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[2]:
					sorted[4] = lst[1]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

				elif lst[2] <= lst[0] and lst[2] <= lst[1]:
					sorted[4] = lst[2]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[4] and lst[5] <= lst[6]:
	sorted[0] = lst[5]

	if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[6]:
		sorted[1] = lst[0]

		if lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[6]:
			sorted[2] = lst[1]

			if lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[3] <= lst[4] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[2] <= lst[4] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[6] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[2] <= lst[3] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[2] <= lst[3] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[4] <= lst[2] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

		elif lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[6]:
			sorted[2] = lst[2]

			if lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[3] <= lst[4] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[1] and lst[3] <= lst[4] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[1] <= lst[4] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[3] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[1] <= lst[3] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[3] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[1] <= lst[3] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

		elif lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[6]:
			sorted[2] = lst[3]

			if lst[1] <= lst[2] and lst[1] <= lst[4] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[2] <= lst[4] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[4] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[1] <= lst[4] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[1] <= lst[2] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[1] <= lst[2] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[6]:
			sorted[2] = lst[4]

			if lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[2] <= lst[3] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[1] <= lst[3] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[1] <= lst[2] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[3]:
				sorted[3] = lst[6]

				if lst[1] <= lst[2] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[3] <= lst[1] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[4]:
			sorted[2] = lst[6]

			if lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[4]:
				sorted[3] = lst[1]

				if lst[2] <= lst[3] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[4] <= lst[2] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[4]:
				sorted[3] = lst[2]

				if lst[1] <= lst[3] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[4]:
				sorted[3] = lst[3]

				if lst[1] <= lst[2] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[3]:
				sorted[3] = lst[4]

				if lst[1] <= lst[2] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[3] <= lst[1] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

	elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[6]:
		sorted[1] = lst[1]

		if lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[6]:
			sorted[2] = lst[0]

			if lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[3] <= lst[4] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[2] <= lst[4] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[2] <= lst[3] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[2] <= lst[3] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[4] <= lst[2] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

		elif lst[2] <= lst[0] and lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[6]:
			sorted[2] = lst[2]

			if lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[3] <= lst[4] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[0] and lst[3] <= lst[4] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[0] <= lst[4] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[3] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[0] <= lst[3] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[3] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[0] <= lst[3] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

		elif lst[3] <= lst[0] and lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[6]:
			sorted[2] = lst[3]

			if lst[0] <= lst[2] and lst[0] <= lst[4] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[2] <= lst[4] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[4] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[0] <= lst[4] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[2] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[0] <= lst[2] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[2] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[0] <= lst[2] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[4] <= lst[0] and lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[6]:
			sorted[2] = lst[4]

			if lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[2] <= lst[3] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[3] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[0] <= lst[3] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[2] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[0] <= lst[2] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[2] and lst[6] <= lst[3]:
				sorted[3] = lst[6]

				if lst[0] <= lst[2] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[6] <= lst[0] and lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[4]:
			sorted[2] = lst[6]

			if lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[4]:
				sorted[3] = lst[0]

				if lst[2] <= lst[3] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[4] <= lst[2] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[3] and lst[2] <= lst[4]:
				sorted[3] = lst[2]

				if lst[0] <= lst[3] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[2] and lst[3] <= lst[4]:
				sorted[3] = lst[3]

				if lst[0] <= lst[2] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[2] and lst[4] <= lst[3]:
				sorted[3] = lst[4]

				if lst[0] <= lst[2] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

	elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[6]:
		sorted[1] = lst[2]

		if lst[0] <= lst[1] and lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[6]:
			sorted[2] = lst[0]

			if lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[3] <= lst[4] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[1] and lst[3] <= lst[4] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[1] <= lst[4] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[3] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[1] <= lst[3] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[3] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[1] <= lst[3] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

		elif lst[1] <= lst[0] and lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[6]:
			sorted[2] = lst[1]

			if lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[3] <= lst[4] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[6] <= lst[3] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[0] and lst[3] <= lst[4] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[0] <= lst[4] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[3] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[0] <= lst[3] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[3] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[0] <= lst[3] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

		elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[4] and lst[3] <= lst[6]:
			sorted[2] = lst[3]

			if lst[0] <= lst[1] and lst[0] <= lst[4] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[1] <= lst[4] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[4] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[0] <= lst[4] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[0] <= lst[1] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[1]:
					sorted[4] = lst[6]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[0] <= lst[1] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[1]:
					sorted[4] = lst[4]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[3] and lst[4] <= lst[6]:
			sorted[2] = lst[4]

			if lst[0] <= lst[1] and lst[0] <= lst[3] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[1] <= lst[3] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[3] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[0] <= lst[3] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[0] <= lst[1] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[1]:
					sorted[4] = lst[6]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[3]:
				sorted[3] = lst[6]

				if lst[0] <= lst[1] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[1]:
					sorted[4] = lst[3]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[3] and lst[6] <= lst[4]:
			sorted[2] = lst[6]

			if lst[0] <= lst[1] and lst[0] <= lst[3] and lst[0] <= lst[4]:
				sorted[3] = lst[0]

				if lst[1] <= lst[3] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[3] and lst[1] <= lst[4]:
				sorted[3] = lst[1]

				if lst[0] <= lst[3] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[4]:
				sorted[3] = lst[3]

				if lst[0] <= lst[1] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[1]:
					sorted[4] = lst[4]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[3]:
				sorted[3] = lst[4]

				if lst[0] <= lst[1] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[1]:
					sorted[4] = lst[3]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

	elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[6]:
		sorted[1] = lst[3]

		if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[4] and lst[0] <= lst[6]:
			sorted[2] = lst[0]

			if lst[1] <= lst[2] and lst[1] <= lst[4] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[2] <= lst[4] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[4] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[1] <= lst[4] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[1] <= lst[2] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[1] <= lst[2] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[4] and lst[1] <= lst[6]:
			sorted[2] = lst[1]

			if lst[0] <= lst[2] and lst[0] <= lst[4] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[2] <= lst[4] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[4] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[0] <= lst[4] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[2] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[0] <= lst[2] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[2] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[0] <= lst[2] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[4] and lst[2] <= lst[6]:
			sorted[2] = lst[2]

			if lst[0] <= lst[1] and lst[0] <= lst[4] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[1] <= lst[4] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[4] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[0] <= lst[4] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[4] <= lst[6]:
						sorted[5] = lst[4]
						sorted[6] = lst[6]

					elif lst[6] <= lst[4]:
						sorted[5] = lst[6]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[6]:
					sorted[4] = lst[4]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[4]:
					sorted[4] = lst[6]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[6]:
				sorted[3] = lst[4]

				if lst[0] <= lst[1] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[1]:
					sorted[4] = lst[6]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[4]:
				sorted[3] = lst[6]

				if lst[0] <= lst[1] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[1]:
					sorted[4] = lst[4]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[6]:
			sorted[2] = lst[4]

			if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[1] <= lst[2] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[0] <= lst[2] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[0] <= lst[1] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[1]:
					sorted[4] = lst[6]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[2]:
				sorted[3] = lst[6]

				if lst[0] <= lst[1] and lst[0] <= lst[2]:
					sorted[4] = lst[0]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[2]:
					sorted[4] = lst[1]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

				elif lst[2] <= lst[0] and lst[2] <= lst[1]:
					sorted[4] = lst[2]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[4]:
			sorted[2] = lst[6]

			if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[4]:
				sorted[3] = lst[0]

				if lst[1] <= lst[2] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[4]:
				sorted[3] = lst[1]

				if lst[0] <= lst[2] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[4]:
				sorted[3] = lst[2]

				if lst[0] <= lst[1] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[1]:
					sorted[4] = lst[4]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[2]:
				sorted[3] = lst[4]

				if lst[0] <= lst[1] and lst[0] <= lst[2]:
					sorted[4] = lst[0]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[2]:
					sorted[4] = lst[1]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

				elif lst[2] <= lst[0] and lst[2] <= lst[1]:
					sorted[4] = lst[2]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

	elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[6]:
		sorted[1] = lst[4]

		if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[6]:
			sorted[2] = lst[0]

			if lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[2] <= lst[3] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[1] <= lst[3] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[1] <= lst[2] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[3]:
				sorted[3] = lst[6]

				if lst[1] <= lst[2] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[3] <= lst[1] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[6]:
			sorted[2] = lst[1]

			if lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[2] <= lst[3] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[6] <= lst[2] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[3] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[0] <= lst[3] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[2] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[0] <= lst[2] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[2] and lst[6] <= lst[3]:
				sorted[3] = lst[6]

				if lst[0] <= lst[2] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[6]:
			sorted[2] = lst[2]

			if lst[0] <= lst[1] and lst[0] <= lst[3] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[1] <= lst[3] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[3] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[0] <= lst[3] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[3] <= lst[6]:
						sorted[5] = lst[3]
						sorted[6] = lst[6]

					elif lst[6] <= lst[3]:
						sorted[5] = lst[6]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[6]:
					sorted[4] = lst[3]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[3]:
					sorted[4] = lst[6]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[6]:
				sorted[3] = lst[3]

				if lst[0] <= lst[1] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[1]:
					sorted[4] = lst[6]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[3]:
				sorted[3] = lst[6]

				if lst[0] <= lst[1] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[1]:
					sorted[4] = lst[3]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[6]:
			sorted[2] = lst[3]

			if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[6]:
				sorted[3] = lst[0]

				if lst[1] <= lst[2] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[6] <= lst[1] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[6]:
				sorted[3] = lst[1]

				if lst[0] <= lst[2] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[2] <= lst[6]:
						sorted[5] = lst[2]
						sorted[6] = lst[6]

					elif lst[6] <= lst[2]:
						sorted[5] = lst[6]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[6]:
					sorted[4] = lst[2]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[2]:
					sorted[4] = lst[6]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[6]:
				sorted[3] = lst[2]

				if lst[0] <= lst[1] and lst[0] <= lst[6]:
					sorted[4] = lst[0]

					if lst[1] <= lst[6]:
						sorted[5] = lst[1]
						sorted[6] = lst[6]

					elif lst[6] <= lst[1]:
						sorted[5] = lst[6]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[6]:
					sorted[4] = lst[1]

					if lst[0] <= lst[6]:
						sorted[5] = lst[0]
						sorted[6] = lst[6]

					elif lst[6] <= lst[0]:
						sorted[5] = lst[6]
						sorted[6] = lst[0]

				elif lst[6] <= lst[0] and lst[6] <= lst[1]:
					sorted[4] = lst[6]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[2]:
				sorted[3] = lst[6]

				if lst[0] <= lst[1] and lst[0] <= lst[2]:
					sorted[4] = lst[0]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[2]:
					sorted[4] = lst[1]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

				elif lst[2] <= lst[0] and lst[2] <= lst[1]:
					sorted[4] = lst[2]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[3]:
			sorted[2] = lst[6]

			if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[3]:
				sorted[3] = lst[0]

				if lst[1] <= lst[2] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[3] <= lst[1] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[3]:
				sorted[3] = lst[1]

				if lst[0] <= lst[2] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[3]:
				sorted[3] = lst[2]

				if lst[0] <= lst[1] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[1]:
					sorted[4] = lst[3]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[2]:
				sorted[3] = lst[3]

				if lst[0] <= lst[1] and lst[0] <= lst[2]:
					sorted[4] = lst[0]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[2]:
					sorted[4] = lst[1]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

				elif lst[2] <= lst[0] and lst[2] <= lst[1]:
					sorted[4] = lst[2]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

	elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[4]:
		sorted[1] = lst[6]

		if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[4]:
			sorted[2] = lst[0]

			if lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[4]:
				sorted[3] = lst[1]

				if lst[2] <= lst[3] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[4] <= lst[2] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[4]:
				sorted[3] = lst[2]

				if lst[1] <= lst[3] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[4]:
				sorted[3] = lst[3]

				if lst[1] <= lst[2] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[3]:
				sorted[3] = lst[4]

				if lst[1] <= lst[2] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[3] <= lst[1] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[4]:
			sorted[2] = lst[1]

			if lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[4]:
				sorted[3] = lst[0]

				if lst[2] <= lst[3] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[4] <= lst[2] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[3] and lst[2] <= lst[4]:
				sorted[3] = lst[2]

				if lst[0] <= lst[3] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[2] and lst[3] <= lst[4]:
				sorted[3] = lst[3]

				if lst[0] <= lst[2] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[2] and lst[4] <= lst[3]:
				sorted[3] = lst[4]

				if lst[0] <= lst[2] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[4]:
			sorted[2] = lst[2]

			if lst[0] <= lst[1] and lst[0] <= lst[3] and lst[0] <= lst[4]:
				sorted[3] = lst[0]

				if lst[1] <= lst[3] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[3] and lst[1] <= lst[4]:
				sorted[3] = lst[1]

				if lst[0] <= lst[3] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[4]:
				sorted[3] = lst[3]

				if lst[0] <= lst[1] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[1]:
					sorted[4] = lst[4]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[3]:
				sorted[3] = lst[4]

				if lst[0] <= lst[1] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[1]:
					sorted[4] = lst[3]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[4]:
			sorted[2] = lst[3]

			if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[4]:
				sorted[3] = lst[0]

				if lst[1] <= lst[2] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[4]:
				sorted[3] = lst[1]

				if lst[0] <= lst[2] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[4]:
				sorted[3] = lst[2]

				if lst[0] <= lst[1] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[1]:
					sorted[4] = lst[4]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[2]:
				sorted[3] = lst[4]

				if lst[0] <= lst[1] and lst[0] <= lst[2]:
					sorted[4] = lst[0]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[2]:
					sorted[4] = lst[1]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

				elif lst[2] <= lst[0] and lst[2] <= lst[1]:
					sorted[4] = lst[2]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[3]:
			sorted[2] = lst[4]

			if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[3]:
				sorted[3] = lst[0]

				if lst[1] <= lst[2] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[3] <= lst[1] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[3]:
				sorted[3] = lst[1]

				if lst[0] <= lst[2] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[3]:
				sorted[3] = lst[2]

				if lst[0] <= lst[1] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[1]:
					sorted[4] = lst[3]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[2]:
				sorted[3] = lst[3]

				if lst[0] <= lst[1] and lst[0] <= lst[2]:
					sorted[4] = lst[0]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[2]:
					sorted[4] = lst[1]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

				elif lst[2] <= lst[0] and lst[2] <= lst[1]:
					sorted[4] = lst[2]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

elif lst[6] <= lst[0] and lst[6] <= lst[1] and lst[6] <= lst[2] and lst[6] <= lst[3] and lst[6] <= lst[4] and lst[6] <= lst[5]:
	sorted[0] = lst[6]

	if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[5]:
		sorted[1] = lst[0]

		if lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[5]:
			sorted[2] = lst[1]

			if lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[3] <= lst[4] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[5] <= lst[3] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[2] <= lst[4] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[5] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[2] <= lst[3] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[2] <= lst[3] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[4] <= lst[2] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

		elif lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[5]:
			sorted[2] = lst[2]

			if lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[3] <= lst[4] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[5] <= lst[3] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[1] and lst[3] <= lst[4] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[1] <= lst[4] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[3] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[1] <= lst[3] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[3] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[1] <= lst[3] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

		elif lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[5]:
			sorted[2] = lst[3]

			if lst[1] <= lst[2] and lst[1] <= lst[4] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[2] <= lst[4] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[4] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[1] <= lst[4] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[1] <= lst[2] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[1] <= lst[2] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[5]:
			sorted[2] = lst[4]

			if lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[2] <= lst[3] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[1] <= lst[3] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[1] <= lst[2] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[3]:
				sorted[3] = lst[5]

				if lst[1] <= lst[2] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[3] <= lst[1] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[4]:
			sorted[2] = lst[5]

			if lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[4]:
				sorted[3] = lst[1]

				if lst[2] <= lst[3] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[4] <= lst[2] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[4]:
				sorted[3] = lst[2]

				if lst[1] <= lst[3] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[4]:
				sorted[3] = lst[3]

				if lst[1] <= lst[2] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[3]:
				sorted[3] = lst[4]

				if lst[1] <= lst[2] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[3] <= lst[1] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

	elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[5]:
		sorted[1] = lst[1]

		if lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[5]:
			sorted[2] = lst[0]

			if lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[3] <= lst[4] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[5] <= lst[3] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[2] <= lst[4] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[2] <= lst[3] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[2] <= lst[3] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[4] <= lst[2] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

		elif lst[2] <= lst[0] and lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[5]:
			sorted[2] = lst[2]

			if lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[3] <= lst[4] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[5] <= lst[3] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[0] and lst[3] <= lst[4] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[0] <= lst[4] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[3] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[0] <= lst[3] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[3] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[0] <= lst[3] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

		elif lst[3] <= lst[0] and lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[5]:
			sorted[2] = lst[3]

			if lst[0] <= lst[2] and lst[0] <= lst[4] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[2] <= lst[4] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[4] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[0] <= lst[4] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[2] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[0] <= lst[2] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[2] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[0] <= lst[2] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[4] <= lst[0] and lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[5]:
			sorted[2] = lst[4]

			if lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[2] <= lst[3] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[3] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[0] <= lst[3] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[2] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[0] <= lst[2] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[2] and lst[5] <= lst[3]:
				sorted[3] = lst[5]

				if lst[0] <= lst[2] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[5] <= lst[0] and lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[4]:
			sorted[2] = lst[5]

			if lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[4]:
				sorted[3] = lst[0]

				if lst[2] <= lst[3] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[4] <= lst[2] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[3] and lst[2] <= lst[4]:
				sorted[3] = lst[2]

				if lst[0] <= lst[3] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[2] and lst[3] <= lst[4]:
				sorted[3] = lst[3]

				if lst[0] <= lst[2] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[2] and lst[4] <= lst[3]:
				sorted[3] = lst[4]

				if lst[0] <= lst[2] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

	elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[4] and lst[2] <= lst[5]:
		sorted[1] = lst[2]

		if lst[0] <= lst[1] and lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[5]:
			sorted[2] = lst[0]

			if lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[3] <= lst[4] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[5] <= lst[3] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[1] and lst[3] <= lst[4] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[1] <= lst[4] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[3] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[1] <= lst[3] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[3] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[1] <= lst[3] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

		elif lst[1] <= lst[0] and lst[1] <= lst[3] and lst[1] <= lst[4] and lst[1] <= lst[5]:
			sorted[2] = lst[1]

			if lst[0] <= lst[3] and lst[0] <= lst[4] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[3] <= lst[4] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[3] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[5] <= lst[3] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

			elif lst[3] <= lst[0] and lst[3] <= lst[4] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[0] <= lst[4] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[3] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[0] <= lst[3] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[3] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[0] <= lst[3] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

		elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[4] and lst[3] <= lst[5]:
			sorted[2] = lst[3]

			if lst[0] <= lst[1] and lst[0] <= lst[4] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[1] <= lst[4] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[4] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[0] <= lst[4] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[0] <= lst[1] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[1]:
					sorted[4] = lst[5]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[0] <= lst[1] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[1]:
					sorted[4] = lst[4]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[3] and lst[4] <= lst[5]:
			sorted[2] = lst[4]

			if lst[0] <= lst[1] and lst[0] <= lst[3] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[1] <= lst[3] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[3] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[0] <= lst[3] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[0] <= lst[1] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[1]:
					sorted[4] = lst[5]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[3]:
				sorted[3] = lst[5]

				if lst[0] <= lst[1] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[1]:
					sorted[4] = lst[3]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[3] and lst[5] <= lst[4]:
			sorted[2] = lst[5]

			if lst[0] <= lst[1] and lst[0] <= lst[3] and lst[0] <= lst[4]:
				sorted[3] = lst[0]

				if lst[1] <= lst[3] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[3] and lst[1] <= lst[4]:
				sorted[3] = lst[1]

				if lst[0] <= lst[3] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[4]:
				sorted[3] = lst[3]

				if lst[0] <= lst[1] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[1]:
					sorted[4] = lst[4]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[3]:
				sorted[3] = lst[4]

				if lst[0] <= lst[1] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[1]:
					sorted[4] = lst[3]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

	elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[4] and lst[3] <= lst[5]:
		sorted[1] = lst[3]

		if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[4] and lst[0] <= lst[5]:
			sorted[2] = lst[0]

			if lst[1] <= lst[2] and lst[1] <= lst[4] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[2] <= lst[4] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[4] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[1] <= lst[4] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[1] <= lst[2] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[1] <= lst[2] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[4] and lst[1] <= lst[5]:
			sorted[2] = lst[1]

			if lst[0] <= lst[2] and lst[0] <= lst[4] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[2] <= lst[4] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[2] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[4] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[0] <= lst[4] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[2] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[0] <= lst[2] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[2] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[0] <= lst[2] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[4] and lst[2] <= lst[5]:
			sorted[2] = lst[2]

			if lst[0] <= lst[1] and lst[0] <= lst[4] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[1] <= lst[4] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[1] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[4] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[0] <= lst[4] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[4] <= lst[5]:
						sorted[5] = lst[4]
						sorted[6] = lst[5]

					elif lst[5] <= lst[4]:
						sorted[5] = lst[5]
						sorted[6] = lst[4]

				elif lst[4] <= lst[0] and lst[4] <= lst[5]:
					sorted[4] = lst[4]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[4]:
					sorted[4] = lst[5]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[5]:
				sorted[3] = lst[4]

				if lst[0] <= lst[1] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[1]:
					sorted[4] = lst[5]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[4]:
				sorted[3] = lst[5]

				if lst[0] <= lst[1] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[1]:
					sorted[4] = lst[4]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[5]:
			sorted[2] = lst[4]

			if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[1] <= lst[2] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[0] <= lst[2] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[0] <= lst[1] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[1]:
					sorted[4] = lst[5]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[2]:
				sorted[3] = lst[5]

				if lst[0] <= lst[1] and lst[0] <= lst[2]:
					sorted[4] = lst[0]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[2]:
					sorted[4] = lst[1]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

				elif lst[2] <= lst[0] and lst[2] <= lst[1]:
					sorted[4] = lst[2]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[4]:
			sorted[2] = lst[5]

			if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[4]:
				sorted[3] = lst[0]

				if lst[1] <= lst[2] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[4]:
				sorted[3] = lst[1]

				if lst[0] <= lst[2] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[4]:
				sorted[3] = lst[2]

				if lst[0] <= lst[1] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[1]:
					sorted[4] = lst[4]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[2]:
				sorted[3] = lst[4]

				if lst[0] <= lst[1] and lst[0] <= lst[2]:
					sorted[4] = lst[0]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[2]:
					sorted[4] = lst[1]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

				elif lst[2] <= lst[0] and lst[2] <= lst[1]:
					sorted[4] = lst[2]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

	elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[3] and lst[4] <= lst[5]:
		sorted[1] = lst[4]

		if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[5]:
			sorted[2] = lst[0]

			if lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[2] <= lst[3] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[1] <= lst[3] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[1] <= lst[2] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[3]:
				sorted[3] = lst[5]

				if lst[1] <= lst[2] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[3] <= lst[1] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[5]:
			sorted[2] = lst[1]

			if lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[2] <= lst[3] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[5] <= lst[2] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[3] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[0] <= lst[3] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[2] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[0] <= lst[2] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[2] and lst[5] <= lst[3]:
				sorted[3] = lst[5]

				if lst[0] <= lst[2] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[5]:
			sorted[2] = lst[2]

			if lst[0] <= lst[1] and lst[0] <= lst[3] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[1] <= lst[3] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[3] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[0] <= lst[3] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[3] <= lst[5]:
						sorted[5] = lst[3]
						sorted[6] = lst[5]

					elif lst[5] <= lst[3]:
						sorted[5] = lst[5]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[5]:
					sorted[4] = lst[3]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[3]:
					sorted[4] = lst[5]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[5]:
				sorted[3] = lst[3]

				if lst[0] <= lst[1] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[1]:
					sorted[4] = lst[5]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[3]:
				sorted[3] = lst[5]

				if lst[0] <= lst[1] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[1]:
					sorted[4] = lst[3]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[5]:
			sorted[2] = lst[3]

			if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[5]:
				sorted[3] = lst[0]

				if lst[1] <= lst[2] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[5] <= lst[1] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[5]:
				sorted[3] = lst[1]

				if lst[0] <= lst[2] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[2] <= lst[5]:
						sorted[5] = lst[2]
						sorted[6] = lst[5]

					elif lst[5] <= lst[2]:
						sorted[5] = lst[5]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[5]:
					sorted[4] = lst[2]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[2]:
					sorted[4] = lst[5]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[5]:
				sorted[3] = lst[2]

				if lst[0] <= lst[1] and lst[0] <= lst[5]:
					sorted[4] = lst[0]

					if lst[1] <= lst[5]:
						sorted[5] = lst[1]
						sorted[6] = lst[5]

					elif lst[5] <= lst[1]:
						sorted[5] = lst[5]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[5]:
					sorted[4] = lst[1]

					if lst[0] <= lst[5]:
						sorted[5] = lst[0]
						sorted[6] = lst[5]

					elif lst[5] <= lst[0]:
						sorted[5] = lst[5]
						sorted[6] = lst[0]

				elif lst[5] <= lst[0] and lst[5] <= lst[1]:
					sorted[4] = lst[5]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[2]:
				sorted[3] = lst[5]

				if lst[0] <= lst[1] and lst[0] <= lst[2]:
					sorted[4] = lst[0]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[2]:
					sorted[4] = lst[1]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

				elif lst[2] <= lst[0] and lst[2] <= lst[1]:
					sorted[4] = lst[2]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[3]:
			sorted[2] = lst[5]

			if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[3]:
				sorted[3] = lst[0]

				if lst[1] <= lst[2] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[3] <= lst[1] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[3]:
				sorted[3] = lst[1]

				if lst[0] <= lst[2] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[3]:
				sorted[3] = lst[2]

				if lst[0] <= lst[1] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[1]:
					sorted[4] = lst[3]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[2]:
				sorted[3] = lst[3]

				if lst[0] <= lst[1] and lst[0] <= lst[2]:
					sorted[4] = lst[0]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[2]:
					sorted[4] = lst[1]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

				elif lst[2] <= lst[0] and lst[2] <= lst[1]:
					sorted[4] = lst[2]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

	elif lst[5] <= lst[0] and lst[5] <= lst[1] and lst[5] <= lst[2] and lst[5] <= lst[3] and lst[5] <= lst[4]:
		sorted[1] = lst[5]

		if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[4]:
			sorted[2] = lst[0]

			if lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[4]:
				sorted[3] = lst[1]

				if lst[2] <= lst[3] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[4] <= lst[2] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[4]:
				sorted[3] = lst[2]

				if lst[1] <= lst[3] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[4]:
				sorted[3] = lst[3]

				if lst[1] <= lst[2] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[3]:
				sorted[3] = lst[4]

				if lst[1] <= lst[2] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[3] <= lst[1] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

		elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[3] and lst[1] <= lst[4]:
			sorted[2] = lst[1]

			if lst[0] <= lst[2] and lst[0] <= lst[3] and lst[0] <= lst[4]:
				sorted[3] = lst[0]

				if lst[2] <= lst[3] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[2] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[4] <= lst[2] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

			elif lst[2] <= lst[0] and lst[2] <= lst[3] and lst[2] <= lst[4]:
				sorted[3] = lst[2]

				if lst[0] <= lst[3] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[2] and lst[3] <= lst[4]:
				sorted[3] = lst[3]

				if lst[0] <= lst[2] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[2] and lst[4] <= lst[3]:
				sorted[3] = lst[4]

				if lst[0] <= lst[2] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

		elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[3] and lst[2] <= lst[4]:
			sorted[2] = lst[2]

			if lst[0] <= lst[1] and lst[0] <= lst[3] and lst[0] <= lst[4]:
				sorted[3] = lst[0]

				if lst[1] <= lst[3] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[1] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[3] and lst[1] <= lst[4]:
				sorted[3] = lst[1]

				if lst[0] <= lst[3] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[3] <= lst[4]:
						sorted[5] = lst[3]
						sorted[6] = lst[4]

					elif lst[4] <= lst[3]:
						sorted[5] = lst[4]
						sorted[6] = lst[3]

				elif lst[3] <= lst[0] and lst[3] <= lst[4]:
					sorted[4] = lst[3]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[3]:
					sorted[4] = lst[4]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[4]:
				sorted[3] = lst[3]

				if lst[0] <= lst[1] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[1]:
					sorted[4] = lst[4]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[3]:
				sorted[3] = lst[4]

				if lst[0] <= lst[1] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[1]:
					sorted[4] = lst[3]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[2] and lst[3] <= lst[4]:
			sorted[2] = lst[3]

			if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[4]:
				sorted[3] = lst[0]

				if lst[1] <= lst[2] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[4] <= lst[1] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[4]:
				sorted[3] = lst[1]

				if lst[0] <= lst[2] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[2] <= lst[4]:
						sorted[5] = lst[2]
						sorted[6] = lst[4]

					elif lst[4] <= lst[2]:
						sorted[5] = lst[4]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[4]:
					sorted[4] = lst[2]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[2]:
					sorted[4] = lst[4]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[4]:
				sorted[3] = lst[2]

				if lst[0] <= lst[1] and lst[0] <= lst[4]:
					sorted[4] = lst[0]

					if lst[1] <= lst[4]:
						sorted[5] = lst[1]
						sorted[6] = lst[4]

					elif lst[4] <= lst[1]:
						sorted[5] = lst[4]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[4]:
					sorted[4] = lst[1]

					if lst[0] <= lst[4]:
						sorted[5] = lst[0]
						sorted[6] = lst[4]

					elif lst[4] <= lst[0]:
						sorted[5] = lst[4]
						sorted[6] = lst[0]

				elif lst[4] <= lst[0] and lst[4] <= lst[1]:
					sorted[4] = lst[4]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[2]:
				sorted[3] = lst[4]

				if lst[0] <= lst[1] and lst[0] <= lst[2]:
					sorted[4] = lst[0]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[2]:
					sorted[4] = lst[1]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

				elif lst[2] <= lst[0] and lst[2] <= lst[1]:
					sorted[4] = lst[2]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

		elif lst[4] <= lst[0] and lst[4] <= lst[1] and lst[4] <= lst[2] and lst[4] <= lst[3]:
			sorted[2] = lst[4]

			if lst[0] <= lst[1] and lst[0] <= lst[2] and lst[0] <= lst[3]:
				sorted[3] = lst[0]

				if lst[1] <= lst[2] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[1] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[3] <= lst[1] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

			elif lst[1] <= lst[0] and lst[1] <= lst[2] and lst[1] <= lst[3]:
				sorted[3] = lst[1]

				if lst[0] <= lst[2] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[2] <= lst[3]:
						sorted[5] = lst[2]
						sorted[6] = lst[3]

					elif lst[3] <= lst[2]:
						sorted[5] = lst[3]
						sorted[6] = lst[2]

				elif lst[2] <= lst[0] and lst[2] <= lst[3]:
					sorted[4] = lst[2]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[2]:
					sorted[4] = lst[3]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

			elif lst[2] <= lst[0] and lst[2] <= lst[1] and lst[2] <= lst[3]:
				sorted[3] = lst[2]

				if lst[0] <= lst[1] and lst[0] <= lst[3]:
					sorted[4] = lst[0]

					if lst[1] <= lst[3]:
						sorted[5] = lst[1]
						sorted[6] = lst[3]

					elif lst[3] <= lst[1]:
						sorted[5] = lst[3]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[3]:
					sorted[4] = lst[1]

					if lst[0] <= lst[3]:
						sorted[5] = lst[0]
						sorted[6] = lst[3]

					elif lst[3] <= lst[0]:
						sorted[5] = lst[3]
						sorted[6] = lst[0]

				elif lst[3] <= lst[0] and lst[3] <= lst[1]:
					sorted[4] = lst[3]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

			elif lst[3] <= lst[0] and lst[3] <= lst[1] and lst[3] <= lst[2]:
				sorted[3] = lst[3]

				if lst[0] <= lst[1] and lst[0] <= lst[2]:
					sorted[4] = lst[0]

					if lst[1] <= lst[2]:
						sorted[5] = lst[1]
						sorted[6] = lst[2]

					elif lst[2] <= lst[1]:
						sorted[5] = lst[2]
						sorted[6] = lst[1]

				elif lst[1] <= lst[0] and lst[1] <= lst[2]:
					sorted[4] = lst[1]

					if lst[0] <= lst[2]:
						sorted[5] = lst[0]
						sorted[6] = lst[2]

					elif lst[2] <= lst[0]:
						sorted[5] = lst[2]
						sorted[6] = lst[0]

				elif lst[2] <= lst[0] and lst[2] <= lst[1]:
					sorted[4] = lst[2]

					if lst[0] <= lst[1]:
						sorted[5] = lst[0]
						sorted[6] = lst[1]

					elif lst[1] <= lst[0]:
						sorted[5] = lst[1]
						sorted[6] = lst[0]

print(sorted)
