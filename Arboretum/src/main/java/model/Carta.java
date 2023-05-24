package model;

import java.util.List;

/**
 *
 * @author estebannajera
 */
public class Carta{

    
    private int id;
    private int posX;
    private int posY;
    private String arbol;
    private int numero;
    private List<Carta> cartasAdyacentes; 

    public Carta() {
    }

    public Carta(int id, String arbol, int numero) {
        this.posX = -1;
        this.posY = -1;
        this.id = id;
        this.arbol = arbol;
        this.numero = numero;
    }

    public Carta(int posX, int posY, int id, String arbol, int numero, List<Carta> cartasAdyacentes) {
        this.posX = posX;
        this.posY = posY;
        this.id = id;
        this.arbol = arbol;
        this.numero = numero;
        this.cartasAdyacentes = cartasAdyacentes;
    }

    public int getPosX() {
        return posX;
    }

    public int getPosY() {
        return posY;
    }

    public void setPosY(int posY) {
        this.posY = posY;
    }

    public void setPosX(int posX) {
        this.posX = posX;
    }

    

    public void setCartasAdyacentes(List<Carta> cartasAdyacentes) {
        this.cartasAdyacentes = cartasAdyacentes;
    }

    public List<Carta> getCartasAdyacentes() {
        return cartasAdyacentes;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setArbol(String arbol) {
        this.arbol = arbol;
    }

    public int getNumero() {
        return numero;
    }

    public int getId() {
        return id;
    }

    public String getArbol() {
        return arbol;
    }
}
