package com.arboretum;

import animatefx.animation.Bounce;
import java.net.URL;
import java.util.ResourceBundle;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;

import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.control.TextField;
import javafx.scene.layout.HBox;
import javafx.scene.layout.StackPane;
import javafx.scene.layout.VBox;
import animatefx.animation.BounceIn;
import java.io.IOException;

import java.util.Random;
import javafx.application.Platform;
import javafx.scene.control.Alert;

import model.Jugador;
import model.Partida;
import utilidades.Alerta;
import utilidades.Data;

import utilidades.Servidor;

/**
 * FXML Controller class
 *
 * @author estebannajera
 */
public class MenuController implements Initializable {

    @FXML
    private HBox panelMenu;
    @FXML
    private Label lblTitulo;
    @FXML
    private VBox panelCrearPartida;
    @FXML
    private TextField txfCrearNombrePartida;
    @FXML
    private TextField txfCrearClavePartida;
    @FXML
    private VBox panelEsperarJugadores;
    @FXML
    private Label lblEsperarNombrePartida;
    @FXML
    private Label lblEsperarClavePartida;
    @FXML
    private Label lblCantidadJugadores;
    @FXML
    private ListView<String> listViewJugadores;
    @FXML
    private VBox panelUnirsePartida;
    @FXML
    private TextField txfUnirseNombrePartida;
    @FXML
    private TextField txfUnirseClavePartida;
    @FXML
    private VBox panelConfiguraciones;
    @FXML
    private TextField txfNombreUsuario;
    @FXML
    private TextField txfDireccionIp;
    @FXML
    private TextField txfPuerto;
    @FXML
    private StackPane panelDerecho;
    @FXML
    private VBox panelIzquierdo;

    private Servidor servidor;

    private Partida partida;

    private Thread hiloEsperarJugadores;

    private Jugador jugador = null;

    private int muerteHiloEsperando = -1;

    private final Object lock = new Object();
    private final Object lockEmpezar = new Object();

    /**
     * Initializes the controller class.
     */
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        servidor = null;
        hiloEsperarJugadores = new Thread(() -> {
            if (partida != null) {
                while (muerteHiloEsperando != -1) {
                    partida = servidor.getPartida();
                    if (muerteHiloEsperando == 1) {
                        synchronized (lock) {
                            try {
                                lock.wait();
                            } catch (Exception e) {
                                e.printStackTrace();
                            }
                        }
                    } else if (partida != null) {
                        Platform.runLater(() -> {//Se actualiza la lista de jugadores
                            lblCantidadJugadores.setText(partida.getJugadores().size() + "/4");
                            listViewJugadores.getItems().clear();
                            partida.getJugadores().forEach((t) -> {
                                listViewJugadores.getItems().add(t.getNombre());
                            });

                        });
                        if (partida.isIniciado()) {
                            //        synchronized (lockEmpezar) {
                            //          lockEmpezar.notify();
                            muerteHiloEsperando = -1;
                            //    }
                        }

                    }

                }

            }
        });
    }

    private void bindData() {
        partida.getJugadores().forEach((t) -> {
            if (t.getNombre().equals(jugador.getNombre())) {
                jugador = t;
            }
        });
        Data.setJugador(jugador);
        Data.setSevidor(servidor);
        Data.setPartida(partida);
    }

    private void reanudarHiloEsperando() {
        synchronized (lock) {
            lock.notify();
        }
        muerteHiloEsperando = 0;
    }

    @FXML
    private void btnCrearPartida(ActionEvent event) {
        if (servidor != null) {
            panelCrearPartida.toFront();
            new BounceIn(panelCrearPartida).play();
        } else {
            Alerta.alerta("Debe crear una conexion primero", "No te apresures", Alert.AlertType.WARNING);
        }
    }

    @FXML
    private void btnUnirsePartida(ActionEvent event) {
        if (servidor != null) {
            panelUnirsePartida.toFront();
            new BounceIn(panelUnirsePartida).play();
        } else {
            Alerta.alerta("Debe crear una conexion primero", "No te apresures", Alert.AlertType.WARNING);
        }
    }

    @FXML
    private void btnConfiguraciones(ActionEvent event) {
        panelConfiguraciones.toFront();
        new BounceIn(panelConfiguraciones).play();
    }

    @FXML
    private void btnCancelarPartida(ActionEvent event) {
        if (servidor.salirPartida(jugador.getNombre())) {
            muerteHiloEsperando = 1;
            panelMenu.toFront();
        }
    }

    @FXML
    private void btnEmpezarPartida(ActionEvent event) throws IOException, InterruptedException {
        if (partida != null && partida.getJugadores().size() > 0) {
            if (servidor.empezarPartida()) {
                //synchronized (lockEmpezar) {
                // lockEmpezar.wait();
                partida = servidor.getPartida();
                if (partida != null) {
                    bindData();
                    App.setRoot("tablero");
                }else{
                    Alerta.alerta("Error al empezar partida", "error", Alert.AlertType.ERROR);
                }
                //}
            }

        } else {
            new Bounce(lblCantidadJugadores).play();

        }
    }

    @FXML
    private void btnUnirse(ActionEvent event) {
        if (servidor != null) {
            partida = servidor.unirsePartida(jugador.getNombre(), txfUnirseNombrePartida.getText(), txfUnirseClavePartida.getText());
            if (partida != null) {
                panelEsperarJugadores.toFront();
                lblEsperarNombrePartida.setText("Nombre de partida: " + partida.getNombre());
                lblEsperarClavePartida.setText("Clave: " + partida.getClave());
                if (muerteHiloEsperando == -1) {
                    muerteHiloEsperando = 0;
                    hiloEsperarJugadores.start();
                } else {
                    reanudarHiloEsperando();
                }
                panelEsperarJugadores.toFront();
                new BounceIn(panelEsperarJugadores).play();
            }
        }
        //servidor.partida();

    }

    @FXML
    private void btnGenerarClave(ActionEvent event) {
        txfCrearClavePartida.setText(generarClave(6));
    }

    @FXML
    private void btnCrear_CrearPartida(ActionEvent event) {

        if (servidor != null) {
            if (servidor.crearPartida(txfCrearNombrePartida.getText(), txfCrearClavePartida.getText())) {
                partida = servidor.unirsePartida(jugador.getNombre(), txfCrearNombrePartida.getText(), txfCrearClavePartida.getText());
                if (partida != null) {
                    lblEsperarNombrePartida.setText("Nombre de partida: " + partida.getNombre());
                    lblEsperarClavePartida.setText("Clave: " + partida.getClave());
                    txfCrearNombrePartida.setText(null);
                    txfCrearClavePartida.setText(null);
                    panelEsperarJugadores.toFront();
                    if (muerteHiloEsperando == -1) {
                        muerteHiloEsperando = 0;
                        hiloEsperarJugadores.start();
                    } else {
                        reanudarHiloEsperando();
                    }
                }
            }

        }
    }

    @FXML
    private void btnConectarServidor(ActionEvent event) {
        try {
            servidor = new Servidor(txfDireccionIp.getText(), Integer.parseInt(txfPuerto.getText()));
            if (servidor.conectar(txfNombreUsuario.getText())) {
                jugador = new Jugador(txfNombreUsuario.getText());
                txfDireccionIp.setText(null);
                txfPuerto.setText(null);
                txfNombreUsuario.setText(null);
                new BounceIn(panelUnirsePartida).play();
                panelUnirsePartida.toFront();
            }
        } catch (Exception e) {
        }
    }

    public static String generarClave(int length) {
        String CHARACTERS = /*"ABCDEFGHIJKLMNOPQRSTUVWXYZ*/ "0123456789";
        String password = "";
        Random random = new Random();
        for (int i = 0; i < length; i++) {
            int index = random.nextInt(CHARACTERS.length());
            char c = CHARACTERS.charAt(index);
            password += c;
        }
        return password;
    }
}
