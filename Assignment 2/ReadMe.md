
## Assignment 2
  Implemented the Loan contract by using the template provided.
  Used `mulDiv` function by referring to the link given in the template. Calculated upto 18 digits after the decimal and returned the integer rounded of to the nearest integer. Checked the first digit, if it was greater than or equal to 5, the value was incremented by 1 and then returned.
  
  ### Functions in the Contract :
  
  - **reqLoan** : Can be used by anyone except the Owner to request back the Loan.
  - **settleDues** : Can only be used by the Owner to return the Loan requested by the Creditor.
  - **getCompoundInterest** : Can be used by anyone to calculate the total amount on the principle value according to the rate and time compounded anually.
  - **getOwnerBalance** : Can be used by anyone to check the current balance of the Owner after many (or no) transactions.
  - **viewDues** : Can only be used by the Owner to check the amount Due at each account.
  
  #### Functions not modified :
  - **sendCoin** : Used to send money from one account to another keeping in my mind the current balance of payer.
  - **getBalance** : Used to check the balance of each account.
  
  #### Functions not visible :
  - **mulDiv** : This function is not visible, it is used to perform the multiplication and division task efficiently.
  
  ## How does the contract work ?
  
  There are many Creditors and one Owner, the Owner has an initial balance of 100K MetaCoins accumulated by taking Loans from the Creditors. \
  First the Creditor checks the available balance of the Owner through the `getOwnerBalance` function, then the Creditor can request the Owner to payback the Loan with any interest rate R in T years. He can use the `getCompoundInterest` function to calculate the total amount that is compounded. He then requests the Loan through the function `reqLoan` and puts in the required values. \
  
  Now comes the role of the Owner, he first checks if he needs to pay any dues through the `viewDues` function and then settles his dues through the `settleDues` function. He can now check his Balance through the `getOwnerBalance` function and check the dues of that particular account through the `viewDues` function to see if the transaction has happened successfully or not.
  
