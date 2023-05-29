package com.arboretum;

import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.ResourceBundle;
import java.util.Stack;
import javafx.application.Platform;
import javafx.event.ActionEvent;
import javafx.event.Event;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ScrollPane;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.Pane;
import javafx.scene.layout.StackPane;
import javafx.scene.layout.VBox;
import javafx.scene.text.Font;
import model.Carta;
import model.Jugador;
import model.Partida;
import utilidades.Alerta;
import utilidades.CartaVisual;
import utilidades.Data;
import utilidades.GridDinamico;
import utilidades.MazoDescarteVisual;
import utilidades.Servidor;

/**
 * FXML Controller class
 *
 * @author estebannajera
 */
public class TableroController implements Initializable {

    private GridPane gridMazos;
    @FXML
    private Label lblUsuario;
    @FXML
    private HBox contenedorUsuarios;
    @FXML
    private HBox contenedorMano;
    @FXML
    private ScrollPane contenedorTablero;
    private Label lblCantidadCartas;
    private Button btnDescartar;
    private VBox panelMensaje;
    private Label lblMensaje;
    //OBJETOS UTILIDADES
    private final GridDinamico gridDinamico = new GridDinamico();
    ///////////////////
    //OBJETOS NECESARIOS
    private Jugador jugador;
    private Partida partida;
    private Servidor servidor;
    //////////////////////
    private List<CartaVisual> cartasVisuales = new ArrayList();//Lista de cartas dentro del grid logicamente
    private final int COLUM = 17;//Tamano del grid inicials
    private final int ROW = 6;//Tamano del grid inicial
    private List<MazoDescarteVisual> mazosDescarteVisual = new Stack<>();
    private CartaVisual cartaSeleccionada = null;
    private GridPane gridTablero = new GridPane();
    //BANDERAS
    private boolean primeraCarta = true;//Verifica si es la primera carta que se pone
    private int cantidadCartasRecogidas = 2;//Cantidad de cartas que puede recoger
    private int cartasPorPoner = 1;//Cantidad de cartas que puede poner
    //HILOS
    private int muerteHilo = -1;
    Thread hiloEsperar;
    private final Object lock = new Object();

    /**
     * Initializes the controller class.
     *
     * @param url
     * @param rb
     */
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        /**
         * Inicia los hilos
         */

        hiloEsperar = new Thread(() -> {
            try {
                Partida p;
                while (muerteHilo != -1) {
                    p = servidor.getPartida();
                    if (p != null) {
                        System.out.println(p.getJugadorActual().getNombre());
                        if (p.getJugadorActual().getNombre().equals(jugador.getNombre())) {
                            partida = p;
                            Platform.runLater(() -> {
                                quitarMensajeEsperar();
                            });
                            synchronized (lock) {
                                try {
                                    System.out.println("esperaHilo");
                                    lock.wait();
                                    System.out.println("libera");
                                } catch (Exception ex) {
                                    System.out.println(ex.toString());

                                }
                            }
                        }
                    }
                }

            } catch (Exception ex) {
                System.out.println(ex.toString());
            }
        });

        /**
         * Inicia las cartas*
         */
        iniciarComponentes();

        /**
         * GRID*
         */
        crearTableroDinamico();
    }

    private void clickMazo(MouseEvent event) {
        if (!partida.getMazo().getCartas().isEmpty() && cantidadCartasRecogidas > 0) {
            cantidadCartasRecogidas--;
            Carta carta = partida.getMazo().getCartas().pop();
            partida.setCartaJugador(jugador.getNombre(), carta);
            servidor.agregarCarta(jugador.getNombre(), carta.getId());
            contenedorMano.getChildren().add(crearCartaVisual(carta).getContenedor());
            actualizarCantidadCartas();
            verificarFinTurno();
        }
    }

    private void btnDescartar(ActionEvent event) {
        if (cartaSeleccionada != null) {
            deselectCard();
            btnDescartar.setDisable(true);
            actualizarPartida(servidor.descartarCarta(jugador.getNombre(), cartaSeleccionada.getId()));
            verificarFinTurno();
        }
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
            cargarMazosDescarte();
            cargarMano(jugador);
            return true;
        }
        return false;
    }

    public void clickPane(Event event) {
        if (cartaSeleccionada != null && cartasPorPoner > 0) {//Si hay una carta en buffer
            int indexColum = GridPane.getColumnIndex((Node) event.getSource());
            int indexRow = GridPane.getRowIndex((Node) event.getSource());
            //se busca la carta visual
            CartaVisual cartaVisual = buscarCartaVisual(cartaSeleccionada.getId());
            if (cartaVisual != null && !CartaVisual.buscarCarta(indexRow, indexColum, cartasVisuales) && reglas(indexColum, indexRow)) {//Se le asigna la posicion donde se va a poner
                //ENVIAR MENSAJE AL SERVIDOR
                Partida partidaActualizada = servidor.agregarCartaTablero(jugador.getNombre(), cartaVisual.getId(), indexColum, indexRow);
                if (partidaActualizada != null) {
                    //contenedorMano.getChildren().remove(cartaSeleccionada.getContenedor());
                    actualizarPartida(partidaActualizada);
                    cartasPorPoner--;
                    //Verifica si es esquina para crecer el tablero
                    verificaEsquinasGrid(indexRow, indexColum);
                    //Se limpia el buffer
                    cartaSeleccionada = null;
                    verificarFinTurno();
                } else {
                    Alerta.alerta("Error al modificar la partida", "error", Alert.AlertType.ERROR);
                }
            }
        }
    }

    private void clickCartaDescarte(MazoDescarteVisual mazoDescarte) {
        if (!mazoDescarte.getCartas().isEmpty() && cantidadCartasRecogidas > 0) {
            CartaVisual ultima = mazoDescarte.getCartas().pop();
            actualizarPartida(servidor.sacarCartaDescarte(mazoDescarte.getNombre(), ultima.getId()));
            cantidadCartasRecogidas--;
            verificarFinTurno();
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
        if (jugadorACargar.getNombre().equals(jugador.getNombre())) {//Si es el mismo
            actualizarPartida(partida);//Simplemente se actualiza la partida
            gridMazos.setDisable(false);//Se habilita los mazos de descarte
        } else {
            contenedorMano.getChildren().clear();//Se borra la mano
            cargarTablero(jugadorACargar);//Se carga el tablero del jugador a cargar
            cargarMazosDescarte();//Cargan nuevamente los mazos de descarte
            gridMazos.setDisable(true);//Se deshabilitan los mazos con el fin de que no pueda realizar acciones
        }
    }

    private void cargarCartasVisuales() {
        jugador.getCartas().forEach((t) -> {
            //Se crea una carta visual por cada carta logica 
            contenedorMano.getChildren().add(crearCartaVisual(t).getContenedor());
        });
    }

    /**
     * Crea una carta visual para poder agregar al tablero, mazo o mano
     *
     * @param cartaLogica
     * @return
     */
    private CartaVisual crearCartaVisual(Carta cartaLogica) {
        CartaVisual cartaVisual = new CartaVisual(cartaLogica.getArbol(), String.valueOf(cartaLogica.getNumero()));
        cartasVisuales.add(cartaVisual);
        cartaVisual.getContenedor().getStyleClass().add("drop-shadow");
        cartaVisual.setId(cartaLogica.getId());
        cartaVisual.setPosX(cartaLogica.getPosX());
        cartaVisual.setPosY(cartaLogica.getPosY());
        cartaVisual.getContenedor().setOnMousePressed(ev -> clickCarta(cartaVisual));//Agrega un evento del click para la carta
        return cartaVisual;
    }

    private void deselectCard() {
        cartaSeleccionada.getContenedor().setStyle("-fx-background-color: #e6e6e6;\n -fx-border-color: #000; ");
    }

    private void iniciarComponentes() {
        jugador = Data.getJugador();
        partida = Data.getPartida();
        servidor = Data.getSevidor();
        if (partida != null && jugador != null) {

            if (partida.getJugadorActual() != null && !jugador.getNombre().equals(partida.getJugadorActual().getNombre())) {
                mostrarMensajeEsperar();
            }
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
            crearLabelesDescarte();
        }
    }

    //UTILIDADES
    /**
     * Actualiza el label con la cantidad de cartas
     */
    private void actualizarCantidadCartas() {
        lblCantidadCartas.setText(String.valueOf(partida.getMazo().getCartas().size()));
    }

    private CartaVisual buscarCartaVisual(int id) {
        for (CartaVisual i : cartasVisuales) {
            if (i.getId() == id) {
                return i;
            }
        }
        return null;
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
     * Obtiene la posicion maxima de la lista de cartas del jugador
     *
     * @param direccion 0-> En X: 1-> en Y
     * @return
     */
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

    /**
     * Crea labeles que se ponen para identificar el mazo de descarte de cada
     * jugador
     */
    private void crearLabelesDescarte() {
        int row = 0;
        int colum = 1;
        mazosDescarteVisual = new ArrayList<>();
        for (Jugador i : partida.getJugadores()) {
            //Creacion del label
            Label label = new Label(i.getNombre());
            label.setFont(new Font("Apple Chancery", 33));
            //Se colorea blanco el del jugador
            if (i.getNombre().equals(jugador.getNombre())) {
                //cartasDescarteVisual.add(label);
                label.setStyle("-fx-text-fill:#fff;");
            } else {//Negro el de los demas
                label.setStyle("-fx-text-fill:#000;");
            }
            label.setRotate(45);//Rotacion de 45 grados
            //  label.setOnMouseClicked(t->clickCartaDescarte(t));
            mazosDescarteVisual.add(new MazoDescarteVisual(label.getText(), colum, row));
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

    private void cargarMazosDescarte() {
        Node mazoPrincipal = null;//Se debe salvar el mazo principal
        for (Node i : gridMazos.getChildren()) {
            if (i instanceof StackPane) {
                mazoPrincipal = i;
            }
        }
        gridMazos.getChildren().clear();
        gridMazos.add(mazoPrincipal, 1, 1);//Se anhade el mazo principal
        crearLabelesDescarte();//Se crean los labeles
        int row = 0;
        int colum = 1;
        for (Jugador i : partida.getJugadores()) {
            for (Carta c : i.getDescartes()) {
                CartaVisual carta = crearCartaVisual(c);
                MazoDescarteVisual mazoDescarteVisual = getMazoDescarteJugador(i.getNombre());
                if (mazoDescarteVisual != null) {
                    mazoDescarteVisual.getCartas().add(carta);
                    carta.getContenedor().setOnMouseClicked(t -> clickCartaDescarte(mazoDescarteVisual));
                    redimensionarCarta(carta, 75, 90, 15);
                    gridMazos.add(carta.getContenedor(), colum, row);
                }
            }
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
        actualizarCantidadCartas();
    }

    private MazoDescarteVisual getMazoDescarteJugador(String nombre) {
        for (MazoDescarteVisual i : mazosDescarteVisual) {
            if (i.getNombre().equals(nombre)) {
                return i;
            }
        }
        return null;
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

    /**
     * Crea un pane con disenho de hover para agregar al tablero
     *
     * @return
     */
    private Pane crearPane() {
        Pane pane = new Pane();
        pane.getStyleClass().add("bg-tablero");
        pane.setOnMouseClicked((event) -> clickPane(event));
        return pane;
    }

    /**
     * Verifica si la carta es adyacente y si es la primera carta
     *
     * @param posX
     * @param posY
     * @return
     */
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
    public void redimensionarCarta(CartaVisual carta, double height, double width, int fuente) {
        carta.getContenedor().setPrefHeight(height);
        carta.getContenedor().prefWidth(width);
        carta.getImagenArbol().setFitHeight(height);
        carta.getImagenArbol().setFitWidth(width);
        carta.getNumeroCarta().setFont(new Font("Arial Black", fuente));
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

    private void verificarFinTurno() {
        if (cantidadCartasRecogidas == 0 && cartasPorPoner == 0 && btnDescartar.isDisable()) {
            partida = servidor.cambiarTurno();
            mostrarMensajeEsperar();
            verificaFinPartida();
        }
    }

    private void mostrarMensajeEsperar() {
        if (muerteHilo == -1) {
            hiloEsperar.start();
            muerteHilo = 1;
        } else {
            reanudarHilo();
        }
        lblMensaje.setText("Esperando Turno");
        panelMensaje.toFront();
        contenedorMano.setDisable(true);
    }

    /**
     * Reanuda el hilo de verificacion de turno
     */
    private void reanudarHilo() {
        synchronized (lock) {
            try {
                lock.notify();
            } catch (Exception ex) {
                System.out.println(ex.toString());
            }
        }
    }

    private void quitarMensajeEsperar() {
        actualizarPartida(partida);//Se actualiza la partida una vez que se inicia el turno
        panelMensaje.toBack();
        contenedorMano.setDisable(false);
        cantidadCartasRecogidas = 2;//Se actualizan los contadores
        cartasPorPoner = 1;
        btnDescartar.setDisable(false);
    }

    public GridPane crearFila_Columna(int desplazamientoX, int desplazamientoY, int cantRow, int cantColum, List<CartaVisual> cartas) {
        //Se crea un nuevo grid con la cantidad de filas y columnas adicionales
        GridPane tableroNuevo = gridDinamico.crearTablero(gridTablero.getRowCount() + cantRow, gridTablero.getColumnCount() + cantColum);
        //Se desplazan las cartas en x,y
        for (CartaVisual carta : cartasVisuales) {
            //Se agrega al nuevo tablero en la nueva posicion
            if (carta.getPosX() != -1 && carta.getPosY() != -1 && carta.getPosX() != -2 && carta.getPosY() != -2) {
                tableroNuevo.add(carta.getContenedor(), carta.getPosX() + desplazamientoX, carta.getPosY() + desplazamientoY);
                //Se actualizan los datos logicos
                jugador.modificarPosicionCartasEnTablero(carta.getId(), carta.getPosX() + desplazamientoX, carta.getPosY() + desplazamientoY);
                partida = servidor.modificarCartaTablero(jugador.getNombre(), carta.getId(), carta.getPosX() + desplazamientoX, carta.getPosY() + desplazamientoY);
                carta.setPosX(carta.getPosX() + desplazamientoX);
                carta.setPosY(carta.getPosY() + desplazamientoY);
            }
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

    private void verificaFinPartida() {
        //Se deben detener los hilos
        //Se puntuan los caminos
        //Se determina quien puede puntuar
        //Se determina el ganador
        //FIN
        if(partida.getMazo().getCartas().isEmpty()){
            servidor.terminarPartida();
        }
    }
}
