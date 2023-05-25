package model;

import java.util.List;

/**
 *
 * @author estebannajera
 */
public class Partida {

    private String nombre;
    private String clave;
    private List<Jugador> jugadores;
    private Mazo mazo;
    private Jugador jugadorActual;
    private boolean iniciado;
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

    public Partida(String nombre, String clave, List<Jugador> jugadores, Mazo mazo, Jugador jugadorActual, boolean iniciado) {
        this.nombre = nombre;
        this.clave = clave;
        this.jugadores = jugadores;
        this.mazo = mazo;
        this.jugadorActual = jugadorActual;
        this.iniciado = iniciado;
    }

    public Jugador getJugadorActual() {
        return jugadorActual;
    }

    public void setJugadorActual(Jugador jugadorActual) {
        this.jugadorActual = jugadorActual;
    }

    public boolean isIniciado() {
        return iniciado;
    }

    public void setIniciado(boolean iniciado) {
        this.iniciado = iniciado;
    }

    public Partida(String nombre, String clave, List<Jugador> jugadores, Mazo mazo) {
        this.nombre = nombre;
        this.clave = clave;
        this.jugadores = jugadores;
        this.mazo = mazo;
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

    public void setCartaJugador(String nombreJugador, Carta carta) {
        for (Jugador j : jugadores) {
            if (j.getNombre().equals(nombreJugador)) {
                j.getCartas().add(carta);
            }
        }
    }

}
