public class Main {
    public static void main(String[] args) {

        float[] arr = new float[]{6.78f, 445, 5.8f};

        float sum = summ(arr);
        System.out.println(sum);

        System.out.println(arr[0] + arr[1] + arr[2]);

    }

    public static float summ(float[] arr){
        int summ_arr = 0;

        for(int i = 0; i < arr.length; i++)

            summ_arr += arr[i];


        return summ_arr;

    }
}
