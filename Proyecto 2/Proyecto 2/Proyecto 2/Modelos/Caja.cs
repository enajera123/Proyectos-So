using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proyecto_2.Modelos
{
    internal class Caja
    {
        private Queue<Peticion> peticiones;
        private string tipoCaja;
        public Caja(string tipoCaja)
        {
           this.tipoCaja = tipoCaja;
        }

        public Caja()
        {
        }
        public string getTipoCaja() {
            return this.tipoCaja;
        }
        public void setTipoCaja(string tipoCaja)
        {
            this.tipoCaja = tipoCaja;
        }
        public void agregarPeticion(Peticion peticion) {
            peticiones.Enqueue(peticion);
        }
        public Peticion obtenerPeticion() {
            return peticiones.Dequeue();
        }
    }
}
