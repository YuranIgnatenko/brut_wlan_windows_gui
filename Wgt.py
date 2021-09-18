from tkinter import *
from datetime import datetime


class WgtLabel():
	def __init__(self):
		pass

	def create(self, win, text1, text2, x, y, font_size=20):
		lb = Label(win, text=text1, relief='groove', bd=3, font='consolas 18')
		lb2 = Label(win, text=text2, relief='groove', bd=3, font='consolas ' + str(font_size))
		lb.place(x=x, y=y, width=200, height=48)
		lb2.place(x=x + 196, y=y, width=200, height=48)
		return lb2


class WgtEntry():
	def __init__(self):
		pass

	def create(self, win, text1, x, y):
		lb = Label(win, text=text1, relief='groove', bd=3, font='consolas 18')
		lb2 = Entry(win, relief='groove', bd=3, font='consolas 14')
		lb.place(x=x, y=y, width=200, height=48)
		lb2.place(x=x + 196, y=y, width=200, height=48)
		return lb2


class WgtFrameMarker():
	def __init__(self):
		pass

	def create(self, win, text1, x, y, w, h):
		f = Frame(win, relief='groove', bd=3)
		lb = Label(win, text=text1, relief='groove', bd=3, font='consolas 12')
		f.place(x=x, y=y, width=w, height=h)
		lb.place(x=x + 10, y=y - 15, width=w / 3 + w / 3, height=30)
		return f, lb


class WgtFrame():
	def __init__(self):
		pass

	def create(self, win, x, y, w, h):
		f = Frame(win, relief='groove', bd=3)
		f.place(x=x, y=y, width=w, height=h)
		return f


class WgtConsole():
	def __init__(self):
		pass

	def create(self, win, x, y, w, h, size_font=12, text=''):
		t = Text(win, relief='groove', bd=3, font='consolas ' + str(size_font))
		t.place(x=x, y=y, width=w, height=h)
		t.insert(0.0, text)
		return t


class WgtButton():
	def __init__(self):
		pass

	def create(self, win, t, x, y, w=120, h=50, com=None):
		b = Button(win, text=t, relief='groove', bd=3, font='consolas 13', command=com)
		b.place(x=x, y=y, width=w - 3, height=h)
		return b


class WgtButtonCustomUser():
	def __init__(self):
		pass

	def create(self, win, x, y, w=120, h=50, img=None, com=None):
		global image, i
		cnv = Canvas(win, bd=0)
		cnv.place(x=x, y=y, width=w + 6, height=h + 6)
		image = PhotoImage(file=img)
		i = cnv.create_image((0, 0), image=image, anchor='nw')
		cnv.bind('<Button-1>', com)
		return cnv


class WgtButtonPickCheck():
	def __init__(self):
		self.result_bool = False

	def com(self, event):
		if self.result_bool == True:
			self.result_bool = False
		elif self.result_bool == False:
			self.result_bool = True
		elif self.result_bool == None:
			self.result_bool = False
		try:
			list_child = self.fr.winfo_children()
			list_child[-1].destroy()
		except IndexError:
			pass
		self.__draw__()

	def __draw__(self):
		if self.result_bool == True:
			self.pick = Canvas(self.fr, bg=self.color_on, bd=2, relief='groove')
			self.pick.place(x=self.w / 2, y=3, width=self.w / 2, height=self.h - 3)
		elif self.result_bool == False:
			self.pick = Canvas(self.fr, bg=self.color_off, bd=2, relief='groove')
			self.pick.place(x=3, y=3, width=self.w / 2, height=self.h - 3)

	def create(self, win, x, y, w=120, h=50, color_on='white', color_off='white'):
		self.color_on = color_on
		self.color_off = color_off
		self.w = w
		self.h = h
		self.x = x
		self.y = y
		self.fr = Canvas(win, bd=2, relief='groove')
		self.fr.place(x=x, y=y, width=w + 4, height=h + 4)
		self.pick = Canvas(self.fr, bg=self.color_off, bd=2, relief='groove')
		self.pick.place(x=3, y=3, width=w / 2, height=h - 3)
		self.fr.bind("<Button-1>", self.com)
		return self.fr

	def get_bool(self):
		return self.result_bool


class WgtLoaderBarMove():
	def __init__(self):
		pass

	def create(self, win, x, y, w=120, h=50, percent=50, color_scale='white', color_signal='white', size_px = 10):
		self.color_scale = color_scale
		self.color_signal = color_signal
		self.size = size_px
		self.w = w
		self.h = h
		self.x = x
		self.y = y
		self.fr = Canvas(win, bd=2, bg=color_scale, relief='groove')
		self.fr.place(x=x, y=y, width=w + 4, height=h + 4)
		if percent > w:
			return self.fr
		self.percent_indicate = Canvas(self.fr, bg=self.color_signal, bd=0, relief='groove')
		self.percent_indicate.place(x=1 * percent, y=3, width=10, height=h - 3)
		return self.fr

	def redraw(self, percent):
		self.percent_indicate.place(x=3+1*percent, y=3, width=self.size+3, height=self.h - 3)


class WgtScrollPanelV():
	def __init__(self):
		pass

	def create(self, win, x, y, w=120, h=50, color_bg='gray', ar_wgts=[]):
		self.Y = 0
		self.Yn = 10
		self.array_wgts = ar_wgts
		self.w = w
		self.h = h
		self.x = x
		self.y = y
		self.fr = Canvas(win, bd=5, bg=color_bg, relief='groove')
		self.fr.place(x=x, y=y, width=w + 4, height=h + 4)
		self.fr.bind_all("<MouseWheel>", self.command_up)
		return self.fr

	def add_wgt(self, wgt):
		self.array_wgts.append(wgt)

	def adds_wgs(self, list_wgts):
		for wgt in list_wgts:
			self.array_wgts.append(wgt)

	def del_wgt(self, index):
		self.array_wgts.pop(index - 1)

	def get_list_wgts(self):
		return self.array_wgts

	def get_parent_wgts(self):
		return self.fr

	def command_up(self, event):
		delta = int(event.delta)
		for i in self.array_wgts:
			if delta == 120:
				# print('UP', i)
				self.Y += 10
				try:
					self.fr.moveto(i, self.w / 2, self.Y)
				except:
					self.pi = i.place_info()
					i.place(x=int(self.pi['x']), y=int(self.pi['y']) + self.Yn, width=int(self.pi['width']),
							height=int(self.pi['height']))
			elif delta == -120:
				# print('DOWN', i)
				self.Y -= 10
				try:
					self.fr.moveto(i, self.w / 2, self.Y)
				except:
					self.pi = i.place_info()
					i.place(x=int(self.pi['x']), y=int(self.pi['y']) - self.Yn, width=int(self.pi['width']),
							height=int(self.pi['height']))


class WgtScrollPanelH():
	def __init__(self):
		pass

	def create(self, win, x, y, w=120, h=50, color_bg='gray', ar_wgts=[]):
		self.X = 0
		self.Xn = 10
		self.array_wgts = ar_wgts
		self.w = w
		self.h = h
		self.x = x
		self.y = y
		self.fr = Canvas(win, bd=5, bg=color_bg, relief='groove')
		self.fr.place(x=x, y=y, width=w + 4, height=h + 4)
		self.fr.bind_all("<MouseWheel>", self.command_up)
		return self.fr

	def add_wgt(self, wgt):
		self.array_wgts.append(wgt)

	def adds_wgs(self, list_wgts):
		for wgt in list_wgts:
			self.array_wgts.append(wgt)

	def del_wgt(self, index):
		self.array_wgts.pop(index - 1)

	def get_list_wgts(self):
		return self.array_wgts

	def get_parent_wgts(self):
		return self.fr

	def command_up(self, event):
		delta = int(event.delta)
		for i in self.array_wgts:
			if delta == 120:
				self.pi = i.place_info()
				i.place(x=int(self.pi['x']) + self.Xn, y=int(self.pi['y']), width=int(self.pi['width']),
						height=int(self.pi['height']))
			elif delta == -120:
				self.pi = i.place_info()
				i.place(x=int(self.pi['x']) - self.Xn, y=int(self.pi['y']), width=int(self.pi['width']),
						height=int(self.pi['height']))


class WgtLoaderBarFill():
	def __init__(self):
		pass

	def create(self, win, x, y, w=120, h=50, percent=50, color_scale='white', color_signal='white'):
		self.color_scale = color_scale
		self.color_signal = color_signal
		self.w = w
		self.h = h
		self.x = x
		self.y = y
		self.fr = Canvas(win, bd=2, bg=color_scale, relief='groove')
		self.fr.place(x=x, y=y, width=w + 4, height=h + 4)
		if percent > w:
			return self.fr
		self.percent_indicate = Canvas(self.fr, bg=self.color_signal, bd=0, relief='groove')
		self.percent_indicate.place(x=3, y=3, width=1 * percent, height=h - 3)
		return self.fr, self.percent_indicate

	def redraw(self, percent):
		self.percent_indicate.place(x=3, y=3, width=1 * percent, height=self.h - 3)


class WgtLabelDateAndTimeNow:
	def __init__(self):
		pass

	def create(self, win, x, y, w=250, h=50):
		t = str(datetime.now())
		try:
			t = t[0: t.index(".")]
		except:
			pass
		l = Label(win, text=t, relief='groove', bd=3, font='consolas 13')
		l.place(x=x, y=y, width=w - 3, height=h)
		return l


class WgtLabelDateNow():
	def __init__(self):
		pass

	def create(self, win, x, y, w=150, h=50):
		t = str(datetime.now())
		try:
			t = t[0: t.index(" ")]
		except:
			pass
		l = Label(win, text=t, relief='groove', bd=3, font='consolas 13')
		l.place(x=x, y=y, width=w - 3, height=h)
		return l


class WgtLabelTimeNow():
	def __init__(self):
		pass

	def create(self, win, x, y, w=120, h=50):
		t = str(datetime.now())
		try:
			t = t[t.index(" "): t.index(".")]
		except:
			t = t[t.index(" "):]
		l = Label(win, text=t, relief='groove', bd=3, font='consolas 13')
		l.place(x=x, y=y, width=w - 3, height=h)
		return l


class WgtLabelTimeNowVertical():
	def __init__(self):
		pass

	def create(self, win, x, y, w=80, h=150, size_font=35):
		t = str(datetime.now())
		try:
			t = t[t.index(" "): t.index(".")]
		except:
			t = t[t.index(" "):]
		t_h = t[:t.index(":")]
		t = t[t.index(":") + 1:]
		t_m = t[:t.index(":")]
		t_s = t[t.index(":") + 1:]
		fr = Frame(win, bd=4, relief='groove')
		fr.place(x=x, y=y, width=w, height=h + 10)
		l_hour = Label(fr, text=t_h.strip(), relief='groove', bd=1, font='magneto ' + str(size_font))
		l_hour.place(x=0, y=0, width=w - 10, height=h / 3)
		l_min = Label(fr, text=t_m.strip(), relief='groove', bd=1, font='magneto ' + str(size_font))
		l_min.place(x=0, y=h / 3, width=w - 10, height=h / 3)
		l_sec = Label(fr, text=t_s.strip(), relief='groove', bd=1, font='magneto ' + str(size_font))
		l_sec.place(x=0, y=h / 3 + (h / 3), width=w - 10, height=h / 3)
		return fr, l_hour, l_min, l_sec


class WgtDrawFromDict():
	def __init__(self):
		pass

	# example:
	# ar = {'Desktop': ['movies', 1, 2, 3], 'Laptop': ['Python', 'javascript', 'PHP']}
	def create(self, win, dict_ar, x, y, w, h, size=20):
		cnv = Canvas(win, bd=2, relief='groove')
		cnv.place(x=x, y=y, width=w, height=h)
		count_key = 1
		count_all = 0
		count_last_master = 0
		counter_elem_in_key = 0
		for key in dict_ar.keys():
			# 1 |
			cnv.create_line(10, size * count_key, size, size * count_key, )
			arr_args = dict_ar.get(key)
			cnv.create_rectangle((size, size * count_key - size / 2,
								  size + size, size * count_key + size - size / 2),
								 fill='red')
			# 2 -
			cnv.create_line((size + size, size * count_key,
							 size + size + size, size * count_key))
			# 2 |
			cnv.create_line((size + size + size, size * count_key,
							 size + size + size, size * count_key + size * len(arr_args)))
			count_last_master += 1
			count_last_master += len(dict_ar.get(key))
			count_key += len(dict_ar.get(key))
			count_key += 2
			count_all += len(dict_ar.get(key))
			count_all += 1
			for arg in arr_args:
				# 3 -
				counter_elem_in_key += 1
				cnv.create_line((size + size + size, size * counter_elem_in_key + size,
								 size + size + size + size, size * counter_elem_in_key + size))
				cnv.create_rectangle(
					(size + size + size + size, size * counter_elem_in_key + size - size / 2 + size / 10,
					 size + size + size + size + size, size * counter_elem_in_key + size + size - size / 2 - size / 10),
					fill='green')
			counter_elem_in_key += 2
		# print(count_all)
		cnv.create_line((10, 10, 10, 10 + size * count_all))
		return cnv


class WgtStatisticBar():
	def __init__(self):
		pass

	def create(self, win, array_data_int, x, y, w=120, h=50,
			   array_colors=['purple', 'violet', 'pink', 'red', 'orange', 'yellow', 'cyan']):
		counter_color = -1
		cnv = Canvas(win, relief='groove', bd=3)
		cnv.place(x=x, y=y, width=w - 3, height=h)
		xx = 0
		run_one = True
		counter_x = -1
		for ww in array_data_int:
			if run_one == False:
				xx += array_data_int[counter_x]
				counter_color += 1
			elif run_one == True:
				counter_color += 1
				run_one = False
			if run_one == True:
				cnv.create_rectangle((xx, 0, ww + xx, y + h - 10), fill=array_colors[counter_color])
			elif run_one == False:
				cnv.create_rectangle((xx, 0, ww + xx, y + h - 10), fill=array_colors[counter_color])
			counter_x += 1
		return cnv


class WgtStatisticBarUniversal():
	def __init__(self):
		pass

	def create(self, win, array_data_int, x, y, w=120, h=50,
			   array_colors=['purple', 'violet', 'pink', 'red', 'orange', 'yellow', 'cyan']):
		counter_color = -1
		one_percept_in_px = int(w / 100)
		cnv = Canvas(win, relief='groove', bd=3)
		cnv.place(x=x, y=y, width=w - 3, height=h)
		xx = 0
		run_one = True
		counter_x = -1
		for ww in array_data_int:
			if run_one == False:
				xx += array_data_int[counter_x] * one_percept_in_px
				counter_color += 1
			elif run_one == True:
				counter_color += 1
				run_one = False
			if run_one == True:
				cnv.create_rectangle((xx, 0, ww * one_percept_in_px + xx, y + h - 10), fill=array_colors[counter_color])
			elif run_one == False:
				cnv.create_rectangle((xx, 0, ww * one_percept_in_px + xx, y + h - 10), fill=array_colors[counter_color])
			counter_x += 1
		return cnv


class WgtStatisticBarMarker():
	def __init__(self):
		pass

	def create(self, win, array_data_int, x, y, w=120, h=50, array_text=['text1', 'text2'],
			   array_colors=['purple', 'violet', 'pink', 'red', 'orange', 'yellow', 'cyan']):
		counter_color = 0
		cnv = Canvas(win, relief='groove', bd=3)
		cnv.place(x=x, y=y, width=w - 3, height=h)
		cnv_text = Canvas(win, relief='groove', bd=3)
		cnv_text.place(x=x, y=y + h - 3, width=w - 3, height=25 * len(array_text))
		y_pos_rect = 10
		y_pos_text = 10
		counter_text = 0
		for t in array_text:
			cnv_text.create_rectangle((10, y_pos_text, 20, y_pos_text + 10), fill=array_colors[counter_color])
			cnv_text.create_text((30, y_pos_text + 5), anchor='w', text=array_text[counter_text])
			y_pos_text += 20
			counter_text += 1
			counter_color += 1
		counter_color = -1
		xx = 0
		run_one = True
		counter_x = -1
		for ww in array_data_int:
			if run_one == False:
				xx += array_data_int[counter_x]
				counter_color += 1
			elif run_one == True:
				counter_color += 1
				run_one = False
			if run_one == True:
				cnv.create_rectangle((xx, 0, ww + xx, y + h - 10), fill=array_colors[counter_color])
			elif run_one == False:
				cnv.create_rectangle((xx, 0, ww + xx, y + h - 10), fill=array_colors[counter_color])
			counter_x += 1
		return cnv


class WgtStatisticBarMarkerUniversal():
	def __init__(self):
		pass

	def create(self, win, array_data_int, x, y, w=120, h=50, array_text=['text1', 'text2'],
			   array_colors=['purple', 'violet', 'pink', 'red', 'orange', 'yellow', 'cyan']):
		counter_color = 0
		cnv = Canvas(win, relief='groove', bd=3)
		cnv.place(x=x, y=y, width=w - 3, height=h)
		cnv_text = Canvas(win, relief='groove', bd=3)
		cnv_text.place(x=x, y=y + h - 3, width=w - 3, height=25 * len(array_text))
		y_pos_rect = 10
		y_pos_text = 10
		counter_text = 0
		for t in array_text:
			cnv_text.create_rectangle((10, y_pos_text, 20, y_pos_text + 10), fill=array_colors[counter_color])
			cnv_text.create_text((30, y_pos_text + 5), anchor='w', text=array_text[counter_text])
			y_pos_text += 20
			counter_text += 1
			counter_color += 1
		counter_color = -1
		xx = 0
		run_one = True
		counter_x = -1
		one_percept_in_px = int(w / 100)
		for ww in array_data_int:
			if run_one == False:
				xx += array_data_int[counter_x] * one_percept_in_px
				counter_color += 1
			elif run_one == True:
				counter_color += 1
				run_one = False
			if run_one == True:
				cnv.create_rectangle((xx, 0, ww * one_percept_in_px + xx, y + h - 10), fill=array_colors[counter_color])
			elif run_one == False:
				cnv.create_rectangle((xx, 0, ww * one_percept_in_px + xx, y + h - 10), fill=array_colors[counter_color])
			print(array_data_int[counter_x])
			counter_x += 1
		return cnv


class WgtCanvasAnimationImage():
	def __init__(self):
		pass

	#
	def create(self, win, array_images, num_img, x, y, w, h):
		global cnv, im
		cnv = Canvas(win, relief='groove', bd=0, )
		cnv.place(x=x, y=y, width=w, height=h)
		im = PhotoImage(file=array_images[num_img])
		cnv.create_image((0, 0), image=im, anchor='nw')


class WgtGridRect():
	def __init__(self):
		pass

	def create(self, win, x, y, w, h, col, row, arr_matrix, color_rect='white'):
		cnv = Canvas(win, relief='groove', bd=3)
		cnv.place(x=x, y=y, width=w * col + 5, height=h * row + 5)
		xx, yy, xx2, yy2 = 0, 0, w, h
		counter_loop_for = 0
		for _ in arr_matrix:
			cnv.create_rectangle((xx, yy, xx2, yy2), fill=color_rect)
			xx += w
			xx2 += w
			counter_loop_for += 1
			if counter_loop_for == col:
				yy += h
				yy2 += h
				xx, xx2 = 0, w
				counter_loop_for = 0
		return cnv


class WgtGridRectColor():
	def __init__(self):
		pass

	def create(self, win, x, y, w, h, col, row, arr_matrix, arr_colors=['red', 'green', 'blue', 'white']):
		cnv = Canvas(win, relief='groove', bd=3)
		cnv.place(x=x, y=y, width=w * col + 5, height=h * row + 5)
		xx, yy, xx2, yy2 = 0, 0, w, h
		counter_loop_for = 0
		for el in arr_matrix:
			cnv.create_rectangle((xx, yy, xx2, yy2), fill=arr_colors[el])
			xx += w
			xx2 += w
			counter_loop_for += 1
			if counter_loop_for == col:
				yy += h
				yy2 += h
				xx, xx2 = 0, w
				counter_loop_for = 0
		return cnv


class WgtDrawNetPoints():
	def __init__(self):
		pass

	def create(self, win, x, y, x2, y2):
		l = win.create_line((x, y, x2, y2))
		length_line = (x2 - x, y2 - y)
		return length_line


#
# root = Tk()
#
# root.geometry("1400x700+-10+0")
# cnv = Canvas(root, bg='black')
# cnv.place(x=0, y=0, width=1400, height=700)
# import random
# import time
# arl = []
# for i in range(2):
# 	x, y = random.randint(0, 1400), random.randint(0, 700)
# 	l = cnv.create_oval((x, y, x + 15, y + 15), fill='white')
# 	arl.append(l)
#
# while True:
# 	for i in arl:
# 		cnv.moveto(i,random.randint(0, 1400), random.randint(0, 700))
# 		root.update()
# 		time.sleep(0.3)
#
# root.mainloop()

if __name__ == '__main__':
	root = Tk()
	root.geometry("1400x700+-10+0")

	percent_progress_1 = 0
	percent_progress_2 = 0
	counter_for_test_18 = 0
	test9 = WgtLoaderBarMove()
	test9.create(root, 450, 10, 500, 20, percent_progress_1, color_scale='blue')
	test10 = WgtLoaderBarFill()
	test10.create(root, 450, 40, 500, 20, percent_progress_2, color_scale='blue')


	def test_1():
		WgtLabel().create(root, 'Имя', 'Юрий', 10, 10)


	def test_2():
		test2 = WgtEntry().create(root, 'Test 2', 10, 70)


	def test_3():
		test3 = WgtFrameMarker().create(root, 'Test 3', 10, 150, 200, 100)


	def test_4():
		test4 = WgtFrame().create(root, 10, 280, 200, 100)


	def test_5():
		test5 = WgtConsole().create(root, 10, 400, 200, 100, text='Test 5')


	def test_6():
		test6 = WgtButton().create(root, 'Test btn 6', 10, 530, 170)


	def test_7():
		test7 = WgtButtonPickCheck().create(root, 10, 600, color_on='black', color_off='black')


	def test_8():
		test8 = WgtButtonCustomUser().create(root, 10, 600, img='btn_normal.png')


	def test_9_10():
		global percent_progress_1, percent_progress_2, test10, test9
		test9.redraw(percent_progress_1)
		test10.redraw(percent_progress_2)
		percent_progress_1 += 101
		percent_progress_2 += 1
		if percent_progress_1 >= 500:
			percent_progress_1 = 0
		if percent_progress_2 >= 500:
			percent_progress_2 = 0
		root.after(100, test_9_10)


	def test_11():
		test11 = WgtLabelDateAndTimeNow().create(root, 450, 80)
		root.after(500, test_11)


	def test_12():
		test12 = WgtLabelDateNow().create(root, 450, 140)


	def test_13():
		test13 = WgtLabelTimeNow().create(root, 630, 140)
		root.update()
		root.after(0, test_13)


	def test_14():
		test14 = WgtLabelTimeNowVertical().create(root, 250, 130)
		root.after(500, test_14)


	def test_15():
		array_for_test15 = {'УТРО': [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6], 'ВЕЧЕР': [1, 2]}
		test15 = WgtDrawFromDict().create(root, array_for_test15, 220, 300, 200, 400, size=20)


	def test_16():
		arr_for_test16 = ['Яблоки', "Апельсины"]
		test16_1 = WgtStatisticBarMarker().create(root, [70, 30], 450, 200, 200, 70, array_text=arr_for_test16,
												  array_colors=['green', 'orange'])
		test16_2 = WgtStatisticBarMarkerUniversal().create(root, [70, 30], 450, 500, 200, 70, array_text=arr_for_test16,
														   array_colors=['green', 'orange'])


	def test_17():
		test17_1 = WgtStatisticBar().create(root, [10, 20, 200, 50, 100], 450, 365, 400, 20)
		test17_2 = WgtStatisticBarUniversal().create(root, [10, 20, 30, 40], 450, 350, 400, 20)


	def test_18():
		ar_image_for_test_18 = ['im1.png', 'im2.png', 'im3.png']
		global counter_for_test_18
		if counter_for_test_18 < len(ar_image_for_test_18):
			WgtCanvasAnimationImage().create(root, array_images=ar_image_for_test_18,
											 x=480, y=400, w=100, h=100, num_img=counter_for_test_18)
		elif counter_for_test_18 == len(ar_image_for_test_18):
			counter_for_test_18 = 0
			WgtCanvasAnimationImage().create(root, array_images=ar_image_for_test_18,
											 x=480, y=400, w=100, h=100, num_img=counter_for_test_18)
		counter_for_test_18 += 1
		root.after(500, test_18)


	def test_19():
		test19 = WgtGridRectColor().create(win=root, x=1000, y=10, w=50, h=50, col=5, row=6,
										   arr_matrix=[0, 1, 2, 1, 1,
													   0, 0, 2, 0, 1,
													   1, 0, 2, 0, 0,
													   1, 3, 1, 1, 2,
													   1, 3, 1, 1, 2,
													   1, 0, 0, 0, 2])


	def test_20():
		test20 = WgtGridRect().create(win=root, x=1000, y=350, w=80, h=80, col=4, row=4,
									  arr_matrix=[0, 1, 1, 1,
												  0, 0, 0, 0,
												  1, 0, 0, 0,
												  1, 1, 1, 1])


	def test_21():
		test21 = WgtScrollPanelH()
		test_21 = test21.create(root, 650, 450, 200, 200)
		b = Button(test_21, text='View Map')
		b.place(x=0, y=0, width=200, height=50)
		b2 = Button(test_21, text='Applications')
		b2.place(x=0, y=50, width=200, height=50)
		b3 = Button(test_21, text='Open Setter')
		b3.place(x=0, y=100, width=200, height=50)
		b4 = Button(test_21, text='Exiting ToGo')
		b4.place(x=0, y=150, width=200, height=50)
		b5 = Button(test_21, text='About Me')
		b5.place(x=0, y=200, width=200, height=50)
		b6 = Button(test_21, text='Network Run')
		b6.place(x=0, y=250, width=200, height=50)
		b7 = WgtButton().create(test_21, "happy test", 0, 300, 200, 50)
		b8 = WgtConsole().create(test_21, 0, 350, 200, 100, 10, "Hello world\nfrom python 3")
		test21.adds_wgs([b, b2, b3, b4, b5, b6, b7, b8])


	test_1()
	test_2()
	test_3()
	test_4()
	test_5()
	test_6()
	test_8()
	test_7()
	test_9_10()
	test_11()
	test_12()
	test_13()
	test_14()
	test_15()
	test_16()
	test_17()
	test_18()
	test_19()
	test_20()
	test_21()

	root.mainloop()
