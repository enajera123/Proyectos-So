module com.arboretum {
    requires javafx.controls;
    requires javafx.media;
    requires javafx.fxml;
    requires java.base;
    requires AnimateFX;
    opens com.arboretum to javafx.fxml;
    
    exports com.arboretum;
}
