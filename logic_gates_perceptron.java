public class Main {
    public static void main(String[] args) {
        System.out.println("And");
        for(int i = 0; i < 4; i++){
            double input1 = i / 2;
            double input2 = i % 2;

            double OUTPUT = AND(input1, input2);
            System.out.printf("%d%d\t%d\n", (int)input1,(int)input2,(int)OUTPUT);
        }

        System.out.println("\nOR");
        for(int i = 0; i < 4; i++){
            double input1 = i / 2;
            double input2 = i % 2;

            double OUTPUT = OR(input1, input2);
            System.out.printf("%d%d\t%d\n", (int)input1,(int)input2,(int)OUTPUT);
        }

        System.out.println("\nNAND");
        for(int i = 0; i < 4; i++){
            double input1 = i / 2;
            double input2 = i % 2;

            double OUTPUT = NAND(input1, input2);
            System.out.printf("%d%d\t%d\n", (int)input1,(int)input2,(int)OUTPUT);
        }
        System.out.println("\nNOR");
        for(int i = 0; i < 4; i++){
            double input1 = i / 2;
            double input2 = i % 2;

            double OUTPUT = NOR(input1, input2);
            System.out.printf("%d%d\t%d\n", (int)input1,(int)input2,(int)OUTPUT);
        }

        System.out.println("\nXOR");
        for(int i = 0; i < 4; i++){
            double input1 = i / 2;
            double input2 = i % 2;

            double OUTPUT = XOR(input1, input2);
            System.out.printf("%d%d\t%d\n", (int)input1,(int)input2,(int)OUTPUT);
        }

        System.out.println("\nXNOR");
        for(int i = 0; i < 4; i++){
            double input1 = i / 2;
            double input2 = i % 2;

            double OUTPUT = XNOR(input1, input2);
            System.out.printf("%d%d\t%d\n", (int)input1,(int)input2,(int)OUTPUT);
        }
    }

    static double Neuron(double[] x, double[] w,double B){
        double Z = 0.0d;

        for(int i = 0; i < x.length; i++)
            Z += x[i] * w[i];

        Z+=B;

        double a = Z > 0? 1: 0;

        return a;
    }

    static double AND(double input1, double input2){

        return Neuron(new double[] {input1, input2}, new double[] {1, 1}, -1);
    }
    static double OR(double input1, double input2){

        return Neuron(new double[] {input1, input2}, new double[] {1, 1}, 0);
    }
    static double NAND(double input1, double input2){

        return Neuron(new double[] {input1, input2}, new double[] {-1, -1}, 2);
    }
    static double NOR(double input1, double input2){

        return Neuron(new double[] {input1, input2}, new double[] {-1, -1}, 1);
    }
    static double XOR(double input1, double input2){

        return AND(OR(input1, input2), NAND(input1, input2));
    }
    static double XNOR(double input1, double input2){

        return OR(AND(input1, input2), NOR(input1, input2));
    }
}
