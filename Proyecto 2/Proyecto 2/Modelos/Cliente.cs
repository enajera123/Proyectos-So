using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proyecto_2.Modelos
{
    internal class Cliente//Peticion
    {
        private string nombre { set; get; }
        private Servicio servicio { set; get; }
        private DateTime tiempoLlegada { set; get; }//Hora de peticion
        private bool isPrioritario { set; get; }//Preferencial
        public Cliente()
        {
        }

        public Cliente(string nombre, string tipoServicio, bool isPrioritario)
        {
            this.nombre = nombre;
            this.tiempoLlegada = DateTime.Now;
            this.isPrioritario = isPrioritario;
            switch (tipoServicio)
            {
                case "deposito":
                    this.servicio = new Servicio("deposito", 0, 0, "caja");
                    break;
                case "pago de servicios publicos":
                    this.servicio = new Servicio("pago de servicios publicos", 0, 0, "caja");
                    break;
                case "pago de creditos":
                    this.servicio = new Servicio("pago de creditos", 0, 0, "caja");
                    break;
                case "solicitar tarjeta":
                    this.servicio = new Servicio("solicitar tarjeta", 0, 0, "plataforma");
                    break;
                case "formalizar credito":
                    this.servicio = new Servicio("formalizar credito", 0, 0, "plataforma");
                    break;
                case "seguridad":
                    this.servicio = new Servicio("seguridad", 0, 0, "plataforma");
                    break;
                case "desbloquear cuenta":
                    this.servicio = new Servicio("desbloquear cuenta", 0, 0, "plataforma");
                    break;
                case "cambiar pin":
                    this.servicio = new Servicio("cambiar pin", 0, 0, "plataforma");
                    break;
                case "retirar tarjeta":
                    this.servicio = new Servicio("retirar tarjeta", 0, 0, "servicio cliente");
                    break;
                case "solicitar informacion de creditos":
                    this.servicio = new Servicio("solicitar informacion de creditos", 0, 0, "servicio cliente");
                    break;
            }
        }



    }
}
