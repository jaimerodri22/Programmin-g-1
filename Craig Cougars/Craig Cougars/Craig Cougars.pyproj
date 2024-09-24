import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ButtonShadow
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(174, 39)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(373, 202)
        self._label1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._button1.ForeColor = System.Drawing.SystemColors.ControlText
        self._button1.Location = System.Drawing.Point(18, 304)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(201, 83)
        self._button1.TabIndex = 1
        self._button1.Text = "SHOW"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._button2.Location = System.Drawing.Point(273, 304)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(197, 82)
        self._button2.TabIndex = 2
        self._button2.Text = "HIDE"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._button3.Location = System.Drawing.Point(514, 307)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(199, 76)
        self._button3.TabIndex = 3
        self._button3.Text = "EXIT"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ControlDark
        self.ClientSize = System.Drawing.Size(738, 429)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Craig Cougars"
        self.ResumeLayout(False)
        
        
    def label1Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
         self._label1.Text = "Go Cougars"

    def Button2Click(self, sender, e):
        self._label1.Text = ""
        

    def Button3Click(self, sender, e):
         Application.Exit()