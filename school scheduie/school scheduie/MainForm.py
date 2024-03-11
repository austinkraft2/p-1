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
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.HotTrack
		self._button1.Location = System.Drawing.Point(206, 427)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(100, 42)
		self._button1.TabIndex = 0
		self._button1.Text = "show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.HotTrack
		self._button2.Location = System.Drawing.Point(402, 427)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(107, 42)
		self._button2.TabIndex = 1
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.HotTrack
		self._button3.Location = System.Drawing.Point(588, 426)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(102, 43)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.HotTrack
		self._label1.Location = System.Drawing.Point(181, 66)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(125, 51)
		self._label1.TabIndex = 3
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.HotTrack
		self._label2.Location = System.Drawing.Point(388, 66)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(106, 51)
		self._label2.TabIndex = 4
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.HotTrack
		self._label3.Location = System.Drawing.Point(601, 66)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(118, 51)
		self._label3.TabIndex = 5
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.HotTrack
		self._label4.Location = System.Drawing.Point(172, 163)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(115, 52)
		self._label4.TabIndex = 6
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.HotTrack
		self._label5.Location = System.Drawing.Point(418, 144)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(136, 53)
		self._label5.TabIndex = 7
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.HotTrack
		self._label6.Location = System.Drawing.Point(637, 181)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(130, 67)
		self._label6.TabIndex = 8
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.HotTrack
		self._label7.Location = System.Drawing.Point(296, 260)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(124, 63)
		self._label7.TabIndex = 9
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.SystemColors.HotTrack
		self._label8.Location = System.Drawing.Point(478, 251)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(132, 63)
		self._label8.TabIndex = 10
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaption
		self.ClientSize = System.Drawing.Size(942, 624)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "school scheduie"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text = "computer programning 1 EM"
		self._label2.Text = "construction"
		self._label3.Text = "english 10"
		self._label4.Text = "math"
		self._label5.Text = "tiping"
		self._label6.Text = "wlding"
		self._label7.Text = "science"
		self._label8.Text = "us history"		
		
		
	def Button2Click(self, sender, e):
		self._label1.Text = ""
		self._label2.Text = ""
		self._label3.Text = ""
		self._label4.Text = ""
		self._label5.Text = ""
		self._label6.Text = ""
		self._label7.Text = ""
		self._label8.Text = ""
		
		

	def Button3Click(self, sender, e):
		Application.Exit()