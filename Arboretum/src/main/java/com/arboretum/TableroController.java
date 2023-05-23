package com.arboretum;

import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.ResourceBundle;
import java.util.Stack;
import javafx.event.ActionEvent;
import javafx.event.Event;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.control.Label;
import javafx.scene.control.ScrollPane;
import javafx.scene.input.MouseEvent;
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

/**
 * FXML Controller class
 *
 * @author estebannajera
 */
public class TableroController implements Initializable {
    
    @FXML
    private GridPane gridMazos;
    @FXML
    private Label lblUsuario;
    @FXML
    private HBox contenedorUsuarios;
    @FXML
    private HBox contenedorMano;
    @FXML
    private ScrollPane contenedorTablero;
    @FXML
    private Label lblCantidadCartas;
    //Objeto utilidad
    private final GridDinamico gridDinamico = new GridDinamico();
    //GridPane dinamico
    private GridPane gridTablero = new GridPane();
    //Lista de cartas dentro del grid logicamente
    private Jugador jugador;
    private Partida partida;
    private final List<CartaVisual> cartasVisuales = new ArrayList();
    private final int COLUM = 17;
    private final int ROW = 6;
    private Stack<CartaVisual> cartasDescarteVisual = new Stack<>();
    private double offsetX = 0;
    private double offsetY = 0;
    private CartaVisual cartaSeleccionada = null;
    private boolean primeraCarta = true;
    int posXDescarte = 0;
    int posYDescarte = 0;
    boolean recogeMazoPrincipal = false;
    

    /**
     * Initializes the controller class.
     *
     * @param url
     * @param rb
     */
    @Override
    public void initialize(URL url, ResourceBundle rb) {

        /**
         * Inicia las cartas*
         */
        iniciarComponentes();
        /**
         * GRID*
         */
        crearTableroDinamico();
    }
    
    private CartaVisual buscarCartaVisual(int id) {
        for (CartaVisual i : cartasVisuales) {
            if (i.getId() == id) {
                return i;
            }
        }
        return null;
    }
    
    @FXML
    private void btnDescartar(ActionEvent event) {
        if (cartaSeleccionada != null) {
            deselectCard();
            
            cartaSeleccionada.setPosX(-2);
            cartaSeleccionada.setPosY(-2);
            redimensionarCarta(cartaSeleccionada, 95, 70);
            cartaSeleccionada.getNumeroCarta().setFont(new Font("Arial Black", 20));
            //VBox.setMargin(cartaSeleccionada.getContenedor(), new Insets(0, 30, 0, 30));
            //cartaSeleccionada.setStyle("");
            cartasDescarteVisual.add(cartaSeleccionada);
            contenedorMano.getChildren().remove(cartaSeleccionada.getContenedor());
            gridMazos.add(cartaSeleccionada.getContenedor(), posXDescarte, posYDescarte);
        }
    }
    
    private void crearLabelesDescarte() {
        int row = 0;
        int colum = 1;
        for (Jugador i : partida.getJugadores()) {
            //Creacion del label
            Label label = new Label(i.getNombre());
            label.setFont(new Font("Apple Chancery", 33));
            //Se colorea blanco el del jugador
            if (i.getNombre().equals(jugador.getNombre())) {
                posXDescarte = colum;
                posYDescarte = row;
                //cartasDescarteVisual.add(label);
                label.setStyle("-fx-text-fill:#fff;");
            } else {//Negro el de los demas
                label.setStyle("-fx-text-fill:#000;");
            }
            label.setRotate(45);//Rotacion de 45 grados
            gridMazos.add(label, colum, row);
            if (colum == 1) {//Verificacion del grid para agregar en cruz
                row++;
                colum = 0;
            } else if (colum == 0) {
                colum = 2;
            } else if (colum == 2) {
                row++;
                colum = 1;
            }
            
        }
        
    }
    
    private void crearTableroDinamico() {
        gridTablero = gridDinamico.crearTablero(ROW, COLUM);
        for (int i = 0; i < ROW; i++) {
            for (int j = 0; j < COLUM; j++) {
                gridTablero.add(crearPane(), j, i);
            }
        }
        gridDinamico.setGrid(gridTablero);
        contenedorTablero.setContent(gridTablero);
    }
    
    private Pane crearPane() {
        Pane pane = new Pane();
        pane.getStyleClass().add("bg-tablero");
        pane.setOnMouseClicked((event) -> clickPane(event));
        return pane;
    }
    
    public void clickPane(Event event) {
        if (cartaSeleccionada != null) {//Si hay una carta en buffer
            int indexColum = GridPane.getColumnIndex((Node) event.getSource());
            int indexRow = GridPane.getRowIndex((Node) event.getSource());
            //se busca la carta visual
            CartaVisual carta = buscarCartaVisual(Integer.valueOf(cartaSeleccionada.getId()));
            
            if (carta != null && !CartaVisual.buscarCarta(indexRow, indexColum, cartasVisuales) && reglas(indexColum, indexRow)) {//Se le asigna la posicion donde se va a poner
                //ENVIAR MENSAJE AL SERVIDOR
                //1 arbol x en la posicion x,y
                carta.setPosX(indexColum);
                carta.setPosY(indexRow);
                deselectCard();//Se deselecciona la carta para que no quede el efecto
                //Remueve de la mano
                contenedorMano.getChildren().remove(cartaSeleccionada);
                //Anhade al tablero
                redimensionarCarta(carta, 95, 70);//Cambia el tamanho para que se ajuste al tablero
                gridTablero.add(carta.getContenedor(), indexColum, indexRow);//Se anhade la carta
                gridTablero.getChildren().remove((Node) event.getSource());//Se remueve el panel
                //Verifica si es esquina para crecer el tablero
                verificaEsquinasGrid(indexRow, indexColum);
                //Se limpia el buffer
                cartaSeleccionada = null;
            }
        }
    }
    
    private void clickCarta(CartaVisual cartaVisual) {
        if (cartaVisual.getPosX() == -1 && cartaVisual.getPosY() == -1) {
            if (cartaSeleccionada != null) {
                deselectCard();
            }
            //Buffer de la carta
            cartaSeleccionada = cartaVisual;
            cartaSeleccionada.getContenedor().setId(String.valueOf(cartaVisual.getId()));
            selectCard();
        }
    }
    
    public GridPane crearFila_Columna(int desplazamientoX, int desplazamientoY, int cantRow, int cantColum, List<CartaVisual> cartas) {
        //Se crea un nuevo grid con la cantidad de filas y columnas adicionales
        GridPane tableroNuevo = gridDinamico.crearTablero(gridTablero.getRowCount() + cantRow, gridTablero.getColumnCount() + cantColum);
        //Se desplazan las cartas en x,y
        for (CartaVisual carta : cartasVisuales) {
            //Se agrega al nuevo tablero en la nueva posicion
            if (carta.getPosX() != -1 && carta.getPosY() != -1) {
                tableroNuevo.add(carta.getContenedor(), carta.getPosX() + desplazamientoX, carta.getPosY() + desplazamientoY);
                carta.setPosX(carta.getPosX() + desplazamientoX);
                carta.setPosY(carta.getPosY() + desplazamientoY);
            }
            //tableroNuevo.add(new Button(), carta.getPosX() + desplazamientoX, carta.getPosY() + desplazamientoY);
            //Desplazamiento
        }
        //Se agregan los paneles y los botones en sus campos correspondientes
        for (int i = 0; i < tableroNuevo.getRowCount(); i++) {
            for (int j = 0; j < tableroNuevo.getColumnCount(); j++) {
                //Se verifica que no haya cartas en esa posicion
                if (!CartaVisual.buscarCarta(i, j, cartasVisuales)) {
                    //Se agrega un pane para simular el hover
                    tableroNuevo.add(crearPane(), j, i);
                }
            }
        }
        //Se cambia el gridaActual
        gridTablero = tableroNuevo;
        return gridTablero;
    }
    
    private void deselectCard() {
        cartaSeleccionada.getContenedor().setStyle("-fx-background-color: #e6e6e6;\n -fx-border-color: #000; ");
    }
    
    private void iniciarComponentes() {
        jugador = Data.getJugador();
        partida = Data.getPartida();
        if (partida != null && jugador != null) {
            lblUsuario.setText(jugador.getNombre());
            actualizarCantidadCartas();
            cargarCartasVisuales();
            partida.getJugadores().forEach((t) -> {
                if (!t.getNombre().equals(jugador.getNombre())) {
                    contenedorUsuarios.getChildren().add(new Label(t.getNombre()));
                }
            });
            crearLabelesDescarte();
        }
    }
    
    private void cargarCartasVisuales() {
        jugador.getCartas().forEach((t) -> {
            //Se crea una carta visual por cada carta logica 
            contenedorMano.getChildren().add(crearCartaVisual(t).getContenedor());
        });
    }
    
    private CartaVisual crearCartaVisual(Carta cartaLogica) {
        CartaVisual cartaVisual = new CartaVisual(cartaLogica.getArbol(), String.valueOf(cartaLogica.getNumero()));
        cartasVisuales.add(cartaVisual);
        cartaVisual.setId(cartaLogica.getId());
        cartaVisual.getContenedor().setOnMousePressed(ev -> clickCarta(cartaVisual));
        return cartaVisual;
    }
    
    private boolean reglas(int posX, int posY) {
        if (primeraCarta) {
            primeraCarta = false;
            return true;
        }
        for (CartaVisual i : cartasVisuales) {
            if (i.getPosX() != -1 && i.getPosY() != -1) {
                if (posX + 1 == i.getPosX() && posY == i.getPosY()) {//Izquierda
                    return true;
                }
                if (posX - 1 == i.getPosX() && posY == i.getPosY()) {//Derecha
                    return true;
                }
                if (posX == i.getPosX() && posY + 1 == i.getPosY()) {//Arriba
                    return true;
                }
                if (posX == i.getPosX() && posY - 1 == i.getPosY()) {//Abajo
                    return true;
                }
            }
        }
        return false;
    }

    /**
     * Busca una carta por id en la lista de cartas visuales
     *
     * @param id
     * @return
     */
    public void redimensionarCarta(CartaVisual carta, double height, double width) {
        carta.getContenedor().setPrefHeight(height);
        carta.getContenedor().prefWidth(width);
        carta.getImagenArbol().setFitHeight(height);
        carta.getImagenArbol().setFitWidth(width);
        carta.getNumeroCarta().setFont(new Font("Arial Black", 10));
    }
    
    private void selectCard() {
        cartaSeleccionada.getContenedor().setStyle("-fx-background-color: #a4740c;\n -fx-border-color: #000; ");
    }
    
    private void verificaEsquinasGrid(int indexRow, int indexColum) {
        if (indexRow == 0) {
            gridTablero = crearFila_Columna(0, 1, 1, 0, cartasVisuales);
            contenedorTablero.setContent(gridTablero);
        }
        if (indexColum == 0) {
            gridTablero = crearFila_Columna(1, 0, 0, 1, cartasVisuales);
            contenedorTablero.setContent(gridTablero);
        }
        if (indexRow == gridTablero.getRowCount() - 1) {
            gridTablero = crearFila_Columna(0, 0, 1, 0, cartasVisuales);
            contenedorTablero.setContent(gridTablero);
        }
        if (indexColum == gridTablero.getColumnCount() - 1) {
            gridTablero = crearFila_Columna(0, 0, 0, 1, cartasVisuales);
            contenedorTablero.setContent(gridTablero);
        }
    }
    
    @FXML
    private void clickMazo(MouseEvent event) {
        if (partida.getMazo().getCartas().size() != 0) {
            recogeMazoPrincipal=true;
            Carta carta = partida.getMazo().getCartas().pop();
            contenedorMano.getChildren().add(crearCartaVisual(carta).getContenedor());
            actualizarCantidadCartas();
        }
    }
    
    @FXML
    private void clickMazoDescarte(MouseEvent event) {
        if (cartasDescarteVisual.size() != 0 && !recogeMazoPrincipal) {
            CartaVisual ultima = cartasDescarteVisual.pop();
            ultima.setPosX(-1);
            ultima.setPosY(-1);
            redimensionarCarta(ultima, 200, 150);
            ultima.getNumeroCarta().setFont(new Font("Arial Black", 40));
            gridMazos.getChildren().remove(ultima.getContenedor());
            contenedorMano.getChildren().add(ultima.getContenedor());
        }else{
        recogeMazoPrincipal = false;
        }
        
    }
    private void actualizarCantidadCartas(){
        lblCantidadCartas.setText(String.valueOf(partida.getMazo().getCartas().size()));
    }
    
}
