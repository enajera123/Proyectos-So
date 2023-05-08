module com.arboretum {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.base;

    opens com.arboretum to javafx.fxml;
    
    exports com.arboretum;
}
