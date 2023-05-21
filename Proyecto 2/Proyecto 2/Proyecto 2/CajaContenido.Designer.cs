namespace Proyecto_2
{
    partial class CajaContenido
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
            panelSuperior = new FlowLayoutPanel();
            panelFoto = new TableLayoutPanel();
            listHistorial = new ListView();
            col1 = new ColumnHeader();
            col2 = new ColumnHeader();
            col3 = new ColumnHeader();
            col4 = new ColumnHeader();
            cbEstado = new ComboBox();
            cbTipoCaja = new ComboBox();
            panelInferior = new Panel();
            btnCancelar = new Button();
            btnAceptar = new Button();
            panelSuperior.SuspendLayout();
            panelInferior.SuspendLayout();
            SuspendLayout();
            // 
            // panelSuperior
            // 
            panelSuperior.BackColor = Color.FromArgb(84, 189, 218);
            panelSuperior.Controls.Add(panelFoto);
            panelSuperior.Controls.Add(listHistorial);
            panelSuperior.Controls.Add(cbEstado);
            panelSuperior.Controls.Add(cbTipoCaja);
            panelSuperior.Dock = DockStyle.Fill;
            panelSuperior.Location = new Point(0, 0);
            panelSuperior.Name = "panelSuperior";
            panelSuperior.Size = new Size(537, 308);
            panelSuperior.TabIndex = 0;
            // 
            // panelFoto
            // 
            panelFoto.ColumnCount = 1;
            panelFoto.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 100F));
            panelFoto.Location = new Point(3, 3);
            panelFoto.Name = "panelFoto";
            panelFoto.RowCount = 1;
            panelFoto.RowStyles.Add(new RowStyle(SizeType.Percent, 100F));
            panelFoto.Size = new Size(186, 176);
            panelFoto.TabIndex = 3;
            // 
            // listHistorial
            // 
            listHistorial.Columns.AddRange(new ColumnHeader[] { col1, col2, col3, col4 });
            listHistorial.GridLines = true;
            listHistorial.Location = new Point(195, 3);
            listHistorial.Name = "listHistorial";
            listHistorial.Size = new Size(339, 176);
            listHistorial.TabIndex = 4;
            listHistorial.UseCompatibleStateImageBehavior = false;
            listHistorial.View = View.Details;
            // 
            // col1
            // 
            col1.Text = "Servicio";
            col1.Width = 120;
            // 
            // col2
            // 
            col2.Text = "Prioridad";
            // 
            // col3
            // 
            col3.Text = "Peso";
            col3.Width = 50;
            // 
            // col4
            // 
            col4.Text = "Tipo";
            col4.Width = 100;
            // 
            // cbEstado
            // 
            cbEstado.DropDownStyle = ComboBoxStyle.DropDownList;
            cbEstado.FormattingEnabled = true;
            cbEstado.Location = new Point(3, 185);
            cbEstado.Name = "cbEstado";
            cbEstado.Size = new Size(186, 23);
            cbEstado.TabIndex = 1;
            cbEstado.SelectedIndexChanged += cbEstado_SelectedIndexChanged;
            // 
            // cbTipoCaja
            // 
            cbTipoCaja.DropDownStyle = ComboBoxStyle.DropDownList;
            cbTipoCaja.FormattingEnabled = true;
            cbTipoCaja.Location = new Point(195, 185);
            cbTipoCaja.Name = "cbTipoCaja";
            cbTipoCaja.Size = new Size(152, 23);
            cbTipoCaja.TabIndex = 2;
            cbTipoCaja.SelectedIndexChanged += cbTipoCaja_SelectedIndexChanged;
            // 
            // panelInferior
            // 
            panelInferior.BackColor = Color.FromArgb(84, 189, 218);
            panelInferior.Controls.Add(btnCancelar);
            panelInferior.Controls.Add(btnAceptar);
            panelInferior.Dock = DockStyle.Bottom;
            panelInferior.Location = new Point(0, 242);
            panelInferior.Name = "panelInferior";
            panelInferior.Size = new Size(537, 66);
            panelInferior.TabIndex = 1;
            // 
            // btnCancelar
            // 
            btnCancelar.BackColor = Color.FromArgb(48, 167, 207);
            btnCancelar.CausesValidation = false;
            btnCancelar.DialogResult = DialogResult.Cancel;
            btnCancelar.FlatAppearance.BorderSize = 0;
            btnCancelar.FlatStyle = FlatStyle.Flat;
            btnCancelar.Location = new Point(12, 29);
            btnCancelar.Name = "btnCancelar";
            btnCancelar.Size = new Size(75, 23);
            btnCancelar.TabIndex = 1;
            btnCancelar.Text = "Cancelar";
            btnCancelar.UseVisualStyleBackColor = false;
            // 
            // btnAceptar
            // 
            btnAceptar.BackColor = Color.FromArgb(48, 167, 207);
            btnAceptar.DialogResult = DialogResult.OK;
            btnAceptar.FlatAppearance.BorderSize = 0;
            btnAceptar.FlatStyle = FlatStyle.Flat;
            btnAceptar.Location = new Point(328, 27);
            btnAceptar.Name = "btnAceptar";
            btnAceptar.Size = new Size(127, 25);
            btnAceptar.TabIndex = 0;
            btnAceptar.Text = "Guardar Cambios";
            btnAceptar.UseVisualStyleBackColor = false;
            btnAceptar.Click += btnAceptar_Click;
            // 
            // CajaContenido
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(537, 308);
            Controls.Add(panelInferior);
            Controls.Add(panelSuperior);
            Name = "CajaContenido";
            Text = "Ajustes";
            panelSuperior.ResumeLayout(false);
            panelInferior.ResumeLayout(false);
            ResumeLayout(false);
        }

        #endregion

        private FlowLayoutPanel panelSuperior;
        private Panel panelInferior;
        private Button btnCancelar;
        private Button btnAceptar;
        private ComboBox cbEstado;
        private ComboBox cbTipoCaja;
        private TableLayoutPanel panelFoto;
        private ListView listHistorial;
        private ColumnHeader col1;
        private ColumnHeader col2;
        private ColumnHeader col3;
        private ColumnHeader col4;
    }
}