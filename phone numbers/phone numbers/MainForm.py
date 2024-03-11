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
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._label1.Location = System.Drawing.Point(178, 57)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(125, 26)
		self._label1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._button1.Location = System.Drawing.Point(72, 347)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 1
		self._button1.Text = "show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._button2.Location = System.Drawing.Point(251, 347)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 2
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._button3.Location = System.Drawing.Point(432, 347)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._label2.Location = System.Drawing.Point(178, 116)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(116, 26)
		self._label2.TabIndex = 4
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._label3.Location = System.Drawing.Point(373, 57)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(108, 26)
		self._label3.TabIndex = 5
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._label4.Location = System.Drawing.Point(359, 116)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(122, 26)
		self._label4.TabIndex = 6
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._label5.Location = System.Drawing.Point(263, 172)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(115, 29)
		self._label5.TabIndex = 7
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.Highlight
		self.ClientSize = System.Drawing.Size(696, 493)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "phone numbers"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text = "608 289 3457"
		self._label2.Text = "608 572 4590"
		self._label3.Text = "608 856 3057"
		self._label4.Text = "608 847 2093"
		self._label5.Text = "608 485 7895"

	def Button2Click(self, sender, e):
		self._label1.Text = ""
		self._label2.Text = ""
		self._label3.Text = ""
		self._label4.Text = ""
		self._label5.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()