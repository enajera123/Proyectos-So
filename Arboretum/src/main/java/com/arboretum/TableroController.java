package com.arboretum;

import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.ResourceBundle;
import javafx.event.Event;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.control.Button;
import javafx.scene.control.ScrollPane;
import javafx.scene.layout.FlowPane;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.Pane;
import javafx.scene.layout.VBox;
import model.CartaDto;
import utilidades.GridDinamico;

/**
 * FXML Controller class
 *
 * @author estebannajera
 */
public class TableroController implements Initializable {

    @FXML
    private VBox panelEsperando;
    @FXML
    private GridPane gridMazos;
    @FXML
    private HBox contenedorUsuarios;
    @FXML
    private FlowPane contenedorMano;
    //Objeto utilidad
    private final GridDinamico gridDinamico = new GridDinamico();
    //GridPane dinamico
    private GridPane gridTablero = new GridPane();
    //Lista de cartas dentro del grid logicamente
    private final List<CartaDto> cartas = new ArrayList();

    private final int COLUM = 17;
    private final int ROW = 6;
    @FXML
    private ScrollPane contenedorTablero;

    /**
     * Initializes the controller class.
     *
     * @param url
     * @param rb
     */
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        /**Inicia las cartas**/
        
        /**GRID**/
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
        int indexColum = GridPane.getColumnIndex((Node) event.getSource());
        int indexRow = GridPane.getRowIndex((Node) event.getSource());
        //Agrega un boton y elimina el pane
        cartas.add(new CartaDto(indexColum, indexRow));
        gridTablero.getChildren().remove((Node) event.getSource());
        gridTablero.add(new Button(), indexColum, indexRow);
        //Verifica si es esquina
        if (indexRow == 0) {
            gridTablero = crearFila_Columna(0, 1, 1, 0, cartas);
            contenedorTablero.setContent(gridTablero);
        }
        if (indexColum == 0) {
            gridTablero = crearFila_Columna(1, 0, 0, 1, cartas);
            contenedorTablero.setContent(gridTablero);
        }
        if (indexRow == gridTablero.getRowCount() - 1) {
            gridTablero = crearFila_Columna(0, 0, 1, 0, cartas);
            contenedorTablero.setContent(gridTablero);
        }
        if (indexColum == gridTablero.getColumnCount() - 1) {
            gridTablero = crearFila_Columna(0, 0, 0, 1, cartas);
            contenedorTablero.setContent(gridTablero);
        }

    }

    public GridPane crearFila_Columna(int desplazamientoX, int desplazamientoY, int cantRow, int cantColum, List<CartaDto> cartas) {
        //Se crea un nuevo grid con la cantidad de filas y columnas adicionales
        GridPane tableroNuevo = gridDinamico.crearTablero(gridTablero.getRowCount() + cantRow, gridTablero.getColumnCount() + cantColum);
        //Se desplazan las cartas en x,y
        for (CartaDto carta : cartas) {
            //Se agrega al nuevo tablero en la nueva posicion
            tableroNuevo.add(new Button(), carta.getPosX() + desplazamientoX, carta.getPosY() + desplazamientoY);
            //Desplazamiento
            carta.setPosX(carta.getPosX() + desplazamientoX);
            carta.setPosY(carta.getPosY() + desplazamientoY);

        }
        //Se agregan los paneles y los botones en sus campos correspondientes
        for (int i = 0; i < tableroNuevo.getRowCount(); i++) {
            for (int j = 0; j < tableroNuevo.getColumnCount(); j++) {
                //Se verifica que no haya cartas en esa posicion
                if (!CartaDto.buscarCarta(i, j, cartas)) {
                    //Se agrega un pane para simular el hover
                    tableroNuevo.add(crearPane(), j, i);
                }
            }
        }
        //Se cambia el gridaActual
        gridTablero = tableroNuevo;
        return gridTablero;
    }
}
