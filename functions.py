def parameterLists(Atoms,LJParams,bondParams,angleParams,dihedralParams,atoms,atomPSF,bonds,angles,dihedrals,atomList,LJList,bondList,angleList,dihedralList):
	# Atoms: mass file [[atomName,m],...]
	# LJparams: lj parameters file [[atomName,epusilon,sigma],...]
	# bondParams: bond parameters file [[atomName1-atomName2,K,l],...]
	# angleParams: angle parameters file [[atomName1-atomName2-atomName3,K,theta],...]
	# dihedralParams: dihedral parameters file [[atomName1-atomName2-atomName3-atomName4,...],...]

	# atoms: [[x,y,z],...]
	# bonds: [[atomID1,atomID2],...]
	# bondUniq: [[atomID1,atomID2],...] (unique bonds array)
	# angles: [[atomID1,atomID2,atomID3],...] (unique bonds array)
	# dihedrals: [[atomID1,atomID2,atomID3,atomID4],...] (unique bonds array)

	# atoms: [[x,y,z],...]
	# atomPSF: [[atomName,charge],...] -> [[atomName,charge,atomID],...]
	# atomID is index of atomList
	# atomList: [] -> [[atomName,m],...]
	for i in atomPSF:
		flag=0
		for j in Atoms:
			if(j[0]==i[0]):	## if the atom names are same
				if(atomList.count(j)==0):	## if atomList don't have the atom name "j[0]" (new atom type)
					atomList.append(j)
				i.append(atomList.index(j))
				flag=1
		if(flag==0):
			print("could not find "+str(i[0])+" "+str(atoms.index(i)))


	# LJList: [] -> [[atomName,epusilon,sigma],...]
	for i in atomPSF:
		for j in LJParams:
			if(j[0]==i[0]):
				if(LJList.count(j)==0):
					LJList.append(j)

	# bonds: [[atomID1,atomID2],...] -> [[atomID1,atomID2,bondID],...]
	# bondList: [] -> [[atomName1-atomName2,K,l],...]
	for i in bonds:
		bondType1=atomPSF[i[0]][0]+"-"+atomPSF[i[1]][0]
		bondType2=atomPSF[i[1]][0]+"-"+atomPSF[i[0]][0]
		flag=0
		for j in bondParams:
			if(j[0]==bondType1 or j[0]==bondType2):
				if(bondList.count(j)==0):
					bondList.append(j)
				indexBondList=bondList.index(j)
				i.append(indexBondList)
				flag=1
		if(flag==0):
			print("could not find "+str(bondType1)+" bid="+str(bondUniq.index(i))+" aid1="+str(i[0])+" aid2="+str(i[1]))

	# angles: [[atomID1,atomID2,atomID3],...] -> [[atomID1,atomID2,atomID3,angleID],...]
	# angleList: [] -> [[atomName1-atomName2-atomName3,K,theta],...]
	for i in angles:
		angleType1=atomPSF[i[0]][0]+"-"+atomPSF[i[1]][0]+"-"+atomPSF[i[2]][0]
		angleType2=atomPSF[i[2]][0]+"-"+atomPSF[i[1]][0]+"-"+atomPSF[i[0]][0]
		flag=0
		for j in angleParams:
			if(j[0]==angleType1 or j[0]==angleType2):
				if(angleList.count(j)==0):
					angleList.append(j)
				indexAngleList=angleList.index(j)
				i.append(indexAngleList)
				flag=1
		if(flag==0):
			print("could not find "+str(angleType1)+ " aid1="+str(i[0])+" aid2="+str(i[1])+" aid3="+str(i[2]))


	for i in dihedrals:
		dihedralType1=atomPSF[i[0]][0]+"-"+atomPSF[i[1]][0]+"-"+atomPSF[i[2]][0]+"-"+atomPSF[i[3]][0]
		dihedralType2=atomPSF[i[3]][0]+"-"+atomPSF[i[2]][0]+"-"+atomPSF[i[1]][0]+"-"+atomPSF[i[0]][0]
		flag=0
		for j in dihedralParams:
			if(j[0]==dihedralType1 or j[0]==dihedralType2):
				if(dihedralList.count(j)==0):
					dihedralList.append(j)
				indexDihedralList=dihedralList.index(j)
				i.append(indexDihedralList)
				flag=1
		if(flag==0):
			dihedralType1="X-"+atomPSF[i[1]][0]+"-"+atomPSF[i[2]][0]+"-X"
			dihedralType2="X-"+atomPSF[i[2]][0]+"-"+atomPSF[i[1]][0]+"-X"
			for j in dihedralParams:
				if(j[0]==dihedralType1 or j[0]==dihedralType2):
					if(dihedralList.count(j)==0):
						dihedralList.append(j)
					indexDihedralList=dihedralList.index(j)
					i.append(indexDihedralList)
					flag=1
		if(flag==0):
			print("could not find "+str(dihedralType1)+ " aid1="+str(i[0])+" aid2="+str(i[1])+" aid3="+str(i[2])+" aid4="+str(i[3]))
