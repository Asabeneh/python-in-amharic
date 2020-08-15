# Python in Amharic

## What is programming

- Write a short description of programming
- List down some of the importance of python programming language
- What version of python are you currently using? 
- What code editor are you using?
- What is the python interactive shell?
- How do you open the python interactive shell and how do you close it?
- What is the extension of the python script file?

## Comments

- What is the use of a comment in programming
- Write a single line python comment
- Write a multiline python comment

## Data types

- List all the data types you know and give one example for each data types
  
## Variables

- Declare a variable of all data types
- Check the type of your variables using type
  
## Operations

### Getting user input

Write a small script that can calculate the age of a person. The program asks the user to enter birth year and the current year.

```sh
Enter your birth year: 1950
Enter the current year: 2020
You are 70 years old.
```

Write a small script that can calculate the weight of an object on earth. The program asks user to enter mass and calculate the weight.

```sh
Enter your weight: 100
Your weight is 98.1 N.
```

### Strings

- Concatenate the string 'Python', 'For','Everyone' to a single string, 'Python for Everyone'
- Concatenate the string 'Coding', 'For', 'All' to a single string, 'Coding For All'
- Declare a variable name company and assign it to an initial value "Coding For All".
- Print company using print()
- Print the length of the company string using len() method and print()
- Change all the string to capital letters using upper() method
- Change all the string to lowercase letters using lower() method
- Use capitalize(),title(), swapcase() methods to format the value stored in the variable name company
- Slice out the first word of the company string
- Check if the string contains a word Coding using the method index or other methods.
- Replace the word coding in the string 'Coding For All' to Python using replace or other methods.
- Change Python for Everyone to Python for All using the replace method or other methods
- Split the string 'Coding For All' at the space using split() method
- "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma
- What is character at index 10 in "Coding For All"
- Create an acronym or an abbreviation for the name 'Python For Everyone'
- Create an acronym or an abbreviation for the name 'Coding For All'
- Use index to determine the position of the first occurrence of C in Coding For All
- Use index to determine the position of the first occurrence of F in Coding For All
- Use rfind to determine the position of the last occurrence of l in Coding For All People.
- Use index or find to find the position of the first occurrence of the word because in the following sentence:'You cannot end a sentence with because because because is a conjunction'
- Use rindex to find the position of the last occurrence of the word because in the following sentence:'You cannot end a sentence with because because because is a conjunction'
- Slice out the phase because because because in the following sentence:'You cannot end a sentence with because because because is a conjunction'
- Use search to find the position of the first occurrence of the word because in the following sentence:'You cannot end a sentence with because because because is a conjunction'
- Slice out the phase because because because in the following sentence:'You cannot end a sentence with because because because is a conjunction'
- Use trim() to remove if there is trailing whitespace at the beginning and the end of a string.E.g " Coding For All ".
- Use startswith() method with the string Coding For All make the result true
- Use endswith() method with the string Python for Everyone make the result true

## Conditionals

- Get user input using input(“Enter your age:”). If the user is 18 or older, give feedback: You are old enough to drive but if not 18 give feedback to wait for the years he supposed to wait for.
  
```py
    Enter your age: 30
    You are old enough to drive.
    Enter your age:15
    You are left with 3 years to drive.
```

- Compare the values of myAge and yourAge using if … else. Based on the comparison log to console who is older (me or you). Use prompt(“Enter your age:”) to get the age as input.

    Enter your age: 30
    You are 5 years older than me.

- If a is greater than b return a is greater than b else a is less than b. Output: sh let a = 4; let b = 3; 4 is greater than 3

    Write a code which give grade students according to theirs scores:
        80-100, A
        70-89, B
        60-69, C
        50-59, D
        0 -49, F

- Check if the season is Autumn, Winter, Spring, or Summer. If the user input is:

    September, October or November, the season is Autumn.
    December, January or February, the season is Winter.
    March, April or May, the season is Spring
    June, July or August, the season is Summer

## Loops

- Iterate 0 to 10 using for loop, do the same using while and do while loop.
Iterate 10 to 0 using for loop, do the same using while and do while loop.
Write a loop that makes seven calls to print() to output the following triangle:

```py
    #
    ##
    ###
    ####
    #####
    ######
    #######
```

- Use nested loops to create the following:

```sh
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
```

- Iterate the list, ['Python', 'Numpy','Pandas','Data Science', AI','ML'] using a for loop and print out the items.
- Use for loop to iterate from 0 to 100 and print only even numbers
- Use for loop to iterate from 0 to 100 and print only odd numbers
- Use for loop to iterate from 0 to 100 and print and print the sum of all numbers.
 The sum of all numbers is 5050.
- Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
 The sum of all evens is 2550. And the sum of all odds is 2500.

## Lists

- Declare an empty list;
- Declare a list with more than 5 number of items
- Find the length of your list
- Get the first item, the middle item and the last item of the list
- Declare a list called mixed_data_types,put different data types and in your array and the array size should be greater than 5
- Declare a list variable name it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
- Print the list using print()
- Print the number of companies in the list
- Print the first, middle and last company
- Print out each company
- Change companies to uppercase and print them out
- Print the list like a sentence: Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon are big IT companies.
- Check if a certain company exists in the itcompanies list. If it exist return the company else return a company is _not found.
- Filter out companies which have more than one 'o' without the filter method
- Sort the array using sort() method
- Reverse the array without method
- Reverse the array using method
- Slice out the first 3 companies from the list
- Slice out the last 3 companies from the list
- Slice out the middle IT company or companies from the list
- Remove the first IT company from the array
- Remove the middle IT company or companies from the list
- Remove the last IT company from the list
- Remove all IT companies

## Functions

- Declare a function full_name and it prints out your full name.

- Declare a function full_name and now it takes firstName, lastName as a parameter and it returns your full - name.

- Declare a function add_two_numbers and it takes two parameters and it returns the sum.

- An area of a rectangle is calculated as follows: area = length x width. Write a function that calculates area_of_rectangle.

- A perimeter of a rectangle is calculated as follows: perimeter= 2x(length + width). Write a function which calculates perimeter_of_rectangle.

- Area of a circle is calculated as follows: area = π x r x r. Write a function which calculates area_of_circle

- Density of a substance is calculated as follows:density= mass/volume. Write a function that calculates density.

- Weight of a substance is calculated as follows: weight = mass x gravity. Write a function that calculates weight.

- Temperature in oC can be converted to oF using this formula: oF = (oC x 9/5) + 32. Write a function which converst oC to oF convert_celcius_to_fahrenheit.

- Body mass index(BMI) is calculated as follows: bmi = weight in Kg / (height x height) in m2. Write a function that calculates bmi. BMI is used to broadly define different weight groups in adults 20 years old or older.Check if a person is underweight, normal, overweight or obsese based the information given below.

The same groups apply to both men and women.
Underweight: BMI is less than 18.5
Normal weight: BMI is 18.5 to 24.9
Overweight: BMI is 25 to 29.9
Obese: BMI is 30 or more

- Write a function called check-season, it takes a month parameter and returns the season:Autumn, Winter, Spring or Summer.

- Quadratic equation is calculated as follows: ax2 + bx + c = 0. Write a function that calculates value or values of a quadratic equation, solve_quadratic_equation.

- Declare a function name _print_list. It takes list as a parameter and it prints out each element of the list.

- Declare a function name swap_values. This function swaps the value of x to y.

```py
    swap_values(3, 4) # x => 4, y=>3
    swap_values(4, 5) # x = 5, y = 4
```

- Declare a function name reverse_list. It takes a list as a parameter and it returns the reverse of the array (don't’ use method).

```py
    pirnt(reverseArray([1, 2, 3, 4, 5]))
    [5, 4, 3, 2, 1]
    print(reverseArray(["A", "B", "C"]))
    ["C", "B", "A"]
```

- Declare a function name capitalize_list_items. It takes a list as a parameter and it returns the capitalized list of the elements

- Declare a function name _add_item. It takes an item parameter and it returns a list after adding the element

- Declare a function name remove_tem. It takes an index parameter and it returns a list after removing an element

- Declare a function name sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

- Declare a function name sum_of_odds. It takes a number parameter and it adds all the odd numbers in that - range.

- Declare a function name sum_of_even. It takes a number parameter and it adds all the even numbers in that range.

- Declare a function name evens_and_odds . It takes a positive integer as a parameter and it counts the number of evens and odds in the number.

```py
    print(evens_and_odds(100))
    The number of odds are 50.
    he number of evens are 51.
```

- Write a function which takes any number of arguments and return the sum of the arguments

sum_all_numbers(1, 2, 3) // -> 6
sum_all_numbers(1, 2, 3, 4) // -> 10
Writ a function which generates a random_user_id.

- Declare a function name user_id_gen. When this function is called it generates seven-character id. The function returns the id.

```sh
    print(user_id_gen());
    41XTDbE
```

- Modify the question number above. Declare a function name user_id_gen_by_user. It doesn’t take any parameter but it takes two inputs using input(). One of the input is the number of characters and the second input is the number of ids that are supposed to be generated.

```sh
user_id_gen_by_user()
"kcsy2
SMFYb
bWmeq
ZXOYh
2Rgxf
"
user_id_gen_by_user()
"1GCSgPLMaBAVQZ26
YD7eFwNQKNs7qXaT
ycArC5yrRupyG00S
UbGxOFI7UXSWAyKN
dIV0SSUTgAdKwStr
"
```

- Call your function _shuffle_list, it takes a list as a parameter and it returns a shuffled list

- Call your function factorial, it takes a whole number as a parameter and it returns a factorial of the number
- Write a function called sum_of_list_items, it takes a list parameter and returns the sum of all the items. Check if all the list items are number types. If not give return reasonable feedback.
- Write a function called average, it takes an array parameter and returns the average of the items. Check if all the array items are number types. If not give return reasonable feedback.
- Write a function called is_prime, which checks if a number is a prime number.
- Write a function that checks if all items are unique in the array.
- Write a function that checks if all the items of the array are the same data type.

- Write a function that returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
  
