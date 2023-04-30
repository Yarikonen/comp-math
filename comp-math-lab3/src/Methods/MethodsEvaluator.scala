package Methods

import scala.annotation.tailrec


class MethodsEvaluator(shit: Double, a:Double, b:Double){


  
  def squareMethod(f: Double => Double, step: Double = 0, n: Int=5,a: Double=this.a,b: Double=this.b): Double=
    @tailrec
    def internalSquareMethod(summ: Double=0, i: Int=0): Double=
      if i==n then summ else internalSquareMethod(summ+f(a+(i+step)*((b-a)/n))*((b-a)/n),i+1)
    internalSquareMethod()
  def trapezoidMethod(f: Double => Double, n: Int=5): Double=
    @tailrec
    def internalTrapezoidMethod(summ: Double=0, i: Int=0): Double =
      if i==n then summ else internalTrapezoidMethod(summ+(f(a+i*((b-a)/n))+f(a+(i+1)*(b-a)/n))*((b-a)/(2*n)),i+1)
    internalTrapezoidMethod()
  def simpsonMethod(f: Double => Double,n: Int=5): Double =
    @tailrec
    def internalSimpsonMethod(summ: Double=(f(a)*(b-a))/(3*n), i:Int=1): Double =
      if i==n then summ+(f(b)*(b-a))/(3*n) else internalSimpsonMethod(summ+((2*(i%2+1))*f(a+i*((b-a)/n)))*((b-a)/(3*n)),i+1)
    internalSimpsonMethod()

}

