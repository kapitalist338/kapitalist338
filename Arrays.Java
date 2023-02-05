import java.util.ArrayList;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) {

        ArrayList<Float> dyn_arr = new ArrayList<> (3);

        dyn_arr.add(3.76f);

        dyn_arr.add(4.76f);

        dyn_arr.add(5.76f);

        dyn_arr.add(6.76f);

        dyn_arr.add(7.76f);

        dyn_arr.add(8.76f);

        for(Float i : dyn_arr)
            System.out.println(i);

        //yn_arr.clear();


        dyn_arr.remove(1);

        for(Float i : dyn_arr)
            System.out.println(i);




        LinkedList<String> names = new LinkedList<>();

        names.add("Dean Winchester");
        names.add("Sam Winchester");
        names.add("Castiel");
        names.add("Bobby Singer");
        names.add("James");

        names.add(4 , "John Winchester");

        names.set(5, "Ruby");


        for(String name : names)
            System.out.println("\n\n\n\n" + name);


    }
}
