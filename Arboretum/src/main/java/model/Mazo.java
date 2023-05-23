
package model;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author estebannajera
 */
public class Mazo {
    private String nombre;
    private List<Carta> cartas;

    public Mazo(String nombre) {
        this.nombre = nombre;
        cartas = new ArrayList<Carta>();
    }
    @JsonCreator
    public Mazo(@JsonProperty("nombre") String nombre, @JsonProperty("cartas")List<Carta> cartas) {
        this.nombre = nombre;
        this.cartas = cartas;
    }

    public List<Carta> getCartas() {
        return cartas;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setCartas(List<Carta> cartas) {
        this.cartas = cartas;
    }
    
}
