# Deep Dive into Web 3.0
## Pranshu Gaur - 200703
The recruitment task involved building a Lender-Borrower System using Object Oriented Programming system.


## Assignment 1 
  Write a code which takes a string and outputs the smallest nonce value which when appended to the string produces the SHA256 hash less than the target i.e. '0x00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'

  The language chosen for the program is python.

  The code accepts a string as input and iterates over positive integers until an integer is found that, when appended to the string, produces a hash that is less than the target.

  The execution time until the nonce value is found has been printed as well.

      Example:
          For the input string 'IITK', the output of the code is :
            The smallest nonce is : 14
            The time taken by the program to get the nonce value is : 1.5564820766448975 seconds

          Note: The time taken is according to the VS Code Terminal in my system.


## Assignment 2
  Implemented the Loan contract by using the template provided.
  Used `mulDiv` function by referring to the link given in the template. Calculated upto 18 digits after the decimal and returned the integer rounded of to the nearest integer. Checked the first digit, if it was greater than or equal to 5, the value was incremented by 1 and then returned.
  
  ### Functions in the Contract :
  
  - **reqLoan** : Can be used by anyone except the Owner to request back the Loan.
  - **settleDues** : Can only be used by the Owner to return the Loan requested by the Creditor.
  - **getCompoundInterest** : Can be used by anyone to calculate the total amount on the principal value according to the rate and time compounded anually.
  - **getOwnerBalance** : Can be used by anyone to check the current balance of the Owner after many (or no) transactions.
  - **viewDues** : Can only be used by the Owner to check the amount Due at each account.
  
  #### Functions not modified :
  - **sendCoin** : Used to send money from one account to another keeping in my mind the current balance of payer.
  - **getBalance** : Used to check the balance of each account.
  
  #### Functions not visible :
  - **mulDiv** : This function is not visible, it is used to perform the multiplication and division task efficiently.
  
  ### How does the contract work ?
  
  There are many Creditors and one Owner, the Owner has an initial balance of 100K MetaCoins accumulated by taking Loans from the Creditors. \
  First the Creditor checks the available balance of the Owner through the `getOwnerBalance` function, then the Creditor can request the Owner to payback the Loan with any interest rate R in T years. He can use the `getCompoundInterest` function to calculate the total amount that is compounded. He then requests the Loan through the function `reqLoan` and puts in the required values. 
  
  Now comes the role of the Owner, he first checks if he needs to pay any dues through the `viewDues` function and then settles his dues through the `settleDues` function. He can now check his updated balance through the `getOwnerBalance` function and check the dues of that particular account through the `viewDues` function to see if the transaction has happened successfully or not.
  
