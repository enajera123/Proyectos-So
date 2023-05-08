
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
    private ListView<?> listViewJugadores;
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

    /**
     * Initializes the controller class.
     */
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        // TODO
    }    

    @FXML
    private void btnCrearPartida(ActionEvent event) {
        panelCrearPartida.toFront();
    }

    @FXML
    private void btnUnirsePartida(ActionEvent event) {
        panelUnirsePartida.toFront();
    }

    @FXML
    private void btnConfiguraciones(ActionEvent event) {
        panelConfiguraciones.toFront();
    }

    @FXML
    private void btnCancelarPartida(ActionEvent event) {
    }

    @FXML
    private void btnEmpezarPartida(ActionEvent event) {
    }

    @FXML
    private void btnUnirse(ActionEvent event) {
        panelEsperarJugadores.toFront();
        
    }

    @FXML
    private void btnGenerarClave(ActionEvent event) {
    }

    @FXML
    private void btnCrear_CrearPartida(ActionEvent event) {
        panelEsperarJugadores.toFront();
    }
    
}
