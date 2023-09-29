# Iterator : AN iterator is an object that allows the programmer


"""
    - To iterate a variable you need range of objects on what
      you can iterate.
    - We can iterate list,string,dictionary,tuple
    - We can't iterate int,float,complex,boolean
    - Iterator first points an object then continuously
      sequentially iterates that object or datatype.
    
      eg.   
            list1 = [1,2,3,4,5]
            it = iter(list1)

            print(next(it))
            print(next(it))
            print(next(it))
            print(next(it))
            print(next(it)) 

          -  First we have a list which have some objects
          -  Then we create an iterator, There is a function called
             iter() in which we will have to pass the variable.
          -  That iter() function will return us an object means
             it pointer will reference it and it will return us an object.
          -  Then we call the iterator by printing next(variable) here
             the variable is which we stored our iter().
          -  By doing this it will return an object
          -  After the last index if we still call iterator
             then it will raise an exception.
          -  We can not go back in iterator.

          -  To get rid of this we can put a try and exception
             block.

             list1 = [1,2,3,4,5]
             it = iter(list1)

             while True:
                try:
                    print(next(it))
                except Exception as e:
                    break    
                
            - In simplle terms iterator is used in loops,
              loops uses iterator to go through the sequence of objects inside a variable. 
               

"""



  
