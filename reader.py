import math
import numpy as np

def readMass(Atoms):
	with open("gaff/mass.dat", "r") as f:
		fileData=f.readlines()
	for line in fileData:
		s=line.split()
		Atoms.append([s[0],float(s[1])])

def readLJ(LJparams):
	with open("gaff/lj.dat", "r") as f:
		fileData=f.readlines()
	for line in fileData:
		s=line.split()
		LJparams.append([s[0],float(s[2]),float(s[3])])

def readBond(bondParams):
	with open("gaff/bond.dat", "r") as f:
		fileData=f.readlines()
	for line in fileData:
		s=line.split()
		bondParams.append([s[0],float(s[1]),float(s[2])])


def readAngle(angleParams):
	with open("gaff/angle.dat", "r") as f:
		fileData=f.readlines()
	for line in fileData:
		s=line.split()
		angleParams.append([s[0],float(s[1]),float(s[2])])


def readDihedral(dihedralParams):
	with open("gaff/dihedral.dat", "r") as f:
		fileData=f.readlines()
	for line in fileData:
		s=line.split()
		if(int(s[1])==1):
			dihedralParams.append([s[0],int(s[1]),float(s[2]),int(s[3]),float(s[4]),0,0,0,0,0,0])
		if(int(s[1])==2):
			dihedralParams.append([s[0],int(s[1]),float(s[2]),int(s[3]),float(s[4]),float(s[5]),int(s[6]),float(s[7]),0,0,0])
		if(int(s[1])==3):
			dihedralParams.append([s[0],int(s[1]),float(s[2]),int(s[3]),float(s[4]),float(s[5]),int(s[6]),float(s[7]),float(s[8]),int(s[9]),float(s[10])])


def readPDBfile(atoms,fileName):
	with open(fileName, "r") as f:
		file_data = f.readlines()
	for line in file_data:
		s=line.split()
		if(s[0]=="HETATM" or s[0]=="ATOM"):
			atoms.append([float(s[5]),float(s[6]),float(s[7])])


def readPSFfile(atomPSF,bonds,angles,dihedrals,fileName):
	with open(fileName, "r") as f:
		file_data = f.readlines()
	flag=0
	Nthings=0
	for line in file_data:
		s=line.split()
		if(np.size(s)<2):
			continue
		if(s[1]=="!NATOM"):
			flag=1
			Nthings=int(s[0])
			continue
		if(s[1]=="!NBOND:"):
			flag=2
			Nthings=int(s[0])
			continue
		if(s[1]=="!NTHETA:"):
			flag=3
			Nthings=int(s[0])
			continue
		if(s[1]=="!NPHI:"):
			flag=4
			Nthings=int(s[0])
			continue
		if(flag==1):
			atomPSF.append([s[5],float(s[6])])
		if(flag==2):
			for loop in np.arange(4):
				bonds.append([int(s[2*loop])-1,int(s[2*loop+1])-1])
				Nthings-=1
				if(Nthings==0):
					flag=0
					break
		if(flag==3):
			for loop in np.arange(3):
				angles.append([int(s[3*loop])-1,int(s[3*loop+1])-1,int(s[3*loop+2])-1])
				Nthings-=1
				if(Nthings==0):
					flag=0
					break
		if(flag==4):
			for loop in np.arange(2):
				dihedrals.append([int(s[4*loop])-1,int(s[4*loop+1])-1,int(s[4*loop+2])-1,int(s[4*loop+3])-1])
				Nthings-=1
				if(Nthings==0):
					flag=0
					break
