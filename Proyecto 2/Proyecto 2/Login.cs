using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Proyecto_2
{
    public partial class Login : Form
    {        
        Button botonSeleccionado;
        Panel? panelSeleccionado;
        public Login()
        {
            InitializeComponent();
        }

        private void btnMenos_Click(object sender, EventArgs e)
        {

        }

        private void btnGrupo1_Click(object sender, EventArgs e)
        {
            asignarDatos(btnGrupo1,panelSubMenu1);
        }

        private void btnServicio1_Click(object sender, EventArgs e)
        {
            asignarDatos(btnServicio1,null);
        }

        private void btnServicio2_Click(object sender, EventArgs e)
        {
            asignarDatos(btnServicio2,null);
        }

        private void btnServicio3_Click(object sender, EventArgs e)
        {
            asignarDatos(btnServicio3,null);
        }

        private void btnServicio4_Click(object sender, EventArgs e)
        {
            asignarDatos(btnServicio4,null);
        }

        private void btnGrupo2_Click(object sender, EventArgs e)
        {
            asignarDatos(btnGrupo2, panelSubMenu2);
        }

        private void btnServicio5_Click(object sender, EventArgs e)
        {
            asignarDatos(btnServicio5,null);
        }

        private void btnServicio6_Click(object sender, EventArgs e)
        {
            asignarDatos(btnServicio6,null);
        }

        private void btnServicio7_Click(object sender, EventArgs e)
        {
            asignarDatos(btnServicio7,null);
        }

        private void btnServicio8_Click(object sender, EventArgs e)
        {
            asignarDatos(btnServicio8,null);
        }

        private void btnServicio9_Click(object sender, EventArgs e)
        {
            asignarDatos(btnServicio9,null);
        }

        private void btnGrupo3_Click(object sender, EventArgs e)
        {
            asignarDatos(btnGrupo3, panelSubMenu3);
            
        }

        private void btnServicio10_Click(object sender, EventArgs e)
        {
            asignarDatos(btnServicio10,null);
        }

        private void btnServicio11_Click(object sender, EventArgs e)
        {
            asignarDatos(btnServicio11, null);
        }
        private void btnHabilitado_CheckedChanged(object sender, EventArgs e)
        {
            if (botonSeleccionado != null) {
                if (btnHabilitado.Checked == false)
                {
                    if (panelSeleccionado != null) {
                        panelSeleccionado.Enabled = false;//255; 192; 192
                        panelSeleccionado.BackColor = Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(192)))), ((int)(((byte)(192)))));
                    }
                    
                }
                else {
                    if (panelSeleccionado != null)
                    {
                        panelSeleccionado.Enabled = true;
                    }
                    botonSeleccionado.Enabled = true;
                    

                }
            }
        }
        private void asignarDatos(Button boton,Panel? panel )
        {
            botonSeleccionado = boton;
            txtNombre.Text = boton.Text;
            panelSeleccionado = panel;
            
        }
        private void btnActualizar_Click(object sender, EventArgs e)
        {

        }
    }
}
