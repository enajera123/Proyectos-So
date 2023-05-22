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
            Alerta.alerta(leerDatos(), "Informacion", Alert.AlertType.INFORMATION);
            return true;
        } catch (IOException ex) {

            ex.printStackTrace();
            return false;
        }
    }

    public String leerDatos() {
        try {
            byte[] buffer = new byte[10000];
            int bytesRead;
            bytesRead = socket.getInputStream().read(buffer);//Lee los bytes
            if (bytesRead != -1) {
                String message = new String(buffer, 0, bytesRead);//Lo pasa a texto
                System.out.println(message);
                return message;
            }
            System.out.println("No hay respuesta");
            return "No hay respuesta";
        } catch (IOException ex) {
            System.err.println(ex);
            return "";
        }
    }

    public void empezarPartida() {
        try {
            iniciar();
            //Envia datos
            dataOutputStream.writeUTF("empezar+");
            //Leo la respuesta
            String datos = leerDatos();
            System.out.println(datos);
        } catch (IOException ex) {
            ex.printStackTrace();
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
//    public boolean getCarta() {
//        try {
//            iniciar();
//            //Envia datos
//            dataOutputStream.writeUTF("carta+");
//            //Leo la respuesta
//            String datos = leerDatos();
//            //datos = datos.replace("\'", "");
//            if (datos.equals("\"Hay una partida existente\"")) {
//                Alerta.alerta(datos, "Informacion", Alert.AlertType.INFORMATION);
//                return false;
//            } else {
//                 Carta carta = JSON.readValue(datos, Carta.class);
//                 System.out.println(carta);
//                return true;
//            }
//        } catch (IOException ex) {
//            System.out.println(ex.toString());
//            return false;
//        }
//    }
//    public boolean getMazo() {
//        try {
//            iniciar();
//            //Envia datos
//            dataOutputStream.writeUTF("mazo+");
//            //Leo la respuesta
//            String datos = leerDatos();
//            //datos = datos.replace("\'", "");
//            if (datos.equals("\"Hay una partida existente\"")) {
//                Alerta.alerta(datos, "Informacion", Alert.AlertType.INFORMATION);
//                return false;
//            } else {
//                 Mazo mazo = JSON.readValue(datos, Mazo.class);
//                 System.out.println(mazo);
//                return true;
//            }
//        } catch (IOException ex) {
//            System.out.println(ex.toString());
//            return false;
//        }
//    }

//    public boolean getJugador() {
//        try {
//            iniciar();
//            //Envia datos
//            dataOutputStream.writeUTF("jugador+");
//            //Leo la respuesta
//            String datos = leerDatos();
//            //datos = datos.replace("\'", "");
//            if (datos.equals("\"Hay una partida existente\"")) {
//                Alerta.alerta(datos, "Informacion", Alert.AlertType.INFORMATION);
//                return false;
//            } else {
//                Jugador mazo = JSON.readValue(datos, Jugador.class);
//                System.out.println(mazo);
//                return true;
//            }
//        } catch (IOException ex) {
//            System.out.println(ex.toString());
//            return false;
//        }
//    }
//
//    public boolean partida() {
//        try {
//            iniciar();
//            //Envia datos
//            dataOutputStream.writeUTF("partida+");
//            //Leo la respuesta
//            String datos = leerDatos();
//            //datos = datos.replace("\'", "");
//            if (datos.equals("\"Hay una partida existente\"")) {
//                Alerta.alerta(datos, "Informacion", Alert.AlertType.INFORMATION);
//                return false;
//            } else {
//                Partida mazo = JSON.readValue(datos, Partida.class);
//                System.out.println(mazo);
//                return true;
//            }
//        } catch (IOException ex) {
//            System.out.println(ex.toString());
//            return false;
//        }
//    }
    public boolean salirPartida(String nombre) {
        try {
            iniciar();
            dataOutputStream.writeUTF("salir+" + nombre);
            String datos = leerDatos();
            if (datos.equals("\"Exito\"")) {
                return true;
            } else {
                return false;
            }
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

    public Partida unirsePartida(String nombre, String nombrePartida, String clave) {
        try {
            iniciar();
            dataOutputStream.writeUTF("unirse+" + nombre + "+" + nombrePartida + "+" + clave);
            String datos = leerDatos();

            if (datos.equals("\"No se encontro partida\"")) {
                Alerta.alerta(datos, "Oh Oh", Alert.AlertType.ERROR);
                return null;
            } else {
                return JSON.readValue(datos, Partida.class);
            }
        } catch (IOException ex) {
            System.out.println(ex.toString());
            return null;
        }
    }
}
