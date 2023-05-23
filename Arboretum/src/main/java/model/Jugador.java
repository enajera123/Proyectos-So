
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
   private Tablero tablero;
   private List<Carta> descartes;

    public Jugador() {
    }

    public Jugador(String nombre, List<Carta> cartas, Tablero tablero, List<Carta> descartes) {
        this.nombre = nombre;
        this.cartas = cartas;
        this.tablero = tablero;
        this.descartes = descartes;
    }

    public List<Carta> getDescartes() {
        return descartes;
    }

    public void setDescartes(List<Carta> descartes) {
        this.descartes = descartes;
    }

    

    public Tablero getTablero() {
        return tablero;
    }

    public void setTablero(Tablero tablero) {
        this.tablero = tablero;
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
