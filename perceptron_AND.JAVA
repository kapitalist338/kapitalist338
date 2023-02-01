public class Main {
    public static void main(String[] args) {

        for(int i = 0; i < 4; i++){
            double x1 = i/2;
            double x2 = i%2;

            double out = AND(x1, x2);

            System.out.printf("%d%d\t%d\n", (int)x1, (int)x2, (int)out);
        }

    }

    static double neuron(double[] x, double[] w, double b){
        double z = 0;

        int i = 0;
        while(i < x.length){

            z += x[i] * w[i];

            i++;
        }

        z += b;

        return z > 0 ? 1: 0;
    }

    static double AND(double x1, double x2){

        return neuron(new double[]{x1, x2}, new double[] {1, 1}, -1);
    }
}
