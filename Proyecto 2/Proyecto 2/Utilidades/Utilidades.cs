using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proyecto_2.Utilidades
{
    internal class Utilidades
    {
        static private List<Control> getAllControls(Control parent)
        {
            var controls = parent.Controls.Cast<Control>().ToList();
            return controls.SelectMany(ctrl => getAllControls(ctrl)).Concat(controls).ToList();
        }
        static public List<Button> getButtonsOfPanel(Panel panel)
        {
            return getAllControls(panel).OfType<Button>().ToList();
        }
        
    }
}
