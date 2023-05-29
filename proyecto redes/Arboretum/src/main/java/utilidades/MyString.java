package utilidades;

import java.util.Random;

/**
 *
 * @author estebannajera
 */
public class MyString {

    public static String generarClave(int length) {
        String CHARACTERS = /*"ABCDEFGHIJKLMNOPQRSTUVWXYZ*/ "0123456789";
        String password = "";
        Random random = new Random();
        for (int i = 0; i < length; i++) {
            int index = random.nextInt(CHARACTERS.length());
            char c = CHARACTERS.charAt(index);
            password += c;
        }
        return password;
    }
}
