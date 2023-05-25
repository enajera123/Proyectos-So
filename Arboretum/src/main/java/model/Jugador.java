package model;

import java.util.ArrayList;
import java.util.List;
import utilidades.CartaVisual;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

/**
 *
 * @author estebannajera
 */
public class Jugador {
    
    private String nombre;
    private List<Carta> cartas;
    private Tablero tablero;
    private List<Carta> descartes;
    private List<String> arbolesPuntuables;
    
    public Jugador() {
    }
    @JsonCreator
    public Jugador(
        @JsonProperty("nombre")String nombre, 
        @JsonProperty("cartas") List<Carta> cartas,
        @JsonProperty("tablero")Tablero tablero, 
        @JsonProperty("descartes")List<Carta> descartes,
        @JsonProperty("arbolesPuntuables")List<String> arbolesPuntuables
    ) {
        this.nombre = nombre;
        this.cartas = cartas;
        this.tablero = tablero;
        this.descartes = descartes;
        this.arbolesPuntuables = arbolesPuntuables;
    }
    
    public void setArbolesPuntuables(List<String> arbolesPuntuables) {
        this.arbolesPuntuables = arbolesPuntuables;
    }
    
    public List<String> getArbolesPuntuables() {
        return this.arbolesPuntuables;
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
    
    public Carta agregarCartaTablero(int cartaId) {
        for (Carta i : cartas) {
            if (i.getId() == cartaId) {
                cartas.remove(i);
                tablero.getCartas().add(i);
                return i;
            }
        }
        return null;
    }

    public void modificarPosicionCartasEnTablero(int id, int posx, int posy) {
        for (Carta c : tablero.getCartas()) {
            if (c.getId() == id) {
                c.setPosX(posx);
                c.setPosY(posy);
            }
        }
    }
}
