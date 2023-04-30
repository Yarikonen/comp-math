package IO
import scala.io.StdIn.{readDouble, readInt,readLine}
import Methods.functionContainer
class IOHandler {
  println("Welcome to scala comp-math lab 3")
  println("--------------------------------")
  println("--------------------------------")
  println("--------------------------------")
  def getFunction: Double=>Double= {
    println("Please choose one of the functions")
    println("1. x^3 + x^2 + cos(x)")
    println("2. |sin(x)|*|x|")
    println("3. e^(-x^2)")

    try
      functionContainer.getFunctionByIndex(readInt()-1)
    catch
      case ex:IndexOutOfBoundsException =>
        println("Wrong index function")
        getFunction
      case ex: NumberFormatException =>
        println("Index must be integer from 1 to 3")
        getFunction
  }
  def getMethod: Int = {
    println("Please choose your method")
    println("1. Square Method")
    println("2. Trapezoid Method")
    println("3. Simpson Method")
    try
      val index = readInt()
      index
    catch
      case ex: NumberFormatException =>
        println("Index must be integer from 1 to 3")
        getMethod
  }
  def concreteSquare: Double = {
    val list = List(0,1,0.5)
    println("Please concretize what square method to use")
    println("1. Left-square")
    println("2. Right-square")
    println("3. Middle-square")
    try
      val index = readInt()
      list(index-1)
    catch
      case ex: NumberFormatException =>
        println("Index must be integer from 1 to 3")
        concreteSquare
      case ex:IndexOutOfBoundsException =>
        println("Wrong index function")
        concreteSquare

  }
  def border(bord: String): Double = {
    println(s"Enter ${bord} boarder")
    try
      val bord = readDouble()
      bord
    catch
      case ex:NumberFormatException=>
        println("index must be floating-point")
        border(bord)

  }
  def getBorders(): List[Double] = {
    println("Enter borders")
    List(border("left"),border("right"))
  }
  def getAccuracy(): Double = {
    println("enter accuracy")
    val a = readLine()
    a.replace(",",".").toDouble
  }



}
