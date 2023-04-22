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
            ocultarSubMenus();

        }

        private void Principal_Load(object sender, EventArgs e)
        {

            inicializarCajas();

        }
        private void Principal_FormClosing(object sender, FormClosingEventArgs e)
        {
            Application.Exit();
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
            //   controlador.registrarPeticion(cliente);
            //   btnGrupo1.Text = controlador.getListaEspera().getClientesEspera().Count.ToString();
        }
        private void inicializarCajas()
        {
            int cajas1, cajas2, cajas3;
            cajas1 = Utilidades.Utilidades.getCantCajas(1);
            cajas2 = Utilidades.Utilidades.getCantCajas(2);
            cajas3 = Utilidades.Utilidades.getCantCajas(3);
            for (int i = 0; i < cajas1; i++)
            {
                flowContenedor1.Controls.Add(crearCaja(1), 0, i);
            }
            for (int i = 0; i < cajas2; i++)
            {
                flowContenedor2.Controls.Add(crearCaja(2), 0, i);
            }
            for (int i = 0; i < cajas3; i++)
            {
                flowContenedor3.Controls.Add(crearCaja(3), 0, i);
            }
        }
        private Panel crearCaja(int tipo)
        {
            Panel panel = new Panel();
            PictureBox foto = new PictureBox();
            foto.SizeMode = PictureBoxSizeMode.Zoom;
            if (tipo == 1)
            {
                foto.Image = Properties.Resources.caja;
            }
            else if (tipo == 2)
            {
                foto.Image = Properties.Resources.plataforma;
            }
            else
            {
                foto.Image = Properties.Resources.servicioCliente;
            }
            ProgressBar barra = new ProgressBar();
            barra.Dock = DockStyle.Top;
            foto.Dock = DockStyle.Fill;
            panel.Controls.Add(foto);
            panel.Controls.Add(barra);
            panel.Dock = DockStyle.Fill;
            panel.Padding = new Padding(20);
            return panel;
        }


    }
}