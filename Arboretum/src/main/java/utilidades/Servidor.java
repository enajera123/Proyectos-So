package utilidades;

import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.Socket;

import model.Partida;

/**
 *
 * @author estebannajera
 */
public class Servidor {

    private Socket socket;
    private OutputStream outputStream;
    private DataOutputStream dataOutputStream;
    private final static ObjectMapper JSON = new ObjectMapper();
    private final static String CONECTAR = "conectar";

    public Servidor() {
    }

    public void setSocket(Socket socket) {
        this.socket = socket;
    }

    public Socket getSocket() {
        return socket;
    }

    public Servidor(Socket socket) {
        this.socket = socket;
    }

    public void conectar(String nombre) {
        try {
            this.outputStream = socket.getOutputStream();
            this.dataOutputStream = new DataOutputStream(outputStream);
            dataOutputStream.writeUTF(CONECTAR+"+"+nombre);
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    public void leerDatos() {
        try {
            byte[] buffer = new byte[1024];
            int bytesRead;
            bytesRead = socket.getInputStream().read(buffer);//Lee los bytes
            System.out.println(bytesRead);
            String message = new String(buffer, 0, bytesRead);//Lo pasa a texto
            Partida partida = JSON.readValue(message, Partida.class);//
            System.out.println(partida.toString());
        } catch (IOException ex) {
            System.err.println(ex);
        }

    }
    
    public void crearPartida(String nombre, String clave) {
        try {
            dataOutputStream.writeUTF(JSON.writeValueAsString(new Partida(nombre, clave)));
            leerDatos();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

}
