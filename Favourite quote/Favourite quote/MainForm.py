﻿import System.Drawing
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
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Yellow
        self._button1.Location = System.Drawing.Point(8, 330)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(183, 69)
        self._button1.TabIndex = 0
        self._button1.Text = "SHOW"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Yellow
        self._button2.Location = System.Drawing.Point(283, 330)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(171, 68)
        self._button2.TabIndex = 1
        self._button2.Text = "HIDE"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Yellow
        self._button3.Location = System.Drawing.Point(543, 330)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(161, 66)
        self._button3.TabIndex = 2
        self._button3.Text = "EXIT"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Yellow
        self._label1.Location = System.Drawing.Point(140, 53)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(470, 200)
        self._label1.TabIndex = 3
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Black
        self.ClientSize = System.Drawing.Size(730, 411)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Favourite quote"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = " My favourite quote is from Star Wars the Return of the Jedi"
    

    def Button2Click(self, sender, e):
        self._label1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()