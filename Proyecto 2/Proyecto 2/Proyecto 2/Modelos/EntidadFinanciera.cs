using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Metadata.Ecma335;
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
            return this.peticiones;
        }
        public Queue<GrupoServicios> getGrupoServicios()
        {
            return this.gruposServicios;
        }
        public GrupoServicios identificarPeticion(Peticion peticion) {
            foreach (GrupoServicios grupo in gruposServicios) {
                if (grupo.obtenerServicio(peticion.getServicio().getNombre()) != null)
                {
                    return grupo;
                }
            }
            return null;
        }
        
        public Caja asignarPeticion(Peticion peticion)
        {
            foreach (GrupoServicios grupo in gruposServicios)
            {
                if (grupo.obtenerServicio(peticion.getServicio().getNombre()) != null)
                {
                    return grupo.agregarPeticionACaja(peticion);
                }
            }
            return null;
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
            List<Peticion> lista = peticiones.OrderBy(o=>o.getGrupoIntervalo()).ThenByDescending(o => o.isPrioritario()).ThenBy(o => o.getServicio().getPrioridad()).ThenBy(o => o.getServicio().getPeso()).ToList();
            peticiones.Clear();
            foreach (Peticion p in lista)
            {
                peticiones.Enqueue(p);
            }
        }
        public Servicio? buscarServicio(string key)
        {
            Servicio? servicio = null;
            foreach (GrupoServicios grupo in gruposServicios)
            {
                servicio = grupo.obtenerServicio(key);
                if (servicio != null)
                {
                    return servicio;
                }
            }
            return null;
        }
        public Caja? obtenerCaja(int id, int opcion)
        {
            ///Opcion 1 remueve la caja de la lista
            foreach (GrupoServicios grupo in gruposServicios)
            {
                foreach (Caja caja in grupo.getCajas())
                {
                    if (caja.getId() == id)
                    {
                        if (opcion == 1)
                        {
                            List<Caja> lista = grupo.getCajas().ToList();
                            lista.Remove(caja);
                            grupo.intercambiarListToCola(lista);
                            return caja;
                        }
                        else
                        {
                            return caja;
                        }
                    }
                }
            }
            return null;
        }
        public void setPeticiones(Queue<Peticion> peticiones) {
            this.peticiones = peticiones;
        }
        public int getCantCajasHabilitadas(String grupo) {
            int n = 0;
            foreach (GrupoServicios g in gruposServicios) {
                if (g.getNombre() == grupo) {
                    n = g.cantCajasHabilitadas();
                }
            }
            return n;
        }
        public void moverDeGrupo_actualizar(Caja actualizada)
        {
            //Mueve
            Caja? caja = obtenerCaja(actualizada.getId(), 1);
            if (caja != null)
            {
                caja.setEstado(actualizada.getEstado());
                caja.setTipoCaja(actualizada.getTipoCaja());
                foreach (GrupoServicios grupo in gruposServicios)
                {
                    if (caja.getTipoCaja() == grupo.getNombre())
                    {
                        grupo.getCajas().Enqueue(caja);
                    }
                }
            }
        }
    }
}
