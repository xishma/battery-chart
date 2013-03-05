file_name=1
complete_list = []
while 1:
	try:
		f=file('%s.txt'%file_name,'r')
		times={}
		list=[]
		for line in f.read().split('\n'):
			if line!='':
				try:
					line=line.strip()
					if not times.has_key(int(line.split(':')[0])):
						times[int(line.split(':')[0])]=int(line.split(' - ')[1])
						list.append(int(line.split(' - ')[1]))
				except:
					pass
		f.close()
		complete_list.append({'name':'%s'%file_name,'data':list})
		file_name+=1
	except IOError:
		break
f=file('./Chart/data.js','w')
f.write('list=%s;'%str(complete_list));
f.close()
