package com.arboretum;

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

import java.util.Random;
import javafx.application.Platform;
import model.Partida;

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

    /**
     * Initializes the controller class.
     */
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        servidor = null;
        hiloEsperarJugadores = new Thread(() -> {
            while (partida.getJugadores().size() < 4) {
                partida = servidor.getPartida();
                Platform.runLater(() -> {
                    lblCantidadJugadores.setText(partida.getJugadores().size() + "/4");
                    listViewJugadores.getItems().clear();
                    partida.getJugadores().forEach((t) -> {
                        listViewJugadores.getItems().add(t);
                    });
                });

            }
        });
    }

    @FXML
    private void btnCrearPartida(ActionEvent event) {

        panelCrearPartida.toFront();
        new BounceIn(panelCrearPartida).play();

    }

    @FXML
    private void btnUnirsePartida(ActionEvent event) {
        panelUnirsePartida.toFront();
        new BounceIn(panelUnirsePartida).play();
    }

    @FXML
    private void btnConfiguraciones(ActionEvent event) {
        panelConfiguraciones.toFront();
        new BounceIn(panelConfiguraciones).play();
    }

    @FXML
    private void btnCancelarPartida(ActionEvent event) {
    }

    @FXML
    private void btnEmpezarPartida(ActionEvent event) {

    }

    @FXML
    private void btnUnirse(ActionEvent event) {
        if (servidor != null) {
            partida = servidor.unirsePartida(txfNombreUsuario.getText(), txfUnirseNombrePartida.getText(), txfUnirseClavePartida.getText());
            if (partida != null) {
                panelEsperarJugadores.toFront();
                hiloEsperarJugadores.start();
            }
        }
        panelEsperarJugadores.toFront();
        new BounceIn(panelEsperarJugadores).play();
    }

    @FXML
    private void btnGenerarClave(ActionEvent event) {
        txfCrearClavePartida.setText(generarClave(6));
    }

    @FXML
    private void btnCrear_CrearPartida(ActionEvent event) {

        if (servidor != null) {
            if (servidor.crearPartida(txfCrearNombrePartida.getText(), txfCrearClavePartida.getText())) {
                partida = servidor.unirsePartida(txfNombreUsuario.getText(), txfCrearNombrePartida.getText(), txfCrearClavePartida.getText());
                panelEsperarJugadores.toFront();
                hiloEsperarJugadores.start();
            }

        }
    }

    @FXML
    private void btnConectarServidor(ActionEvent event) {
        if (verificaCofiguraciones()) {
            try {
                servidor = new Servidor(txfDireccionIp.getText(), Integer.parseInt(txfPuerto.getText()));
                servidor.conectar(txfNombreUsuario.getText());
            } catch (Exception e) {
            }
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

    public boolean verificaCofiguraciones() {
        if (txfDireccionIp.getText().isBlank() || txfPuerto.getText().isBlank() || txfNombreUsuario.getText().isBlank()) {
            return false;
        }
        return true;
    }

}
