
package utilidades;

import model.Jugador;
import model.Partida;

/**
 *
 * @author estebannajera
 */
public class Data {
    private static Jugador jugador;
    private static Partida partida;
    private static Servidor sevidor;
    public static Jugador getJugador() {
        return jugador;
    }

    public static Partida getPartida() {
        return partida;
    }

    public static void setSevidor(Servidor sevidor) {
        Data.sevidor = sevidor;
    }

    public static Servidor getSevidor() {
        return sevidor;
    }

    public static void setJugador(Jugador jugador) {
        Data.jugador = jugador;
    }

    public static void setPartida(Partida partida) {
        Data.partida = partida;
    }
    
    
    
}
