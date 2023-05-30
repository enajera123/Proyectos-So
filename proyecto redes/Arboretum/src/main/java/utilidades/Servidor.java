package utilidades;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;
import javafx.scene.control.Alert;
import model.Partida;

/**
 *
 * @author estebannajera
 */
public class Servidor {

    private Socket socket;
    private String direccionIp;
    private int puerto;
    private OutputStream outputStream;
    private DataOutputStream dataOutputStream;
    private final static ObjectMapper JSON = new ObjectMapper();

    public Servidor() {
    }

    public Servidor(String ip, int puerto) {
        try {
            this.direccionIp = ip;
            this.puerto = puerto;
            socket = new Socket(ip, puerto);
        } catch (IOException ex) {

        }
    }

    public void setSocket(Socket socket) {
        this.socket = socket;
    }

    public Socket getSocket() {
        return socket;
    }

    public void iniciar() {
        try {
            socket = new Socket(direccionIp, puerto);
            this.outputStream = socket.getOutputStream();
            this.dataOutputStream = new DataOutputStream(outputStream);
        } catch (IOException ex) {

        }
    }

    public boolean conectar(String nombre) {
        try {
            iniciar();
            //Intento conectar
            dataOutputStream.writeUTF("conectar" + "+" + nombre);
            String datos = leerDatos();
            if (!"\"Conectado Correctamente\"".equals(datos)) {
                Alerta.alerta(datos, "Error", Alert.AlertType.ERROR);
                return false;
            }
            //Alerta.alerta(leerDatos(), "Informacion", Alert.AlertType.INFORMATION);
            return true;
        } catch (IOException ex) {

            ex.printStackTrace();
            return false;
        }
    }

    public String leerDatos() {
        try {
            byte[] buffer = new byte[20000];
            int bytesRead;
            bytesRead = socket.getInputStream().read(buffer);//Lee los bytes
            if (bytesRead != -1) {
                String message = new String(buffer, 0, bytesRead);//Lo pasa a texto
                System.out.println(message);
                return message;
            }
            Alerta.alerta("No hay respuesta por parte del servidor", "Error", Alert.AlertType.WARNING);
            System.out.println("No hay respuesta");
            return "No hay respuesta";
        } catch (IOException ex) {
            System.err.println(ex);
            return "";
        }
    }

    public boolean empezarPartida(String jugador) {
        try {
            iniciar();
            //Envia datos
            dataOutputStream.writeUTF("empezar+" + jugador);
            //Leo la respuesta
            String datos = leerDatos();
            System.out.println(datos);
            if (datos == "No hay respuesta") {
                return false;
            }

            return true;
        } catch (IOException ex) {
            ex.printStackTrace();
            return false;
        }
    }

    public boolean crearPartida(String nombre, String clave) {
        try {
            iniciar();
            //Envia datos
            dataOutputStream.writeUTF("crear+" + nombre + "+" + clave);
            //Leo la respuesta
            String datos = leerDatos();
            if (datos.equals("\"Hay una partida existente\"")) {
                Alerta.alerta(datos, "Informacion", Alert.AlertType.INFORMATION);
                return false;
            } else {
                Alerta.alerta("Partida creada correctamente", "Informacion", Alert.AlertType.INFORMATION);
                return true;
            }
        } catch (IOException ex) {
            ex.printStackTrace();
            return false;
        }
    }

    public Partida cambiarTurno() {
        try {
            iniciar();
            dataOutputStream.writeUTF("cambiarTurno+");
            String datos = leerDatos();
            System.out.println(datos);
            return JSON.readValue(datos, Partida.class);
        } catch (IOException ex) {
            return null;
        }
    }

    public Partida agregarCartaTablero(String nombreJugador, int idCarta, int posX, int posY) {
        try {
            iniciar();
            dataOutputStream.writeUTF("agregarCartaTablero+" + nombreJugador + "+" + idCarta + "+" + posX + "+" + posY);
            String datos = leerDatos();
            System.out.println(datos);
            Partida partida = JSON.readValue(datos, Partida.class);
            return partida;
        } catch (Exception ex) {
            System.out.println(ex.toString());
            return null;
        }
    }

    public Partida agregarCarta(String nombreJugador, int idCarta) {
        try {
            iniciar();
            dataOutputStream.writeUTF("agregarCartaJugador+" + nombreJugador + "+" + idCarta);
            String datos = leerDatos();
            System.out.println(datos);
            Partida partida = JSON.readValue(datos, Partida.class);
            return partida;
        } catch (Exception ex) {
            System.out.println(ex.toString());
            return null;
        }
    }

    public Partida sacarCartaDescarte(String descarteJugador, int idCarta) {
        try {
            iniciar();
            dataOutputStream.writeUTF("sacarCartaDescarte+" + descarteJugador + "+" + idCarta);
            String datos = leerDatos();
            System.out.println(datos);
            Partida partida = JSON.readValue(datos, Partida.class);
            return partida;
        } catch (Exception ex) {
            System.out.println(ex.toString());
            return null;
        }
    }

    public Partida descartarCarta(String nombreJugador, int idCarta) {
        try {
            iniciar();
            dataOutputStream.writeUTF("descartaCarta+" + nombreJugador + "+" + idCarta);
            String datos = leerDatos();
            System.out.println(datos);
            Partida partida = JSON.readValue(datos, Partida.class);
            return partida;
        } catch (Exception ex) {
            System.out.println(ex.toString());
            return null;
        }
    }

    public Partida modificarCartaTablero(String nombreJugador, int idCarta, int posX, int posY) {
        try {
            iniciar();
            dataOutputStream.writeUTF("modificarCartaTablero+" + nombreJugador + "+" + idCarta + "+" + posX + "+" + posY);
            String datos = leerDatos();
            System.out.println(datos);
            Partida partida = JSON.readValue(datos, Partida.class);
            return partida;
        } catch (Exception ex) {
            System.out.println(ex.toString());
            return null;
        }
    }

    public boolean salirPartida(String nombre) {
        try {
            iniciar();
            dataOutputStream.writeUTF("salir+" + nombre);
            String datos = leerDatos();
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    public Partida getPartida() {
        try {
            iniciar();
            dataOutputStream.writeUTF("getPartida");
            String datos = leerDatos();

            if (datos.equals("\"error\"")) {
                return null;
            }
            return JSON.readValue(datos, Partida.class);
        } catch (IOException ex) {
            return null;
        }
    }

    public List<String> terminarPartida() {
        try {
            iniciar();
            dataOutputStream.writeUTF("terminar+");
//            List<String>informacion = new ArrayList<String>();

            String datos = leerDatos();
            List<String> informacion = JSON.readValue(datos, new TypeReference<List<String>>() {
            });
            return informacion;
            //System.out.println(datos);
        } catch (IOException ex) {
            System.out.println(ex.toString());
            return null;
        }
    }

    public Partida unirsePartida(String nombre, String nombrePartida, String clave) {
        String datos = "";
        try {
            iniciar();
            dataOutputStream.writeUTF("unirse+" + nombre + "+" + nombrePartida + "+" + clave);
            datos = leerDatos();
            return JSON.readValue(datos, Partida.class);
        } catch (IOException ex) {
            Alerta.alerta(datos, "Ups", Alert.AlertType.ERROR);
            return null;
        }
    }
}
