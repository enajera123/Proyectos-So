package utilidades;

import javafx.geometry.HPos;
import javafx.geometry.VPos;
import javafx.scene.layout.ColumnConstraints;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.RowConstraints;

/**
 *
 * @author estebannajera
 */
public class GridDinamico {

    public GridPane grid;
    public GridPane getGrid() {
        return grid;
    }

    public void setGrid(GridPane grid) {
        this.grid = grid;
    }

    public GridPane crearTablero(int row, int colum) {
        GridPane grid = new GridPane();
        for (int i = 0; i < row; i++) {
            grid.getRowConstraints().add(crearFila());
        }
        for (int i = 0; i < colum; i++) {
            grid.getColumnConstraints().add(crearColumna());
        }
        return grid;
    }

    public RowConstraints crearFila() {
        RowConstraints row = new RowConstraints(75);
        row.setValignment(VPos.CENTER);
        return row;
    }

    public ColumnConstraints crearColumna() {
        ColumnConstraints column = new ColumnConstraints(50);
        column.setHalignment(HPos.CENTER);
        return column;
    }

    

}
