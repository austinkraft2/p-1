import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkSalmon
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(13, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 24)
		self._label1.TabIndex = 0
		self._label1.Text = "pick a car "
		# 
		# comboBox1
		# 
		self._comboBox1.BackColor = System.Drawing.Color.LightCoral
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["1970 VW Bug ",
			"1979 firebird",
			"1980 subaru",
			"1975 cultiass"]))
		self._comboBox1.Location = System.Drawing.Point(169, 12)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(121, 21)
		self._comboBox1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkSalmon
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(13, 57)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "miles"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkSalmon
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(13, 99)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 3
		self._label3.Text = "gallons"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkSalmon
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(13, 150)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 4
		self._label4.Text = "mpg"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.DarkSalmon
		self._label5.Location = System.Drawing.Point(169, 57)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 5
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.DarkSalmon
		self._label6.Location = System.Drawing.Point(169, 99)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 6
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.DarkSalmon
		self._label7.Location = System.Drawing.Point(169, 150)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 7
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.RosyBrown
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 211)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(114, 55)
		self._button1.TabIndex = 8
		self._button1.Text = "show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.RosyBrown
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(133, 211)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(97, 55)
		self._button2.TabIndex = 9
		self._button2.Text = "cear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.RosyBrown
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(247, 211)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(104, 55)
		self._button3.TabIndex = 10
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Chocolate
		self.ClientSize = System.Drawing.Size(357, 275)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._comboBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "p 54a"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		miles = 6 
		gallons = 1
		mpg = 76
		car = self._comboBox1.Text
		
		if car == "1970 VW Bug":
			miles = 286
			gallons = 9
			
		if car == "1979 firebird":
			miles = 412
			gallons = 40
			
		if car == "1980 subaru":
			miles = 361
			gallons = 18
			
		if car == "1975 cultiass":
			miles = 161
			gallons = 11
			
		mpg = miles / float(gallons)
		mpg = round(mpg, 1)
		
		self._label7.Text = str(mpg)
		self._label6.Text = str(gallons)
		self._label5.Text = str(miles)

	def Button2Click(self, sender, e):
		self._label7.Text = ""
		self._label6.Text = ""
		self._label5.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()