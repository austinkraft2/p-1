import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkSalmon
		self._label1.Location = System.Drawing.Point(34, 77)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkSalmon
		self._label2.Location = System.Drawing.Point(175, 316)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkSalmon
		self._label3.Location = System.Drawing.Point(175, 258)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkSalmon
		self._label4.Location = System.Drawing.Point(184, 206)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 3
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.DarkSalmon
		self._label5.Location = System.Drawing.Point(184, 142)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 4
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.DarkSalmon
		self._label6.Location = System.Drawing.Point(34, 316)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 5
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.DarkSalmon
		self._label7.Location = System.Drawing.Point(34, 258)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 6
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.DarkSalmon
		self._label8.Location = System.Drawing.Point(184, 77)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 7
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.DarkSalmon
		self._label9.Location = System.Drawing.Point(34, 206)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 8
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.DarkSalmon
		self._label10.Location = System.Drawing.Point(34, 142)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(100, 23)
		self._label10.TabIndex = 9
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Orange
		self._button1.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._button1.Location = System.Drawing.Point(370, 108)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(87, 47)
		self._button1.TabIndex = 10
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Orange
		self._button2.Location = System.Drawing.Point(370, 182)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(87, 47)
		self._button2.TabIndex = 11
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Orange
		self._button3.Location = System.Drawing.Point(370, 258)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(87, 47)
		self._button3.TabIndex = 12
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Bisque
		self.ClientSize = System.Drawing.Size(470, 552)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "p93a"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		

	def Button3Click(self, sender, e):
		pass