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
        private int tiempoEjecucion;//Tiempo de ejecucion del servicio
        private string tipoServicio;//Caja,Plataforma,Servicio al cliente;

        public Servicio(string nombre, int prioridad, int tiempoEjecucion, string tipoServicio)
        {
            this.nombre = nombre;
            this.prioridad = prioridad;
            this.tiempoEjecucion = tiempoEjecucion;
            this.tipoServicio = tipoServicio;
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
        public int getTiempoEjecucion()
        {
            return this.tiempoEjecucion;
        }
        public void setTiempoEjecucion(int tiempoEjecucion)
        {
            this.tiempoEjecucion = tiempoEjecucion;
        }
        public string getTipoServicio()
        {
            return this.nombre;
        }
        public void setTipoServicio(string tipoServicio)
        {
            this.tipoServicio = tipoServicio;
        }
    }
}
