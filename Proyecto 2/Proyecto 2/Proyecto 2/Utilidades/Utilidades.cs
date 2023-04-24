using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proyecto_2.Utilidades
{
    internal class Utilidades
    {
        //Login login = null;
        static int cant1 = 0;
        static int cant2 = 0;
        static int cant3 = 0;
        static PictureBox fotoAModificar = new PictureBox();

        static public int getCantCajas(int numeroGrupoServicio) {
            switch (numeroGrupoServicio)
            {
                case 1:
                    return cant1;
                case 2:
                    return cant2;
                case 3:
                    return cant3;
                default:
                    return 0;
            }
        }
        static public void setCantCajas(int numeroGrupoServicio, int cant)
        {
            switch (numeroGrupoServicio)
            {
                case 1:
                    cant1 = cant;
                    break;
                case 2:
                    cant2 = cant;
                    break;
                case 3:
                    cant3 = cant;
                    break;
                default:
                    break;
            }
        }
        static private List<Control> getAllControls(Control parent)
        {
            var controls = parent.Controls.Cast<Control>().ToList();
            return controls.SelectMany(ctrl => getAllControls(ctrl)).Concat(controls).ToList();
        }
        static public List<Button> getButtonsOfPanel(Panel panel)
        {
            return getAllControls(panel).OfType<Button>().ToList();
        }
        static public void setFotoAModificar(PictureBox foto) {
            fotoAModificar = foto;
        }
        static public PictureBox getFotoAModificar()
        {
            PictureBox foto = new PictureBox();
            foto.Dock = fotoAModificar.Dock;
            foto.SizeMode = fotoAModificar.SizeMode;
            foto.Image = fotoAModificar.Image;
            foto.Name = fotoAModificar.Name;
            return foto;
        }
    }
}
