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
        private ListaEspera listaEsperas { set; get; }
        private int tiempoIntervalo { set; get; }

        public Controlador(List<Caja> listaCajas, List<Caja> listaPlataformas, List<Caja> listaServicioCliente, ListaEspera listaEsperas, int tiempoIntervalo)
        {
            this.listaCajas = listaCajas;
            this.listaPlataformas = listaPlataformas;
            this.listaServicioCliente = listaServicioCliente;
            this.listaEsperas = listaEsperas;
            this.tiempoIntervalo = tiempoIntervalo;
        }

        public Controlador()
        {
            this.listaCajas = new List<Caja>();
            this.listaPlataformas = new List<Caja>();
            this.listaServicioCliente = new List<Caja>();
            this.listaEsperas = new ListaEspera();
            this.tiempoIntervalo = 0;
        }
        public ListaEspera getListaEspera() {
            return this.listaEsperas;
        }
        public void registrarPeticion(Cliente cliente) {
            //Registra en la lista indicada
            listaEsperas.agregarCliente(cliente);
        }
        public void atenderPeticiones() { 
            //atiende en orden de prioridad y tiempo de llegada
            //Hilos
        }
    }
}
