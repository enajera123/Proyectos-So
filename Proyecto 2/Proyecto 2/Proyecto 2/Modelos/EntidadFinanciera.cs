using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proyecto_2.Modelos
{
    internal class EntidadFinanciera
    {
        private Queue<Peticion> peticiones;
        private Queue<GrupoServicios> gruposServicios;

        public EntidadFinanciera()
        {
            peticiones = new Queue<Peticion>();
            gruposServicios = new Queue<GrupoServicios>();
        }
        public Queue<Peticion> getPeticiones()
        {
            return peticiones;
        }
        public Queue<GrupoServicios> getGrupoServicios()
        {
            return this.gruposServicios;
        }
        public void agregarGrupoServicio(GrupoServicios grupoServicio)
        {
            gruposServicios.Enqueue(grupoServicio);
        }
        public void agregarPeticion(Peticion peticion)
        {
            peticiones.Enqueue(peticion);
        }
        public void ordernarPeticiones()
        {
            List<Peticion> lista = peticiones.OrderBy(o => o.getServicio().getPrioridad()).ThenBy(o => o.getServicio().getPeso()).ToList();
            
            peticiones.Clear();
            foreach (Peticion p in lista)
            {
                peticiones.Enqueue(p);
            }
        }
    }
}
