package model;

/**
 *
 * @author estebannajera
 */
public class Partida {

    private String nombre;
    private String clave;

    public Partida() {
    }

    public Partida(String nombre, String clave) {
        this.nombre = nombre;
        this.clave = clave;
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
