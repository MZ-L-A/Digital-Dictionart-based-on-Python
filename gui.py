import tkinter as tk, lookup as lk
from algorithm import prefix, correct as corr
bg="#FFFFCC"
bg_deep="#FFFFAA"
fg="#000000"
fg_link="#444444"

t=prefix(lk.get_what_to_find())

cor=corr(lk.dic)

root=tk.Tk()
root.title("English-Chinese Dictionary")
root.geometry("1200x600")

main=tk.Frame(root, bg=bg)
searcher=tk.Frame(main, bg=bg)
searcher.pack(side='top', fill='x')
searcher_sub=tk.Frame(searcher, bg=bg)
searcher_sub.pack(side='top', fill='x')
btn_search=tk.Button(searcher_sub, text="search", bg=bg_deep, font=(None, 17, "bold"))
btn_correct=tk.Button(searcher_sub, text="correct", bg=bg_deep,  font=(None, 17, "bold"))
btn_correct.pack(side='right')
btn_search.pack(side='right')
inputer=tk.Entry(searcher_sub, bg="#FFFFAA", font=(None, 17, "bold"))
inputer.pack(side='right', expand=1, fill='both')

controls=[]
history=[]
def lookup(word, backed=False):
    tab.pack_forget()
    root.focus_set()
    for i in controls:
        i.destroy()
    result=lk.lookup_format(word)
    if not backed:
        history.append(word)
    if len(history)>1:
        def back(word):
            def f(word):
                print(history)
                history.pop()
                lookup(word, True)
            return lambda:f("".join(word[:]))
        controls.append(tk.Button(main, text="return to \""+history[-2]+"\"", bg=bg, font=(None, 15, "bold"), command=back(history[-2])))
        controls[-1].pack(side='right', anchor='ne')
    
    for i in result:
        controls.append(tk.Frame(main, bg=bg))
        controls[-1].pack(side='top', anchor='w')
        frame=controls[-1]
        txt=i[2]
        for j in range(i[1]):
            tk.Label(frame, text=" ", bg=bg, fg=fg, font=(None, 14+i[0], "bold" if i[0]>0 else "normal")).pack(side='left')
        for j in txt.split():
            if j in lk.dic:
                def f(x):
                    return lambda *args:lookup(x)
                lb=tk.Label(frame, text=j, bg=bg, fg=fg if i[0]>0 else fg_link, font=(None, 14+i[0], "bold" if i[0]>0 else "normal"))
                lb.bind("<Button-1>", f(j))            
                lb.pack(side='left')
            else:
                tk.Label(frame, text=j, bg=bg, fg=fg, font=(None, 14+i[0], "bold" if i[0]>0 else "normal")).pack(side='left')
            
        #tk.Label(main, text="  "*i[1]+i[2], bg=bg, fg=fg, font=(None, 14+i[0], "bold" if i[0]>0 else "normal"))
def correct(word):
    tab.pack(side='top', fill='both', expand=1)
    tab.delete(0, "end")
    q=cor.query(word, word_limit=30, edit_limit=0.36)    
    for i in q:
        tab.insert("end", i)
btn_search.config(command=lambda:lookup(inputer.get()))
btn_correct.config(command=lambda:correct(inputer.get()))
inputer.bind("<Return>", lambda e:lookup(inputer.get()))

tab=tk.Listbox(searcher, bg="#FFFFBB", font=(None, 12), height=999)

def show_tab(e):
    if e.keysym=="Enter":
        return None
    if e.keysym=="Escape":
        tab.pack_forget()
        root.focus_set()
    else:
        tab.pack(side='top', fill='both', expand=1)
        tab.delete(0, "end")
        if inputer.get()=="":
            q=sorted(lk.dic.keys())
            q.extend(sorted(lk.phrase.keys()))
        else:
            q=t.query(inputer.get())
        for i in q:
            tab.insert("end", i)
tab.call_count=0
def show_tab_timer(e):
    def call(e, t):
        if tab.call_count==t:
            show_tab(e)
    
    tab.call_count+=1
    root.after(4, call, e, tab.call_count)
inputer.bind("<KeyRelease>", show_tab_timer)

def ondoubleclick(*args):
    sel=tab.get(tab.curselection())
    inputer.delete(0, "end")
    inputer.insert("end", sel)
    tab.pack_forget()
    root.focus_set()
    lookup(sel)
tab.bind("<Double-Button-1>", ondoubleclick)
main.pack(side='top', fill='both', expand=1)
root.mainloop()
