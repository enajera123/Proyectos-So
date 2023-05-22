package utilidades;

import javafx.scene.control.Label;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.VBox;
import javafx.scene.text.Font;

/**
 *
 * @author estebannajera
 */
public class CartaVisual {
    VBox contenedor = new VBox();
    ImageView imagenArbol = new ImageView();
    Label numeroCarta = new Label();

    public CartaVisual() {
        
        contenedor.setPrefSize(150, 200);
    }

    public CartaVisual(String nombreCarta, String numeroCarta) {
        contenedor.setPrefSize(150, 200);   
        contenedor.setStyle("background-color: #e6e6e6; border-color: #000;");
        this.imagenArbol.setImage(new Image(CartaVisual.class.getResource(nombreCarta+".png").toString()));
        imagenArbol.setFitHeight(200);
        imagenArbol.setFitWidth(150);
        this.numeroCarta.setText(numeroCarta);
        this.numeroCarta.setFont(new Font("Arial Black", 40));
        contenedor.getChildren().add(this.numeroCarta);
        contenedor.getChildren().add(this.imagenArbol);
    }

    public VBox getContenedor() {
        return contenedor;
    }

    public ImageView getImagenArbol() {
        return imagenArbol;
    }

    public Label getNumeroCarta() {
        return numeroCarta;
    }

    public void setContenedor(VBox contenedor) {
        this.contenedor = contenedor;
    }

    public void setImagenArbol(ImageView imagenArbol) {
        this.imagenArbol = imagenArbol;
    }

    public void setNumeroCarta(Label numeroCarta) {
        this.numeroCarta = numeroCarta;
    }
    
    
}
