import webbrowser
import time

total_breaks=3
break_count=0

print("This program started on "+time.ctime())
while(break_count < total_breaks):
 time.sleep(10)
 webbrowser.open("https://www.youtube.com/watch?v=9658rKyah6I&list=PLIUT-JkJtnDzrWMiUMKGTXunoJzI_e1Sw&index=61")
 break_count=break_count+1
