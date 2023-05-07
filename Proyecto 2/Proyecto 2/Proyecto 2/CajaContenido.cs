using Proyecto_2.Modelos;
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
    public partial class CajaContenido : Form
    {
        string grupo1 = "";
        string grupo2 = "";
        string grupo3 = "";
        PictureBox? foto = null;
        Color colorHabilitado = Color.FromArgb(128, Color.Green);
        Color colorDesHabilitado = Color.FromArgb(128, Color.Red);
        Caja cajaAModificar = new Caja();

        public CajaContenido()
        {
            InitializeComponent();
            iniciarComponentes();
        }
        private void iniciarComponentes()
        {
            grupo1 = Utilidades.Utilidades.getNombreGrupo(1);
            grupo2 = Utilidades.Utilidades.getNombreGrupo(2);
            grupo3 = Utilidades.Utilidades.getNombreGrupo(3);
            cajaAModificar = Utilidades.Utilidades.getCaja();
            foto = Utilidades.Utilidades.getFotoAModificar();
            panelFoto.Controls.Add(foto);
            cbEstado.Items.Add("Habilitado");
            cbEstado.Items.Add("Inhabilitado");
            cbTipoCaja.Items.Add(grupo1);
            cbTipoCaja.Items.Add(grupo2);
            cbTipoCaja.Items.Add(grupo3);
            cbTipoCaja.SelectedItem = cajaAModificar.getTipoCaja();
            cbEstado.SelectedItem = cajaAModificar.getEstado() == true ? "Habilitado" : "Inhabilitado";
        }
        private void btnAceptar_Click(object sender, EventArgs e)
        {
            cajaAModificar.setEstado((cbEstado.SelectedItem.ToString()=="Habilitado")?true:false);
            cajaAModificar.setTipoCaja(cbTipoCaja.SelectedItem.ToString());
            Utilidades.Utilidades.setCaja(cajaAModificar);
        }

        private void cbEstado_SelectedIndexChanged(object sender, EventArgs e)
        {

            string item = (string)cbEstado.SelectedItem;
            if (foto != null)
            {
                if (item.Equals("Habilitado"))
                {
                    foto.BackColor = colorHabilitado;
                }
                else
                {
                    foto.BackColor = colorDesHabilitado;
                }
            }
        }

        private void cbTipoCaja_SelectedIndexChanged(object sender, EventArgs e)
        {
            string item = (string)cbTipoCaja.SelectedItem;
            if (item == grupo1)
            {
                if (foto != null)
                {
                    foto.Image = Properties.Resources.caja;
                }
            }
            else if (item == grupo2)
            {
                if (foto != null)
                {
                    foto.Image = Properties.Resources.plataforma;
                }
            }
            if (item == grupo3)
            {
                if (foto != null)
                {
                    foto.Image = Properties.Resources.servicioCliente;
                }
            }

        }
    }
}
