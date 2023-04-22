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
            this.lblNombre = new System.Windows.Forms.Label();
            this.txtNombre = new System.Windows.Forms.TextBox();
            this.panelPrincipal = new System.Windows.Forms.Panel();
            this.btnCancelar = new System.Windows.Forms.Button();
            this.btnAceptar = new System.Windows.Forms.Button();
            this.checkPreferencial = new System.Windows.Forms.CheckBox();
            this.checkNoPreferencial = new System.Windows.Forms.CheckBox();
            this.panelPrincipal.SuspendLayout();
            this.SuspendLayout();
            // 
            // lblNombre
            // 
            this.lblNombre.AutoSize = true;
            this.lblNombre.Font = new System.Drawing.Font("Segoe UI", 10F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.lblNombre.Location = new System.Drawing.Point(12, 30);
            this.lblNombre.Name = "lblNombre";
            this.lblNombre.Size = new System.Drawing.Size(135, 19);
            this.lblNombre.TabIndex = 0;
            this.lblNombre.Text = "Escriba su nombre:";
            // 
            // txtNombre
            // 
            this.txtNombre.Location = new System.Drawing.Point(153, 30);
            this.txtNombre.Name = "txtNombre";
            this.txtNombre.Size = new System.Drawing.Size(165, 23);
            this.txtNombre.TabIndex = 1;
            // 
            // panelPrincipal
            // 
            this.panelPrincipal.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(97)))), ((int)(((byte)(189)))), ((int)(((byte)(212)))));
            this.panelPrincipal.Controls.Add(this.btnCancelar);
            this.panelPrincipal.Controls.Add(this.btnAceptar);
            this.panelPrincipal.Controls.Add(this.checkPreferencial);
            this.panelPrincipal.Controls.Add(this.checkNoPreferencial);
            this.panelPrincipal.Controls.Add(this.txtNombre);
            this.panelPrincipal.Controls.Add(this.lblNombre);
            this.panelPrincipal.Dock = System.Windows.Forms.DockStyle.Fill;
            this.panelPrincipal.Location = new System.Drawing.Point(0, 0);
            this.panelPrincipal.Name = "panelPrincipal";
            this.panelPrincipal.Size = new System.Drawing.Size(330, 226);
            this.panelPrincipal.TabIndex = 2;
            // 
            // btnCancelar
            // 
            this.btnCancelar.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.btnCancelar.FlatAppearance.BorderSize = 0;
            this.btnCancelar.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.btnCancelar.Location = new System.Drawing.Point(12, 191);
            this.btnCancelar.Name = "btnCancelar";
            this.btnCancelar.Size = new System.Drawing.Size(75, 23);
            this.btnCancelar.TabIndex = 5;
            this.btnCancelar.Text = "Cancelar";
            this.btnCancelar.UseVisualStyleBackColor = true;
            // 
            // btnAceptar
            // 
            this.btnAceptar.DialogResult = System.Windows.Forms.DialogResult.OK;
            this.btnAceptar.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(128)))), ((int)(((byte)(128)))), ((int)(((byte)(255)))));
            this.btnAceptar.FlatAppearance.BorderSize = 0;
            this.btnAceptar.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.btnAceptar.Location = new System.Drawing.Point(243, 191);
            this.btnAceptar.Name = "btnAceptar";
            this.btnAceptar.Size = new System.Drawing.Size(75, 23);
            this.btnAceptar.TabIndex = 4;
            this.btnAceptar.Text = "Aceptar";
            this.btnAceptar.UseVisualStyleBackColor = true;
            // 
            // checkPreferencial
            // 
            this.checkPreferencial.AutoSize = true;
            this.checkPreferencial.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point);
            this.checkPreferencial.Location = new System.Drawing.Point(235, 98);
            this.checkPreferencial.Name = "checkPreferencial";
            this.checkPreferencial.Size = new System.Drawing.Size(88, 19);
            this.checkPreferencial.TabIndex = 3;
            this.checkPreferencial.Text = "Preferencial";
            this.checkPreferencial.UseVisualStyleBackColor = true;
            this.checkPreferencial.CheckedChanged += new System.EventHandler(this.checkPreferencial_CheckedChanged);
            // 
            // checkNoPreferencial
            // 
            this.checkNoPreferencial.AutoSize = true;
            this.checkNoPreferencial.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point);
            this.checkNoPreferencial.Location = new System.Drawing.Point(12, 98);
            this.checkNoPreferencial.Name = "checkNoPreferencial";
            this.checkNoPreferencial.Size = new System.Drawing.Size(106, 19);
            this.checkNoPreferencial.TabIndex = 2;
            this.checkNoPreferencial.Text = "No Preferencial";
            this.checkNoPreferencial.UseVisualStyleBackColor = true;
            this.checkNoPreferencial.CheckedChanged += new System.EventHandler(this.checkNoPreferencial_CheckedChanged);
            // 
            // alertaInformacion
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(330, 226);
            this.Controls.Add(this.panelPrincipal);
            this.Name = "alertaInformacion";
            this.Text = "Informacion del Cliente";
            this.panelPrincipal.ResumeLayout(false);
            this.panelPrincipal.PerformLayout();
            this.ResumeLayout(false);

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
        public void limpiarAlerta() {
            checkPreferencial.Checked = false;
            checkNoPreferencial.Checked = false;
            txtNombre.ResetText();
        }
    }
}