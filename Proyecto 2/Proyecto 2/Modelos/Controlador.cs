using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proyecto_2.Modelos
{
    internal class Controlador
    {
        private List<Caja> listaCajas { set; get; }
        private List<Caja> listaPlataformas { set; get; }
        private List<Caja> listaServicioCliente { set; get; }
        private List<ListaEspera> listaEsperas { set; get; }
        private int tiempoIntervalo { set; get; }

        public Controlador(List<Caja> listaCajas, List<Caja> listaPlataformas, List<Caja> listaServicioCliente, List<ListaEspera> listaEsperas, int tiempoIntervalo)
        {
            this.listaCajas = listaCajas;
            this.listaPlataformas = listaPlataformas;
            this.listaServicioCliente = listaServicioCliente;
            this.listaEsperas = listaEsperas;
            this.tiempoIntervalo = tiempoIntervalo;
        }

        public Controlador()
        {
        }
    }
}
