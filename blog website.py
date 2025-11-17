blog_views = [150, 800, 2500, 600, 1200, 450, 3000]
for x in blog_views:
    if x>1000:
        print('trending')
    elif x>=500 and x<=1000:
        print('average')
    else:
        print('low traffic')
        total=0
for x in blog_views:
 total+=x
print('total number of views is',total)
trending=0
for x in blog_views:
    if x>1000:
     trending+=1
print('no of post which where trending views',trending)
    

            
        
    
