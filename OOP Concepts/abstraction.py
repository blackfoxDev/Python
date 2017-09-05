class Person:
       def __init__(self,first,last,id,email):

            self.firstName=first
            self.lastName=last
            self.id=id
            self.email=email
            self.friends=[]

        def add_friend(self,friend):
            if len(self.friends)<10 and len(friend.friends)<10:
               self.friends.append(friend)
               friend.friends.append(self)

      # main
      p1 =Person("David","Wolber","922-43-9873","wolber@usfca.edu")             
      p2 =Person("Bob","Jones","902-38-9973","jones@usfca.edu") 
      p1.add_friend(p2)
