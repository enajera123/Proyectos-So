using Proyecto_2.Modelos;

namespace Proyecto_2
{
    public partial class Principal : Form
    {
        Controlador controlador;
        alertaInformacion alerta;
        public Principal()
        {
            InitializeComponent();
            controlador = new Controlador();
            alerta = new alertaInformacion();
        }

        private void Principal_Load(object sender, EventArgs e)
        {
            ocultarSubMenus();
            bindServicios();
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
                btnGrupo2.Visible = false;
                btnGrupo1.Visible = false;
                btnGrupo3.Visible = false;
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
                btnGrupo1.Visible = true;
                btnGrupo2.Visible = true;
                btnGrupo3.Visible = true;
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
            generarPeticion("retiro");
            ocultarSubMenus();
        }

        private void btnDepositos_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            generarPeticion("deposito");
            ocultarSubMenus();
        }

        private void btnPagoServiciosPublicos_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            generarPeticion("pago de servicios publicos");
            ocultarSubMenus();
        }

        private void btnPagoCreditos_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            generarPeticion("pago de creditos");
            ocultarSubMenus();
        }
        /**Botones de SubMenu PLATAFORMA**/
        private void btnSolicitarTarjeta_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            generarPeticion("solicitar tarjeta");
            ocultarSubMenus();
        }

        private void btnFormalizarCredito_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            generarPeticion("formalizar credito");
            ocultarSubMenus();
        }

        private void btnCajaSeguridad_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            generarPeticion("seguridad");
            ocultarSubMenus();

        }

        private void btnDesbloquearCuenta_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            generarPeticion("desbloquear cuenta");
            ocultarSubMenus();
        }

        private void btnCambiarPin_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            generarPeticion("cambiar pin");
            ocultarSubMenus();
        }
        /**Botones de SubMenu SERVICIO AL CLIENTE**/
        private void btnRetirarTarjeta_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            generarPeticion("retirar tarjeta");
            ocultarSubMenus();
        }

        private void btnSolicitarInfoCreditos_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            generarPeticion("solicitar informacion de creditos");
            ocultarSubMenus();
        }
        public void generarPeticion(string nombreServicio)
        {
            bool bucle = false;
            do
            {
                if (alerta.ShowDialog() == DialogResult.OK)
                {
                    string check = alerta.getCheckOpcion(), nombre = alerta.getTxtNombre();
                    if (check != "" && nombre != "")
                    {
                        MessageBox.Show("Querid@ " + alerta.getTxtNombre() + " espere a ser atendido", "Confirmacion");
                        registrarPeticion(new Cliente(nombre, nombreServicio, check == "preferencial" ? true : false));
                        alerta.limpiarAlerta();
                        bucle = false;
                    }
                    else
                    {
                        MessageBox.Show("Debe llenar todos los campos", "Error");
                        bucle = true;
                    }
                }
                else
                {
                    bucle = false;
                }
            } while (bucle);
        }
        private void registrarPeticion(Cliente cliente)
        {
            controlador.registrarPeticion(cliente);
            //controlador.getListaEspera().getClientesEspera();

           
            btnGrupo1.Text = controlador.getListaEspera().getClientesEspera().Count.ToString();



        }

    }
}