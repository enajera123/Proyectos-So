namespace Proyecto_2
{
    partial class alertaInformacion
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
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
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            lblNombre = new Label();
            txtNombre = new TextBox();
            panelPrincipal = new Panel();
            btnCancelar = new Button();
            btnAceptar = new Button();
            checkPreferencial = new CheckBox();
            checkNoPreferencial = new CheckBox();
            panelPrincipal.SuspendLayout();
            SuspendLayout();
            // 
            // lblNombre
            // 
            lblNombre.AutoSize = true;
            lblNombre.Font = new Font("Segoe UI", 10F, FontStyle.Bold, GraphicsUnit.Point);
            lblNombre.Location = new Point(12, 30);
            lblNombre.Name = "lblNombre";
            lblNombre.Size = new Size(135, 19);
            lblNombre.TabIndex = 0;
            lblNombre.Text = "Escriba su nombre:";
            // 
            // txtNombre
            // 
            txtNombre.Location = new Point(153, 30);
            txtNombre.Name = "txtNombre";
            txtNombre.Size = new Size(165, 23);
            txtNombre.TabIndex = 1;
            // 
            // panelPrincipal
            // 
            panelPrincipal.BackColor = Color.FromArgb(97, 189, 212);
            panelPrincipal.Controls.Add(btnCancelar);
            panelPrincipal.Controls.Add(btnAceptar);
            panelPrincipal.Controls.Add(checkPreferencial);
            panelPrincipal.Controls.Add(checkNoPreferencial);
            panelPrincipal.Controls.Add(txtNombre);
            panelPrincipal.Controls.Add(lblNombre);
            panelPrincipal.Dock = DockStyle.Fill;
            panelPrincipal.Location = new Point(0, 0);
            panelPrincipal.Name = "panelPrincipal";
            panelPrincipal.Size = new Size(330, 226);
            panelPrincipal.TabIndex = 2;
            // 
            // btnCancelar
            // 
            btnCancelar.DialogResult = DialogResult.Cancel;
            btnCancelar.FlatAppearance.BorderSize = 0;
            btnCancelar.FlatStyle = FlatStyle.Popup;
            btnCancelar.Location = new Point(12, 191);
            btnCancelar.Name = "btnCancelar";
            btnCancelar.Size = new Size(75, 23);
            btnCancelar.TabIndex = 5;
            btnCancelar.Text = "Cancelar";
            btnCancelar.UseVisualStyleBackColor = true;
            // 
            // btnAceptar
            // 
            btnAceptar.DialogResult = DialogResult.OK;
            btnAceptar.FlatAppearance.BorderColor = Color.FromArgb(128, 128, 255);
            btnAceptar.FlatAppearance.BorderSize = 0;
            btnAceptar.FlatStyle = FlatStyle.Popup;
            btnAceptar.Location = new Point(243, 191);
            btnAceptar.Name = "btnAceptar";
            btnAceptar.Size = new Size(75, 23);
            btnAceptar.TabIndex = 4;
            btnAceptar.Text = "Aceptar";
            btnAceptar.UseVisualStyleBackColor = true;
            // 
            // checkPreferencial
            // 
            checkPreferencial.AutoSize = true;
            checkPreferencial.Font = new Font("Segoe UI", 9F, FontStyle.Italic, GraphicsUnit.Point);
            checkPreferencial.Location = new Point(235, 98);
            checkPreferencial.Name = "checkPreferencial";
            checkPreferencial.Size = new Size(88, 19);
            checkPreferencial.TabIndex = 3;
            checkPreferencial.Text = "Preferencial";
            checkPreferencial.UseVisualStyleBackColor = true;
            checkPreferencial.Click += checkPreferencial_Click;
            // 
            // checkNoPreferencial
            // 
            checkNoPreferencial.AutoSize = true;
            checkNoPreferencial.Font = new Font("Segoe UI", 9F, FontStyle.Italic, GraphicsUnit.Point);
            checkNoPreferencial.Location = new Point(12, 98);
            checkNoPreferencial.Name = "checkNoPreferencial";
            checkNoPreferencial.Size = new Size(106, 19);
            checkNoPreferencial.TabIndex = 2;
            checkNoPreferencial.Text = "No Preferencial";
            checkNoPreferencial.UseVisualStyleBackColor = true;
            checkNoPreferencial.Click += checkNoPreferencial_Click;
            // 
            // alertaInformacion
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(330, 226);
            Controls.Add(panelPrincipal);
            Name = "alertaInformacion";
            Text = "Informacion del Cliente";
            panelPrincipal.ResumeLayout(false);
            panelPrincipal.PerformLayout();
            ResumeLayout(false);
        }

        #endregion

        private Label lblNombre;
        private TextBox txtNombre;
        private Panel panelPrincipal;
        private Button btnAceptar;
        private CheckBox checkPreferencial;
        private CheckBox checkNoPreferencial;
        private Button btnCancelar;

        public string getTxtNombre()
        {
            return txtNombre.Text;
        }
        public string getCheckOpcion()
        {
            if (checkPreferencial.Checked)
                return "preferencial";
            else if (checkNoPreferencial.Checked)
                return "no preferencial";
            return "";
        }
        public void limpiarAlerta()
        {
            checkPreferencial.Checked = false;
            checkNoPreferencial.Checked = false;
            txtNombre.ResetText();
        }
    }
}