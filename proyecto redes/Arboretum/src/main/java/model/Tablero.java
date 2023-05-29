package model;

import java.util.List;

/**
 *
 * @author estebannajera
 */
public class Tablero {

    private String nombre;
    private List<Carta> cartas;

    public Tablero() {
    }

    public Tablero(String nombre, List<Carta> cartas) {
        this.nombre = nombre;
        this.cartas = cartas;
    }

    public List<Carta> getCartas() {
        return cartas;
    }

    public String getNombre() {
        return nombre;
    }

    public void setCartas(List<Carta> cartas) {
        this.cartas = cartas;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

}
