def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email


print(replace_domain("tar@gmail.ru", "gmail.ru", "gmail.com"))
---------------------------------------------------------------------
def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for word in input_string.lower():
		# Add any non-blank letters to the
		# end of one string, and to the front
		# of the other string.
		if word != " ":
			new_string = new_string + word
			reverse_string = word + reverse_string
	# Compare the strings
	if reverse_string == new_string:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
---------------------------------------------------------------------
