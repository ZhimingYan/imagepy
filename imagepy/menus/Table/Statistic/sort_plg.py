from imagepy.core.engine import Table
import pandas as pd
from imagepy import IPy

class Sort(Table):
	title = 'Table Sort By Key'

	para = {'major':None, 'minor':None, 'descend':False}
		
	view = [('field', 'major', 'major', 'key'),
			('field', 'minor', 'minor', 'key'),
			(bool, 'descend', 'descend')]

	def run(self, tps, data, snap, para=None):
		by = [para['major'], para['minor']]
		tps.data.sort_values(by=[i for i in by if i != 'None'], 
			axis=0, ascending=not para['descend'], inplace=True)

plgs = [Sort]