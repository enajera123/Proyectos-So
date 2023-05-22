package model;

/**
 *
 * @author estebannajera
 */
public class Carta{

//    private int posX;
//    private int posY;

    private int id;
    private String arbol;
    private int numero;
    //private List<Carta> cartasAdyacentes; 

    public Carta() {
    }

    public Carta(int id, String arbol, int numero) {
        this.id = id;
        this.arbol = arbol;
        this.numero = numero;
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
