using Proyecto_2.Modelos;

namespace Proyecto_2
{
    public partial class Principal : Form
    {
        EntidadFinanciera entidadFinanciera;
        alertaInformacion alerta;
        public Principal()
        {
            InitializeComponent();
            entidadFinanciera = new EntidadFinanciera();
            alerta = new alertaInformacion();
            ocultarSubMenus();

        }

        private void Principal_Load(object sender, EventArgs e)
        {

            inicializarCajas();

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
            generarPeticion(btnServicio1.Text);
            ocultarSubMenus();
        }

        private void btnDepositos_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            generarPeticion(btnServicio2.Text);
            ocultarSubMenus();
        }

        private void btnPagoServiciosPublicos_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            generarPeticion(btnServicio3.Text);
            ocultarSubMenus();
        }

        private void btnPagoCreditos_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            generarPeticion(btnServicio4.Text);
            ocultarSubMenus();
        }
        /**Botones de SubMenu PLATAFORMA**/
        private void btnSolicitarTarjeta_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            generarPeticion(btnServicio5.Text);
            ocultarSubMenus();
        }

        private void btnFormalizarCredito_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            generarPeticion(btnServicio6.Text);
            ocultarSubMenus();
        }

        private void btnCajaSeguridad_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            generarPeticion(btnServicio7.Text);
            ocultarSubMenus();

        }

        private void btnDesbloquearCuenta_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            generarPeticion(btnServicio8.Text);
            ocultarSubMenus();
        }

        private void btnCambiarPin_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            generarPeticion(btnServicio9.Text);
            ocultarSubMenus();
        }
        /**Botones de SubMenu SERVICIO AL CLIENTE**/
        private void btnRetirarTarjeta_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            generarPeticion(btnServicio10.Text);
            ocultarSubMenus();
        }

        private void btnSolicitarInfoCreditos_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            generarPeticion(btnServicio11.Text);
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
                        //MessageBox.Show("Querid@ " + alerta.getTxtNombre() + " espere a ser atendido", "Confirmacion");
                        registrarPeticion(new Peticion(nombre, nombreServicio, check == "preferencial" ? true : false));
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
        private void registrarPeticion(Peticion peticion)
        {

            entidadFinanciera.agregarPeticion(peticion);
            entidadFinanciera.ordernarPeticiones();
            ingresarDatosListView(entidadFinanciera.getPeticiones());
        }
        private void ingresarDatosListView(Queue<Peticion> lista)
        {
            listProcesos.Items.Clear();
            foreach (Peticion i in lista)
            {
                ListViewItem item = new ListViewItem(i.getServicio().getNombre());
                item.SubItems.Add(i.getServicio().getPrioridad().ToString());
                item.SubItems.Add(i.getServicio().getPeso().ToString());
                item.SubItems.Add(i.getNombre());
                listProcesos.Items.Add(item);

            }
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
                panelContenedor5.Controls.Add(crearCaja(2), 0, i);
            }
            for (int i = 0; i < cajas3; i++)
            {
                panelContenedor6.Controls.Add(crearCaja(3), 0, i);
            }
        }
        private void clickImagenes(object sender, EventArgs e)
        {
            PictureBox foto = (PictureBox)sender;
            //boton.Visible = false;

        }
        private Panel crearCaja(int tipo)
        {
            Panel panel = new Panel();
            PictureBox foto = new PictureBox();
            foto.Name = tipo.ToString();
            foto.Click += clickImagenes;

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

        private void Principal_FormClosing(object sender, FormClosingEventArgs e)
        {
            Application.Exit();
        }
    }
}