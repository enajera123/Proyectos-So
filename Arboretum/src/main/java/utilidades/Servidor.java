package utilidades;

import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.Socket;
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
    private final static String CONECTAR = "conectar";

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

    public void conectar(String nombre) {
        try {
            iniciar();
            //Intento conectar
            dataOutputStream.writeUTF(CONECTAR + "+" + nombre);
            Alerta.alerta(leerDatosSinJSON(), "Informacion", Alert.AlertType.INFORMATION);
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    public String leerDatosSinJSON() {
        try {
            byte[] buffer = new byte[1024];
            int bytesRead;
            bytesRead = socket.getInputStream().read(buffer);//Lee los bytes
            if (bytesRead != -1) {
                String message = new String(buffer, 0, bytesRead);//Lo pasa a texto
                return message;
            }
            return "No hay respuesta";
        } catch (IOException ex) {
            System.err.println(ex);
            return ex.toString();
        }

    }

    public String leerDatos() {
        try {
            byte[] buffer = new byte[1024];
            int bytesRead;
            bytesRead = socket.getInputStream().read(buffer);//Lee los bytes
            if (bytesRead != -1) {
                String message = new String(buffer, 0, bytesRead);//Lo pasa a texto
                return message;
            }
            return "No hay respuesta";
        } catch (IOException ex) {
            System.err.println(ex);
            return "";
        }

    }

    public boolean crearPartida(String nombre, String clave) {
        try {
            iniciar();
            //Envia datos
            dataOutputStream.writeUTF("crear+" + nombre + "+" + clave);
            //Leo la respuesta
            if (leerDatos() == "Hay una partida existente") {
                return false;
            }
            Alerta.alerta("Partida creada correctamente", "Informacion", Alert.AlertType.INFORMATION);
            return true;
        } catch (IOException ex) {

            ex.printStackTrace();
            return false;
        }
    }

    public Partida getPartida() {
        try {
            iniciar();
            dataOutputStream.writeUTF("getPartida+");
            String datos = leerDatos();
            return JSON.readValue(datos, Partida.class);
        } catch (IOException ex) {
            return null;
        }
    }

    public Partida unirsePartida(String nombre, String nombrePartida, String clave) {
        try {
            iniciar();
            dataOutputStream.writeUTF("unirse+" + nombre + "+" + nombrePartida + "+" + clave);
            String datos = leerDatos();
            if (datos == "No se encontro partida") {
                return null;
            } else {
                return JSON.readValue(datos, Partida.class);
            }
            //Alerta.alerta(leerDatos(), "Informacion", Alert.AlertType.INFORMATION);
        } catch (IOException ex) {
            return null;
        }
    }
}
