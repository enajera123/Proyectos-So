using Microsoft.VisualBasic.Logging;
using Proyecto_2.Modelos;

namespace Proyecto_2
{
    partial class Principal
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            panelMenu = new Panel();
            panelSubMenuServicioCliente = new Panel();
            btnServicio11 = new Button();
            btnServicio10 = new Button();
            panelMenuServicioCliente = new Panel();
            btnGrupo3 = new Button();
            picIconServicioCliente = new PictureBox();
            panelSubMenuPlataforma = new Panel();
            btnServicio9 = new Button();
            btnServicio8 = new Button();
            btnServicio7 = new Button();
            btnServicio6 = new Button();
            btnServicio5 = new Button();
            panelMenuPlataforma = new Panel();
            btnGrupo2 = new Button();
            picIconPlataforma = new PictureBox();
            panelSubMenuCaja = new Panel();
            btnServicio4 = new Button();
            btnServicio3 = new Button();
            btnServicio2 = new Button();
            btnServicio1 = new Button();
            panelMenuCaja = new Panel();
            btnGrupo1 = new Button();
            picIconCaja = new PictureBox();
            panelMenuSuperior = new Panel();
            hamburguerPic = new PictureBox();
            tituloPic = new PictureBox();
            panelNavegador = new Panel();
            panelPrincipal = new Panel();
            panelResponsive = new TableLayoutPanel();
            panelContenedor2 = new TableLayoutPanel();
            panelContenedor1 = new TableLayoutPanel();
            listProcesos = new ListView();
            columNombre = new ColumnHeader();
            columPrioridad = new ColumnHeader();
            columPeso = new ColumnHeader();
            columnCliente = new ColumnHeader();
            panelContenedor3 = new TableLayoutPanel();
            tableLayoutPanel1 = new TableLayoutPanel();
            btnPlay = new PictureBox();
            btnStop = new PictureBox();
            btnDesacelerar = new PictureBox();
            btnAcelerar = new PictureBox();
            lblVelocidad = new Label();
            panelMenu.SuspendLayout();
            panelSubMenuServicioCliente.SuspendLayout();
            panelMenuServicioCliente.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)picIconServicioCliente).BeginInit();
            panelSubMenuPlataforma.SuspendLayout();
            panelMenuPlataforma.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)picIconPlataforma).BeginInit();
            panelSubMenuCaja.SuspendLayout();
            panelMenuCaja.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)picIconCaja).BeginInit();
            panelMenuSuperior.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)hamburguerPic).BeginInit();
            ((System.ComponentModel.ISupportInitialize)tituloPic).BeginInit();
            panelNavegador.SuspendLayout();
            panelPrincipal.SuspendLayout();
            panelResponsive.SuspendLayout();
            tableLayoutPanel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)btnPlay).BeginInit();
            ((System.ComponentModel.ISupportInitialize)btnStop).BeginInit();
            ((System.ComponentModel.ISupportInitialize)btnDesacelerar).BeginInit();
            ((System.ComponentModel.ISupportInitialize)btnAcelerar).BeginInit();
            SuspendLayout();
            // 
            // panelMenu
            // 
            panelMenu.BackColor = Color.FromArgb(11, 110, 165);
            panelMenu.Controls.Add(panelSubMenuServicioCliente);
            panelMenu.Controls.Add(panelMenuServicioCliente);
            panelMenu.Controls.Add(panelSubMenuPlataforma);
            panelMenu.Controls.Add(panelMenuPlataforma);
            panelMenu.Controls.Add(panelSubMenuCaja);
            panelMenu.Controls.Add(panelMenuCaja);
            panelMenu.Controls.Add(panelMenuSuperior);
            panelMenu.Dock = DockStyle.Left;
            panelMenu.Location = new Point(0, 0);
            panelMenu.Name = "panelMenu";
            panelMenu.Size = new Size(237, 581);
            panelMenu.TabIndex = 0;
            // 
            // panelSubMenuServicioCliente
            // 
            panelSubMenuServicioCliente.BackColor = Color.FromArgb(17, 121, 174);
            panelSubMenuServicioCliente.Controls.Add(btnServicio11);
            panelSubMenuServicioCliente.Controls.Add(btnServicio10);
            panelSubMenuServicioCliente.Dock = DockStyle.Top;
            panelSubMenuServicioCliente.Location = new Point(0, 482);
            panelSubMenuServicioCliente.Name = "panelSubMenuServicioCliente";
            panelSubMenuServicioCliente.Padding = new Padding(20, 0, 0, 0);
            panelSubMenuServicioCliente.Size = new Size(237, 70);
            panelSubMenuServicioCliente.TabIndex = 8;
            // 
            // btnServicio11
            // 
            btnServicio11.Dock = DockStyle.Top;
            btnServicio11.FlatAppearance.BorderSize = 0;
            btnServicio11.FlatStyle = FlatStyle.Flat;
            btnServicio11.Font = new Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point);
            btnServicio11.Location = new Point(20, 30);
            btnServicio11.Name = "btnServicio11";
            btnServicio11.Padding = new Padding(10, 0, 0, 0);
            btnServicio11.Size = new Size(217, 30);
            btnServicio11.TabIndex = 5;
            btnServicio11.Text = "Solicitar Informacion de Creditos";
            btnServicio11.TextAlign = ContentAlignment.MiddleLeft;
            btnServicio11.UseVisualStyleBackColor = true;
            btnServicio11.Click += btnSolicitarInfoCreditos_Click;
            // 
            // btnServicio10
            // 
            btnServicio10.Dock = DockStyle.Top;
            btnServicio10.FlatAppearance.BorderSize = 0;
            btnServicio10.FlatStyle = FlatStyle.Flat;
            btnServicio10.Font = new Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point);
            btnServicio10.Location = new Point(20, 0);
            btnServicio10.Name = "btnServicio10";
            btnServicio10.Padding = new Padding(10, 0, 0, 0);
            btnServicio10.Size = new Size(217, 30);
            btnServicio10.TabIndex = 4;
            btnServicio10.Text = "Retirar Tarjeta";
            btnServicio10.TextAlign = ContentAlignment.MiddleLeft;
            btnServicio10.UseVisualStyleBackColor = true;
            btnServicio10.Click += btnRetirarTarjeta_Click;
            // 
            // panelMenuServicioCliente
            // 
            panelMenuServicioCliente.Controls.Add(btnGrupo3);
            panelMenuServicioCliente.Controls.Add(picIconServicioCliente);
            panelMenuServicioCliente.Dock = DockStyle.Top;
            panelMenuServicioCliente.Location = new Point(0, 437);
            panelMenuServicioCliente.Name = "panelMenuServicioCliente";
            panelMenuServicioCliente.Size = new Size(237, 45);
            panelMenuServicioCliente.TabIndex = 10;
            // 
            // btnGrupo3
            // 
            btnGrupo3.Cursor = Cursors.Hand;
            btnGrupo3.Dock = DockStyle.Fill;
            btnGrupo3.FlatAppearance.BorderSize = 0;
            btnGrupo3.FlatStyle = FlatStyle.Flat;
            btnGrupo3.Font = new Font("Segoe UI", 12F, FontStyle.Bold, GraphicsUnit.Point);
            btnGrupo3.Location = new Point(42, 0);
            btnGrupo3.Name = "btnGrupo3";
            btnGrupo3.Padding = new Padding(10, 0, 0, 0);
            btnGrupo3.Size = new Size(195, 45);
            btnGrupo3.TabIndex = 3;
            btnGrupo3.Text = "Servicio al Cliente";
            btnGrupo3.TextAlign = ContentAlignment.MiddleLeft;
            btnGrupo3.UseVisualStyleBackColor = true;
            btnGrupo3.Click += btnServicioCliente_Click;
            // 
            // picIconServicioCliente
            // 
            picIconServicioCliente.Dock = DockStyle.Left;
            picIconServicioCliente.Image = Properties.Resources.servicioCliente;
            picIconServicioCliente.Location = new Point(0, 0);
            picIconServicioCliente.Name = "picIconServicioCliente";
            picIconServicioCliente.Size = new Size(42, 45);
            picIconServicioCliente.SizeMode = PictureBoxSizeMode.Zoom;
            picIconServicioCliente.TabIndex = 4;
            picIconServicioCliente.TabStop = false;
            picIconServicioCliente.Click += picIconServicioCliente_Click;
            // 
            // panelSubMenuPlataforma
            // 
            panelSubMenuPlataforma.BackColor = Color.FromArgb(17, 121, 174);
            panelSubMenuPlataforma.Controls.Add(btnServicio9);
            panelSubMenuPlataforma.Controls.Add(btnServicio8);
            panelSubMenuPlataforma.Controls.Add(btnServicio7);
            panelSubMenuPlataforma.Controls.Add(btnServicio6);
            panelSubMenuPlataforma.Controls.Add(btnServicio5);
            panelSubMenuPlataforma.Dock = DockStyle.Top;
            panelSubMenuPlataforma.Location = new Point(0, 279);
            panelSubMenuPlataforma.Name = "panelSubMenuPlataforma";
            panelSubMenuPlataforma.Padding = new Padding(20, 0, 0, 0);
            panelSubMenuPlataforma.Size = new Size(237, 158);
            panelSubMenuPlataforma.TabIndex = 6;
            // 
            // btnServicio9
            // 
            btnServicio9.Dock = DockStyle.Top;
            btnServicio9.FlatAppearance.BorderSize = 0;
            btnServicio9.FlatStyle = FlatStyle.Flat;
            btnServicio9.Font = new Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point);
            btnServicio9.Location = new Point(20, 120);
            btnServicio9.Name = "btnServicio9";
            btnServicio9.Padding = new Padding(10, 0, 0, 0);
            btnServicio9.Size = new Size(217, 30);
            btnServicio9.TabIndex = 8;
            btnServicio9.Text = "Cambiar Pin Olvidado";
            btnServicio9.TextAlign = ContentAlignment.MiddleLeft;
            btnServicio9.UseVisualStyleBackColor = true;
            btnServicio9.Click += btnCambiarPin_Click;
            // 
            // btnServicio8
            // 
            btnServicio8.Dock = DockStyle.Top;
            btnServicio8.FlatAppearance.BorderSize = 0;
            btnServicio8.FlatStyle = FlatStyle.Flat;
            btnServicio8.Font = new Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point);
            btnServicio8.Location = new Point(20, 90);
            btnServicio8.Name = "btnServicio8";
            btnServicio8.Padding = new Padding(10, 0, 0, 0);
            btnServicio8.Size = new Size(217, 30);
            btnServicio8.TabIndex = 7;
            btnServicio8.Text = "Desbloquear Cuenta";
            btnServicio8.TextAlign = ContentAlignment.MiddleLeft;
            btnServicio8.UseVisualStyleBackColor = true;
            btnServicio8.Click += btnDesbloquearCuenta_Click;
            // 
            // btnServicio7
            // 
            btnServicio7.Dock = DockStyle.Top;
            btnServicio7.FlatAppearance.BorderSize = 0;
            btnServicio7.FlatStyle = FlatStyle.Flat;
            btnServicio7.Font = new Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point);
            btnServicio7.Location = new Point(20, 60);
            btnServicio7.Name = "btnServicio7";
            btnServicio7.Padding = new Padding(10, 0, 0, 0);
            btnServicio7.Size = new Size(217, 30);
            btnServicio7.TabIndex = 6;
            btnServicio7.Text = "Caja de Seguridad";
            btnServicio7.TextAlign = ContentAlignment.MiddleLeft;
            btnServicio7.UseVisualStyleBackColor = true;
            btnServicio7.Click += btnCajaSeguridad_Click;
            // 
            // btnServicio6
            // 
            btnServicio6.Dock = DockStyle.Top;
            btnServicio6.FlatAppearance.BorderSize = 0;
            btnServicio6.FlatStyle = FlatStyle.Flat;
            btnServicio6.Font = new Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point);
            btnServicio6.Location = new Point(20, 30);
            btnServicio6.Name = "btnServicio6";
            btnServicio6.Padding = new Padding(10, 0, 0, 0);
            btnServicio6.Size = new Size(217, 30);
            btnServicio6.TabIndex = 5;
            btnServicio6.Text = "Formalizar Credito";
            btnServicio6.TextAlign = ContentAlignment.MiddleLeft;
            btnServicio6.UseVisualStyleBackColor = true;
            btnServicio6.Click += btnFormalizarCredito_Click;
            // 
            // btnServicio5
            // 
            btnServicio5.Dock = DockStyle.Top;
            btnServicio5.FlatAppearance.BorderSize = 0;
            btnServicio5.FlatStyle = FlatStyle.Flat;
            btnServicio5.Font = new Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point);
            btnServicio5.Location = new Point(20, 0);
            btnServicio5.Name = "btnServicio5";
            btnServicio5.Padding = new Padding(10, 0, 0, 0);
            btnServicio5.Size = new Size(217, 30);
            btnServicio5.TabIndex = 4;
            btnServicio5.Text = "Solicitar Tarjeta";
            btnServicio5.TextAlign = ContentAlignment.MiddleLeft;
            btnServicio5.UseVisualStyleBackColor = true;
            btnServicio5.Click += btnSolicitarTarjeta_Click;
            // 
            // panelMenuPlataforma
            // 
            panelMenuPlataforma.Controls.Add(btnGrupo2);
            panelMenuPlataforma.Controls.Add(picIconPlataforma);
            panelMenuPlataforma.Dock = DockStyle.Top;
            panelMenuPlataforma.Location = new Point(0, 234);
            panelMenuPlataforma.Name = "panelMenuPlataforma";
            panelMenuPlataforma.Size = new Size(237, 45);
            panelMenuPlataforma.TabIndex = 9;
            // 
            // btnGrupo2
            // 
            btnGrupo2.Cursor = Cursors.Hand;
            btnGrupo2.Dock = DockStyle.Fill;
            btnGrupo2.FlatAppearance.BorderSize = 0;
            btnGrupo2.FlatStyle = FlatStyle.Flat;
            btnGrupo2.Font = new Font("Segoe UI", 12F, FontStyle.Bold, GraphicsUnit.Point);
            btnGrupo2.Location = new Point(42, 0);
            btnGrupo2.Name = "btnGrupo2";
            btnGrupo2.Padding = new Padding(10, 0, 0, 0);
            btnGrupo2.Size = new Size(195, 45);
            btnGrupo2.TabIndex = 3;
            btnGrupo2.Text = "Plataforma";
            btnGrupo2.TextAlign = ContentAlignment.MiddleLeft;
            btnGrupo2.UseVisualStyleBackColor = true;
            btnGrupo2.Click += btnPlataforma_Click;
            // 
            // picIconPlataforma
            // 
            picIconPlataforma.Dock = DockStyle.Left;
            picIconPlataforma.Image = Properties.Resources.plataforma;
            picIconPlataforma.Location = new Point(0, 0);
            picIconPlataforma.Name = "picIconPlataforma";
            picIconPlataforma.Size = new Size(42, 45);
            picIconPlataforma.SizeMode = PictureBoxSizeMode.Zoom;
            picIconPlataforma.TabIndex = 4;
            picIconPlataforma.TabStop = false;
            picIconPlataforma.Click += picIconPlataforma_Click;
            // 
            // panelSubMenuCaja
            // 
            panelSubMenuCaja.BackColor = Color.FromArgb(17, 121, 174);
            panelSubMenuCaja.Controls.Add(btnServicio4);
            panelSubMenuCaja.Controls.Add(btnServicio3);
            panelSubMenuCaja.Controls.Add(btnServicio2);
            panelSubMenuCaja.Controls.Add(btnServicio1);
            panelSubMenuCaja.Dock = DockStyle.Top;
            panelSubMenuCaja.Location = new Point(0, 106);
            panelSubMenuCaja.Name = "panelSubMenuCaja";
            panelSubMenuCaja.Padding = new Padding(20, 0, 0, 0);
            panelSubMenuCaja.Size = new Size(237, 128);
            panelSubMenuCaja.TabIndex = 4;
            // 
            // btnServicio4
            // 
            btnServicio4.Dock = DockStyle.Top;
            btnServicio4.FlatAppearance.BorderSize = 0;
            btnServicio4.FlatStyle = FlatStyle.Flat;
            btnServicio4.Font = new Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point);
            btnServicio4.Location = new Point(20, 90);
            btnServicio4.Name = "btnServicio4";
            btnServicio4.Padding = new Padding(10, 0, 0, 0);
            btnServicio4.Size = new Size(217, 30);
            btnServicio4.TabIndex = 7;
            btnServicio4.Text = "Pago de Creditos";
            btnServicio4.TextAlign = ContentAlignment.MiddleLeft;
            btnServicio4.UseVisualStyleBackColor = true;
            btnServicio4.Click += btnPagoCreditos_Click;
            // 
            // btnServicio3
            // 
            btnServicio3.Dock = DockStyle.Top;
            btnServicio3.FlatAppearance.BorderSize = 0;
            btnServicio3.FlatStyle = FlatStyle.Flat;
            btnServicio3.Font = new Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point);
            btnServicio3.Location = new Point(20, 60);
            btnServicio3.Name = "btnServicio3";
            btnServicio3.Padding = new Padding(10, 0, 0, 0);
            btnServicio3.Size = new Size(217, 30);
            btnServicio3.TabIndex = 6;
            btnServicio3.Text = "Pago de Servicios Publicos";
            btnServicio3.TextAlign = ContentAlignment.MiddleLeft;
            btnServicio3.UseVisualStyleBackColor = true;
            btnServicio3.Click += btnPagoServiciosPublicos_Click;
            // 
            // btnServicio2
            // 
            btnServicio2.Dock = DockStyle.Top;
            btnServicio2.FlatAppearance.BorderSize = 0;
            btnServicio2.FlatStyle = FlatStyle.Flat;
            btnServicio2.Font = new Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point);
            btnServicio2.Location = new Point(20, 30);
            btnServicio2.Name = "btnServicio2";
            btnServicio2.Padding = new Padding(10, 0, 0, 0);
            btnServicio2.Size = new Size(217, 30);
            btnServicio2.TabIndex = 5;
            btnServicio2.Text = "Depositos";
            btnServicio2.TextAlign = ContentAlignment.MiddleLeft;
            btnServicio2.UseVisualStyleBackColor = true;
            btnServicio2.Click += btnDepositos_Click;
            // 
            // btnServicio1
            // 
            btnServicio1.Dock = DockStyle.Top;
            btnServicio1.FlatAppearance.BorderSize = 0;
            btnServicio1.FlatStyle = FlatStyle.Flat;
            btnServicio1.Font = new Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point);
            btnServicio1.Location = new Point(20, 0);
            btnServicio1.Name = "btnServicio1";
            btnServicio1.Padding = new Padding(10, 0, 0, 0);
            btnServicio1.Size = new Size(217, 30);
            btnServicio1.TabIndex = 4;
            btnServicio1.Text = "Retiros";
            btnServicio1.TextAlign = ContentAlignment.MiddleLeft;
            btnServicio1.UseVisualStyleBackColor = true;
            btnServicio1.Click += btnRetiros_Click;
            // 
            // panelMenuCaja
            // 
            panelMenuCaja.Controls.Add(btnGrupo1);
            panelMenuCaja.Controls.Add(picIconCaja);
            panelMenuCaja.Dock = DockStyle.Top;
            panelMenuCaja.Location = new Point(0, 61);
            panelMenuCaja.Name = "panelMenuCaja";
            panelMenuCaja.Size = new Size(237, 45);
            panelMenuCaja.TabIndex = 2;
            // 
            // btnGrupo1
            // 
            btnGrupo1.Cursor = Cursors.Hand;
            btnGrupo1.Dock = DockStyle.Fill;
            btnGrupo1.FlatAppearance.BorderSize = 0;
            btnGrupo1.FlatStyle = FlatStyle.Flat;
            btnGrupo1.Font = new Font("Segoe UI", 12F, FontStyle.Bold, GraphicsUnit.Point);
            btnGrupo1.Location = new Point(42, 0);
            btnGrupo1.Name = "btnGrupo1";
            btnGrupo1.Padding = new Padding(10, 0, 0, 0);
            btnGrupo1.Size = new Size(195, 45);
            btnGrupo1.TabIndex = 3;
            btnGrupo1.Text = "Caja";
            btnGrupo1.TextAlign = ContentAlignment.MiddleLeft;
            btnGrupo1.UseVisualStyleBackColor = true;
            btnGrupo1.Click += btnCaja_Click;
            // 
            // picIconCaja
            // 
            picIconCaja.Dock = DockStyle.Left;
            picIconCaja.Image = Properties.Resources.caja;
            picIconCaja.Location = new Point(0, 0);
            picIconCaja.Name = "picIconCaja";
            picIconCaja.Size = new Size(42, 45);
            picIconCaja.SizeMode = PictureBoxSizeMode.Zoom;
            picIconCaja.TabIndex = 4;
            picIconCaja.TabStop = false;
            picIconCaja.Click += picIconCaja_Click;
            // 
            // panelMenuSuperior
            // 
            panelMenuSuperior.Controls.Add(hamburguerPic);
            panelMenuSuperior.Controls.Add(tituloPic);
            panelMenuSuperior.Dock = DockStyle.Top;
            panelMenuSuperior.Location = new Point(0, 0);
            panelMenuSuperior.Name = "panelMenuSuperior";
            panelMenuSuperior.Size = new Size(237, 61);
            panelMenuSuperior.TabIndex = 2;
            // 
            // hamburguerPic
            // 
            hamburguerPic.Cursor = Cursors.Hand;
            hamburguerPic.Dock = DockStyle.Fill;
            hamburguerPic.Image = Properties.Resources.menu;
            hamburguerPic.Location = new Point(170, 0);
            hamburguerPic.Name = "hamburguerPic";
            hamburguerPic.Size = new Size(67, 61);
            hamburguerPic.SizeMode = PictureBoxSizeMode.Zoom;
            hamburguerPic.TabIndex = 1;
            hamburguerPic.TabStop = false;
            hamburguerPic.Click += hamburguerPic_Click;
            // 
            // tituloPic
            // 
            tituloPic.Dock = DockStyle.Left;
            tituloPic.Image = Properties.Resources.Logo_removebg_preview;
            tituloPic.Location = new Point(0, 0);
            tituloPic.Name = "tituloPic";
            tituloPic.Size = new Size(170, 61);
            tituloPic.SizeMode = PictureBoxSizeMode.Zoom;
            tituloPic.TabIndex = 0;
            tituloPic.TabStop = false;
            // 
            // panelNavegador
            // 
            panelNavegador.BackColor = Color.FromArgb(124, 210, 225);
            panelNavegador.Controls.Add(tableLayoutPanel1);
            panelNavegador.Dock = DockStyle.Top;
            panelNavegador.Location = new Point(237, 0);
            panelNavegador.Name = "panelNavegador";
            panelNavegador.Size = new Size(745, 61);
            panelNavegador.TabIndex = 1;
            // 
            // panelPrincipal
            // 
            panelPrincipal.BackColor = Color.FromArgb(233, 200, 123);
            panelPrincipal.Controls.Add(panelResponsive);
            panelPrincipal.Dock = DockStyle.Fill;
            panelPrincipal.Font = new Font("Segoe UI", 9F, FontStyle.Regular, GraphicsUnit.Point);
            panelPrincipal.Location = new Point(237, 61);
            panelPrincipal.Name = "panelPrincipal";
            panelPrincipal.Size = new Size(745, 520);
            panelPrincipal.TabIndex = 2;
            // 
            // panelResponsive
            // 
            panelResponsive.ColumnCount = 4;
            panelResponsive.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 22.375391F));
            panelResponsive.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 22.3753872F));
            panelResponsive.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 22.3753834F));
            panelResponsive.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 32.873848F));
            panelResponsive.Controls.Add(panelContenedor2, 0, 0);
            panelResponsive.Controls.Add(panelContenedor1, 0, 0);
            panelResponsive.Controls.Add(listProcesos, 3, 0);
            panelResponsive.Controls.Add(panelContenedor3, 2, 0);
            panelResponsive.Dock = DockStyle.Fill;
            panelResponsive.Location = new Point(0, 0);
            panelResponsive.Name = "panelResponsive";
            panelResponsive.RowCount = 1;
            panelResponsive.RowStyles.Add(new RowStyle(SizeType.Percent, 100F));
            panelResponsive.Size = new Size(745, 520);
            panelResponsive.TabIndex = 4;
            // 
            // panelContenedor2
            // 
            panelContenedor2.ColumnCount = 1;
            panelContenedor2.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 100F));
            panelContenedor2.Dock = DockStyle.Fill;
            panelContenedor2.Location = new Point(169, 3);
            panelContenedor2.Name = "panelContenedor2";
            panelContenedor2.RowCount = 3;
            panelContenedor2.RowStyles.Add(new RowStyle(SizeType.Percent, 33.3333321F));
            panelContenedor2.RowStyles.Add(new RowStyle(SizeType.Percent, 33.3333321F));
            panelContenedor2.RowStyles.Add(new RowStyle(SizeType.Percent, 33.3333321F));
            panelContenedor2.RowStyles.Add(new RowStyle(SizeType.Absolute, 20F));
            panelContenedor2.Size = new Size(160, 514);
            panelContenedor2.TabIndex = 4;
            // 
            // panelContenedor1
            // 
            panelContenedor1.ColumnCount = 1;
            panelContenedor1.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 100F));
            panelContenedor1.Dock = DockStyle.Fill;
            panelContenedor1.Location = new Point(3, 3);
            panelContenedor1.Name = "panelContenedor1";
            panelContenedor1.RowCount = 3;
            panelContenedor1.RowStyles.Add(new RowStyle(SizeType.Percent, 33.3333321F));
            panelContenedor1.RowStyles.Add(new RowStyle(SizeType.Percent, 33.3333321F));
            panelContenedor1.RowStyles.Add(new RowStyle(SizeType.Percent, 33.3333321F));
            panelContenedor1.RowStyles.Add(new RowStyle(SizeType.Absolute, 20F));
            panelContenedor1.Size = new Size(160, 514);
            panelContenedor1.TabIndex = 3;
            // 
            // listProcesos
            // 
            listProcesos.Columns.AddRange(new ColumnHeader[] { columNombre, columPrioridad, columPeso, columnCliente });
            listProcesos.Dock = DockStyle.Fill;
            listProcesos.Location = new Point(501, 3);
            listProcesos.Name = "listProcesos";
            listProcesos.Size = new Size(241, 514);
            listProcesos.TabIndex = 0;
            listProcesos.UseCompatibleStateImageBehavior = false;
            listProcesos.View = View.Details;
            // 
            // columNombre
            // 
            columNombre.Text = "Nombre";
            columNombre.Width = 140;
            // 
            // columPrioridad
            // 
            columPrioridad.Text = "Prioridad";
            // 
            // columPeso
            // 
            columPeso.Text = "Peso";
            // 
            // columnCliente
            // 
            columnCliente.Text = "Nombre de Cliente";
            columnCliente.Width = 120;
            // 
            // panelContenedor3
            // 
            panelContenedor3.ColumnCount = 1;
            panelContenedor3.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 100F));
            panelContenedor3.Dock = DockStyle.Fill;
            panelContenedor3.Location = new Point(335, 3);
            panelContenedor3.Name = "panelContenedor3";
            panelContenedor3.RowCount = 3;
            panelContenedor3.RowStyles.Add(new RowStyle(SizeType.Percent, 33.3333321F));
            panelContenedor3.RowStyles.Add(new RowStyle(SizeType.Percent, 33.3333321F));
            panelContenedor3.RowStyles.Add(new RowStyle(SizeType.Percent, 33.3333321F));
            panelContenedor3.RowStyles.Add(new RowStyle(SizeType.Absolute, 20F));
            panelContenedor3.Size = new Size(160, 514);
            panelContenedor3.TabIndex = 1;
            // 
            // tableLayoutPanel1
            // 
            tableLayoutPanel1.ColumnCount = 5;
            tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 20F));
            tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 20F));
            tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 20F));
            tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 20F));
            tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 20F));
            tableLayoutPanel1.Controls.Add(btnPlay, 0, 0);
            tableLayoutPanel1.Controls.Add(btnStop, 1, 0);
            tableLayoutPanel1.Controls.Add(btnAcelerar, 4, 0);
            tableLayoutPanel1.Controls.Add(btnDesacelerar, 2, 0);
            tableLayoutPanel1.Controls.Add(lblVelocidad, 3, 0);
            tableLayoutPanel1.Dock = DockStyle.Fill;
            tableLayoutPanel1.Location = new Point(0, 0);
            tableLayoutPanel1.Name = "tableLayoutPanel1";
            tableLayoutPanel1.RowCount = 1;
            tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 100F));
            tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Absolute, 20F));
            tableLayoutPanel1.Size = new Size(745, 61);
            tableLayoutPanel1.TabIndex = 0;
            // 
            // btnPlay
            // 
            btnPlay.Dock = DockStyle.Fill;
            btnPlay.Image = Properties.Resources.play;
            btnPlay.Location = new Point(3, 10);
            btnPlay.Margin = new Padding(3, 10, 3, 10);
            btnPlay.Name = "btnPlay";
            btnPlay.Size = new Size(143, 41);
            btnPlay.SizeMode = PictureBoxSizeMode.Zoom;
            btnPlay.TabIndex = 0;
            btnPlay.TabStop = false;
            btnPlay.Click += btnPlay_Click;
            // 
            // btnStop
            // 
            btnStop.Dock = DockStyle.Fill;
            btnStop.Image = Properties.Resources.pausa;
            btnStop.Location = new Point(152, 10);
            btnStop.Margin = new Padding(3, 10, 3, 10);
            btnStop.Name = "btnStop";
            btnStop.Size = new Size(143, 41);
            btnStop.SizeMode = PictureBoxSizeMode.Zoom;
            btnStop.TabIndex = 1;
            btnStop.TabStop = false;
            btnStop.Click += btnStop_Click;
            // 
            // btnDesacelerar
            // 
            btnDesacelerar.Dock = DockStyle.Fill;
            btnDesacelerar.Image = Properties.Resources.hacia_atras;
            btnDesacelerar.Location = new Point(301, 10);
            btnDesacelerar.Margin = new Padding(3, 10, 3, 10);
            btnDesacelerar.Name = "btnDesacelerar";
            btnDesacelerar.Size = new Size(143, 41);
            btnDesacelerar.SizeMode = PictureBoxSizeMode.Zoom;
            btnDesacelerar.TabIndex = 2;
            btnDesacelerar.TabStop = false;
            btnDesacelerar.Click += btnDesacelerar_Click;
            // 
            // btnAcelerar
            // 
            btnAcelerar.Dock = DockStyle.Fill;
            btnAcelerar.Image = Properties.Resources.adelante;
            btnAcelerar.Location = new Point(599, 10);
            btnAcelerar.Margin = new Padding(3, 10, 3, 10);
            btnAcelerar.Name = "btnAcelerar";
            btnAcelerar.Size = new Size(143, 41);
            btnAcelerar.SizeMode = PictureBoxSizeMode.Zoom;
            btnAcelerar.TabIndex = 3;
            btnAcelerar.TabStop = false;
            btnAcelerar.Click += btnAcelerar_Click;
            // 
            // lblVelocidad
            // 
            lblVelocidad.AutoSize = true;
            lblVelocidad.Dock = DockStyle.Fill;
            lblVelocidad.Font = new Font("Segoe UI", 25F, FontStyle.Bold, GraphicsUnit.Point);
            lblVelocidad.Location = new Point(450, 10);
            lblVelocidad.Margin = new Padding(3, 10, 3, 10);
            lblVelocidad.Name = "lblVelocidad";
            lblVelocidad.Size = new Size(143, 41);
            lblVelocidad.TabIndex = 4;
            lblVelocidad.Text = "X2";
            lblVelocidad.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // Principal
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(982, 581);
            Controls.Add(panelPrincipal);
            Controls.Add(panelNavegador);
            Controls.Add(panelMenu);
            Name = "Principal";
            Text = "Principal";
            FormClosing += Principal_FormClosing;
            Load += Principal_Load;
            panelMenu.ResumeLayout(false);
            panelSubMenuServicioCliente.ResumeLayout(false);
            panelMenuServicioCliente.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)picIconServicioCliente).EndInit();
            panelSubMenuPlataforma.ResumeLayout(false);
            panelMenuPlataforma.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)picIconPlataforma).EndInit();
            panelSubMenuCaja.ResumeLayout(false);
            panelMenuCaja.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)picIconCaja).EndInit();
            panelMenuSuperior.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)hamburguerPic).EndInit();
            ((System.ComponentModel.ISupportInitialize)tituloPic).EndInit();
            panelNavegador.ResumeLayout(false);
            panelPrincipal.ResumeLayout(false);
            panelResponsive.ResumeLayout(false);
            tableLayoutPanel1.ResumeLayout(false);
            tableLayoutPanel1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)btnPlay).EndInit();
            ((System.ComponentModel.ISupportInitialize)btnStop).EndInit();
            ((System.ComponentModel.ISupportInitialize)btnDesacelerar).EndInit();
            ((System.ComponentModel.ISupportInitialize)btnAcelerar).EndInit();
            ResumeLayout(false);
        }


        #endregion

        private Panel panelMenu;
        private Panel panelNavegador;
        private Panel panelPrincipal;
        private PictureBox hamburguerPic;
        private PictureBox tituloPic;
        private Panel panelMenuSuperior;
        private Panel panelSubMenuCaja;
        private Button btnServicio3;
        private Button btnServicio2;
        private Button btnServicio1;
        private Panel panelSubMenuServicioCliente;
        private Button btnServicio11;
        private Button btnServicio10;
        private Panel panelSubMenuPlataforma;
        private Button btnServicio7;
        private Button btnServicio6;
        private Button btnServicio5;
        private Button btnServicio4;
        private Button btnServicio9;
        private Button btnServicio8;
        private PictureBox picIconCaja;
        internal Button btnGrupo1;
        private Panel panelMenuCaja;
        private Panel panelMenuServicioCliente;
        internal Button btnGrupo3;
        private PictureBox picIconServicioCliente;
        private Panel panelMenuPlataforma;
        internal Button btnGrupo2;
        private PictureBox picIconPlataforma;
        private TableLayoutPanel panelContenedor1;
        private TableLayoutPanel panelContenedor2;
        private TableLayoutPanel panelContenedor3;
        private TableLayoutPanel panelResponsive;
        private ColumnHeader columNombre;
        private ColumnHeader columPeso;
        private ColumnHeader columPrioridad;
        private ColumnHeader columnCliente;//
        private ListView listProcesos;
        private TableLayoutPanel tableLayoutPanel1;
        private PictureBox btnPlay;
        private PictureBox btnStop;
        private PictureBox btnAcelerar;
        private PictureBox btnDesacelerar;
        private Label lblVelocidad;
    }
}