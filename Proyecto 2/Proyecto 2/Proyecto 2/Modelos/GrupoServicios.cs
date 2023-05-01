﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proyecto_2.Modelos
{
    internal class GrupoServicios
    {
        private Queue<Servicio> servicios;
        private Queue<Caja> cajas;
        public GrupoServicios()
        {
            servicios = new Queue<Servicio>();
            cajas = new Queue<Caja>();
        }

        public GrupoServicios(Queue<Servicio> servicios, Queue<Caja> cajas)
        {
            this.servicios = servicios;
            this.cajas = cajas;
        }
        public Queue<Caja> getCajas() {
            return this.cajas;
        }
        public void agregarCaja(Caja caja)
        {
            //Agrega a la lista y reordena
            this.cajas.Enqueue(caja);
            //ordenarClientes();
        }
        public Caja obtenerCaja()
        {
            //Obtiene el siguiente cliente de la cola
            return cajas.Dequeue();
        }
        public void agregarServicio(Servicio servicio)
        {
            //Agrega a la lista y reordena
            this.servicios.Enqueue(servicio);
          //  ordenarServicios();
        }
        public Servicio? obtenerServicio(string key)
        {
            foreach (Servicio servicio in servicios) {
                if (servicio.getNombre() == key) {
                    return servicio;
                }
            }
            return null;
        }
        

    }
}