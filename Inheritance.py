class Animal( ):
    def walk( self ):
        print( "걷는다" )

    def eat( self ):
        print( "먹는다" )

class Human( Animal ):
    def wave( self ):
        print( "손을 흔든다" )

class Dog( Animal ):
    def wag( self ):
        print( "꼬리를 흔든다" )


# 다중 상속
class Person():
    def walk(self):
        print("걷는다")
    def eat(self):
        print("먹는다")

class Student():
    def study(self):
        print("공부한다")

class Me(Person, Student):
    def grow(self):
        print("자란다")