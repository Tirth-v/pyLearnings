# Scope :

"""
    A variable is only available from inside the region it is created.\
    this is called Scope.
    
   =>  Scope has two types :
        1. Local scope
        2. Global scope

        
    1. Local scope :
        - A variable created inside a function belongs to the local 
          scope of that function, and can only be used inside
          that function.

          def myFunc():
            x = 10
            print(x)
          
          myFunc()

          => Function inside function :
            - in the above x is not accessed outside
              the function but it is availabe for any function
              inside the function.

             def myfunc():
                x = 300
                def myinnerfunc():
                    print(x)
                myinnerfunc()

             myfunc() 


    2. Global scope : as explained in variables file.         

"""