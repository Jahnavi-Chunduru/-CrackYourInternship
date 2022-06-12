class Solution:
	def isNumber(self, s: str) -> bool:    
		exp = False
		exp_dig = False
		dig = False
		dec = False
		prev_char = None
		if not s: return False

		for char in s:    
			if char == "+" or char == "-":
				if prev_char != None and prev_char != "E" and prev_char != "e": return False
				prev_char = char

			elif char == ".":
				if dec == True or exp == True: return False
				dec = True
				prev_char = char

			elif char == "E" or char == "e":
				if exp == True or dig == False: return False
				exp = True
				prev_char = char

			elif char.isnumeric():
				prev_char = char
				if exp == True: exp_dig = True
				dig = True

			else:
				return False
		if dig == False: return False
		if exp == True and exp_dig == False: return False


		return True
