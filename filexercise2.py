#...

# with open('demo.html','r') as rf:
#     with open('newlink.txt', 'a') as wf:
#         for line in rf.readlines():
#             if '<a href=' in line:
#                  n = line.find("<a href=")
#                  #rf.seek(n)
#                  firstQuot = line.find('\"',n)
#                  secondQuot = line.find('\"',firstQuot+1)
#                  url = line[firstQuot+1:secondQuot]
#                  wf.write(url +"\n")






with open('demo.html','r') as webpage:
     with open('Output.txt', 'a') as wf:
         page = webpage.read()
         link_exist = True
         while link_exist:
             pos = page.find('<a href=')
             if pos == -1:
                 link_exist = False
             else:
                 firstQuot = page.find('\"',pos)
                 secondQuot = page.find('\"',firstQuot+1)
                 url = page[firstQuot+1:secondQuot]
                 wf.write(url +"\n")
                 page = page[secondQuot:]



