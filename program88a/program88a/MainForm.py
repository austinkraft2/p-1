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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
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
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._label15 = System.Windows.Forms.Label()
		self._label16 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Salmon
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(298, 145)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(102, 58)
		self._button1.TabIndex = 0
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Salmon
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.Black
		self._button2.Location = System.Drawing.Point(298, 219)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(102, 58)
		self._button2.TabIndex = 1
		self._button2.Text = "Cear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Salmon
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(298, 295)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(102, 62)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(159, 13)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(159, 64)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 4
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Coral
		self._label1.Location = System.Drawing.Point(13, 16)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 5
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Coral
		self._label2.Location = System.Drawing.Point(12, 62)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 6
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.OrangeRed
		self._label3.Location = System.Drawing.Point(40, 147)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 7
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.OrangeRed
		self._label4.Location = System.Drawing.Point(40, 234)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 8
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.OrangeRed
		self._label5.Location = System.Drawing.Point(40, 191)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 9
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.OrangeRed
		self._label6.Location = System.Drawing.Point(40, 284)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 10
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.OrangeRed
		self._label7.Location = System.Drawing.Point(40, 405)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 11
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.OrangeRed
		self._label8.Location = System.Drawing.Point(40, 362)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 12
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.OrangeRed
		self._label9.Location = System.Drawing.Point(40, 322)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 13
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.OrangeRed
		self._label10.Location = System.Drawing.Point(159, 322)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(100, 23)
		self._label10.TabIndex = 14
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.OrangeRed
		self._label11.Location = System.Drawing.Point(159, 191)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(100, 23)
		self._label11.TabIndex = 15
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.OrangeRed
		self._label12.Location = System.Drawing.Point(159, 362)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(100, 23)
		self._label12.TabIndex = 16
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.OrangeRed
		self._label13.Location = System.Drawing.Point(159, 405)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(100, 23)
		self._label13.TabIndex = 17
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.Color.OrangeRed
		self._label14.Location = System.Drawing.Point(159, 284)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(100, 23)
		self._label14.TabIndex = 18
		# 
		# label15
		# 
		self._label15.BackColor = System.Drawing.Color.OrangeRed
		self._label15.Location = System.Drawing.Point(159, 234)
		self._label15.Name = "label15"
		self._label15.Size = System.Drawing.Size(100, 23)
		self._label15.TabIndex = 19
		# 
		# label16
		# 
		self._label16.BackColor = System.Drawing.Color.OrangeRed
		self._label16.Location = System.Drawing.Point(159, 147)
		self._label16.Name = "label16"
		self._label16.Size = System.Drawing.Size(100, 23)
		self._label16.TabIndex = 20
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.IndianRed
		self.ClientSize = System.Drawing.Size(412, 471)
		self.Controls.Add(self._label16)
		self.Controls.Add(self._label15)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
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
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "program88a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		min._textBox1
		self._label16.Text = ""
		self._label11.Text = ""
		self._label15.Text = ""
		self._label14.Text = ""
		self._label10.Text = ""
		self._label12.Text = "" 
		self._label13.Text = "" 
		
		

	def Button2Click(self, sender, e):
		self._label16.Text = ""
		self._label11.Text = ""
		self._label15.Text = ""
		self._label14.Text = ""
		self._label10.Text = ""
		self._label12.Text = ""
		self._label13.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()