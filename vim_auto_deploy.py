import os

def execcmds(cmds):
    for cmd in cmds:
        if type(cmd) == str:
            ret = os.system(cmd)
        else:
            cmd()
        print ret,

def vimrc_deploy():
    cmds = [
        "rm -rf ~/.vimrc",
        "cp vimrc ~/.vimrc",
    ]
    execcmds(cmds)

def pathogen_install():
    cmds = [
        "rm -rf ~/.vim/autoload",
        "rm -rf ~/.vim/bundle",
        "mkdir -p ~/.vim/autoload ~/.vim/bundle && curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim",
    ]
    execcmds(cmds)

def powerline_install():
    def chdir_install():
        pwd = os.getcwd()
        os.chdir("/tmp/powerline")
        os.system("python setup.py install")
        os.chdir(pwd)

    cmds = [
    "rm -rf /tmp/powerline",
    "git clone https://github.com/Lokaltog/powerline /tmp/powerline",
    chdir_install,
    ]
    execcmds(cmds)
    
def monokai_install():
    cmds = [
    "rm -rf ~/.vim/bundle/powerline",
    "git clone https://github.com/sickill/vim-monokai ~/.vim/bundle/vim-monokai",
    "cp monokai.vim ~/.vim/bundle/vim-monokai/colors/monokai.vim"
    ]
    execcmds(cmds)

def nerdtree_install():
    cmds = [
    "rm -rf ~/.vim/bundle/nerdtree",
    "git clone https://github.com/scrooloose/nerdtree ~/.vim/bundle/nerdtree",
    ]
    execcmds(cmds)

def snipmate_install():
    cmds = [
    "rm -rf ~/.vim/bundle/tlib_vim",
    "git clone https://github.com/tomtom/tlib_vim.git ~/.vim/bundle/tlib_vim",
    "rm -rf ~/.vim/bundle/vim-addon-mw-utils",
    "git clone https://github.com/MarcWeber/vim-addon-mw-utils.git ~/.vim/bundle/vim-addon-mw-utils",
    "rm -rf ~/.vim/bundle/vim-snipmate",
    "git clone https://github.com/garbas/vim-snipmate.git ~/.vim/bundle/vim-snipmate",
    "rm -rf ~/.vim/bundle/vim-snippets",
    "git clone https://github.com/honza/vim-snippets.git ~/.vim/bundle/vim-snippets",
    ]
    execcmds(cmds)

def syntastic_install():
    cmds = [
    "rm -rf ~/.vim/bundle/syntastic",
    "git clone https://github.com/scrooloose/syntastic ~/.vim/bundle/syntastic",
    ]
    execcmds(cmds)

def supertab_install():
    cmds = [
    "rm -rf ~/.vim/bundle/supertab",
    "git clone https://github.com/ervandew/supertab ~/.vim/bundle/supertab",
    ]
    execcmds(cmds)
   
def ctrlp_install():
    cmds = [
    "rm -rf ~/.vim/bundle/ctrlp",
    "git clone https://github.com/kien/ctrlp.vim ~/.vim/bundle/ctrlp.vim"
    ]
    execcmds(cmds)
    
def airline_install():
    cmds = [
    "rm -rf ~/.vim/bundle/airline",
    "git clone https://github.com/vim-airline/vim-airline ~/.vim/bundle/vim-airline",
    ]
    execcmds(cmds)

def fugitive_install():
    cmds = [
    "rm -rf ~/.vim/bundle/fugitive",
    "git clone https://github.com/tpope/vim-fugitive ~/.vim/bundle/vim-fugitive",
    ]
    execcmds(cmds)
    
Procedure = [
    ('Deploy vimrc', vimrc_deploy),
    ('Install pathogen', pathogen_install),
    ('Install powerline', powerline_install),
    ('Install airline', airline_install),
    ('Install monokai', monokai_install),
    ('Install nerdtree', nerdtree_install),
    ('Install snipmate', snipmate_install),
    ('Install syntastic', syntastic_install),
    ('Install supertab', supertab_install),
    ('Install ctrlp', ctrlp_install),
    ('Install fugitive', fugitive_install),
]

def main():
    for p in Procedure:
        print p[0],
        p[1]()
        print
if __name__ == "__main__":
    main()