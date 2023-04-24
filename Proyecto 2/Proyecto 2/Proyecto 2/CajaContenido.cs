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

        public CajaContenido()
        {
            InitializeComponent();
            iniciarComponentes();
        }
        private void iniciarComponentes()
        {
            PictureBox foto = Utilidades.Utilidades.getFotoAModificar();
            panelFoto.Controls.Add(foto);
            cbEstado.Items.Add("Habilitado");
            cbEstado.Items.Add("Inhabilitado");
            

        }
        private void btnAceptar_Click(object sender, EventArgs e)
        {

        }

        private void cbEstado_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void cbTipoCaja_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
    }
}
