
package model;


import java.util.Stack;

/**
 *
 * @author estebannajera
 */
public class Mazo {
    private String nombre;
    private Stack<Carta> cartas;

    public Mazo() {
    }

    public Mazo(String nombre, Stack<Carta> cartas) {
        this.nombre = nombre;
        this.cartas = cartas;
    }

    public Stack<Carta> getCartas() {
        return cartas;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setCartas(Stack<Carta> cartas) {
        this.cartas = cartas;
    }
    
}
