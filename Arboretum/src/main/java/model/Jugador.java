
package model;
//import model.Mazo;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author estebannajera
 */
public class Jugador {
   private String nombre;
   private Tablero tablero ;
   private Mazo descartes;
   private Mazo baraja;
   private List<String> tiposArbolPuntuable;

    public Jugador() {
        this.nombre = "";
        this.baraja = new Mazo(nombre);
        this.descartes = new Mazo(nombre);
        this.tablero = new Tablero(nombre);
        this.tiposArbolPuntuable = new ArrayList<String>();
    }
    @JsonCreator
    public Jugador(
        @JsonProperty("nombre")String nombre,@JsonProperty("tablero")Tablero tablero,
        @JsonProperty("descartes")Mazo descartes,@JsonProperty("baraja")Mazo baraja,
        @JsonProperty("tiposArbolPuntuable")List<String>tiposArbolPuntuable) 
    {
        this.nombre = nombre;
        this.baraja = baraja;
        this.descartes = descartes;
        this.tablero = tablero;
        this.tiposArbolPuntuable = tiposArbolPuntuable;
    }

    public Jugador(String nombre) {
        this.nombre = nombre;
        this.baraja = new Mazo(nombre);
        this.descartes = new Mazo(nombre);
        this.tablero = new Tablero(nombre);
        this.tiposArbolPuntuable = new ArrayList<String>();
    }

    public Mazo getBaraja() {
        return this.baraja;
    }
    public Mazo getDescartes() {
        return this.descartes;
    }
    
    public Tablero getTablero() {
        return this.tablero;
    }

    public String getNombre() {
        return nombre;
    }
    
    public List<String> getTiposArbolPuntuable(){
        return this.tiposArbolPuntuable;
    }
    
    public void setTiposArbolPuntuable(List<String> tiposArbolPuntuable){
        this.tiposArbolPuntuable = tiposArbolPuntuable;
    }
    
    public void setBaraja(Mazo baraja) {
        this.baraja = baraja;
    }
    public void setDescartes(Mazo descartes) {
        this.descartes = descartes;
    }
    
    public void setTablero(Tablero tablero) {
        this.tablero = tablero;
    }
    
}
