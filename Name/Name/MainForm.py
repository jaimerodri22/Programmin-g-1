import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._button4 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._button1.Location = System.Drawing.Point(25, 295)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(163, 70)
        self._button1.TabIndex = 0
        self._button1.Text = "MY NAME"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._button2.Location = System.Drawing.Point(368, 297)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(173, 68)
        self._button2.TabIndex = 1
        self._button2.Text = "HIDE"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._button3.Location = System.Drawing.Point(547, 294)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(140, 69)
        self._button3.TabIndex = 2
        self._button3.Text = "EXIT"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(193, 66)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(388, 163)
        self._label1.TabIndex = 3
        # 
        # button4
        # 
        self._button4.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._button4.Location = System.Drawing.Point(203, 297)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(145, 65)
        self._button4.TabIndex = 4
        self._button4.Text = "I'M FROM"
        self._button4.UseVisualStyleBackColor = False
        self._button4.Click += self.Button4Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ControlDark
        self.ClientSize = System.Drawing.Size(725, 386)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "About Me"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
         self._label1.Text = "My name is Jaime"

    def Button2Click(self, sender, e):
         self._label1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button4Click(self, sender, e):
         self._label1.Text = "I'm from Spain"
