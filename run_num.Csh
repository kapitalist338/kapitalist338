using System;

namespace std
{
    class Program
    {
        static void Main()
        {
            int end = 10;
            int user_input;
            bool is_true = true;

            while (is_true)
            {
                Random ran_num = new Random();
                int rundom = ran_num.Next(end);

                Console.WriteLine("I guessed a random number from 1 to 10.");
                Console.Write("Enter number(0 - 10): ");
                user_input = Convert.ToInt32(Console.ReadLine());

                if (user_input == rundom)
                {
                    Console.WriteLine("Ok youre win: {0}", rundom);
                }

                else
                {
                    Console.WriteLine("oh no you lose: {0}", rundom);
                }
            }

            Console.ReadKey();
        }
    }
}
