def transform_gender(val):
	if val == 'male':
		return 1
	elif val == 'female':
		return 0
	else:
		return 1
def transform_married(val):
	if val == 'no':
		return 0
	elif val == 'yes':
		return 1
	else:
		return 0

def transform_education(val):
	if val == 'graduate':
		return 0
	elif val == 'not graduate':
		return 1
	else:
		return 0
		
def transform_self_emp(val):
	if val == 'no':
		return 0
	elif val == 'yes':
		return 1
	else:
		return 0
def transform_prop_area(val):
	if val == 'urban':
		return 2
	elif val == 'rural':
		return 0
	elif val == 'semiurban':
		return 1
	else:
		return 0