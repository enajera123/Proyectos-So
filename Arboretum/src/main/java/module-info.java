module com.arboretum {
    requires javafx.controls;
    requires javafx.media;
    requires javafx.fxml;
    requires java.base;
    requires AnimateFX;
    requires com.fasterxml.jackson.databind;
    opens model to com.fasterxml.jackson.databind;//---
    opens com.arboretum to javafx.fxml;
    exports model;
    exports com.arboretum;
}
