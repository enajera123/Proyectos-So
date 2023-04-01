using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proyecto_2.Modelos
{
    internal class ListaEspera
    {
        private Queue<Servicio> serviciosEspera;
        private Queue<Cliente> clientesEspera;
        public ListaEspera()
        {
            serviciosEspera = new Queue<Servicio>();
            clientesEspera = new Queue<Cliente>();
        }

        public ListaEspera(Queue<Servicio> serviciosEspera, Queue<Cliente> clientesEspera)
        {
            this.serviciosEspera = serviciosEspera;
            this.clientesEspera = clientesEspera;
        }
        public Queue<Cliente> getClientesEspera() {
            return this.clientesEspera;
        }
        public void agregarCliente(Cliente cliente)
        {
            //Agrega a la lista y reordena
            clientesEspera.Enqueue(cliente);
            ordenarClientes();
        }
        public Cliente obtenerCliente()
        {
            //Obtiene el siguiente cliente de la cola
            return clientesEspera.Dequeue();
        }
        public void agregarServicio(Servicio servicio)
        {
            //Agrega a la lista y reordena
            serviciosEspera.Enqueue(servicio);
            ordenarServicios();
        }
        public Servicio obtenerServicio()
        {
            //Agrega a la lista y reordena
            return serviciosEspera.Dequeue();
        }
        public void ordenarServicios() {
            serviciosEspera = new Queue<Servicio>(serviciosEspera.OrderBy(s => s.getPrioridad()));
        }
        public void ordenarClientes() {
            clientesEspera = new Queue<Cliente>(clientesEspera.OrderBy(s => s.getServicio().getPrioridad()));
        }

    }
}
