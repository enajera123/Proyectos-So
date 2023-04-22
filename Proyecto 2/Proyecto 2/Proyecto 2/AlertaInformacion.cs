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
    public partial class alertaInformacion : Form
    {
        public alertaInformacion()
        {
            InitializeComponent();
        }

        private void checkNoPreferencial_CheckedChanged(object sender, EventArgs e)
        {
            checkPreferencial.Checked = false;
        }

        private void checkPreferencial_CheckedChanged(object sender, EventArgs e)
        {
            checkNoPreferencial.Checked = false; 
        }
        
    }
}
