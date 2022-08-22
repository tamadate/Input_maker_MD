import numpy as np
import reader
import functions
import output

##  Input parameters
fileName="angiotensinII2+.pdb"  # file name
L=300.0000      # calculation domain size (only of lammps input)
q=2     # net charge
outputName="angiotensinII2+"

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
bonds=[]
bondUniq=[]
angles=[]
dihedrals=[]
reader.readPDBfile(atoms,bonds,bondUniq,angles,dihedrals,fileName)

##  Create each list
atomList=[]
LJList=[]
bondList=[]
angleList=[]
dihedralList=[]
functions.parameterLists(Atoms,LJParams,bondParams,angleParams,dihedralParams,atoms,bonds,bondUniq,angles,dihedrals,atomList,LJList,bondList,angleList,dihedralList)


qeach=q/float(len(atoms))
output.outputMyInpute(Atoms,LJParams,bondParams,angleParams,dihedralParams,atoms,bonds,bondUniq,angles,dihedrals,atomList,LJList,bondList,angleList,dihedralList,L,q,qeach,outputName)

print("**Done")
