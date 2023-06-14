p = [3,0,0,1]
q = [-1,0,1,0,1]
p0 = [2,0,3,0]
q0 = [0,0,0]


"""
This program contains several functions for manipulating polynomials.
Read notes for each function.
"""

def polynomial_to_string(p_list):
    terms = []
    terms_coefficient_checked = []
    degree = 0

    # First collect a list of terms
    if not any(p_list): #If all numbers in the list are false, returns zero
        return 0
    for coeff in p_list:
        if coeff != 0:                  #Removes the zeroes in the list, e.g [1,0,1] returns 1 + 1x^2
            if degree == 0:
                terms.append(str(coeff))
            elif degree == 1:
                terms.append(str(coeff) + 'x')
            else:
                term = str(coeff) + 'x^' + str(degree)
                terms.append(term)
        degree += 1
    for j in terms: #for loop iterating through each element in "terms" checking if there´s 1 or -1 infront of x
        j = j.replace("-1x", "-x")
        j = j.replace("1x", "x")
        terms_coefficient_checked.append(j)

    final_string = ' + '.join(terms_coefficient_checked)  # The string ' + ' is used as "glue" between the elements in the string
    return final_string


def leading_coefficent(p_list):
    if any(p_list):
        for j in p_list[::-1]: #Iterates backwards in the list, ignoring zeros
            if j > 0:
                return j
    else:
        return 0

def degree(p_list):
    if any(p_list):
        power_to = len(p_list)-1
        for j in p_list[::-1]:
            if j > 0:
                return power_to
            power_to -= 1
    else:
        return 0

def eval_poly(p_list, n): #"p_list" is the polynomial in list format and "n" is the value for the variable X
    poly_sum = 0
    degree = 0
    for c in p_list: #c for coefficent. Uses the skeleton of "polynomial to string" as a basis
        if degree == 0:
            poly_sum += c
        else:
            poly_sum += c * (n ** degree)
        degree += 1 #degrees of power
    return poly_sum

def neg_poly(p_list):
    reversed_coeff = []
    for j in p_list:
        j = j * -1 #returns all positives as negatives and vice versa
        reversed_coeff.append(j)
    return reversed_coeff

def add_poly(p_list, q_list):
    p_q_list = []
    length = 0 #Lists can be different length, so need different conditions
    while len(p_list) > length or len(q_list) > length: #While loop, compares length of lists to incremental increasing variable
        if length > len(p_list) - 1: #indexing starts at 0 and len() from 1, therefore -1
            p_q_list.append(q_list[length])
        elif length > len(q_list) - 1:
            p_q_list.append(p_list[length])
        else:
            p_q_list.append(p_list[length] + q_list[length])
        length += 1
    return p_q_list

def sub_poly(p_list,q_list):
    p_minus_q_list = [] #Same logic as add_poly
    length = 0
    while len(p_list) > length or len(q_list) > length:
        if length > len(p_list) - 1:
            p_minus_q_list.append(q_list[length]*-1)
        elif length > len(q_list) - 1:
            p_minus_q_list.append(p_list[length])
        else:
            p_minus_q_list.append(p_list[length] - q_list[length])
        length += 1
    return p_minus_q_list

def eq_poly(p_list,q_list):

    r = sub_poly(p_list,q_list) #subtract both parameters

    if not any(r): #If the variable r isn´t empty or contains only zeroes, the two parameters are NOT equal
        return True
    return False

print(eq_poly(p,p0))
#False

print(eq_poly(q,p0))
#False

print(eq_poly(q0,[]))
#True

print(eq_poly(add_poly(p,q),add_poly(q,p)))
#True

print(eq_poly(sub_poly(p,p),[]))
#True

print(eq_poly(sub_poly(p,neg_poly(q)),add_poly(p,q)))
#True

print(eq_poly(add_poly(p,p),[]))
#False

print(eval_poly(add_poly(p,q),12) == eval_poly(p,12) + eval_poly(q,12))
#True