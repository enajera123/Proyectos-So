/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package model;

import java.util.List;

/**
 *
 * @author estebannajera
 */
public class CartaDto {

    private int posX;
    private int posY;

    private int id;
    private String arbol;
    private int numero;
    //private List<Carta> cartasAdyacentes; 

    public CartaDto() {
    }

    public CartaDto(int posX, int posY) {
        this.posX = posX;
        this.posY = posY;
    }

    public CartaDto(int id, String arbol, int numero) {
        this.id = id;
        this.arbol = arbol;
        this.numero = numero;
    }

    public void setPosY(int posY) {
        this.posY = posY;
    }

    public void setPosX(int posX) {
        this.posX = posX;
    }

    public int getPosY() {
        return posY;
    }

    public int getPosX() {
        return posX;
    }

    public String getArbol() {
        return arbol;
    }

    public int getId() {
        return id;
    }

    public int getNumero() {
        return numero;
    }

    public void setArbol(String arbol) {
        this.arbol = arbol;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public static boolean buscarCarta(int i, int j, List<CartaDto> cartas) {
        for (CartaDto carta : cartas) {
            if (carta.getPosX() == j && carta.getPosY() == i) {
                return true;
            }
        }
        return false;
    }

}
