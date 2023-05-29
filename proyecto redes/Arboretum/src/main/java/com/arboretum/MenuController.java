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
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import javafx.application.Platform;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;

import model.Jugador;
import model.Partida;
import utilidades.Alerta;
import utilidades.Data;
import utilidades.MyString;

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
    private HBox contenedorFiguras;
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
    @FXML
    private StackPane contenedor;
    @FXML
    private Button btnEmpezarPartida;

    private Servidor servidor;

    private Partida partida;

    private Thread hiloEsperarJugadores;

    private Jugador jugador = null;

    private int muerteHiloEsperando = -1;
    private boolean creadorPartida = false;
    private final Object lock = new Object();
    private final Object lockEmpezar = new Object();

    /**
     * Initializes the controller class.
     */
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        servidor = null;
        crearFiguras();
        hiloEsperarJugadores = new Thread(() -> {

            if (partida != null) {
                while (muerteHiloEsperando != -1) {
                    partida = servidor.getPartida();
                    if (muerteHiloEsperando == 1) {//Se pone el hilo en espera en 1
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
                            muerteHiloEsperando = -1;
                            Platform.runLater(() -> {
                                btnEmpezarPartida.setDisable(false);
                            });
                        }

                    }

                }

            }
        });
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
        if (btnEmpezarPartida.getText().equals("Iniciar")) {
            partida = servidor.getPartida();
            bindData();
            App.setRoot("tablero");
        } else {
            if (partida != null && !partida.getJugadores().isEmpty()) {
                if (servidor.empezarPartida(jugador.getNombre())) {
                    partida = servidor.cambiarTurno();
                    if (partida != null) {
                        bindData();
                        App.setRoot("tablero");
                    } else {
                        Alerta.alerta("Error al empezar partida", "error", Alert.AlertType.ERROR);
                    }
                }
            } else {
                new Bounce(lblCantidadJugadores).play();
            }
        }
    }

    @FXML
    private void btnUnirse(ActionEvent event) throws IOException, InterruptedException {
        if (servidor != null) {
            partida = servidor.unirsePartida(jugador.getNombre(), txfUnirseNombrePartida.getText(), txfUnirseClavePartida.getText());
            if (partida != null) {
                panelEsperarJugadores.toFront();
                cargarDatosLabeles(partida);
                iniciarHilo();
                panelEsperarJugadores.toFront();
                new BounceIn(panelEsperarJugadores).play();
                if (!creadorPartida) {
                    btnEmpezarPartida.setText("Iniciar");
                    btnEmpezarPartida.setDisable(true);
                }
            }
        }
    }

    @FXML
    private void btnGenerarClave(ActionEvent event) {
        txfCrearClavePartida.setText(MyString.generarClave(6));
    }

    @FXML
    private void btnCrear_CrearPartida(ActionEvent event) {

        if (servidor != null) {
            if (servidor.crearPartida(txfCrearNombrePartida.getText(), txfCrearClavePartida.getText())) {
                partida = servidor.unirsePartida(jugador.getNombre(), txfCrearNombrePartida.getText(), txfCrearClavePartida.getText());
                if (partida != null) {
                    cargarDatosLabeles(partida);
                    panelEsperarJugadores.toFront();
                    creadorPartida = true;
                    iniciarHilo();
                }
            }

        }
    }

    @FXML
    private void btnConectarServidor(ActionEvent event) {
        try {
            servidor = new Servidor(txfDireccionIp.getText(), Integer.parseInt(txfPuerto.getText()));//Se crea un objeto tipo servidor
            if (servidor.conectar(txfNombreUsuario.getText())) {//Se envia un mensaje de conexion
                jugador = new Jugador(txfNombreUsuario.getText());//Se crea un jugador
                txfDireccionIp.setText(null);//Se limpian los campos de texto
                txfPuerto.setText(null);
                txfNombreUsuario.setText(null);
                new BounceIn(panelUnirsePartida).play();//Animacion
                panelUnirsePartida.toFront();//Se muestra la pantalla de unirsePartida
            }
        } catch (Exception e) {
            System.out.println(e.toString());
        }
    }

    //METODOS UTILIDADES
    /**
     * Carga los datos en el flow para los otros controladores
     */
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

    /**
     * Carga datos a los labeles de la pantalla de esperar jugadores
     *
     * @param partida
     */
    private void cargarDatosLabeles(Partida partida) {
        lblEsperarNombrePartida.setText("Nombre de partida: " + partida.getNombre());
        lblEsperarClavePartida.setText("Clave: " + partida.getClave());
        txfCrearNombrePartida.setText(null);
        txfCrearClavePartida.setText(null);
    }

    /**
     * Inicia un hilo que verfica la union de nuevos jugadores
     */
    private void iniciarHilo() {
        if (muerteHiloEsperando == -1) {
            muerteHiloEsperando = 0;
            hiloEsperarJugadores.setDaemon(true);
            hiloEsperarJugadores.start();
        } else {
            reanudarHiloEsperando();
        }
    }

    /**
     * Metodo de disenho
     */
    private void crearFiguras() {
        List<Integer> numeros = new ArrayList<>();
        for (int i = 1; i < 11; i++) {
            numeros.add(i);
        }
        Random rand = new Random();
        while (!numeros.isEmpty()) {
            int i = rand.nextInt(numeros.size());
            ImageView imagen = new ImageView(new Image(App.class.getResource("/img/figuras/" + numeros.get(i) + ".png").toString()));
            numeros.remove(numeros.get(i));
            imagen.setFitWidth(50);
            imagen.setFitHeight(70);
            imagen.setPreserveRatio(false);
            imagen.setSmooth(false);
            imagen.getStyleClass().add("drop-shadow");
            imagen.setOnMouseClicked((t) -> {
                new Bounce(imagen).play();
            });
            contenedorFiguras.getChildren().add(imagen);
        }
    }
}
