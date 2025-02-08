class SubfieldsInAI():
    def Subfields():
        print("Subfields AI are:")
        items=["Machine Learning", "Nural Network", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        for lists in items:
            print(lists)

class OddEven():   
    def OddEven():
        num=int(input("Enter a number:"))
        if((num%2)==1):
            print("Odd number")
            message="Odd number"
        else:
            print("52452 is Even number")
            message="52452 is Even number"
        return message    

class EligibilityForMarriage():
    def Elegible():
        name=input("Your Gender:")
        age=int(input("Your Age:"))
        if(age<21)=="male":
            print("ELIGIBLE")
            cate="ELIGIBLE"
        elif(age<18)=="female":
            print("ELIGIBLE")
            message="ELIGIBLE"
        else:
            print("NOT ELIGIBLE")
            cate="NOT ELIGIBLE"
        return cate

class FindPercent():
    def percentage():
        print("Findpercent.percentage()")
        Tamil=int(input("Subject1="))
        English=int(input("Subject2="))
        Maths=int(input("Subject3="))
        Social=int(input("Subject4="))
        Science=int(input("Subject5="))
        print()
        total=Tamil+English+Maths+Social+Science
        print("Total Score: ",total)
        percentage = (total/500)*100
        print("Percentage= ",percentage,"%")

class triangle():
    def area():
        Height=int(input("Height="))
        Breadth=int(input("Breadth="))
        print("Area formula =(Height*Breadth)/2")
        Area=(Height*Breadth)/2
        return Area
    
    def perimeter():
        Height1=int(input("Height1="))
        Height2=int(input("Height2="))
        Breadth=int(input("Breadth="))
        print("Perimeter formula=(Height1+Height2+Breadth)")
        Perimeter=(Height1+Height2+Breadth)
        return Perimeter
    
    #call the function and print the result
    
    print("Area of the triangle = ", area())
    print("Perimete of the tringle = ", perimeter())