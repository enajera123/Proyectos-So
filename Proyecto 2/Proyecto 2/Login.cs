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


        public Login()
        {
            InitializeComponent();
        }
        /**UTILIDADES**/
        private void asignarDatos(Button boton, Panel? panel)
        {
            //Variables buffer
            botonSeleccionado = boton;
            txtNombre.Text = boton.Text;
            panelSeleccionado = panel;
            //Se modifica el check
            if (botonSeleccionado.BackColor == colorDeshabilitado)
            {
                btnHabilitado.Checked = false;
            }
            else
            {
                btnHabilitado.Checked = true;
            }
            //Se modifica la cantidad de cajas y el panel
            if (botonSeleccionado.Name.Contains("Grupo"))
            {
                panelIzquierdoInferior.Visible = true;
                if (botonSeleccionado.Name.Contains("Grupo1"))
                {
                    txtCantidad.Text = cajasGrupo1.ToString();
                }
                else if (botonSeleccionado.Name.Contains("Grupo2"))
                {
                    txtCantidad.Text = cajasGrupo2.ToString();
                }
                else
                {
                    txtCantidad.Text = cajasGrupo3.ToString();
                }
            }
            else
            {
                panelIzquierdoInferior.Visible = false;
            }

        }
        private bool setCantidadCajas(int min, int max, int n, char operacion)
        {

            switch (operacion)
            {
                case '+':
                    if (n < max)
                    {
                        txtCantidad.Text = (n + 1).ToString();
                        return true;
                    }
                    return false;
                case '-':
                    if (n > min)
                    {
                        txtCantidad.Text = (n - 1).ToString();
                        return true;
                    }
                    return false;
                default:
                    return false;
            }
        }
        /**EVENTOS**/
        private void btnMenos_Click(object sender, EventArgs e)
        {
            if (botonSeleccionado.Name.Contains("Grupo1") && setCantidadCajas(2, 3, Convert.ToInt16(txtCantidad.Text), '-'))
            {
                cajasGrupo1--;
            }
            if (botonSeleccionado.Name.Contains("Grupo2") && setCantidadCajas(2, 3, Convert.ToInt16(txtCantidad.Text), '-'))
            {
                cajasGrupo2--;
            }
            if (botonSeleccionado.Name.Contains("Grupo3") && setCantidadCajas(1, 3, Convert.ToInt16(txtCantidad.Text), '-'))
            {
                cajasGrupo3--;
            }
        }
        private void btnMas_Click(object sender, EventArgs e)
        {
            if (botonSeleccionado.Name.Contains("Grupo1") && setCantidadCajas(2, 3, Convert.ToInt16(txtCantidad.Text), '+'))
            {
                cajasGrupo1++;
            }
            if (botonSeleccionado.Name.Contains("Grupo2") && setCantidadCajas(2, 3, Convert.ToInt16(txtCantidad.Text), '+'))
            {
                cajasGrupo2++;
            }
            if (botonSeleccionado.Name.Contains("Grupo3") && setCantidadCajas(1, 3, Convert.ToInt16(txtCantidad.Text), '+'))
            {
                cajasGrupo3++;
            }
        }

        private void btnGrupo1_Click(object sender, EventArgs e)
        {
            asignarDatos(btnGrupo1, panelSubMenu1);
        }

        private void btnServicio1_Click(object sender, EventArgs e)
        {
            asignarDatos(btnServicio1, null);
        }

        private void btnServicio2_Click(object sender, EventArgs e)
        {
            asignarDatos(btnServicio2, null);
        }

        private void btnServicio3_Click(object sender, EventArgs e)
        {
            asignarDatos(btnServicio3, null);
        }

        private void btnServicio4_Click(object sender, EventArgs e)
        {
            asignarDatos(btnServicio4, null);
        }

        private void btnGrupo2_Click(object sender, EventArgs e)
        {
            asignarDatos(btnGrupo2, panelSubMenu2);
        }

        private void btnServicio5_Click(object sender, EventArgs e)
        {
            asignarDatos(btnServicio5, null);
        }

        private void btnServicio6_Click(object sender, EventArgs e)
        {
            asignarDatos(btnServicio6, null);
        }

        private void btnServicio7_Click(object sender, EventArgs e)
        {
            asignarDatos(btnServicio7, null);
        }

        private void btnServicio8_Click(object sender, EventArgs e)
        {
            asignarDatos(btnServicio8, null);
        }

        private void btnServicio9_Click(object sender, EventArgs e)
        {
            asignarDatos(btnServicio9, null);
        }

        private void btnGrupo3_Click(object sender, EventArgs e)
        {
            asignarDatos(btnGrupo3, panelSubMenu3);
        }

        private void btnServicio10_Click(object sender, EventArgs e)
        {
            asignarDatos(btnServicio10, null);
        }

        private void btnServicio11_Click(object sender, EventArgs e)
        {
            asignarDatos(btnServicio11, null);
        }
        private void btnHabilitado_CheckedChanged(object sender, EventArgs e)
        {
            if (botonSeleccionado != null)
            {
                if (btnHabilitado.Checked == false)
                {
                    if (panelSeleccionado != null)
                    {
                        panelSeleccionado.BackColor = colorDeshabilitado;//Color rojo para deshabilitar
                    }
                    botonSeleccionado.BackColor = colorDeshabilitado;

                }
                else
                {
                    if (panelSeleccionado != null)
                    {

                        panelSeleccionado.BackColor = colorHabilitado;//Color Azul para habilitad
                    }
                    botonSeleccionado.BackColor = Color.Empty;
                }
            }
        }

        private void txtNombre_TextChanged(object sender, EventArgs e)
        {
            if (botonSeleccionado != null)
            {
                botonSeleccionado.Text = txtNombre.Text;
            }
        }

        private void buttonAceptar_Click(object sender, EventArgs e)
        {
            Principal principal = new Principal();
            principal.bindServicios(this);
            this.Hide();
            principal.Show();
        }
    }
}
