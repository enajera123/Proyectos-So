using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proyecto_2.Modelos
{
    internal class Peticion//Peticion
    {
        private string nombre;
        private Servicio servicio;
        private DateTime tiempoLlegada;
        private bool prioritario;
        public Peticion()
        {
        }

        public Peticion(string nombre, Servicio servicio, bool prioritario)
        {
            this.nombre = nombre;
            this.tiempoLlegada = DateTime.Now;
            this.prioritario = prioritario;
            this.servicio = servicio;

        }
        public string getNombre()
        {
            return this.nombre;
        }
        public void setNombre(string nombre)
        {
            this.nombre = nombre;
        }
        public Servicio getServicio()
        {
            return this.servicio;
        }
        public void setServicio(Servicio servicio)
        {
            this.servicio = servicio;
        }
        public DateTime getTiempoLlegada()
        {
            return this.tiempoLlegada;
        }
        public void setTiempoLlegada(DateTime tiempoLlegada)
        {
            this.tiempoLlegada = tiempoLlegada;
        }
        public bool isPrioritario()
        {
            return this.prioritario;
        }
        public void setPrioritario(bool prioritario)
        {
            this.prioritario = prioritario;
        }



    }
}
