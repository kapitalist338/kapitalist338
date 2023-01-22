using System;
// my neural network with one neuron

namespace std
{
    class Program
    {
        public class Neuron
        {
            private decimal weights = 0.5m;
            public decimal Last_Error { get; private set; }
            public decimal Smoothing { get; set; } = 0.00001m;

            public decimal InputWeights(decimal Input)
            {
                return Input * weights;
            }

            public decimal Restore_input_data(decimal Out)
            {
                return Out / weights;
            }

            public void Train(decimal Input, decimal Expected_Res)
            {
                var Actual_Result = Input * weights;
                Last_Error = Expected_Res - Actual_Result;
                var correction = (Last_Error / Actual_Result) * Smoothing;
                weights += correction;

            }
        }

        static void Main()
        {
            decimal km = 100;
            decimal miles = 62.1371m;

            Neuron neuron = new Neuron();

            int i = 0;
            do {
                i++;
                neuron.Train(km, miles);

                Console.WriteLine($"interation {i}\t error:\t {neuron.Last_Error}");
            } while (neuron.Last_Error > neuron.Smoothing || neuron.Last_Error < -neuron.Smoothing);

            Console.WriteLine("I end my training! :>");

            // Console.WriteLine($"{neuron.InputWeights(km)} miles in {100} km!");
            Console.WriteLine($"{neuron.InputWeights(200)} miles in {200}");
            Console.WriteLine($"{neuron.InputWeights(671)} miles in {671}");
            Console.WriteLine($"{neuron.InputWeights(356)} miles in {356}");

            Console.WriteLine($"{neuron.Restore_input_data(175)} km in {175} miles");
            Console.ReadKey();
        }
    }
}
