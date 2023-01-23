using System;

namespace std
{
    class Program
    {
        static void Main() { 

            float a = 5f, b = 10f;

            // CONSTANST

            Console.WriteLine(Math.E);// 2.7182
            Console.WriteLine(Math.PI);// 3.1415...
            Console.WriteLine(Math.Tau);// 6.28...

            // TRIGONOMETRY

            Console.WriteLine(Math.Sin(a));
            Console.WriteLine(Math.Cos(a));
            Console.WriteLine(Math.Tan(a));
            Console.WriteLine(Math.Sinh(a));
            Console.WriteLine(Math.Cosh(a));
            Console.WriteLine(Math.Tanh(a));
            Console.WriteLine(Math.SinCos(a));

            // BASIC ARIFMETHIC ACTIONS

            Console.WriteLine(Math.Min(a, b));
            Console.WriteLine(Math.Max(a, b));
            Console.WriteLine(Math.Pow(a, b));
            Console.WriteLine(Math.Abs(a));
            Console.WriteLine(Math.Sqrt(a));
            Console.WriteLine(Math.Ceiling(a));
            Console.WriteLine(Math.Floor(a));
            Console.WriteLine(Math.Round(a));

            // ALGEBRIA

            Console.WriteLine(Math.Log(a));
            Console.WriteLine(Math.Log10(a));
            Console.WriteLine(Math.Exp(a));
            Console.WriteLine(Math.Truncate(a));

            ////////////////////////////////////////////
            Console.ReadKey();
        }
    }
}
