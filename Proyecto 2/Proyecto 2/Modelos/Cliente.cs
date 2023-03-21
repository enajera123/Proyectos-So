using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proyecto_2.Modelos
{
    internal class Cliente
    {
        private string nombre { set; get; }
        private string tipoServicio { set; get; }
        private int prioridad { set; get; }
        private DateTime tiempoLlegada { set; get; }
        private bool isPrioritario { set; get; }
        public Cliente()
        {
        }

        public Cliente(string nombre, string tipoServicio, int prioridad, DateTime tiempoLlegada, bool isPrioritario)
        {
            this.nombre = nombre;
            this.tipoServicio = tipoServicio;
            this.prioridad = prioridad;
            this.tiempoLlegada = tiempoLlegada;
            this.isPrioritario = isPrioritario;
        }



    }
}
