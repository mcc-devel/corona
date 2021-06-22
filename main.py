from processinfo import process as p
from pyecharts.charts import Bar, Timeline
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from time import localtime
import datetime

rret = p()
ret = rret[0]
unix = 1583020800
tm = datetime.date(2020, 3, 1)
cur = datetime.date.today()
space = (cur - tm).days
confirm = []
dead = []
diff = 86400
tms = []
for i in range(space):
    tms.append(localtime(unix))
    unix += diff
    confirm.append([])
    dead.append([])
    for j in range(5):
        confirm[i].append(ret[0][j][i])
        dead[i].append(ret[1][j][i])
cntlst = rret[1]
'''
    Definition of a lot of Bars and a timeline
'''
timeline = (
    Timeline(init_opts=opts.InitOpts(page_title='Coronavirus', theme=ThemeType.LIGHT))
)
for i in range(space):
    tm = tms[i]
    date = str(tm.tm_year) + '-' + str(tm.tm_mon) + '-' + str(tm.tm_mday)
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(cntlst)
        .add_yaxis('Confirmed', confirm[i])
        .add_yaxis('Deaths', dead[i])
        .reversal_axis()
        .set_global_opts(title_opts=opts.TitleOpts(title='Coronavirus ' + date, subtitle='Coronavirus Statistics ' + date))
        .set_series_opts(label_opts=opts.LabelOpts(position='right'))
    )
    timeline.add(bar, date)
timeline.add_schema(play_interval=150)
timeline.render('Corona.html')
