
package utilidades;

import java.util.List;
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
    private static List<String> puntuaciones;

    public static List<String> getPuntuaciones() {
        return puntuaciones;
    }

    public static void setPuntuaciones(List<String> puntuaciones) {
        Data.puntuaciones = puntuaciones;
    }
    
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
