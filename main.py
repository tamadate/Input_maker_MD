import numpy as np
import reader
import functions
import output

##  Input parameters
fileName="alcohol/input/MeOHRESP"  # file name
L=300.0000      # calculation domain size (only of lammps input)
outputName="MeOH"

##  Read potential file
Atoms=[]
reader.readMass(Atoms)
LJParams=[]
reader.readLJ(LJParams)
bondParams=[]
reader.readBond(bondParams)
angleParams=[]
reader.readAngle(angleParams)
dihedralParams=[]
reader.readDihedral(dihedralParams)

##  Read atom file (only PDB 8/23/2022)
atoms=[]
atomPSF=[]
bonds=[]
bondUniq=[]
angles=[]
dihedrals=[]
reader.readPDBfile(atoms,fileName+".pdb")
reader.readPSFfile(atomPSF,bonds,angles,dihedrals,fileName+".psf")

##  Create each list
atomList=[]
LJList=[]
bondList=[]
angleList=[]
dihedralList=[]
functions.parameterLists(Atoms,LJParams,bondParams,angleParams,dihedralParams,atoms,atomPSF,bonds,angles,dihedrals,atomList,LJList,bondList,angleList,dihedralList)


output.outputMyInpute(Atoms,LJParams,bondParams,angleParams,dihedralParams,atoms,atomPSF,bonds,angles,dihedrals,atomList,LJList,bondList,angleList,dihedralList,L,outputName)

print("**Done")
