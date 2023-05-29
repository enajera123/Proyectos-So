package com.arboretum;

import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.ResourceBundle;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Label;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.Pane;
import javafx.scene.text.Font;
import model.Carta;
import model.Jugador;
import model.Partida;
import utilidades.CartaVisual;
import utilidades.Data;
import utilidades.GridDinamico;
import utilidades.Servidor;

/**
 * FXML Controller class
 *
 * @author estebannajera
 */
public class GanadorController implements Initializable {

    @FXML
    private TableView<String> tbPuntaje;
    @FXML
    private TableColumn<String, String> cArbol;
    @FXML
    private TableColumn<String, String> cPuntos;
    @FXML
    private Label lblTotalPuntos;
    @FXML
    private Label lblUsuario;
    @FXML
    private HBox contenedorUsuarios;
    @FXML
    private HBox contenedorMano;
    @FXML
    private ScrollPane contenedorTablero;
    private GridPane gridTablero = new GridPane();
    private List<CartaVisual> cartasVisuales = new ArrayList();//Lista de cartas dentro del grid logicament
    //OBJETOS UTILIDADES
    private final GridDinamico gridDinamico = new GridDinamico();
    private final int COLUM = 17;//Tamano del grid inicials
    private final int ROW = 6;//Tamano del grid inicial
    private Partida partida;
    private Servidor servidor;
    private Jugador jugador;
    private List<String> puntuaciones;

    @Override
    public void initialize(URL url, ResourceBundle rb) {
        iniciarComponentes();
        //actualizarPartida(partida);
    }

    private void iniciarComponentes() {
        bindData();
        if (partida != null && jugador != null) {
            actualizarPartida(partida);
            lblUsuario.setText(jugador.getNombre());
            lblUsuario.setOnMouseClicked(t -> clickLabelUsuario(lblUsuario));
            lblUsuario.getStyleClass().add("labelHover");
            partida.getJugadores().forEach((t) -> {
                if (!t.getNombre().equals(jugador.getNombre())) {
                    Label label = new Label(t.getNombre());//Se crea el label del jugador
                    label.setFont(new Font("Apple Chancery", 30));
                    label.setOnMouseClicked(event -> clickLabelUsuario(label));
                    label.getStyleClass().add("labelHover");
                    contenedorUsuarios.getChildren().add(label);
                }
            });
        }
    }

    public void bindData() {
        partida = Data.getPartida();
        servidor = Data.getSevidor();
        jugador = Data.getJugador();
        puntuaciones = Data.getPuntuaciones();
        puntuaciones.forEach((t) -> {System.out.println(t);});
    }

    private void clickLabelUsuario(Label label) {
        partida = servidor.getPartida();//Se actualiza la partida
        Jugador jugadorACargar = null;
        if (partida != null) {
            for (Jugador j : partida.getJugadores()) {//Se busca el jugador a cargar
                if (j.getNombre().equals(label.getText())) {
                    jugadorACargar = j;
                }
            }
        }
        actualizarPartida(partida);//Simplemente se actualiza la partida
    }

    private boolean actualizarPartida(Partida partidaActualizada) {
        if (partidaActualizada != null) {
            partida = partidaActualizada;
            partida.getJugadores().forEach((t) -> {
                if (t.getNombre().equals(jugador.getNombre())) {
                    jugador = t;
                }
            });
            cargarTablero(jugador);
            cargarMano(jugador);
            return true;
        }
        return false;
    }

    private void cargarMano(Jugador jugador) {
        contenedorMano.getChildren().clear();
        if (jugador != null) {
            for (Carta c : jugador.getCartas()) {
                CartaVisual cartaVisual = crearCartaVisual(c);
                contenedorMano.getChildren().add(cartaVisual.getContenedor());
            }
        }
    }

    private void crearTableroDinamico() {
        int maxX = getMaxPos(0), maxY = getMaxPos(1);
        gridTablero = gridDinamico.crearTablero(maxY > ROW ? maxY + 2 : ROW, maxX > COLUM ? maxX + 2 : COLUM);
        for (int i = 0; i < ROW; i++) {
            for (int j = 0; j < COLUM; j++) {
                gridTablero.add(crearPane(), j, i);
            }
        }
        gridDinamico.setGrid(gridTablero);
        contenedorTablero.setContent(gridTablero);
    }

    private void cargarTablero(Jugador jugadorCargar) {
        if (jugadorCargar != null) {
            int maxX = getMaxPos(0), maxY = getMaxPos(1);
            gridTablero = gridDinamico.crearTablero(maxY > ROW ? maxY + 2 : ROW, maxX > COLUM ? maxX + 2 : COLUM);
            cartasVisuales = new ArrayList<>();
            for (Carta c : jugadorCargar.getTablero().getCartas()) {
                CartaVisual cartaVisual = crearCartaVisual(c);
                redimensionarCarta(cartaVisual, 95, 70, 10);//Cambia el tamanho para que se ajuste al tablero
                gridTablero.add(cartaVisual.getContenedor(), cartaVisual.getPosX(), cartaVisual.getPosY());
            }
            jugadorCargar.getCartas().forEach(t -> crearCartaVisual(t));
            for (int i = 0; i < gridTablero.getRowCount(); i++) {
                for (int j = 0; j < gridTablero.getColumnCount(); j++) {
                    if (!CartaVisual.buscarCarta(i, j, cartasVisuales)) {
                        gridTablero.add(crearPane(), j, i);
                    }
                }
            }
        }
        contenedorTablero.setContent(gridTablero);
    }

    /**
     * Busca una carta por id en la lista de cartas visuales
     *
     * @param id
     * @return
     */
    public void redimensionarCarta(CartaVisual carta, double height, double width, int fuente) {
        carta.getContenedor().setPrefHeight(height);
        carta.getContenedor().prefWidth(width);
        carta.getImagenArbol().setFitHeight(height);
        carta.getImagenArbol().setFitWidth(width);
        carta.getNumeroCarta().setFont(new Font("Arial Black", fuente));
    }

    private int getMaxPos(int direccion) {
        int max = 0;
        for (Carta c : jugador.getTablero().getCartas()) {
            if (direccion == 0) {
                if (max < c.getPosX()) {
                    max = c.getPosX();
                }
            } else {
                if (max < c.getPosY()) {
                    max = c.getPosY();
                }
            }
        }
        return max;
    }

    private CartaVisual crearCartaVisual(Carta cartaLogica) {
        CartaVisual cartaVisual = new CartaVisual(cartaLogica.getArbol(), String.valueOf(cartaLogica.getNumero()));
        cartasVisuales.add(cartaVisual);
        cartaVisual.getContenedor().getStyleClass().add("drop-shadow");
        cartaVisual.setId(cartaLogica.getId());
        cartaVisual.setPosX(cartaLogica.getPosX());
        cartaVisual.setPosY(cartaLogica.getPosY());
        //cartaVisual.getContenedor().setOnMousePressed(ev -> clickCarta(cartaVisual));//Agrega un evento del click para la carta
        return cartaVisual;
    }

    private Pane crearPane() {
        Pane pane = new Pane();
        pane.getStyleClass().add("bg-tablero");
        //pane.setOnMouseClicked((event) -> clickPane(event));
        return pane;
    }

    private void bindListPuntaje(ObservableList listaVisual) {
        tbPuntaje.setItems(listaVisual);
    }
}
