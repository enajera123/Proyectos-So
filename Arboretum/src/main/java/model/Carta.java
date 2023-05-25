package model;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

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
    public Carta( int id, String arbol, int numero) {
        this.posX = -1;
        this.posY = -1;
        this.id = id;
        this.arbol = arbol;
        this.numero = numero;
    }
    
    @JsonCreator
    public Carta(
            @JsonProperty("posX") int posX, 
            @JsonProperty("posY") int posY,
            @JsonProperty("id") int id, 
            @JsonProperty("arbol") String arbol, 
            @JsonProperty("numero") int numero,
            @JsonProperty("cartasAdyacentes") List<Carta> cartasAdyacentes
    ) {
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
