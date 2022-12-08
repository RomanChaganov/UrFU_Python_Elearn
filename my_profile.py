import cProfile
from pstats import Stats, SortKey
import report_out
from datetime import datetime

cProfile.run('report_out.InputConnect()', 'restats')
p = Stats('restats')
p.sort_stats(SortKey.TIME).print_stats(1)
