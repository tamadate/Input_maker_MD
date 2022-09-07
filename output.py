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
		f.write("atom type name mass coeff1 coeff2\n")
		for i in np.arange(len(atomList)):
			f.write(str(i+1)+"\t#"+str(atomList[i][0])+"\t"+str(atomList[i][1])+"\t"+str(LJList[i][1])+"\t"+str(LJList[i][2])+"\n")
		f.write("\nbond type name coeff1 coeff2\n")
		for i in np.arange(len(bondList)):
			f.write(str(i+1)+"\t"+str(bondList[i][0])+"\t"+str(bondList[i][1])+"\t"+str(bondList[i][2])+"\n")
		f.write("\nangle type name coeff1 coeff2\n")
		for i in np.arange(len(angleList)):
			f.write(str(i+1)+"\t"+str(angleList[i][0])+"\t"+str(angleList[i][1])+"\t"+str(angleList[i][2])+"\n")
		f.write("\ndihedral type name coeff1 coeff2 coeff3 coeff4\n")
		for i in np.arange(len(dihedralList)):
			f.write(str(i+1)+"\t"+str(dihedralList[i][0])+"\t"+str(dihedralList[i][1]))
			for j in np.arange(dihedralList[i][1]):
				f.write("\t"+str(dihedralList[i][j*3+2])+"\t"+str(dihedralList[i][j*3+3])+"\t"+str(dihedralList[i][j*3+4]))
			for j in np.arange(3-dihedralList[i][1]):
				f.write("\t"+str(-1)+"\t"+str(-1)+"\t"+str(-1))
			f.write("\n")
		f.write("\natoms\n")
		for i in np.arange(len(atoms)):
			f.write(str(i+1)+"\t"+str(int(atomsPSF[i][2]+1))+"\t"+str(atomsPSF[i][1])+"\t"+str(atoms[i][0])+"\t"+str(atoms[i][1])+"\t"+str(atoms[i][2])+"\n")
		f.write("\nbonds\n")
		for i in np.arange(len(bonds)):
			f.write(str(bonds[i][0]+1)+"\t"+str(bonds[i][1]+1)+"\t"+str(bonds[i][2]+4)+"\n")
		f.write("\nangles\n")
		for i in np.arange(len(angles)):
			f.write(str(angles[i][0]+1)+"\t"+str(angles[i][1]+1)+"\t"+str(angles[i][2]+1)+"\t"+str(angles[i][3]+4)+"\n")
		f.write("\ndihedrals\n")
		for i in np.arange(len(dihedrals)):
			f.write(str(dihedrals[i][0]+1)+"\t"+str(dihedrals[i][1]+1)+"\t"+str(dihedrals[i][2]+1)+"\t"+str(dihedrals[i][3]+1)+"\t"+str(dihedrals[i][4]+2)+"\t"+"\n")
