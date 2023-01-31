public class Main {
    public static void main(String[] args) {
      // inputs
        double[] x = {0, 1};
      // weights
        double[] w = {0.5, 0.5};
      // bias
        double B = 0.5d;
        
      // summ
        double sum = 0;

        int i = 0;

        while(i < x.length){

            sum += x[i] * w[i];

            i++;
        }

        sum += B;
        // act.function
        double a = sum > 0 ? 1: 0;

      // output
        System.out.println(a);

    }
}
