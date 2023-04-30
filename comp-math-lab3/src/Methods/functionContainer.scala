package Methods
import scala.math
object functionContainer{
  private val f1= (x:Double) => math.pow(x,3)+math.pow(x,2)+math.cos(x)
  private val f2 = (x:Double) => math.abs(math.sin(x))*math.abs(x)
  private val f3 = (x:Double)=> math.exp((-math.pow(x,2)))
  private val functionsList = List(f1,f2,f3)
  def getFunctionByIndex(index: Int): Double=>Double=functionsList(index)

}

