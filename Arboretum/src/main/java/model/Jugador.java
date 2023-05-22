
package model;

import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author estebannajera
 */
public class Jugador {
   private String nombre;
   private List<Carta> cartas;

    public Jugador() {
    }

    public Jugador(String nombre, List<Carta> cartas) {
        this.nombre = nombre;
        this.cartas = cartas;
    }

    public Jugador(String nombre) {
        this.nombre = nombre;
        this.cartas = new ArrayList<Carta>();
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
