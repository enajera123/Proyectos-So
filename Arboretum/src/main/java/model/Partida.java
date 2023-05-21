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
    private List<String> tableros;
    private List<String> mazos;
    private List<String> barajas;
    
    /*
    self.tableros = [] #Cuando se crea el tablero se le da un nombre el del jugador asi se identifican facil
        self.mazos = [] #Tambien se les da un nombre para idenficarlos mas facil puede ser el del jugador tambien
        self.barajas = [] #Tambien se les da un nombre para idenficarlos mas facil puede ser el del jugador tambien
    */

    public Partida() {
    }

    public Partida(String nombre, String clave, List<String> jugadores) {
        this.nombre = nombre;
        this.clave = clave;
        this.jugadores = jugadores;
    }

    public List<String> getBarajas() {
        return barajas;
    }

    public List<String> getMazos() {
        return mazos;
    }

    public List<String> getTableros() {
        return tableros;
    }

    public void setBarajas(List<String> barajas) {
        this.barajas = barajas;
    }

    public void setMazos(List<String> mazos) {
        this.mazos = mazos;
    }

    public void setTableros(List<String> tableros) {
        this.tableros = tableros;
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
