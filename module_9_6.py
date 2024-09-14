def all_variants(text):

	n = len(text)


	for start in range(n):
		for end in range(start + 1, n + 1):
			yield text[start:end]



text = "abc"
generator = all_variants(text)


for variant in generator:
	print(variant)