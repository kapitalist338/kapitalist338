import javax.swing.JFrame;
import javax.swing.ImageIcon;
import java.awt.*;


public class Main {
    public static void main(String[] args) {

        JFrame window = new JFrame();

        window.setSize(300, 350);

        window.setTitle("Flagshtok Kun");

        window.setResizable(false);

        window.setVisible(true);

        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        ImageIcon icon = new ImageIcon("logo.png");

        window.setIconImage(icon.getImage()); // only in Windows OS

        window.getContentPane().setBackground(Color.BLACK);
        // or window.getContentPane().setBackground(new Color(0,0,0));

        

    }
}
