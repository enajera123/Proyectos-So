package model;

import java.util.List;

/**
 *
 * @author estebannajera
 */
public class Partida {

    private String nombre;
    private String clave;
    private List<String> jugadores;

    public Partida() {
    }

    public Partida(String nombre, String clave, List<String> jugadores) {
        this.nombre = nombre;
        this.clave = clave;
        this.jugadores = jugadores;
    }

    public List<String> getJugadores() {
        return jugadores;
    }

    public void setJugadores(List<String> jugadores) {
        this.jugadores = jugadores;
    }

    

    public String getClave() {
        return clave;
    }

    public String getNombre() {
        return nombre;
    }

    public void setClave(String clave) {
        this.clave = clave;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return "nombre: " + nombre + ", clave: " + clave;
    }

}
