import numpy as np

def outputMyInpute(Atoms,LJParams,bondParams,angleParams,dihedralParams,atoms,atomsPSF,bonds,angles,dihedrals,atomList,LJList,bondList,angleList,dihedralList,L,fileName):
	with open(fileName+".lam", "w") as f:
		f.write("\n")
		f.write(str(len(atoms))+"\tatoms\n")
		f.write(str(len(bonds))+"\tbonds\n")
		f.write(str(len(angles))+"\tangles\n")
		f.write(str(len(dihedrals))+"\tdihedrals\n\n")
		f.write(str(len(atomList))+"\tatom types\n")
		f.write(str(len(bondList))+"\tbond types\n")
		f.write(str(len(angleList))+"\tangle types\n")
		f.write(str(len(dihedralList))+"\tdihedral types\n\n")
		f.write(str(-L)+" "+str(L)+" xlo xhi\n")
		f.write(str(-L)+" "+str(L)+" ylo yhi\n")
		f.write(str(-L)+" "+str(L)+" zlo zhi\n\n")
		f.write("Masses\n\n")
		for i in np.arange(len(atomList)):
			f.write(str(i+1)+"\t"+str(atomList[i][1])+"\t#"+str(atomList[i][0])+"\n")
		f.write("\nPair Coeffs\n\n")
		for i in np.arange(len(LJList)):
			f.write(str(i+1)+"\t"+str(LJList[i][1])+"\t"+str(LJList[i][2])+"\t#"+str(LJList[i][0])+"\n")
		f.write("\nBond Coeffs\n\n")
		for i in np.arange(len(bondList)):
			f.write(str(i+1)+"\t"+str(bondList[i][1])+"\t"+str(bondList[i][2])+"\t#"+str(bondList[i][0])+"\n")
		f.write("\nAngle Coeffs\n\n")
		for i in np.arange(len(angleList)):
			f.write(str(i+1)+"\t"+str(angleList[i][1])+"\t"+str(angleList[i][2])+"\t#"+str(angleList[i][0])+"\n")
		f.write("\nDihedral Coeffs\n\n")
		for i in np.arange(len(dihedralList)):
			f.write(str(i+1)+"\t"+str(dihedralList[i][1]))
			for j in np.arange(dihedralList[i][1]):
				f.write("\t"+str(dihedralList[i][j*3+2])+"\t"+str(dihedralList[i][j*3+3])+"\t"+str(dihedralList[i][j*3+4]))
			f.write("\t#"+str(dihedralList[i][0])+"\n")
		f.write("\n\n\n\nAtoms\n\n")
		for i in np.arange(len(atoms)):
			f.write(str(i+1)+"\t"+str(int(1))+"\t"+str(int(atomsPSF[i][2]+1))+"\t"+str(atomsPSF[i][1])+"\t"+str(atoms[i][0])+"\t"+str(atoms[i][1])+"\t"+str(atoms[i][2])+"\n")
		f.write("\n\nBonds\n\n")
		for i in np.arange(len(bonds)):
			f.write(str(i+1)+"\t"+str(bonds[i][2]+1)+"\t"+str(bonds[i][0]+1)+"\t"+str(bonds[i][1]+1)+"\n")
		f.write("\n\nAngles\n\n")
		for i in np.arange(len(angles)):
			f.write(str(i+1)+"\t"+str(angles[i][3]+1)+"\t"+str(angles[i][0]+1)+"\t"+str(angles[i][1]+1)+"\t"+str(angles[i][2]+1)+"\n")
		f.write("\n\nDihedrals\n\n")
		for i in np.arange(len(dihedrals)):
			f.write(str(i+1)+"\t"+str(dihedrals[i][4]+1)+"\t"+str(dihedrals[i][0]+1)+"\t"+str(dihedrals[i][1]+1)+"\t"+str(dihedrals[i][2]+1)+"\t"+str(dihedrals[i][3]+1)+"\n")

	with open("potential.dat", "w") as f:
		for i in np.arange(0,len(LJList)-1):
			for j in np.arange(i+1,len(LJList)):
				sigma=0.5*(LJList[i][2]+LJList[j][2])
				epsilon=(LJList[i][1]*LJList[j][1])**0.5
				f.write("pair_coeff"+"\t"+str(i+1)+"\t"+str(j+1)+"\t"+str(epsilon)+"\t"+str(sigma)+"\n")


	with open(fileName+".atom", "w") as f:
		Nmyatom=12
		f.write("atom type name mass coeff1 coeff2\n")
		f.write("1	He	4.027	0.0203	2.556\n")
		f.write("2	n1	14.01	0.1636	3.18086478325\n")
		f.write("3	n2	28.02	0.14397	3.798\n")
		f.write("4	Ar	28.02	0.14397	3.798\n")
		f.write("5	c3(MeOH)	12.011	0.1094	3.4\n")
		f.write("6	oh(MeOH)	15.999	0.21	2.96\n")
		f.write("7	h1(MeOH)	1.008	0.0157	2.471\n")
		f.write("8	ho(MeOH)	1.008	0	0\n")
		f.write("9	o(H2O)	15.999	0.1521	3.15061\n")
		f.write("10	h(H2O)	1.008	0.046	0.4\n")
		f.write("11	Na	22.99	0.1	2.583\n")
		f.write("12	Cl	35.453	0.1	4.4\n")


		for i in np.arange(len(atomList)):
			f.write(str(i+Nmyatom+1)+"\t#"+str(atomList[i][0])+"\t"+str(atomList[i][1])+"\t"+str(LJList[i][1])+"\t"+str(LJList[i][2])+"\n")
		f.write("\nbond type name coeff1 coeff2\n")
		f.write("1	c3-h1(MeOH)	335.9	1.093\n")
		f.write("2	c3-oh(MeOH)	314.1	1.4260\n")
		f.write("3	ho-oh(MeOH)	369.6	0.974\n")
		for i in np.arange(len(bondList)):
			f.write(str(i+4)+"\t"+str(bondList[i][0])+"\t"+str(bondList[i][1])+"\t"+str(bondList[i][2])+"\n")
		f.write("\nangle type name coeff1 coeff2\n")
		f.write("1	h1-c3-h1(MeOH)	39.18	109.55\n")
		f.write("2	h1-c3-oh(MeOH)	50.97	109.88\n")
		f.write("3	c3-oh-ho(MeOH)	47.09	108.16\n")
		for i in np.arange(len(angleList)):
			f.write(str(i+4)+"\t"+str(angleList[i][0])+"\t"+str(angleList[i][1])+"\t"+str(angleList[i][2])+"\n")
		f.write("\ndihedral type name coeff1 coeff2 coeff3 coeff4\n")
		f.write("1	X-c3-oh-X	1	0.166666666667	3	0.0	-1	-1	-1	-1	-1	-1\n")
		for i in np.arange(len(dihedralList)):
			f.write(str(i+2)+"\t"+str(dihedralList[i][0])+"\t"+str(dihedralList[i][1]))
			for j in np.arange(dihedralList[i][1]):
				f.write("\t"+str(dihedralList[i][j*3+2])+"\t"+str(dihedralList[i][j*3+3])+"\t"+str(dihedralList[i][j*3+4]))
			for j in np.arange(3-dihedralList[i][1]):
				f.write("\t"+str(-1)+"\t"+str(-1)+"\t"+str(-1))
			f.write("\n")
		f.write("\natoms\n")
		for i in np.arange(len(atoms)):
			f.write(str(i+1)+"\t"+str(int(atomsPSF[i][2]+Nmyatom+1))+"\t"+str(atomsPSF[i][1])+"\t"+str(atoms[i][0])+"\t"+str(atoms[i][1])+"\t"+str(atoms[i][2])+"\n")
		f.write("\nbonds\n")
		for i in np.arange(len(bonds)):
			f.write(str(bonds[i][0]+1)+"\t"+str(bonds[i][1]+1)+"\t"+str(bonds[i][2]+4)+"\n")
		f.write("\nangles\n")
		for i in np.arange(len(angles)):
			f.write(str(angles[i][0]+1)+"\t"+str(angles[i][1]+1)+"\t"+str(angles[i][2]+1)+"\t"+str(angles[i][3]+4)+"\n")
		f.write("\ndihedrals\n")
		for i in np.arange(len(dihedrals)):
			f.write(str(dihedrals[i][0]+1)+"\t"+str(dihedrals[i][1]+1)+"\t"+str(dihedrals[i][2]+1)+"\t"+str(dihedrals[i][3]+1)+"\t"+str(dihedrals[i][4]+2)+"\t"+"\n")
