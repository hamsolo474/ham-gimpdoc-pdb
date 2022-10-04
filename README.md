# ham-gimpdoc-pdb
Gimp PDB docs

pdb.html is the latest PDB docs i have created.
view it here https://htmlpreview.github.io/?https://github.com/hamsolo474/ham-gimpdoc-pdb/blob/main/pdb.html


Presently I create PDB docs in a semi automated way, 

i start by opening Gimp then going Filters > Python-Fu > Console 

then i type
pdb.gimp_procedural_db_dump(r'/somepath/pdbdump.scm')

drag and drop that on to ham-gimpdoc.py or using the cmd put the path to pdbdump.scm as an argument to ham-gimpdoc.py

ham-gimpdoc.py /somepath/pdbdump.scm

then it will create pdb.html
