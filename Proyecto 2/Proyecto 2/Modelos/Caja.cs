using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proyecto_2.Modelos
{
    internal class Caja
    {
        private int id { set; get; }
        private string tipoServicio { set; get; }
        private bool estado { set; get; }
        private Servicio servicioActual { set; get; }
        private int tiempoAtencion { set; get; }

        public Caja(int id, string tipoServicio, bool estado, Servicio servicioActual, int tiempoAtencion)
        {
            this.id = id;
            this.tipoServicio = tipoServicio;
            this.estado = estado;
            this.servicioActual = servicioActual;
            this.tiempoAtencion = tiempoAtencion;
        }

        public Caja()
        {
        }
    }
}
