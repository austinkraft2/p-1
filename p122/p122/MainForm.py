import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(13, 13)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(392, 290)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Tan
		self._button1.Location = System.Drawing.Point(29, 343)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(106, 65)
		self._button1.TabIndex = 1
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Tan
		self._button2.Location = System.Drawing.Point(160, 343)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(100, 65)
		self._button2.TabIndex = 2
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Tan
		self._button3.Location = System.Drawing.Point(299, 343)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(106, 65)
		self._button3.TabIndex = 3
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightSalmon
		self.ClientSize = System.Drawing.Size(429, 486)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "p122"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		heading = "Number\t\tSquare\t\tsquare Root"
		self._listBox1.Items.Add(heading)
		for num in range(1, 50+1):
			nsqrd = num**2
			nsqrt = math.sqrt(num)
			msg = str(num) + "\t\t" + str(nsqrd) + \
							 "\t\t" + str(round(nsqrt, 4))
			self._listBox1.Items.Add(msg)				 

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()