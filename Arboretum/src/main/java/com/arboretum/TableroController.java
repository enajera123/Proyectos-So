
package com.arboretum;

import java.net.URL;
import java.util.ResourceBundle;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.layout.FlowPane;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;

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
    @FXML
    private GridPane gridTablero;

    /**
     * Initializes the controller class.
     */
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        // TODO
    }    
    
}
