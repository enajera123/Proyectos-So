
package model;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author raul
 */

public class Tablero {
    private String nombre;
    private List<Carta> cartas;
    private String rutaCaminos;

    public Tablero(){
    }

    public Tablero(String nombre){
        this.nombre = nombre;
        this.cartas = new ArrayList<Carta>();
    }
    
    public Tablero(String nombre, List<Carta> cartas){
        this.nombre = nombre;
        this.cartas = cartas;
    }
    @JsonCreator
    public Tablero(@JsonProperty("nombre")String nombre, @JsonProperty("cartas")List<Carta> cartas,@JsonProperty("rutaCaminos") String rutaCaminos){
        this.nombre = nombre;
        this.cartas = cartas;
        this.rutaCaminos = rutaCaminos;
    }
    public List<Carta> getCartas() {
        return cartas;
    }

    public String getNombre() {
        return nombre;
    }
    
    public String getRutaCaminos() {
        return rutaCaminos;
    }

    public void setRutaCaminos(String rutaCaminos) {
        this.rutaCaminos = rutaCaminos;
    }
    
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setCartas(List<Carta> cartas) {
        this.cartas = cartas;
    }
}
