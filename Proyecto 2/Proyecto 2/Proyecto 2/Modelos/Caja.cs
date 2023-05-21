using System;
using System.Collections.Generic;
using System.Drawing.Printing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proyecto_2.Modelos
{
    internal class Caja
    {
        private Peticion peticionActual;
        private int id;
        private string tipoCaja;
        private bool estado;
        private List<Peticion> peticionesProcesadas;

        public Caja(string tipoCaja)
        {
            int id = 0;
            this.tipoCaja = tipoCaja;
            this.estado = true;
            peticionActual = null;
            peticionesProcesadas = new List<Peticion>();
        }
        public Caja(string tipoCaja, int id)
        {
            this.id = id;
            this.tipoCaja = tipoCaja;
            this.estado = true;
            peticionActual = null;
            peticionesProcesadas = new List<Peticion>();
        }
        public Caja()
        {
            peticionActual = null;
            peticionesProcesadas = new List<Peticion>();
        }
        public void setPeticionProcesada(Peticion peticion)
        {
            peticionesProcesadas.Add(peticion);
        }
        public void eliminarPeticion()
        {
            if (peticionActual != null)
            {
                peticionesProcesadas.Add(peticionActual);
                peticionActual = null;
            }
        }
        public List<Peticion> getPeticionesProcesadas()
        {
            return this.peticionesProcesadas;
        }
        public bool getEstado()
        {
            return estado;
        }
        public void setEstado(bool estado)
        {
            this.estado = estado;
        }
        public int getId()
        {
            return id;
        }
        public string getTipoCaja()
        {
            return this.tipoCaja;
        }
        public void setTipoCaja(string tipoCaja)
        {
            this.tipoCaja = tipoCaja;
        }
        public void agregarPeticion(Peticion peticion)
        {
            peticionActual = peticion;
        }
        public Peticion obtenerPeticion()
        {
            return this.peticionActual;
        }
        public void setPeticion(Peticion peticion)
        {
            peticionActual = peticion;
        }
    }
}
