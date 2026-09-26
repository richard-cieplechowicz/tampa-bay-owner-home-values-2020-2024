import csv, json, math
from pathlib import Path
root=Path(__file__).parent
prior=list(csv.DictReader(open(str(root/'prior-tampa-bay-zip-housing-2024.csv'))))
source=json.load(open(str(root/'census-reporter-acs2024-5yr-b25075-b25077.json')))
assert source['release']['id']=='acs2024_5yr' and len(prior)==len(source['data'])==132

def clean(x):
    return '' if x is None or x < 0 else int(x)

def pct(a,b):
    return '' if not isinstance(a,int) or not isinstance(b,int) or b<=0 else round(100*a/b,1)
fields=['zcta','county','population','owner_occupied_units','median_owner_occupied_value_usd','median_value_moe_90pct_usd','owner_units_value_below_300k','owner_units_value_300k_to_499k','owner_units_value_500k_to_999k','owner_units_value_1m_plus','owner_share_value_500k_plus_pct','small_owner_sample_flag']
rows=[]
for p in prior:
    z=p['zip']; d=source['data']['86000US'+z]; b=d['B25075']['estimate']; med=clean(d['B25077']['estimate']['B25077001']); moe=clean(d['B25077']['error']['B25077001']); own=clean(b['B25075001'])
    assert med==int(float(p['median_home_value'])) if p['median_home_value'] else med==''
    v=lambda lo,hi:sum(int(b['B25075%03d'%i]) for i in range(lo,hi+1))
    counts=[v(2,20),v(21,22),v(23,24),v(25,27)]
    assert sum(counts)==own,(z,counts,own)
    rows.append([z,p['county'],int(float(p['population'])),own,med,moe,*counts,pct(counts[2]+counts[3],own),'yes' if own<300 else 'no'])
with open(root/'tampa-bay-owner-home-values-by-zcta-2020-2024.csv','w',newline='') as f:
    w=csv.writer(f);w.writerow(fields);w.writerows(rows)
bycounty={}
for r in rows:
    x=bycounty.setdefault(r[1],{'zctas':0,'owner_units':0,'value_500k_plus':0,'medians':[],'flagged':0})
    x['zctas']+=1;x['owner_units']+=r[3];x['value_500k_plus']+=r[8]+r[9];x['flagged']+=r[11]=='yes'
    if r[4]!='' and r[3]>=300:x['medians'].append(r[4])
print('rows',len(rows),'missing',sum(r[4]=='' for r in rows),'small sample',sum(r[11]=='yes' for r in rows))
for c,x in sorted(bycounty.items()):print(c,x['zctas'],x['owner_units'],round(100*x['value_500k_plus']/x['owner_units'],1),'small',x['flagged'],'range',min(x['medians']),max(x['medians']))
print('all',sum(r[3] for r in rows),sum(r[8]+r[9] for r in rows),round(100*sum(r[8]+r[9] for r in rows)/sum(r[3] for r in rows),1))
