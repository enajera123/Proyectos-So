package utilidades;

import java.util.List;
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

    private int id;
    private int posX;
    private int posY;
    VBox contenedor = new VBox();
    ImageView imagenArbol = new ImageView();
    Label numeroCarta = new Label();

    public CartaVisual() {
        posX = -1;
        posY = -1;
        contenedor.setPrefSize(150, 200);
    }

    public CartaVisual(String nombreCarta, String numeroCarta) {
        posX = -1;
        posY = -1;
        contenedor.setPrefSize(150, 200);
        contenedor.setStyle("-fx-background-color: #e6e6e6; -fx-border-color: #000;");
        //contenedor.getStylesheets().add("carta");
        this.imagenArbol.setImage(new Image(CartaVisual.class.getResource("/img/cartas/" + nombreCarta + ".png").toString()));
        imagenArbol.setFitHeight(200);
        imagenArbol.setFitWidth(150);
        this.numeroCarta.setText(numeroCarta);
        this.numeroCarta.setFont(new Font("Arial Black", 40));
        contenedor.getChildren().add(this.numeroCarta);
        contenedor.getChildren().add(this.imagenArbol);
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getId() {
        return id;
    }

    public int getPosX() {
        return posX;
    }

    public int getPosY() {
        return posY;
    }

    public void setPosX(int posX) {
        this.posX = posX;
    }

    public void setPosY(int posY) {
        this.posY = posY;
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

    public static boolean buscarCarta(int i, int j, List<CartaVisual> cartas) {
        for (CartaVisual carta : cartas) {
            if (carta.getPosX() == j && carta.getPosY() == i) {
                return true;
            }
        }
        return false;
    }
    

}
