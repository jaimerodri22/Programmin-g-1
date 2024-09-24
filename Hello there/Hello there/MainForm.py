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
        self._buttoN3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(68, 21)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(537, 241)
        self._label1.TabIndex = 0
        self._label1.Text = " "
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label1.Click += self.Label1Click
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(68, 286)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(149, 57)
        self._button1.TabIndex = 1
        self._button1.Text = "SHOW"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(266, 290)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(204, 46)
        self._button2.TabIndex = 2
        self._button2.Text = "CLEAR"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # buttoN3
        # 
        self._buttoN3.Location = System.Drawing.Point(519, 290)
        self._buttoN3.Name = "buttoN3"
        self._buttoN3.Size = System.Drawing.Size(146, 41)
        self._buttoN3.TabIndex = 3
        self._buttoN3.Text = "EXIT"
        self._buttoN3.UseVisualStyleBackColor = True
        self._buttoN3.Click += self.ButtoN3Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(704, 356)
        self.Controls.Add(self._buttoN3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Hello there"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)


    def MainFormLoad(self, sender, e):
        pass

    def Label1Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        self._label1.Text = "Hello, world!"

    def Button2Click(self, sender, e):
        self._label1.Text = ""

    def ButtoN3Click(self, sender, e):
        Application.Exit()