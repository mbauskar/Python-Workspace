# program to perform addition and multiplication of two matrix

m1 = []				# list to store the matrix
m2 = []

def getMatrixFromUser(rows, column):
	matrix = []
	for i in range(rows):
		row = []
		
		for j in range(column):
			usr_ip = raw_input("Enter the number for matrix[%d,%d] : "%(i, j))
			row.append(int(usr_ip))

		matrix.append(row)

	return matrix

def getMatrixFromUser():
	matrix = []

	usr_ip = raw_input("Enter the total number of rows : ")
	rows = int(usr_ip)

	usr_ip = raw_input("Enter the total number of column : ")
	column = int(usr_ip)

	for i in range(rows):
		row = []
		
		for j in range(column):
			usr_ip = raw_input("Enter the number for matrix[%d,%d] : "%(i, j))
			row.append(int(usr_ip))

		matrix.append(row)

	return matrix

def additionMatrices(m1, m2):
	# function to add two matrices
	#pass
	print len(m1), "x", len(m1[0])
	m1_row = len(m1)
	m1_column = len(m1[0])
	m2_row = len(m2)
	m2_column = len(m2[0])

	print "m1", m1_row, "x", m1_column
	print "m2", m2_row, "x", m2_column

	if ( m1_row == m2_row ) & ( m1_column == m2_column ):
		m3 = []
		for i in range(len(m1)):
			row = []
			
			for j in range(len(m1[i])):
				add = m1[i][j] + m2[i][j]
				row.append(add)

			m3.append(row)

		return m3
	else:
		print "For addition total number rows and columns should be same"

def multiplyMatrices(m1, m2):
	# Function to multiply two matrices

	m3 = []

	if (m1 != None) & (m2 != None):
		m1_row = len(m1)
		m1_column = len(m1[0])
		m2_row = len(m2)
		m2_column = len(m2[0])

		if(m1_column == m2_row):
			for i in range(m1_row):
				row = []
				for j in range(m2_column):
					sum = 0
					for k in range(m2_row):
						sum += ( m1[i][k] * m2[k][j] )
					
					row.append(sum)
				m3.append(row)
			return m3
		else:
			print "For multiplication the number of columns of first matrix should be equal to number of rows of second matrix"

def printMatrix(matrix):
	# function to print the matrix
	
	if matrix != None:
		rows = len(matrix)

		for i in range(rows):
			for j in range(len(matrix[i])):
				print matrix[i][j],
			print "\n"

# get the matrices from user
#print "Enter the size of matrix m1 and m2"

#rows = int(raw_input("Enter the number rows : "))
#column = int(raw_input("Enter the number of column : "))

print "\nEnter the values for first matrix"
m1 = getMatrixFromUser()
print "\nEnter the values for second matrix"
m2 = getMatrixFromUser()

print "\nAddition of matrix m1 and m2 : "
m3 = additionMatrices(m1,m2)
printMatrix(m3)

print "\nMultiplication of matrices : "
m3 = multiplyMatrices(m1, m2)
printMatrix(m3)