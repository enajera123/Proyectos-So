
package model;

import java.util.List;

/**
 *
 * @author estebannajera
 */
public class Carta {
    private int posX;
    private int posY;

    public Carta(int posX, int posY) {
        this.posX = posX;
        this.posY = posY;
    }

    public Carta() {
    }

    public int getPosX() {
        return posX;
    }

    public int getPosY() {
        return posY;
    }

    public void setPosX(int posX) {
        this.posX = posX;
    }

    public void setPosY(int posY) {
        this.posY = posY;
    }
    public static boolean buscarCarta(int i, int j, List<Carta>cartas) {
        for (Carta carta : cartas) {
            if (carta.getPosX() == j && carta.getPosY() == i) {
                return true;
            }
        }
        return false;
    }

}
