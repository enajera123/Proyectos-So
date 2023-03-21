using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proyecto_2.Modelos
{
    internal class Servicio
    {
        private string nombre { get; set; }//Nombre del Servicio
        private int prioridad { get; set; }//Prioridad del servicio(1-5)
        private int tiempoEjecucion { get; set; }//Tiempo de ejecucion del servicio
        private string tipoServicio { get; set; }//Caja,Plataforma,Servicio al cliente;

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
    }
}
