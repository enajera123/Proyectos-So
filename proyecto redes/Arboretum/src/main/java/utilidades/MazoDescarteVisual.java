package utilidades;

import java.util.Stack;

/**
 *
 * @author estebannajera
 */
public class MazoDescarteVisual {

    private String nombre;
    private int posx;
    private int posy;
    private Stack<CartaVisual> cartas;

    public MazoDescarteVisual() {
    }

    public MazoDescarteVisual(String nombre, int posx, int posy) {
        this.nombre = nombre;
        this.posx = posx;
        this.posy = posy;
        cartas = new Stack<>();
    }

    public MazoDescarteVisual(String nombre, int posx, int posy, Stack<CartaVisual> cartas) {
        this.nombre = nombre;
        this.posx = posx;
        this.posy = posy;
        this.cartas = cartas;
    }

    public Stack<CartaVisual> getCartas() {
        return cartas;
    }

    public String getNombre() {
        return nombre;
    }

    public int getPosx() {
        return posx;
    }

    public int getPosy() {
        return posy;
    }

    public void setCartas(Stack<CartaVisual> cartas) {
        this.cartas = cartas;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setPosy(int posy) {
        this.posy = posy;
    }

    public void setPosx(int posx) {
        this.posx = posx;
    }

}
