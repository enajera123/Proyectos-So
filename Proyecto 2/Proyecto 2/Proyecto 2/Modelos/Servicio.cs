using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proyecto_2.Modelos
{
    internal class Servicio
    {
        private string nombre;//Nombre del Servicio
        private int prioridad;//Prioridad del servicio(1-5)
        private int peso;
        //private int tiempoEjecucion;//Tiempo de ejecucion del servicio
        //private string tipoServicio;//Caja,Plataforma,Servicio al cliente;

        public Servicio(string nombre, int peso, int prioridad)
        {
            this.nombre = nombre;
            this.prioridad = prioridad;
            this.peso = peso;
        }
        public Servicio()
        {
        }
        public string getNombre()
        {
            return this.nombre;
        }
        public void setNombre(string nombre)
        {
            this.nombre = nombre;
        }
        public int getPrioridad()
        {
            return this.prioridad;
        }
        public void setPrioridad(int prioridad)
        {
            this.prioridad = prioridad;
        }
        public void setPeso(int peso)
        {
            this.peso = peso;

        }
        public int getPeso()
        {
            return this.peso;
        }
    }
}
