import java.lang.Math;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {

        Scanner scan_for_num1 = new Scanner(System.in);
        Scanner scan_for_num2 = new Scanner(System.in);
        double x = scan_for_num1.nextDouble();
        double y = scan_for_num2.nextDouble();
        Basic_math(x, y);
        non_Basic_Math(x, y);
        Trigonometry(x, y);
        constants();
        factorial(6);
    }

    public static void Basic_math(double in1, double in2){
        System.out.println(in1 + in2);
        System.out.println(in1 - in2);
        System.out.println(in1 * in2);
        System.out.println(in1 / in2);
        System.out.println(in1 % in2);
    }

    public static void non_Basic_Math(double in1, double in2){
        System.out.println(Math.min(in1, in2));
        System.out.println(Math.max(in1, in2));
        System.out.println(Math.pow(in1, in2));
        System.out.println(Math.sqrt(in1));
        System.out.println(Math.floor(in1));
        System.out.println(Math.abs(in1));
        System.out.println(Math.ceil(in1));
        System.out.println(Math.round(in1));
    }

    public static void Trigonometry(double in1, double in2){
        System.out.println(Math.sin(in1));
        System.out.println(Math.sinh(in1));
        System.out.println(Math.cos(in1));
        System.out.println(Math.cosh(in1));
        System.out.println(Math.tan(in1));
        System.out.println(Math.tanh(in1));
    }

    public static void constants(){
        System.out.println(Math.PI);
        System.out.println(Math.E);
        System.out.println(Math.TAU);
    }
    public static void factorial(double factor){
        int i,fact=1;
        
        for(i=1;i<=factor;i++){
            fact=fact*i;
        }
        System.out.println("Factorial of "+factor+" is: "+fact);
    }

}
