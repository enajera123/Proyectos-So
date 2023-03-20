namespace Proyecto_2
{
    public partial class Principal : Form
    {
        public Principal()
        {
            InitializeComponent();
        }

        private void hamburguerPic_Click(object sender, EventArgs e)
        {
            if (panelMenu.Width > 200)
            {
                panelMenu.Width = 70;
                tituloPic.Visible = false;
                hamburguerPic.Dock = DockStyle.Top;
            }
            else {
                panelMenu.Width = 210;
                tituloPic.Visible = true;
                hamburguerPic.Dock = DockStyle.None;
            }
        }
    }
}