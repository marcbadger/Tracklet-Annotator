import tkinter as tk

N = tk.N
S = tk.S
E = tk.E
W = tk.W

class BoxEditor(tk.Frame):
    """Creates Box Editor Buttons."""

    def __init__(self, ann, **kwargs):
        super().__init__(**kwargs)

        btn_new_box = tk.Button(master=self, text="Create new box", command=ann.newBox)
        btn_delete_box = tk.Button(master=self, text="Delete box", command=ann.deleteBox)
        btn_redraw_box = tk.Button(master=self, text="Redraw box", command=ann.redrawBox)
        btn_cancel = tk.Button(master=self, text="Cancel", command=ann.esc)
        
        btn_new_box.grid(sticky=S + W, row=1, column=0)
        btn_delete_box.grid(sticky=S + W, row=2, column=0)
        btn_redraw_box.grid(sticky=S + W, row=3, column=0)
        btn_cancel.grid(sticky=S + W, row=4, column=0)

        # ckb_prev = tk.Checkbutton(master=self, text="Show previous boxes", variable=ann.p, command=ann.showPrev)
        # ckb_next = tk.Checkbutton(master=self, text="Show next boxes", variable=ann.n, command=ann.showNext)
        # ckb_prev.grid(sticky=S + W, row=5, column=0)
        # ckb_next.grid(sticky=S + W, row=6, column=0)

        
class IdentityEditor(tk.Frame):
    """Creates Identity Editor Buttons."""

    def __init__(self, ann, **kwargs):
        super().__init__(**kwargs)

        lbl_labelerHeader = tk.Label(master=self, text="Identity Editor", bg=ann.col_leftPanel, width=int(ann.leftPanelWidth / 10))
        btn_swap_id = tk.Button(master=self, text="Swap track IDs", command=ann.changeId)
        btn_merge_id = tk.Button(master=self, text="Merge tracks into one ID", command=ann.mergeId)
        btn_unite_id = tk.Button(master=self, text="Unite boxes into one ID", command=ann.uniteId)
        btn_delete_id = tk.Button(master=self, text="Delete track and ID", command=ann.deleteId)
        btn_name_id = tk.Button(master=self, text="Customize ID name/color", command=ann.nameId)
        lbl_labelerHeader.grid(sticky=N + W, row=0, column=0)
        btn_swap_id.grid(sticky=S + W, row=1, column=0)
        btn_merge_id.grid(sticky=S + W, row=2, column=0)
        btn_unite_id.grid(sticky=S + W, row=3, column=0)
        btn_delete_id.grid(sticky=S + W, row=4, column=0)
        btn_name_id.grid(sticky=S + W, row=5, column=0)

class IdentityPanel(tk.Frame):
    """Creates Identity Display Panel."""

    def __init__(self, ann, **kwargs):
        super().__init__(**kwargs)

        lbl_allidheader = tk.Label(master=self, text=" All Identities", bg=ann.col_leftPanel)
        btn_new_id = tk.Button(master=self, text="New ID", command=ann.newId, highlightbackground=ann.col_leftPanel, border=3)
        self.list_ids = tk.Listbox(master=self, borderwidth=6, relief="flat", height=int(
            1.8 * ann.leftPanelHeight_Row1), bg=ann.col_light, selectforeground="blue", selectbackground=ann.col_main, activestyle="underline")
        lbl_allidheader.grid(sticky=W + E, row=0, column=0)
        btn_new_id.grid(sticky=N + E, row=0, column=1)
        self.list_ids.grid(sticky=N + W, row=1, column=0, columnspan=2)

        self.list_ids.bind('<<ListboxSelect>>', ann.clickId)

class CommitPanel(tk.Frame):
    """Creates Commit and Reload Buttons."""

    def __init__(self, ann, **kwargs):
        super().__init__(**kwargs)

        btn_commit = tk.Button(master=self, text="Commit Edits", command=ann.commitEdits)
        btn_reload = tk.Button(master=self, text="Commit and Reload", command=ann.commitReload)
        btn_commit.grid(sticky=S + W, row=2, column=0)
        btn_reload.grid(sticky=S + W, row=3, column=0)
