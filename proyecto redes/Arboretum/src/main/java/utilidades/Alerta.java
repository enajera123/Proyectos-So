
package utilidades;

import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Alert;
/**
 *
 * @author estebannajera
 */
public class Alerta {
    public static void alerta(String mensaje, String titulo, AlertType tipo){
        Alert alerta = new Alert(tipo);
        alerta.setContentText(mensaje);
        alerta.setTitle(titulo);
        alerta.setHeaderText(null);
        alerta.getDialogPane().setStyle("-fx-font-family: 'Apple Chancery';"
                + "-fx-background-color: linear-gradient(#e6b850,#c48c15);");
        alerta.show();
    }
}
