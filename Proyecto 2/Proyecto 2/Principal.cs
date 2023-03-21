using Proyecto_2.Modelos;

namespace Proyecto_2
{
    public partial class Principal : Form
    {
        public Principal()
        {
            InitializeComponent();
        }

        private void Principal_Load(object sender, EventArgs e)
        {
            ocultarSubMenus();
        }
        /**Menu de hamburguesa**/
        private void hamburguerPic_Click(object sender, EventArgs e)
        {
            desplegarMenu();
        }
        private void desplegarMenu()
        {
            if (panelMenu.Width > 200)
            {
                panelMenu.Width = 70;
                btnPlataforma.Visible = false;
                btnCaja.Visible = false;
                btnServicioCliente.Visible = false;
                tituloPic.Visible = false;
                picIconCaja.Dock = DockStyle.Top;
                picIconPlataforma.Dock = DockStyle.Top;
                picIconServicioCliente.Dock = DockStyle.Top;
                hamburguerPic.Dock = DockStyle.Top;
                picIconCaja.Cursor = System.Windows.Forms.Cursors.Hand;
                picIconPlataforma.Cursor = System.Windows.Forms.Cursors.Hand; 
                picIconServicioCliente.Cursor = System.Windows.Forms.Cursors.Hand;
                ocultarSubMenus();
            }
            else
            {
                panelMenu.Width = 237;
                tituloPic.Visible = true;
                btnCaja.Visible = true;
                btnPlataforma.Visible = true;
                btnServicioCliente.Visible = true;
                picIconCaja.Dock = DockStyle.Left;
                picIconPlataforma.Dock = DockStyle.Left;
                picIconServicioCliente.Dock = DockStyle.Left;
                hamburguerPic.Dock = DockStyle.None;
                picIconCaja.Cursor = System.Windows.Forms.Cursors.Default;
                picIconPlataforma.Cursor = System.Windows.Forms.Cursors.Default;
                picIconServicioCliente.Cursor = System.Windows.Forms.Cursors.Default;
            }
        }
        /**Funciones de desplegar SubMenus**/
        private void ocultarSubMenus()
        {
            if (panelSubMenuCaja.Visible)
                panelSubMenuCaja.Visible = false;
            if (panelSubMenuPlataforma.Visible)
                panelSubMenuPlataforma.Visible = false;
            if (panelSubMenuServicioCliente.Visible)
                panelSubMenuServicioCliente.Visible = false;
        }
        private void mostrarSubMenu(Panel subMenu)
        {
            if (!subMenu.Visible)
            {
                
                ocultarSubMenus();
                subMenu.Visible = true;
            }
            else
            {   
                subMenu.Visible = false;
            }
        }

        /**Botones del MENU**/
        private void btnCaja_Click(object sender, EventArgs e)
        {
            mostrarSubMenu(panelSubMenuCaja);
        }
        
        private void btnPlataforma_Click(object sender, EventArgs e)
        {
            mostrarSubMenu(panelSubMenuPlataforma);
        }

        private void btnServicioCliente_Click(object sender, EventArgs e)
        {
            mostrarSubMenu(panelSubMenuServicioCliente);
        }
        /**Funciones de deplegar desde Iconos de Menu**/
        private void picIconCaja_Click(object sender, EventArgs e)
        {
            if (panelMenu.Width < 200)
            {
                desplegarMenu();
                mostrarSubMenu(panelSubMenuCaja);
            }
        }

        private void picIconPlataforma_Click(object sender, EventArgs e)
        {
            if (panelMenu.Width < 200)
            {
                desplegarMenu();
                mostrarSubMenu(panelSubMenuPlataforma);
            }
        }

        private void picIconServicioCliente_Click(object sender, EventArgs e)
        {
            if (panelMenu.Width < 200)
            {
                desplegarMenu();
                mostrarSubMenu(panelSubMenuServicioCliente);
            }
        }
        /**Botones de SubMenus CAJA**/
        private void btnRetiros_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            ocultarSubMenus();
        }

        private void btnDepositos_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            ocultarSubMenus();
        }

        private void btnPagoServiciosPublicos_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            ocultarSubMenus();
        }

        private void btnPagoCreditos_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            ocultarSubMenus();
        }
        /**Botones de SubMenu PLATAFORMA**/
        private void btnSolicitarTarjeta_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            ocultarSubMenus();
        }

        private void btnFormalizarCredito_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            ocultarSubMenus();
        }

        private void btnCajaSeguridad_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            ocultarSubMenus();
        }

        private void btnDesbloquearCuenta_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            ocultarSubMenus();
        }

        private void btnCambiarPin_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            ocultarSubMenus();
        }
        /**Botones de SubMenu SERVICIO AL CLIENTE**/
        private void btnRetirarTarjeta_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            ocultarSubMenus();
        }

        private void btnSolicitarInfoCreditos_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            ocultarSubMenus();
        }
    }
}