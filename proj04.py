#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 16:11:03 2022

Algorithm
Functions defined for each mathn function
Main:
    displays opening statement
    prompts for z c or q, loops until one is input
    if z input:
        prints Zeta
        prompts for a float, loops until valid float input
        references zeta function and prints zeta value
    if c is input:
        prints Conway
        prompts for positive integer, loops until valid pos int input
        references base 13 function, tridecimal function, and conway function
            converts pos int to base 13 and prints
            converts base 13 to tridecimal and prints
            converts tridecimal to conway and prints
    if q is input:
        closing statement
    prompts for z c or q again, continues until q is input
        closing statement
"""


DELTA = 10**-7  # used for the zeta function

#function to convert int to a base13
def int_to_base13(n):
    base_str = ''#initializes bas13 string
    while n > 0:#loops until n is <= 0
        n_r = n%13 #finds the remainder of n/13
        #adds onto string based off of remainder
        if n_r == 10:
            base_str += 'A'
        elif n_r == 11 :
            base_str +='B'
        elif n_r == 12:
            base_str += 'C'
        else:
            base_str += str(n_r)
        
        n = n//13 #changes n to quotient of n, continues with loops unless = 0
    return base_str[::-1]#reads string backwards because base13 goes from last to first term
    
#function to convert base13 to tridecimal
def tridecimal_expansion(n_str):
    n_str = n_str.replace('A','+')#replaces A's with +'s
    n_str = n_str.replace('B','-')#replaces B's with -'s
    n_str = n_str.replace('C','.')#replaces C's with .'s
    return n_str #returns new tridecimal string
#function to convert tridecimal string to conway float
def tridecimal_to_conway(n_str):
    a=0#initializes variable to 0
    #finds the index of the last + or -
    for i, ch in enumerate(n_str):
        if ch == '+' or ch == '-':
            a = i 
    b = n_str.rfind('.')#finds index of last .
    #returns 0 if index of last - or + is after index of last . 
    if a>b:
        return 0
    #trys to return conway float, returns 0 if ValueError
    else:
        try: 
            return float(n_str[a:])
        except ValueError:
            return 0
#Function to convert float to zeta    
def zeta(n):
    #returns None if input is not positive
    if n<=0:
        return None
    #else loops contains code for positive floats input
    else: 
        #initializes variables
        term = 0.0
        term_l = 1.0
        sum = 1.0
        c = 2
        #loops until difference of current term and last term is less than delta
        while abs(term_l-term) >= DELTA:
            sum += 1/((c)**n) #adds current term to sum
            term = 1/((c)**n) #changes current term
            c+=1 # increases count
            term_l = 1/((c)**n) #changes last term
        return sum #returns sum after loops exited
#main function which has all inputs and outputs
def main():
    # by convention "main" doesn't need a docstring
    print("Functions") #opening statement
    #prompts for z, c or q, loops until valid input
    answer = input('Enter Z for Zeta, C for Conway, Q to quit: ').lower()
    while answer != 'z' and answer != 'c' and answer != 'q':
        print("Error in input.  Please try again.")
        answer = input('Enter Z for Zeta, C for Conway, Q to quit: ').lower()
    #while loop loops unless user qants to quit
    while answer != 'q':
        #user inputs z
        if answer == 'z':
            print('Zeta') #Zeta opening statement
            #prompts for float, loops until valid input
            num = input("Input a number: ")
            d = 0
            while d ==0:
                try:
                    float(num)
                    d= 1
                except ValueError:
                    print("Error in input.  Please try again.")
                    num = input("Input a number: ")
            print(zeta(float(num)))#referenes zeta function and printszeta value
       #user inputs c
        if answer == 'c':
            print('Conway') #Conway opening statement
            #prompts for positive integer, loops until valid input
            pos_int = input("Input a positive integer: ")
            while not pos_int.isdigit():
                print("Error in input.  Please try again.")
                pos_int = input("Input a positive integer: ")
            #references base13 function and converts pos int to base 13 and prints
            conway = int_to_base13(int(pos_int))
            print("Base 13:",conway)
            #references tridecimal function and converts base13 to tridecimal and prints
            conway = tridecimal_expansion(conway)
            print("Tridecimal:",conway)
            #references conway function and converts tridecimal to conway and prints
            conway = tridecimal_to_conway(conway)
            print("Conway float:",conway)
            
            
        answer = input('Enter Z for Zeta, C for Conway, Q to quit: ').lower()#prompts for user to continue with another calculation or quit
    
    # your code goes here    
    print("\nThank you for playing.")#closing statement
        
# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main()
        
    