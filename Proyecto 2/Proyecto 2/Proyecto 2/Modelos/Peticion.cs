using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proyecto_2.Modelos
{
    internal class Peticion//Peticion
    {
        private int grupoIntervalo;
        private string nombre;
        private Servicio servicio;
        // private TimeSpan tiempoLlegada;
        private bool prioritario;
        //private bool cambiado;
        private String subioProridad;
        public Peticion()
        {
        }

        public Peticion(string nombre, Servicio servicio, bool prioritario)
        {
            //cambiado = false;
            subioProridad = "0:0";
            this.nombre = nombre;
            //this.tiempoLlegada = TimeSpan.FromMinutes(5);
            this.prioritario = prioritario;
            this.servicio = servicio;

        }
        public string getNombre()
        {
            return this.nombre;
        }
        public void setGrupoIntervalo(int grupo)
        {
            this.grupoIntervalo = grupo;
        }
        public int getGrupoIntervalo()
        {
            return this.grupoIntervalo;
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
        /*        public DateTime getTiempoLlegada()
                {
                    return this.tiempoLlegada;
                }
                public void setTiempoLlegada(DateTime tiempoLlegada)
                {
                    this.tiempoLlegada = tiempoLlegada;
                }*/
        public bool isPrioritario()
        {
            return this.prioritario;
        }
        public void setPrioritario(bool prioritario)
        {
            this.prioritario = prioritario;
        }
        public void subirPrioridad(DateTime horaActual, DateTime horaSistema, int intervaloTiempo)
        {
            //GRUPO: Identificar el intervalo
            //RESAGO
            TimeSpan diferencia = horaActual - horaSistema;
            int resago = diferencia.Minutes / intervaloTiempo;
            String[] array = subioProridad.Split(":");
            resago = resago - grupoIntervalo;
            if ((resago / 2).ToString() == array[0] && array[1] == "0")
            {
                if (/*!cambiado &&*/ (resago / 2) > 0 && servicio.getPrioridad() != 1)
                {
                    servicio.setPrioridad(servicio.getPrioridad() - 1);
                    subioProridad = resago / 2 + ":" + 1;
                    //    cambiado = true;
                }
            }
            else if ((resago / 2).ToString() != array[0])
            {
                subioProridad = resago / 2 + ":" + 0;
            }
        }

    }
}

