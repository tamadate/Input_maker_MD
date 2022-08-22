import math
import numpy as np

def readMass(Atoms):
	with open("mass.dat", "r") as f:
		fileData=f.readlines()
	for line in fileData:
		s=line.split()
		Atoms.append([s[0],float(s[1])])

def readLJ(LJparams):
	with open("lj.dat", "r") as f:
		fileData=f.readlines()
	for line in fileData:
		s=line.split()
		LJparams.append([s[0],float(s[2]),float(s[3])])

def readBond(bondParams):
	with open("bond.dat", "r") as f:
		fileData=f.readlines()
	for line in fileData:
		s=line.split()
		bondParams.append([s[0],float(s[1]),float(s[2])])


def readAngle(angleParams):
	with open("angle.dat", "r") as f:
		fileData=f.readlines()
	for line in fileData:
		s=line.split()
		angleParams.append([s[0],float(s[1]),float(s[2])])


def readDihedral(dihedralParams):
	with open("dihedral.dat", "r") as f:
		fileData=f.readlines()
	for line in fileData:
		s=line.split()
		if(int(s[1])==1):
			dihedralParams.append([s[0],int(s[1]),float(s[2]),int(s[3]),float(s[4]),0,0,0,0,0,0])
		if(int(s[1])==2):
			dihedralParams.append([s[0],int(s[1]),float(s[2]),int(s[3]),float(s[4]),float(s[5]),int(s[6]),float(s[7]),0,0,0])
		if(int(s[1])==3):
			dihedralParams.append([s[0],int(s[1]),float(s[2]),int(s[3]),float(s[4]),float(s[5]),int(s[6]),float(s[7]),float(s[8]),int(s[9]),float(s[10])])


def readPDBfile(atoms,bonds,bondUniq,angles,dihedrals,fileName):
	with open(fileName, "r") as f:
		file_data = f.readlines()
	for line in file_data:
		s=line.split()
		if(s[0]=="HETATM" or s[0]=="ATOM"):
			atoms.append([s[2],float(s[6]),float(s[7]),float(s[8])])
		if(s[0]=="CONECT"):
			bond=[int(s[1])-1]
			for i in s[2:]:
				bond.append(int(i)-1)
				if(int(s[1])<int(i)):
					bondUniq.append([int(s[1])-1,int(i)-1])
			bonds.append(bond)
	for i in bonds:
		if(len(i)<3):
			continue
		for j in np.arange(1,len(i)):
			for k in np.arange(j+1,len(i)):
				angles.append([i[j],i[0],i[k]])
	for i in bonds:
		if(len(i)<3):
			continue
		i2=i[0]
		for i3 in i[1:]:
			if(i3>i2):
				for i1 in i[1:]:
					if(i3!=i1):
						for i4 in bonds[i3][1:]:
							if(i4!=i2):
								dihedrals.append([i1,i2,i3,i4])
