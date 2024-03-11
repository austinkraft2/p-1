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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(58, 102)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "length"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(58, 150)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "width"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(240, 99)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 2
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(240, 170)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 3
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(58, 207)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 4
		self._label3.Text = "area"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.HighlightText
		self._label4.Location = System.Drawing.Point(58, 262)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 5
		self._label4.Text = "perimeter"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label5.Location = System.Drawing.Point(240, 217)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 6
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label6.Location = System.Drawing.Point(240, 262)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 7
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(73, 349)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(108, 39)
		self._button1.TabIndex = 8
		self._button1.Text = "calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(230, 349)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(110, 39)
		self._button2.TabIndex = 9
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(148, 400)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(107, 40)
		self._button3.TabIndex = 10
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.InactiveBorder
		self.ClientSize = System.Drawing.Size(387, 468)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog52a"
		self.ResumeLayout(False)
		self.PerformLayout()


	

	def Button1Click(self, sender, e):
		length = int(self._textbox1.text)
		width = int(self._textbox2.text)
		# + - * / % ** pow  // divide and round down 
		area = length * width
		perim = 2 * length + 2 * width 
		
		self._label3.text = str(area)
		self._label4.text = str(perim)
		#int (tnteager): a whole number pos/neg 
		

	def Button2Click(self, sender, e):
		self._textbox1.text = ""
		self._textbox2.text = ""
		self._labl3.text = ""
		self._label4.text = ""

	def Button3Click(self, sender, e):
		Application.Exit()