using Proyecto_2.Modelos;
using Proyecto_2.Utilidades;
using System.Collections;
using System.Windows.Forms.VisualStyles;

namespace Proyecto_2
{
    public partial class Principal : Form
    {
        private EntidadFinanciera entidadFinanciera;
        private alertaInformacion alerta;
        private List<PictureBox> fotosVisual = new List<PictureBox> { };
        private int velocidadHilo = -1;
        private object lockObject = new object();
        public Principal()
        {
            alerta = new alertaInformacion();
            entidadFinanciera = new EntidadFinanciera();
            InitializeComponent();


        }
        //Eventos Form
        private void Principal_Load(object sender, EventArgs e)
        {

            ocultarSubMenus();
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
            generarPeticion(btnServicio1.Text);
            ocultarSubMenus();
        }

        private void btnDepositos_Click(object sender, EventArgs e)
        {
            generarPeticion(btnServicio2.Text);
            ocultarSubMenus();
        }

        private void btnPagoServiciosPublicos_Click(object sender, EventArgs e)
        {
            generarPeticion(btnServicio3.Text);
            ocultarSubMenus();
        }

        private void btnPagoCreditos_Click(object sender, EventArgs e)
        {
            generarPeticion(btnServicio4.Text);
            ocultarSubMenus();
        }
        /**Botones de SubMenu PLATAFORMA**/
        private void btnSolicitarTarjeta_Click(object sender, EventArgs e)
        {
            generarPeticion(btnServicio5.Text);
            ocultarSubMenus();
        }

        private void btnFormalizarCredito_Click(object sender, EventArgs e)
        {
            generarPeticion(btnServicio6.Text);
            ocultarSubMenus();
        }

        private void btnCajaSeguridad_Click(object sender, EventArgs e)
        {
            generarPeticion(btnServicio7.Text);
            ocultarSubMenus();

        }

        private void btnDesbloquearCuenta_Click(object sender, EventArgs e)
        {
            generarPeticion(btnServicio8.Text);
            ocultarSubMenus();
        }

        private void btnCambiarPin_Click(object sender, EventArgs e)
        {
            generarPeticion(btnServicio9.Text);
            ocultarSubMenus();
        }
        /**Botones de SubMenu SERVICIO AL CLIENTE**/
        private void btnRetirarTarjeta_Click(object sender, EventArgs e)
        {
            generarPeticion(btnServicio10.Text);
            ocultarSubMenus();
        }

        private void btnSolicitarInfoCreditos_Click(object sender, EventArgs e)
        {
            //Codigo aqui
            generarPeticion(btnServicio11.Text);
            ocultarSubMenus();
        }
        /**UTILIDADES**/
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
                        Servicio? servicio = entidadFinanciera.buscarServicio(nombreServicio);
                        if (servicio != null)
                        {
                            registrarPeticion(new Peticion(nombre, servicio, check == "preferencial" ? true : false));
                        }
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
            if (velocidadHilo != -1)
            {
                ejecutar();
            }


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

        private void clickImagenes(object sender, EventArgs e)
        {

            PictureBox foto = (PictureBox)sender;
            var contenido = foto.Name.Split('.');//Formato "grupo.nombre"
            string grupo = contenido[0];
            string id = contenido[1];
            Caja? caja = entidadFinanciera.obtenerCaja(Convert.ToInt32(id), 0);
            if (caja != null)
            {
                Utilidades.Utilidades.setCaja(caja);
            }

            Utilidades.Utilidades.setFotoAModificar(foto);
            Utilidades.Utilidades.setNombresGrupos(btnGrupo1.Text, btnGrupo2.Text, btnGrupo3.Text);
            CajaContenido cajaContenido = new CajaContenido();
            if (cajaContenido.ShowDialog() == DialogResult.OK)
            {
                actualizarCajaVisual(Utilidades.Utilidades.getCaja());
                actualizarCajaLogica(Utilidades.Utilidades.getCaja());
            }
        }
        private void actualizarCajaLogica(Caja cajaActualizada)
        {
            entidadFinanciera.moverDeGrupo_actualizar(cajaActualizada);
        }
        private void actualizarCajaVisual(Caja cajaActualizada)
        {
            //Visual
            string tipoCaja = cajaActualizada.getTipoCaja();
            int id = cajaActualizada.getId();
            Image image = Properties.Resources.caja;
            Color color = Color.FromArgb(128, Color.Green);
            List<PictureBox> fotos = new List<PictureBox>();
            fotos = Utilidades.Utilidades.getPictureBoxOfPanel(panelContenedor1);
            fotos.AddRange(Utilidades.Utilidades.getPictureBoxOfPanel(panelContenedor2));
            fotos.AddRange(Utilidades.Utilidades.getPictureBoxOfPanel(panelContenedor3));
            //Cambia el color de fondo de acuerdo al estado
            if (cajaActualizada.getEstado() == false)
            {
                color = Color.FromArgb(128, Color.Red);
            }
            //Cambia la imagen de fondo de acuerdo al tipo
            if (tipoCaja == btnGrupo2.Text)
            {
                image = Properties.Resources.plataforma;
            }
            else if (tipoCaja == btnGrupo3.Text)
            {
                image = Properties.Resources.servicioCliente;
            }
            //Busca la imagen a actualizar en la lista de fotos
            foreach (PictureBox foto in fotos)
            {
                if (foto.Name.Contains("." + id))//Formato grupo.id
                {
                    foto.Image = image;
                    foto.BackColor = color;
                    break;
                }
            }
        }
        private Panel crearCaja(int tipo, int id)
        {

            Panel panel = new Panel();
            PictureBox foto = new PictureBox();
            foto.Name = tipo.ToString() + "." + id.ToString();
            //Se debe agregar esta caja a la entidad
            foto.BackColor = Color.FromArgb(128, Color.Green);
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
            fotosVisual.Add(foto);
            return panel;
        }
        //Funciones de menu hamburguesa
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
        //Funciones inicializadoras
        public void bindServicios(Login login)
        {
            bindBotones(login);
            inicializarCajas(login);
        }
        private void bindBotones(Login login)
        {
            List<Button> botonesMenuLogin = login.getAllButtonsOfPanelMenu();
            List<Button> botonesMenu = Utilidades.Utilidades.getButtonsOfPanel(panelMenu);
            foreach (Button buttonLogin in botonesMenuLogin)
            {
                foreach (Button button in botonesMenu)
                {
                    if (buttonLogin.Name == button.Name)
                    {
                        if (buttonLogin.BackColor == login.getColorDeshabilitado())
                        {
                            button.Visible = false;
                            if (button.Name.Contains("Grupo1"))
                            {
                                Utilidades.Utilidades.setCantCajas(1, 0);
                                panelMenuCaja.Visible = false;
                            }
                            if (button.Name.Contains("Grupo2"))
                            {
                                Utilidades.Utilidades.setCantCajas(2, 0);
                                panelMenuPlataforma.Visible = false;
                            }
                            if (button.Name.Contains("Grupo3"))
                            {
                                Utilidades.Utilidades.setCantCajas(3, 0);
                                panelMenuServicioCliente.Visible = false;
                            }
                        }
                        else
                        {
                            button.Text = buttonLogin.Text;
                        }
                    }
                }
            }
        }
        private void inicializarCajas(Login login)
        {
            int cajas1, cajas2, cajas3;
            cajas1 = Utilidades.Utilidades.getCantCajas(1);
            cajas2 = Utilidades.Utilidades.getCantCajas(2);
            cajas3 = Utilidades.Utilidades.getCantCajas(3);
            int id = 0;
            Queue<Caja> listCajas1 = new Queue<Caja>();
            Queue<Caja> listCajas2 = new Queue<Caja>();
            Queue<Caja> listCajas3 = new Queue<Caja>();

            for (int i = 0; i < cajas1; i++)
            {

                panelContenedor1.Controls.Add(crearCaja(1, id + 1), 0, i);
                listCajas1.Enqueue(new Caja(btnGrupo1.Text, id + 1));
                id++;
            }//Llena las cajas visual y logicamente

            //Se agrega la lista a la entidad, junto con sus grupo
            crearGrupoServicio(login, btnGrupo1.Text, listCajas1, Utilidades.Utilidades.getButtonsOfPanel(panelSubMenuCaja));
            for (int i = 0; i < cajas2; i++)
            {

                panelContenedor2.Controls.Add(crearCaja(2, id + 1), 0, i);
                listCajas2.Enqueue(new Caja(btnGrupo2.Text, id + 1));
                id++;
            }//Llena las cajas visual y logicamente

            //Se agrega la lista a la entidad, junto con sus grupo
            crearGrupoServicio(login, btnGrupo2.Text, listCajas2, Utilidades.Utilidades.getButtonsOfPanel(panelSubMenuPlataforma));

            for (int i = 0; i < cajas3; i++)
            {
                panelContenedor3.Controls.Add(crearCaja(3, id + 1), 0, i);
                listCajas3.Enqueue(new Caja(btnGrupo3.Text, id + 1));
                id++;
            }//Llena las cajas visual y logicamente

            //Se agrega la lista a la entidad, junto con sus grupo

            crearGrupoServicio(login, btnGrupo3.Text, listCajas3, Utilidades.Utilidades.getButtonsOfPanel(panelSubMenuServicioCliente));

        }
        private void crearGrupoServicio(Login login, string nombreGrupo, Queue<Caja> cajas, List<Button> botones)
        {
            Queue<Servicio> servicios = new Queue<Servicio> { };
            foreach (Button boton in botones)
            {
                if (boton.BackColor != login.getColorDeshabilitado())
                {
                    servicios.Enqueue(new Servicio(boton.Text));
                }
            }
            entidadFinanciera.agregarGrupoServicio(new GrupoServicios(nombreGrupo, servicios, cajas));
        }

        private void ejecutar()
        {

            Queue<Peticion> peticionesNoAsignadas = new Queue<Peticion> { };
            while (entidadFinanciera.getPeticiones().Count() > 0)
            {
                if (asignarPeticion(entidadFinanciera.getPeticiones().Peek()))
                {
                    entidadFinanciera.getPeticiones().Dequeue();
                }
                else
                {
                    peticionesNoAsignadas.Enqueue(entidadFinanciera.getPeticiones().Dequeue());
                }
            }
            entidadFinanciera.setPeticiones(peticionesNoAsignadas);
            ingresarDatosListView(entidadFinanciera.getPeticiones());
        }
        private bool asignarPeticion(Peticion peticion)
        {
            Caja caja = entidadFinanciera.asignarPeticion(peticion);
            if (caja != null)
            {
                Thread hilo = new Thread(new ParameterizedThreadStart(hilo_caja));
                hilo.Start(caja);
                return true;
            }
            else
            {
                return false;
            }
        }
        private void hilo_caja(Object objeto)
        {
            Caja caja = (Caja)objeto;
            foreach (PictureBox foto in fotosVisual)
            {
                if (foto.Name.Contains("." + caja.getId()))
                {
                    Panel panel = (Panel)foto.Parent;
                    foreach (ProgressBar barra in Utilidades.Utilidades.getProgressbarOfPanel(panel))
                    {
                        Peticion peticion = caja.obtenerPeticion();
                        if (peticion != null)
                        {
                            int peso = peticion.getServicio().getPeso();
                            int progreso = 0;
                            for (int i = 0; i <= peso; i++)
                            {
                                progreso = (100 * i) / peso;
                                barra.Invoke((MethodInvoker)delegate { barra.Value = progreso; });
                                while (velocidadHilo == -1)
                                {

                                }
                                Thread.Sleep(velocidadHilo);
                            }
                            //Finalizacion
                            Thread.Sleep(1000);
                            //Elimino la caja
                            barra.Invoke((MethodInvoker)delegate { barra.Value = 0; });
                            caja.setPeticion(null);
                            //Evaluar la conversion
                            //Cuenta peticiones
                            lock (lockObject)
                            {
                                double promedio1 = 0, promedio2 = 0, promedio3 = 0;
                                int peticionesG1 = 0, peticionesG2 = 0, peticionesG3 = 0;
                                //contarPeticiones(ref peticionesG1, ref peticionesG2, ref peticionesG3);
                                //contarPromedios(ref promedio1, ref promedio2, ref promedio3, peticionesG1, peticionesG2, peticionesG3);
                                //Transformo la actual
                                //transformarCajas(caja, promedio1, promedio2, promedio3);
                                //Transformo las desocupadas

                                for (int i = 0; i < entidadFinanciera.getGrupoServicios().Count(); i++)
                                {
                                    foreach (Caja c in entidadFinanciera.getGrupoServicios().ElementAt(i).getCopiaCajas())
                                    {
                                        if (c.obtenerPeticion() == null && c.getEstado())
                                        {
                                            contarPeticiones(ref peticionesG1, ref peticionesG2, ref peticionesG3);
                                            contarPromedios(ref promedio1, ref promedio2, ref promedio3, peticionesG1, peticionesG2, peticionesG3);
                                            if (promedio1 > 1 || promedio2 > 1 || promedio3 > 1)
                                            {
                                                transformarCajas(c, promedio1, promedio2, promedio3);
                                            }
                                        }
                                    }

                                }
                                ejecutar();
                            }
                        }
                    }
                }
            }
        }
        private void contarPromedios(ref double promedio1, ref double promedio2, ref double promedio3, int peticiones1, int peticiones2, int peticiones3)
        {
            foreach (GrupoServicios i in entidadFinanciera.getGrupoServicios())
            {
                if (i.getNombre() == btnGrupo1.Text)
                {
                    promedio1 = (double)peticiones1 / i.getCajas().Count();
                }
                else if (i.getNombre() == btnGrupo2.Text)
                {
                    promedio2 = (double)peticiones2 / i.getCajas().Count();
                }
                else
                {
                    promedio3 = (double)peticiones3 / i.getCajas().Count();
                }
            }
        }
        private void transformarCajas(Caja caja, double promedio1, double promedio2, double promedio3)
        {
            double rangoDiferencia = 1.5;
            //Saca cantidad de cajas habilitadas
            int cantCajas1 = 0, cantCajas2 = 0, cantCajas3 = 0;
            foreach (GrupoServicios g in entidadFinanciera.getGrupoServicios())
            {

                if (g.getNombre() == btnGrupo1.Text)
                {
                    cantCajas1 = g.cantCajasHabilitadas();
                }
                if (g.getNombre() == btnGrupo2.Text)
                {
                    cantCajas2 = g.cantCajasHabilitadas();
                }
                if (g.getNombre() == btnGrupo3.Text)
                {
                    cantCajas3 = g.cantCajasHabilitadas();
                }
            }

            if (caja.getTipoCaja() == btnGrupo1.Text && cantCajas1 > 1)
            {
                if (promedio1 * rangoDiferencia < promedio2)
                { //El 1 es el doble de mayor que el 2
                  //Transforma de 1 a 2
                    caja.setTipoCaja(btnGrupo2.Text);
                    actualizarCajaLogica(caja);
                    actualizarCajaVisual(caja);

                }
                else if (promedio1 * rangoDiferencia < promedio3)
                { //El 1 es el doble de mayor que el 3
                  //Transforma de 1 a 3
                    caja.setTipoCaja(btnGrupo3.Text);
                    actualizarCajaLogica(caja);
                    actualizarCajaVisual(caja);
                }
            }
            if (caja.getTipoCaja() == btnGrupo2.Text && cantCajas2 > 1)
            {
                if (promedio2 * rangoDiferencia < promedio1)
                {
                    //El 2 es el doble de mayor que el 1
                    //Transforma de 2 a 1
                    caja.setTipoCaja(btnGrupo1.Text);
                    actualizarCajaLogica(caja);
                    actualizarCajaVisual(caja);
                }
                else if (promedio2 * rangoDiferencia < promedio3)
                {
                    //El 2 es el doble de mayor que el 3
                    //Transforma de 2 a 3
                    caja.setTipoCaja(btnGrupo3.Text);
                    actualizarCajaLogica(caja);
                    actualizarCajaVisual(caja);
                }
            }
            if (caja.getTipoCaja() == btnGrupo3.Text && cantCajas3 > 1)
            {
                if (promedio3 * rangoDiferencia < promedio1)
                {
                    //El 3 es el doble de mayor que el 1
                    //Transforma de 3 a 1
                    caja.setTipoCaja(btnGrupo1.Text);
                    actualizarCajaLogica(caja);
                    actualizarCajaVisual(caja);
                }
                else if (promedio3 * rangoDiferencia < promedio2)
                {
                    //El 3 es el doble de mayor que el 1
                    //Transforma de 3 a 2
                    caja.setTipoCaja(btnGrupo2.Text);
                    actualizarCajaLogica(caja);
                    actualizarCajaVisual(caja);
                }
            }
        }
        private void contarPeticiones(ref int peticiones1, ref int peticiones2, ref int peticiones3)
        {
            Queue<Peticion> peticiones = entidadFinanciera.getPeticiones();
            GrupoServicios grupo;
            foreach (Peticion i in peticiones)
            {
                grupo = entidadFinanciera.identificarPeticion(i);
                if (grupo != null)
                {
                    if (grupo.getNombre() == btnGrupo1.Text)
                    {
                        peticiones1++;
                    }
                    if (grupo.getNombre() == btnGrupo2.Text)
                    {
                        peticiones2++;
                    }
                    else
                    {
                        peticiones3++;
                    }
                }
            }
        }
        private void btnPlay_Click(object sender, EventArgs e)
        {

            if (velocidadHilo == -1)
            {
                velocidadHilo = lblVelocidad.Text == "X1" ? 1000 : lblVelocidad.Text == "X2" ? 500 : lblVelocidad.Text == "X3" ? 250 : 125;
            }

            ejecutar();
        }

        private void btnStop_Click(object sender, EventArgs e)
        {
            velocidadHilo = -1;
        }

        private void btnDesacelerar_Click(object sender, EventArgs e)
        {
            modificarVelocidad("desacelerar");
        }


        private void btnAcelerar_Click(object sender, EventArgs e)
        {
            modificarVelocidad("acelerar");
        }
        private void modificarVelocidad(String opcion)
        {
            switch (lblVelocidad.Text)
            {
                case "X1":
                    if (opcion == "acelerar")
                    {

                        lblVelocidad.Text = "X2";
                    }
                    break;
                case "X2":
                    if (opcion == "acelerar")
                    {

                        lblVelocidad.Text = "X3";
                    }
                    else
                    {

                        lblVelocidad.Text = "X1";
                    }
                    break;
                case "X3":
                    if (opcion == "desacelerar")
                    {

                        lblVelocidad.Text = "X2";
                    }
                    else
                    {
                        lblVelocidad.Text = "X4";
                    }
                    break;
                case "X4":
                    if (opcion == "desacelerar")
                    {
                        lblVelocidad.Text = "X3";
                    }
                    break;
            }
            if (velocidadHilo != -1)
            {
                velocidadHilo = lblVelocidad.Text == "X1" ? 1000 : lblVelocidad.Text == "X2" ? 500 : lblVelocidad.Text == "X3" ? 250 : 125;

            }
        }
    }
}