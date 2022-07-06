#===================================================================
#--------------------------------E10--------------------------------
#===================================================================


#------------------------------E10-1--------------------------------
# Function for nth Fibonacci number

def Fibonacci(n):
	a = 0
	b = 1
	if n < 0:
		print("Incorrect input")
	elif n == 0:
		return a
	elif n == 1:
		return b
	else:
		for i in range(2, n):
			c = a + b
			a = b
			b = c
		return b

	    
#------------------------------E10-1--------------------------------
# Function for nth Fibonacci number (recursive function)

def FibonacciRec(n):
    
	if n < 0:
		print("Incorrect input")
	elif n == 0:
		return 0

	elif n == 1 or n == 2:
		return 1
	    
	else:
		return Fibonacci(n-1) + Fibonacci(n-2)



#------------------------------E10-2--------------------------------
# Function for nth fibonacci numbers list

def Fibonacci_list(n):
    
  if n < 0:
      print("Incorrect input")
      
  elif n == 0:
    return [0]

  sequence = [0, 1]
  while len(sequence) <= n:
    next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
    sequence.append(next_value)
  return sequence


#------------------------------E10-2--------------------------------
# Function for nth fibonacci number numbers list (recursive function)

def Fibonacci_listRec(n):
    
    if n < 0:
        print("Incorrect input")
        
    elif n == 0:
        return [0]

    elif n == 1 :
    	result=[0,1]
    	return result
      
    else:
        result=[0,1]
        while len(result)<=n:
            nextvalue= Fibonacci_listRec(len(result)-1)[len(result)-1]+ Fibonacci_listRec(len(result)-1)[len(result)-2]
            result.append(nextvalue)
        return result

           
            
        
