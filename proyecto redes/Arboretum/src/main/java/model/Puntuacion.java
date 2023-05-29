package model;

/**
 *
 * @author estebannajera
 */
public class Puntuacion {

    private String nombre;
    private String camino;
    private String puntos;

    public Puntuacion() {
    }

    public Puntuacion(String nombre, String camino, String puntos) {
        this.nombre = nombre;
        this.camino = camino;
        this.puntos = puntos;
    }

    public String getCamino() {
        return camino;
    }

    public String getNombre() {
        return nombre;
    }

    public String getPuntos() {
        return puntos;
    }

    public void setCamino(String camino) {
        this.camino = camino;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setPuntos(String puntos) {
        this.puntos = puntos;
    }
    
    
}
