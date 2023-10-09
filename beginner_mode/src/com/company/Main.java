/*import java.util.Scanner;
public class Main{
  public static void main(String[] args){
    Scanner scanner = new Scanner(System.in);
    System.out.println("Enter the radius of the circle");
    double radius = scanner.nextDouble();
    double circleArea = Math.PI * Math.pow(radius,2);
    System.out.println("The are of the circle is " + circleArea + "cm^2");
  }
}
*/

import java.util.Scanner;
public class Main{
  public static void main(String[] args){
    Scanner scanner = new Scanner(System.in);

    System.out.println("Enter the radius of the circle: ");
    double radius = scanner.nextInt();
    double PI = 3.1428;

    double circleArea = PI * Math.pow(radius, 2);

    System.out.println("The area of the circle is: " + circleArea);

  }
}

