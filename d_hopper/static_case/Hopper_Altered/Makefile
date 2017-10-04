


all: 
	echo try 'make clean' or 'make mesh'

clean:
	rm -rf `find -iname log.*`
	rm -rf `find -iname *.log`
	rm -rf `find -iname *.txt`
	rm -rf `find -iname liggghts.restart*`
	rm -rf CFD/processor*  
	rm -rf DEM/dump*	
	#rm -rf CFD/constant/polyMesh
	#rm -rf CFD/constant/extendedFeatureEdgeMesh
	#rm -rf CFD/constant/trisurface	
	#rm -rf CFD/0/pointLevel
	#rm -rf CFD/0/cellLevel

mesh:
	echo using existing mesh
	#blockMesh -case CFD
	#surfaceFeatureExtract -case CFD
	#snappyHexMesh -case CFD -overwrite
	#transformPoints -case CFD -scale "(0.1 0.1 0.1)"	


