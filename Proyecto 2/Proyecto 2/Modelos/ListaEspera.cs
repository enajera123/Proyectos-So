using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proyecto_2.Modelos
{
    internal class ListaEspera
    {
        private List<Servicio> serviciosEspera { set; get; }
        private List<Cliente> clientesEspera { set; get; }

        public ListaEspera()
        {
        }

        public ListaEspera(List<Servicio> serviciosEspera, List<Cliente> clientesEspera)
        {
            this.serviciosEspera = serviciosEspera;
            this.clientesEspera = clientesEspera;
        }
        public void agregarCliente(Cliente cliente) { 
            //Agrega a la lista y reordena
        }
        public Cliente obtenerCliente() {
            //Obtiene el siguiente cliente de la cola
            return new Cliente();
        }
    }
}
