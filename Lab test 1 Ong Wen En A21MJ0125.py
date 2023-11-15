# ONG WEN EN A21MJ015 LAB TEST 1 SMJE4383 SECTION 1 DR.SHAHRUM
#Ong Wen En A21MJ0125

#1. Takes two positive integers, a and d, as input from the user. These represent the first term 
#and the common difference of an arithmetic sequence.

first_positive_integer_str = input("Enter the first term (a) of the arithmetic sequence:")
first_positive_integer_int = int (first_positive_integer_str)

second_positive_integer_str = input("Enter the common difference (d) of the arithmetic sequence :")
second_positive_integer_int = int (second_positive_integer_str)

number_of_term_str = input(" Enter the number of terms (n) to sum:")
number_of_term_int = int(number_of_term_str)

count_int = 1
sum_int = 0

while count_int <= number_of_term_int:

    sum_int = sum_int +first_positive_integer_int + second_positive_integer_int
    count_int = count_int + 1


print ("The final sum is :",sum_int)
