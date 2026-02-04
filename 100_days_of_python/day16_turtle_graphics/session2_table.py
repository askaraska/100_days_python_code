from prettytable import PrettyTable
table = PrettyTable()
print(table)
#create the column with fieldname:pokeman name and its type
table.add_column("Pokemon Name", ["Pikachu","Squirtle","Charmander"])
print(table)
table.add_column("Type", ["Electric","Water","Fire"])
print(table)

#for aligning the table left
table.align = "l"
print(table)
