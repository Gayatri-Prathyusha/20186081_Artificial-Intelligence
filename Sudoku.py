def cross(A,B):
	return [a + b for a in A for b in B]

digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits
squares = cross(rows,cols)
unitlist = ([cross(rows,c) for c in cols] + [cross(r, cols) for r in rows]
	+ [cross(rs,cs) for rs in ('ABC','DEF','GHI') for cs in('123','456','789')])
# print(unitlist)


units = dict((s, [unit for unit in unitlist if s in unit])for s in squares)
peers = dict((s,set(sum(units[s],[])) - set([s]))for s in squares)
test()

def test():
	assert len(squares) == 81
	assert len(unitlist) == 21
	assert all(len(units[s]) == 3 for s in squares)
	assert all(len(peer[s]) == 20 for s in squares)
	assert units['C2'] == [['A2','B2','C2','D2','E2','F2','G2','H2','I2'],
	['C1','C2','C3','C4','C5','C6','C7','C8','C9'],['A1','A2','A3','B1','B2','B3','C1','C2','C3']]
	assert peers['C2'] ==  [['A2','B2','D2','E2','F2','G2','H2','I2',
	'C1','C3','C4','C5','C6','C7','C8','C9','A1','A3','B1','B3']

	print("all tests pass")




