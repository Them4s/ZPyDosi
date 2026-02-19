from ZPyDosi.Common.ExcelSheet import ExcelSheet
import datetime

input = ExcelSheet("petale_test24.xlsx")
path_out = "petale_test25b.xlsx"

def aff(d):
	return str(d).split()[0].replace("-","_")

def to_date(s):
	return datetime.datetime(*map(lambda s:int(s), s.split("_")))


if False:
	d1 = datetime.datetime(2020, 9, 7)
	d2 = datetime.datetime(2020,10,12)
	dt = d2-d1
	
	for i in range(input.get_nb_row()):
		for j in [1,8]:
			v = input.get(i,j)
			if type(v)==str and v.startswith("2020_"):
				d = datetime.datetime(*map(lambda s:int(s), v.split("_")))
				print(aff(d), aff(d+dt))
				input.set(i,j, aff(d+dt))

if False:
	d_replace = {
		"expSS":"expNi",
		"Pss"  :"Pni",
		#"expCr":"expCr",
		"expFe":"expSS",
		"Pfe"  :"Pss",
		"expNi":"expFe",
		"Pni"  :"Pfe",
	}
	#for i in range(20, 240):
	for i in range(input.get_nb_row()):
		for j in [0, 1, 2]:
			v = input.get(i,j)
			if type(v)==str:
				v_new = None
				for k,r in d_replace.items():
					if v_new is None and k in v:
						v_new = v.replace(k,r)
				if v_new is not None:
					print(v+" "*(20-len(v)),v_new)
					input.set(i,j, v_new)

if True:
	imax = input.get_nb_row()

	def comp(e1,e2, startswith=None):
		print("\n"+"#"*20,e1,e2)
		i = 0
		while type(input.get(i,0)) != str or not input.get(i,0) == e1: i += 1
		d1 = to_date(input.get(i+3,1))
		while str(input.get(i,1)) != "name": i += 1
		i += 1
		l1 = []
		while type(input.get(i,1)) == str:
			#print(" "*10,input.get(i,1), to_date(input.get(i,8)),input.get(i,9),input.get(i,10))
			#l1 += [[input.get(i,1),to_date(input.get(i,8)),input.get(i,9),input.get(i,10)]]
			l1 += [list(map(lambda j: input.get(i,j), range(19)))]
			i += 1
		
		i = 0
		while type(input.get(i,0)) != str or not input.get(i,0) == e2: i += 1
		d2 = to_date(input.get(i+3,1))
		diff_d = (d2-d1)#.total_seconds()/3600/24
		while str(input.get(i,1)) != "name": i += 1
		i += 1
		i0 = i
		d_pos = input.get(i,16) - l1[0][16]
		while type(input.get(i,1)) == str:
			l_arg = l1.pop(0)

			if l_arg[1].split("-")[0] != input.get(i,1).split("-")[0] or l_arg[1].split("-")[-1] != input.get(i,1).split("-")[-1]:
				print(i-i0, l_arg[1] , input.get(i,1), "name")
				exit()
			if l_arg[5] != input.get(i,5):
				print(i-i0, l_arg[1] , input.get(i,1), "pos_barre")
				exit()
			if l_arg[6] != input.get(i,6):
				print(i-i0, l_arg[1] , input.get(i,1), "pos [cm]")
				exit()
			if startswith is None or input.get(i,1).startswith(startswith):
				change, old = False, list(map(lambda j: input.get(i,j), range(19)))
				new_date = to_date(l_arg[8]) + diff_d
				if new_date != to_date(input.get(i,8)):
					#print('coin', new_date, to_date(input.get(i,8)))
					change = True
					input.set(i, 8, aff(new_date))
				#else:
				#	print(new_date, to_date(input.get(i,8)))
				if l_arg[16] != input.get(i,16) + d_pos:
					change = True
					input.set(i, 16, l_arg[16] + d_pos)
				for j in [9,10,11,12,13,14,15,17,18]:
					if input.get(i,j) != l_arg[j]:
						change = True
						input.set(i, j, l_arg[j])
				if change:
					print()
					print (old)
					print (list(map(lambda j: input.get(i,j), range(19))))
			else:
				print(input.get(i,1), "pass")
			i += 1
	
	comp("expNi_al", "expSS_al", "Al")
	comp("expNi_al", "expCr_al", "Al")
	comp("expNi_al", "expFe_al", "Al")
	'''
	comp("expCr_fe_ni", "expNi_fe_ni")
	
	comp("expCr_fe_ni", "expSS_fe_ni")
	comp("expCr_in1"  , "expSS_in1"  )
	comp("expCr_in2"  , "expSS_in2"  )
	comp("expCr_au"   , "expSS_au"   )
	comp("expCr_al"   , "expSS_al"   )
	
	comp("expCr_fe_ni", "expFe_fe_ni")
	comp("expCr_in1"  , "expFe_in1"  )
	comp("expCr_in2"  , "expFe_in2"  )
	comp("expCr_au"   , "expFe_au"   )
	comp("expCr_al"   , "expFe_al"   )
	'''
	'''
	i = 0
	while i<imax:
		if type(input.get(i,0)) == str and input.get(i,0).startswith("exp"):
			name = input.get(i,0)
			if "expSS" in name:
				break
			d = to_date(input.get(i+3,1))
			print(name,d)
			while str(input.get(i,1)) != "name": #type(input.get(i,1)) == str and
				i += 1
			i += 1
			l = []
			while type(input.get(i,1)) == str:
				print(" "*10,input.get(i,1), to_date(input.get(i,8)),input.get(i,9),input.get(i,10))
				l += [[to_date(input.get(i,8)),input.get(i,9),input.get(i,10)]]
				i += 1
		i += 1'''
	
print(path_out)
input.save(path_out)
