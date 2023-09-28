# type casting

"""
    - Type casting is used to convert the datatype of variable
      from one to another
    - By simply writing type of the datatype we want
      to convert a variable and passing the variable name 
      as an argument we can change it's type.

      eg. print(int("10")+int("10"))
          print(10+ float("10"))

          x = 10
          a = float(x)
          b = str(x)
          print(type(x))
          print(type(a))
          print(type(b))

"""

# which types can be converted from which type :

"""
        data type  :  can be converted to

        - int : float,complex,str,bool
        - float : int,complex,str,bool
        - complex : bool,str
        - boolean : int,float,complex,str
        - str : int,float,boolean,complex,list,tuple,set
                (Mostly when it has numeric value, otherwise will throw an error)
        - list : tuple,set(unordered),str
        - tuple : list,set(unordered),str
        - set : list,tuple,str (all in unordered)
        - dict :  list(will create list of keys),
                  tuple(will create tuple of keys),
                  set(will create set of keys),
                  str      


"""
a = {"a":"b"}
print(str(a))