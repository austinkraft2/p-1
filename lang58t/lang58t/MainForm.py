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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._label15 = System.Windows.Forms.Label()
		self._label16 = System.Windows.Forms.Label()
		self._label17 = System.Windows.Forms.Label()
		self._label18 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightSeaGreen
		self._label1.Location = System.Drawing.Point(39, 185)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "dollars"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightSeaGreen
		self._label2.Location = System.Drawing.Point(39, 242)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "quarters"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LightSeaGreen
		self._label3.Location = System.Drawing.Point(39, 298)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "dimes"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.LightSeaGreen
		self._label4.Location = System.Drawing.Point(39, 358)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "nickels"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.LightSeaGreen
		self._label5.Location = System.Drawing.Point(39, 422)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 4
		self._label5.Text = "pennies"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Aquamarine
		self._label6.Location = System.Drawing.Point(206, 185)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 5
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Aquamarine
		self._label7.Location = System.Drawing.Point(206, 242)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 6
		self._label7.Text = "1"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Aquamarine
		self._label8.Location = System.Drawing.Point(206, 298)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 7
		self._label8.Text = "1"
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.Aquamarine
		self._label9.Location = System.Drawing.Point(206, 358)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 8
		self._label9.Text = "1"
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.Aquamarine
		self._label10.Location = System.Drawing.Point(206, 422)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(100, 23)
		self._label10.TabIndex = 9
		self._label10.Text = "1"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(330, 256)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 10
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(330, 185)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 11
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(354, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(89, 39)
		self._button1.TabIndex = 12
		self._button1.Text = "show"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(354, 54)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(86, 39)
		self._button2.TabIndex = 13
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(354, 96)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(86, 40)
		self._button3.TabIndex = 14
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label11.Location = System.Drawing.Point(27, 32)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(100, 23)
		self._label11.TabIndex = 15
		self._label11.Text = "starting money"
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label12.Location = System.Drawing.Point(27, 73)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(100, 23)
		self._label12.TabIndex = 16
		self._label12.Text = "money left "
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label13.Location = System.Drawing.Point(27, 114)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(100, 23)
		self._label13.TabIndex = 17
		self._label13.Text = "change due "
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label14.Location = System.Drawing.Point(184, 113)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(100, 23)
		self._label14.TabIndex = 18
		# 
		# label15
		# 
		self._label15.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label15.Location = System.Drawing.Point(330, 159)
		self._label15.Name = "label15"
		self._label15.Size = System.Drawing.Size(100, 23)
		self._label15.TabIndex = 19
		self._label15.Text = "label15"
		# 
		# label16
		# 
		self._label16.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label16.Location = System.Drawing.Point(330, 221)
		self._label16.Name = "label16"
		self._label16.Size = System.Drawing.Size(100, 23)
		self._label16.TabIndex = 20
		self._label16.Text = "label16"
		# 
		# label17
		# 
		self._label17.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label17.Location = System.Drawing.Point(184, 32)
		self._label17.Name = "label17"
		self._label17.Size = System.Drawing.Size(100, 23)
		self._label17.TabIndex = 21
		# 
		# label18
		# 
		self._label18.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label18.Location = System.Drawing.Point(184, 74)
		self._label18.Name = "label18"
		self._label18.Size = System.Drawing.Size(100, 23)
		self._label18.TabIndex = 22
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(452, 645)
		self.Controls.Add(self._label18)
		self.Controls.Add(self._label17)
		self.Controls.Add(self._label16)
		self.Controls.Add(self._label15)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
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
		self.Text = "lang58t"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
	

	def Button2Click(self, sender, e):
		self._label6.Text = ""
		self._label7.Text = ""
		self._label8.Text = ""
		self._label9.Text = ""
		self._label10.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()