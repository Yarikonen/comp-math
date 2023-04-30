import Methods.MethodsEvaluator
import Methods.functionContainer
import IO.IOHandler
import scala.math
object Evaluator {
  @main
  def main(args: String*): Unit =
    val io = new IOHandler()
    val f = io.getFunction
    val method = io.getMethod
    val concrete = if method==1 then io.concreteSquare else 0
    val list= io.getBorders()
    val a =list(0)
    val b = list(1)
    val acc= io.getAccuracy()
    val methodsEvaluator = new MethodsEvaluator(acc,a,b)
    val methodd = if method==1 then methodsEvaluator.squareMethod(f,concrete,_)
    else if method==2 then
      methodsEvaluator.trapezoidMethod(f,_)
    else
      methodsEvaluator.simpsonMethod(f,_)

    def recursiveMehodInvocation(n:Int):List[Double]= {
      if!((math.abs((methodd(n)-methodd(n*2))/(2 +2*(method/3)))<acc)||n>=2000) then recursiveMehodInvocation(n*2) else List(methodd(2*n),(methodd(2*n)-methodd(n*4))/(2 +2*(method/3)),2*n)
    }
    val answ = recursiveMehodInvocation(2)
    if(answ(2)>=10000){
      println("N overflow")
    }
    println(s"Your answer ${answ(0)}")
    println(s"Was found with ${math.abs(answ(1))} accuracy")
    println(s"With ${answ(2)} fragments")



}
