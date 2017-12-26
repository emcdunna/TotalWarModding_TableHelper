from table_module import *
oldFileN = "C:\Users\emcdonoX\EvanFile\db\Warhammer\main_units_tables\evan.tsv"
newFileN = "C:\Users\emcdonoX\EvanFile\db\Warhammer\main_units_tables\main_evan.tsv"

oldFile = open(oldFileN, 'r')
newFile = open(newFileN, 'r')

oldTable = file_loader(oldFile,17)
newTable = file_loader(newFile,17)

'''
print "Old Table"
print oldTable
print "-"*80
print "New Table"
print newTable
print "-"*80
'''
print "Table diff"
tablediff = TableDiff(oldTable, newTable) # detects differences between two tables

print tablediff.to_tsv()

print "-"*100
apply_differences(tablediff, oldTable) # applies differences to the old table (makes it into new table)

sys.stderr.write("New diff:\n")
sys.stderr.write(str(TableDiff(oldTable,newTable)) + "\n\n")
