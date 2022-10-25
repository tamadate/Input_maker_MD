import numpy as np
import reader
import functions
import output

##  Input parameters
fileName="protein/angiotensinII+1"  # file name
L=300.0000      # calculation domain size (only of lammps input)
outputName="test"
chargeFile="/home/tama3rdgen/ChargeCalculation/angio1+/a.dump"
chargeFile="net"
netCharge=2
HDX_locations=np.array(["hn","ho"])

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
if(chargeFile=="net"):
    partialQ=netCharge/float(len(atoms))
    for i in atomPSF:
        i[1]=partialQ
else:
    if(chargeFile!="psf"):
        reader.readDumpFile(atomPSF,chargeFile)
print(atomPSF)

##  Create each list
atomList=[]
LJList=[]
bondList=[]
angleList=[]
dihedralList=[]
functions.parameterLists(Atoms,LJParams,bondParams,angleParams,dihedralParams,atoms,atomPSF,bonds,angles,dihedrals,atomList,LJList,bondList,angleList,dihedralList)

output.outputMyInpute(Atoms,LJParams,bondParams,angleParams,dihedralParams,atoms,atomPSF,bonds,angles,dihedrals,atomList,LJList,bondList,angleList,dihedralList,L,outputName)
if(np.size(HDX_locations)>0):
    output.outputLocationFile(atomPSF,HDX_locations,outputName)


print("**Done")
