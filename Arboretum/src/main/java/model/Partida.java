package model;

import java.util.List;

/**
 *
 * @author estebannajera
 */

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

public class Partida {

    private String nombre;
    private String clave;
    private List<Jugador> jugadores;
    private List<String> arboles;
    private Mazo mazo;
    private boolean iniciado;
    private Jugador jugadorActual;
    //  private List<String> tableros;
    //private List<String> mazo;
    //private List<String> barajas;

    /*
    self.tableros = [] #Cuando se crea el tablero se le da un nombre el del jugador asi se identifican facil
        self.mazos = [] #Tambien se les da un nombre para idenficarlos mas facil puede ser el del jugador tambien
        self.barajas = [] #Tambien se les da un nombre para idenficarlos mas facil puede ser el del jugador tambien
     */
    public Partida() {
    }
    @JsonCreator
    public Partida(
        @JsonProperty("nombre") String nombre, 
        @JsonProperty("clave") String clave, 
        @JsonProperty("jugadores") List<Jugador> jugadores, 
        @JsonProperty("mazo") Mazo mazo, 
        @JsonProperty("iniciado") boolean iniciado, 
        @JsonProperty("arboles") List<String> arboles,
        @JsonProperty("jugadorActual") Jugador jugadorActual
    ) {
        this.nombre = nombre;
        this.clave = clave;
        this.jugadores = jugadores;
        this.arboles = arboles;
        this.mazo = mazo;
        this.iniciado = iniciado;
        this.jugadorActual = jugadorActual;
    }

    public boolean isIniciado() {
        return iniciado;
    }

    public void setIniciado(boolean iniciado) {
        this.iniciado = iniciado;
    }

    public Partida(String nombre, String clave, List<Jugador> jugadores, Mazo mazo, List<String> arboles) {
        this.nombre = nombre;
        this.clave = clave;
        this.mazo = mazo;
        this.jugadores = jugadores;
        this.arboles = arboles;
    }

    public void setMazo(Mazo mazo) {
        this.mazo = mazo;
    }

    public Mazo getMazo() {
        return mazo;
    }

    public List<Jugador> getJugadores() {
        return jugadores;
    }

    public void setJugadores(List<Jugador> jugadores) {
        this.jugadores = jugadores;
    }

//    public List<String> getBarajas() {
//        return barajas;
//    }
//
//    public List<String> getMazos() {
//        return mazos;
//    }
//
//    public List<String> getTableros() {
//        return tableros;
//    }
//
//    public void setBarajas(List<String> barajas) {
//        this.barajas = barajas;
//    }
//
//    public void setMazos(List<String> mazos) {
//        this.mazos = mazos;
//    }
//
//    public void setTableros(List<String> tableros) {
//        this.tableros = tableros;
//    }
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

    public void actualizarJugador(Jugador jugador) {
        for (Jugador j : jugadores) {
            if (j.getNombre() == jugador.getNombre()) {
                j = jugador;
                return;
            }
        }
    }
    public void setCartaJugador(String nombreJugador, Carta carta){
        for(Jugador j: jugadores){
            if(j.getNombre().equals(nombreJugador)){
                j.getCartas().add(carta);
            }
        }
    }

}
