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
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label1.Location = System.Drawing.Point(349, 239)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(148, 56)
		self._label1.TabIndex = 0
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label2.Location = System.Drawing.Point(207, 80)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(162, 49)
		self._label2.TabIndex = 1
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label3.Location = System.Drawing.Point(495, 80)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(163, 49)
		self._label3.TabIndex = 2
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label4.Location = System.Drawing.Point(207, 159)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(162, 55)
		self._label4.TabIndex = 3
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label5.Location = System.Drawing.Point(495, 159)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(163, 55)
		self._label5.TabIndex = 4
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button1.Location = System.Drawing.Point(162, 339)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(103, 41)
		self._button1.TabIndex = 5
		self._button1.Text = "show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button2.Location = System.Drawing.Point(360, 339)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(96, 41)
		self._button2.TabIndex = 6
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button3.Location = System.Drawing.Point(543, 339)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(97, 41)
		self._button3.TabIndex = 7
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.HotTrack
		self.ClientSize = System.Drawing.Size(802, 497)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "quotes"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text = "sometimes you will win somwtimes you will learn"
		self._label2.Text = "all is well "
		self._label3.Text = "be there now "
		self._label4.Text = "believe you can "
		self._label5.Text = "do it now "
		
	def Button2Click(self, sender, e):
		self._label1.Text = ""
		self._label2.Text = ""
		self._label3.Text = ""
		self._label4.Text = ""
		self._label5.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()