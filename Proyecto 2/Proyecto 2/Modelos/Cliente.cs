using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proyecto_2.Modelos
{
    internal class Cliente//Peticion
    {
        private string nombre;
        private Servicio servicio;
        private DateTime tiempoLlegada;
        private bool prioritario;
        public Cliente()
        {
        }

        public Cliente(string nombre, string tipoServicio, bool prioritario)
        {
            this.nombre = nombre;
            this.tiempoLlegada = DateTime.Now;
            this.prioritario = prioritario;
            switch (tipoServicio)
            {
                case "retiro":
                    this.servicio = new Servicio("retiro", 1, 0, "caja");
                    break;
                case "deposito":
                    this.servicio = new Servicio("deposito", 1, 0, "caja");
                    break;
                case "pago de servicios publicos":
                    this.servicio = new Servicio("pago de servicios publicos", 1, 0, "caja");
                    break;
                case "pago de creditos":
                    this.servicio = new Servicio("pago de creditos", 2, 0, "caja");
                    break;
                case "solicitar tarjeta":
                    this.servicio = new Servicio("solicitar tarjeta", 4, 0, "plataforma");
                    break;
                case "formalizar credito":
                    this.servicio = new Servicio("formalizar credito", 4, 0, "plataforma");
                    break;
                case "seguridad":
                    this.servicio = new Servicio("seguridad", 2, 0, "plataforma");
                    break;
                case "desbloquear cuenta":
                    this.servicio = new Servicio("desbloquear cuenta", 2, 0, "plataforma");
                    break;
                case "cambiar pin":
                    this.servicio = new Servicio("cambiar pin", 3, 0, "plataforma");
                    break;
                case "retirar tarjeta":
                    this.servicio = new Servicio("retirar tarjeta", 4, 0, "servicio cliente");
                    break;
                case "solicitar informacion de creditos":
                    this.servicio = new Servicio("solicitar informacion de creditos", 4, 0, "servicio cliente");
                    break;
            }
        }
        public string getNombre()
        {
            return this.nombre;
        }
        public void setNombre(string nombre)
        {
            this.nombre = nombre;
        }
        public Servicio getServicio()
        {
            return this.servicio;
        }
        public void setServicio(Servicio servicio)
        {
            this.servicio = servicio;
        }
        public DateTime getTiempoLlegada()
        {
            return this.tiempoLlegada;
        }
        public void setTiempoLlegada(DateTime tiempoLlegada)
        {
            this.tiempoLlegada = tiempoLlegada;
        }
        public bool isPrioritario()
        {
            return this.prioritario;
        }
        public void setPrioritario(bool prioritario)
        {
            this.prioritario = prioritario;
        }



    }
}
