from matplotlib.pyplot import *
from numpy import *
from matplotlib.patches import Rectangle

figure(figsize=(10,3))
axis('off')
x=range(0,800)
y1=[50]*len(x)
y2=[150]*len(x)

plot(x,y1,'k--')
plot(x,y2,'k--')


def draw_line(line,c='k'):
    x1,y1,x2,y2=line
    if(x1==x2):
        x=[x1]*1000
    else:
        x_step=(x2-x1)/1000.0
        x=arange(x1,x2,x_step)
    if(y1==y2):
        y=[y1]*1000
    else:
        y_step=(y2-y1)/1000.0
        y=arange(y1,y2,y_step)
    plot(x,y,c,linewidth=3,)

    
def draw_box(box,c='b'):
    x1,y1,x2,y2=box
    currentAxis = gca()
    currentAxis.add_patch(Rectangle((x1, y1), x2-x1, y2-y1, fill = c, alpha=0.3,linewidth=0))

    
def draw_text(txt):
    x,y,s=txt
    text(x,y,s,fontsize=24,horizontalalignment='center',
         verticalalignment='center')

    
def generate_lines(upsegs,downsegs):
    lines = []
    yup = 150
    ydown = 50
    for seg in upsegs:
        if seg[0] < seg[1]:
            lines.append([seg[0],yup,seg[1],yup])
        else:
            lines.append([0,yup,seg[1],yup])
            lines.append([seg[0],yup,800,yup])
    for seg in downsegs:
        if seg[0] < seg[1]:
            lines.append([seg[0],ydown,seg[1],ydown])
        else:
            lines.append([0,ydown,seg[1],ydown])
            lines.append([seg[0],ydown,800,ydown])
    #Two vertical lines at each end
    lines.append([0,20,0,180])
    lines.append([800,20,800,180])
    return lines


def overlap(useg, dseg):
    start = max(useg[0],dseg[0])
    end = min(useg[1],dseg[1])
    if end > start:
        return([start,end])
    else:
        return None

    
def break_segs(segs):
    segs_broken=[]
    for seg in segs:
        if seg[0]<seg[1]:
            segs_broken.append(seg)
        else:
            segs_broken.append([0,seg[1]])
            segs_broken.append([800,seg[0]])
    return segs_broken


def generate_boxes(upsegs,downsegs):
    yup=150
    ydown=50
    boxes=[]
    upsegs_break=break_segs(upsegs)
    downsegs_break=break_segs(downsegs)
    for upseg in upsegs_break:
        for downseg in downsegs_break:
            ov=overlap(upseg,downseg)
            if ov != None:
                boxes.append([ov[0],yup,ov[1],ydown])
    return boxes


def generate_texts(upsegs,downsegs):
    texts=[[0,0,r'$\beta$'],[800,0,r'$0$']]
    yup = 175
    ydown = 25
    idx=len(upsegs)-1
    for upseg in upsegs:
        texts.append([upseg[0],yup,r"$\tau^\uparrow_%d$"%idx])
        texts.append([upseg[1],yup,r"${\tau'}^\uparrow_%d$"%idx])
        idx-=1
    idx=len(downsegs)-1
    for downseg in downsegs:
        texts.append([downseg[0],ydown,r"$\tau^\downarrow_%d$"%idx])
        texts.append([downseg[1],ydown,r"${\tau'}^\downarrow_%d$"%idx])
        idx-=1
    return texts
        

#lines=[[50,50,300,50],[400,50,580,50],[0,150,200,150],[280,150,550,150],
#        [600,150,650,150],[700,150,800,150],[0,20,0,180],[800,20,800,180]]

#boxes=[[50,50,200,150],[280,50,300,150],[400,50,550,150]]

#texts=[[0,0,r'$\beta$'],[800,0,r'$0$'],[50,25,r'$\tau^\downarrow_2$'],
#       [300,25,r"${\tau'}^\downarrow_2$"],[400,25,r'$\tau^\downarrow_1$'],
#       [580,25,r"${\tau'}^\downarrow_1$"],[280,175,r'$\tau^\uparrow_2$'],
#       [550,175,r"${\tau'}^\uparrow_2$"],[600,175,r'$\tau^\uparrow_1$'],
#       [650,175,r"${\tau'}^\uparrow_1$"],[700,175,r'$\tau^\uparrow_3$'],
#       [200,175,r"${\tau'}^\uparrow_3$"]]


downsegs=[[50,300],[400,580]]
upsegs=[[700,200],[280,550],[600,650]]

lines=generate_lines(upsegs,downsegs)
boxes=generate_boxes(upsegs,downsegs)
texts=generate_texts(upsegs,downsegs)

for line in lines:
    draw_line(line)

for box in boxes:
    draw_box(box)

for txt in texts:
    draw_text(txt)


xlim(-20,820)
ylim(-20,220)
tight_layout()
savefig("segment_test.png")
